import os
import re
from pathlib import Path

def check_links():
    md_files = list(Path('.').rglob('*.md'))
    broken_links = []
    
    # Regex para capturar [texto](link)
    link_pattern = re.compile(r'\[.*?\]\((?!http)(.*?)\)')
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            links = link_pattern.findall(content)
            
            for link in links:
                # Limpiar anclas de HTML
                path_part = link.split('#')[0]
                if not path_part:
                    continue
                
                # Resolver ruta relativa
                target_path = (md_file.parent / path_part).resolve()
                
                if not target_path.exists():
                    broken_links.append({
                        'file': str(md_file),
                        'link': link,
                        'target': str(target_path)
                    })

    if broken_links:
        print(f"❌ Se encontraron {len(broken_links)} enlaces rotos:")
        for bl in broken_links:
            print(f"  - En {bl['file']}: '{bl['link']}' -> No encontrado")
    else:
        print("✅ No se encontraron enlaces rotos locales.")

if __name__ == "__main__":
    check_links()
