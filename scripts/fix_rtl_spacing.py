import re
from pathlib import Path

p = Path('src/content/blog/security-plus-guide.md')
s = p.read_text(encoding='utf-8')

# Ensure a space after Markdown heading markers
s = re.sub(r'^(#{1,6})([^\s#])', r'\1 \2', s, flags=re.MULTILINE)

# Insert space between Hebrew and Latin letters/digits/symbols
he = r'\u0590-\u05FF\uFB1D-\uFB4F'
# Hebrew followed by Latin/digits/some symbols
s = re.sub(r'([' + he + r'])([A-Za-z0-9@#%&\+\-_/:\.])', r'\1 \2', s)
# Latin/digits followed by Hebrew
s = re.sub(r'([A-Za-z0-9@#%&\+\-_/:\.])([' + he + r'])', r'\1 \2', s)

# Collapse multiple spaces into single, but preserve newlines
s = re.sub(r'(?<=\S) {2,}(?=\S)', ' ', s)

p.write_text(s, encoding='utf-8')
print('Fixed spacing in', p)
