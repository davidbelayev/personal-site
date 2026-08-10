from pathlib import Path
p = Path('src/content/blog/security-plus-guide.md')
s = p.read_text(encoding='utf-8')
# remove spaces before punctuation .,;:!? and before closing paren
s = s.replace(' .', '.').replace(' ,', ',').replace(' :', ':').replace(' ;', ';').replace(' !', '!').replace(' ?', '?')
# normalize multiple spaces
import re
s = re.sub(r' {2,}', ' ', s)
p.write_text(s, encoding='utf-8')
print('Cleaned punctuation in', p)
