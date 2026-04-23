import re
import unicodedata
from pathlib import Path


FENCED_CODE_BLOCK_RE = re.compile(r"```.*?```", re.DOTALL)
LINK_RE = re.compile(r"!?(?<!!)\[[^\]]*?\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)
IGNORED_SCHEMES = ("http://", "https://", "mailto:", "tel:", "data:")
IGNORED_PATH_PARTS = {"_borradores"}
DUPLICATE_NAME_RE = re.compile(r" \d+\.md$")


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

    duplicate_paths = find_editorial_duplicates()
    if duplicate_paths:
        print(
            f"❌ Se encontraron {len(duplicate_paths)} archivos con nombres editoriales ambiguos:"
        )
        for path in duplicate_paths:
            print(f"  - {path}")
        print(
            "   Mueve estas variantes a `Tutorial/_borradores/` o renómbralas con una convención inequívoca."
        )
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
