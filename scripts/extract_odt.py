import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

ODT_PATH = Path("new_blog.odt")
OUT_PATH = Path("src/content/blog/security-plus-guide.md")
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

def local_name(tag):
    if '}' in tag:
        return tag.split('}', 1)[1]
    return tag

with zipfile.ZipFile(ODT_PATH, 'r') as z:
    content_xml = z.read('content.xml')

root = ET.fromstring(content_xml)

# collect paragraphs and headings
md_lines = []
for elem in root.iter():
    name = local_name(elem.tag)
    if name in ("p", "h"):
        text = ''.join(elem.itertext()).strip()
        if not text:
            continue
        if name == 'h':
            level = elem.attrib.get('{urn:oasis:names:tc:opendocument:xmlns:text:1.0}outline-level') or elem.attrib.get('outline-level') or '1'
            try:
                lvl = int(level)
            except Exception:
                lvl = 1
            md_lines.append('#' * max(1, lvl) + ' ' + text)
            md_lines.append('')
        else:
            md_lines.append(text)
            md_lines.append('')

# Build frontmatter
title = 'מדריך להרשמה וללמידה ל-Security+'
date_str = datetime.now().strftime('%b %d %Y')
frontmatter = [
    '---',
    f"title: '{title}'",
    "description: ''",
    f"pubDate: '{date_str}'",
    "heroImage: '../../assets/blog-placeholder-3.jpg'",
    '---',
    '',
]

content = '\n'.join(frontmatter + md_lines)

OUT_PATH.write_text(content, encoding='utf-8')
print(f'Wrote: {OUT_PATH}')
