import json
import re
import unicodedata
from pathlib import Path


FENCED_CODE_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
LINK_RE = re.compile(r"!?(?<!!)\[[^\]]*?\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)
IGNORED_SCHEMES = ("http://", "https://", "mailto:", "tel:", "data:")
IGNORED_PATH_PARTS = {"_borradores"}
DUPLICATE_NAME_RE = re.compile(r" \d+\.md$")
MODULE_DIR_RE = re.compile(r"^\d+_")
CHAPTER_FILE_RE = re.compile(r"^\d+_.*\.md$")
EDITORIAL_RULES = (
    ("titulo_h1", re.compile(r"^#\s+\S+", re.MULTILINE), "titulo principal H1"),
    ("metadata", re.compile(r"^\*\*Nivel:\*\*", re.MULTILINE), "bloque de metadatos"),
    (
        "purpose",
        re.compile(r"^##\s+(?:\d+\.\s+)?(?:Proposito|Objetivo)\b", re.MULTILINE),
        "seccion de Proposito u Objetivo",
    ),
    (
        "references",
        re.compile(r"^##\s+(?:\d+\.\s+)?Referencias", re.MULTILINE),
        "seccion de Referencias",
    ),
    (
        "questions",
        re.compile(r"^##\s+(?:\d+\.\s+)?Preguntas", re.MULTILINE),
        "seccion de Preguntas de comprobacion o estudio",
    ),
    (
        "navigation",
        re.compile(r"^##\s+Navegacion del tutorial\b", re.MULTILINE),
        "seccion de Navegacion del tutorial",
    ),
)


def strip_code_blocks(content: str) -> str:
    return FENCED_CODE_BLOCK_RE.sub("", content)


def normalize_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    return target


def slugify_heading(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii").lower()
    ascii_text = re.sub(r"[^\w\s-]", "", ascii_text)
    ascii_text = re.sub(r"\s+", "-", ascii_text.strip())
    return re.sub(r"-{2,}", "-", ascii_text)


def collect_anchors(content: str) -> set[str]:
    anchors = set()
    for match in HEADING_RE.finditer(content):
        heading = match.group(2).strip()
        if heading:
            anchors.add(slugify_heading(heading))
    return anchors


def is_placeholder_target(target: str) -> bool:
    placeholder_tokens = ("MODULO_", "DOCUMENTO_", "CAPITULO_", "TITULO_")
    return "[" in target or "]" in target or any(
        token in target for token in placeholder_tokens
    )


def validate_anchor(target_file: Path, anchor: str) -> bool:
    if not anchor or target_file.suffix.lower() != ".md" or not target_file.exists():
        return True
    content = target_file.read_text(encoding="utf-8")
    return anchor in collect_anchors(content)


def find_editorial_duplicates() -> list[str]:
    duplicate_paths: list[str] = []
    for md_file in sorted(Path("Tutorial").rglob("*.md")):
        if any(part in IGNORED_PATH_PARTS for part in md_file.parts):
            continue
        if DUPLICATE_NAME_RE.search(md_file.name):
            duplicate_paths.append(str(md_file))
    return duplicate_paths


def iter_public_chapter_files() -> list[Path]:
    chapter_files: list[Path] = []
    for md_file in sorted(Path("Tutorial").rglob("*.md")):
        if any(part in IGNORED_PATH_PARTS for part in md_file.parts):
            continue
        if md_file.name == "README.md":
            continue
        parts = md_file.parts
        if len(parts) < 3:
            continue
        _, module_dir, filename = parts[:3]
        if not MODULE_DIR_RE.match(module_dir):
            continue
        if not CHAPTER_FILE_RE.match(filename):
            continue
        chapter_files.append(md_file)
    return chapter_files


def validate_editorial_consistency() -> list[dict[str, str]]:
    issues: list[dict[str, str]] = []
    for md_file in iter_public_chapter_files():
        content = md_file.read_text(encoding="utf-8")
        for _, pattern, description in EDITORIAL_RULES:
            if not pattern.search(content):
                issues.append({"file": str(md_file), "missing": description})
    return issues


def extract_notebook_markdown(nb_path: Path) -> str:
    try:
        data = json.loads(nb_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return ""
    lines = []
    for cell in data.get("cells", []):
        if cell.get("cell_type") == "markdown":
            lines.append("".join(cell.get("source", [])))
    return "\n".join(lines)


def check_notebook_links(broken_links: list[dict[str, str]]) -> None:
    for nb_file in sorted(Path("Cuadernos").rglob("*.ipynb")):
        content = extract_notebook_markdown(nb_file)
        sanitized_content = strip_code_blocks(content)
        for match in LINK_RE.finditer(sanitized_content):
            raw_target = normalize_target(match.group(1))
            if not raw_target or raw_target.startswith(IGNORED_SCHEMES):
                continue
            if is_placeholder_target(raw_target):
                continue
            path_part, _, _ = raw_target.partition("#")
            if not path_part:
                continue
            target_path = (nb_file.parent / path_part).resolve()
            if not target_path.exists():
                broken_links.append(
                    {
                        "file": str(nb_file),
                        "link": raw_target,
                        "reason": "ruta inexistente",
                    }
                )


def check_links() -> int:
    md_files = sorted(
        path
        for path in Path(".").rglob("*.md")
        if not any(part in IGNORED_PATH_PARTS for part in path.parts)
    )
    broken_links: list[dict[str, str]] = []

    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        sanitized_content = strip_code_blocks(content)

        for match in LINK_RE.finditer(sanitized_content):
            raw_target = normalize_target(match.group(1))
            if not raw_target or raw_target.startswith(IGNORED_SCHEMES):
                continue
            if is_placeholder_target(raw_target):
                continue

            path_part, _, anchor = raw_target.partition("#")

            if not path_part:
                target_path = md_file
            else:
                target_path = (md_file.parent / path_part).resolve()
                if not target_path.exists():
                    broken_links.append(
                        {
                            "file": str(md_file),
                            "link": raw_target,
                            "reason": "ruta inexistente",
                        }
                    )
                    continue

            if anchor and not validate_anchor(target_path, anchor):
                broken_links.append(
                    {
                        "file": str(md_file),
                        "link": raw_target,
                        "reason": "ancla inexistente",
                    }
                )

    check_notebook_links(broken_links)

    duplicate_paths = find_editorial_duplicates()
    if duplicate_paths:
        print(
            f"❌ Se encontraron {len(duplicate_paths)} archivos con nombres editoriales ambiguos:"
        )
        for path in duplicate_paths:
            print(f"  - {path}")
        print(
            "   Renómbralos con una convención inequívoca o elimínalos si son duplicados."
        )
        return 1

    editorial_issues = validate_editorial_consistency()
    if editorial_issues:
        print(
            f"❌ Se encontraron {len(editorial_issues)} incumplimientos de consistencia editorial:"
        )
        for issue in editorial_issues:
            print(f"  - En {issue['file']}: falta {issue['missing']}")
        return 1

    if broken_links:
        print(f"❌ Se encontraron {len(broken_links)} enlaces rotos o inconsistentes:")
        for broken in broken_links:
            print(
                f"  - En {broken['file']}: '{broken['link']}' -> {broken['reason']}"
            )
        return 1

    print("✅ No se encontraron enlaces rotos locales ni anclas inválidas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(check_links())
