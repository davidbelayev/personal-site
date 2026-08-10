from pathlib import Path
import re

p = Path('src/content/blog/security-plus-guide.md')
s = p.read_text(encoding='utf-8')

# small fixes
s = s.replace('mustnot', 'must not')
s = s.replace('PASSMastery streak:', 'PASS — Mastery streak:')

# space after colon if missing (English and Hebrew letters)
s = re.sub(r':(?=[A-Za-z\u0590-\u05FF])', ': ', s)

# insert newline before numbered objective if it was concatenated after 'Strong'
s = re.sub(r'(Strong)(?=\d)', r'\1\n', s)

# fix 'Test meonly' if exists
s = s.replace('Test meonly', 'Test me only')

# collapse multiple blank lines to max two
s = re.sub(r'\n{3,}', '\n\n', s)

# trim trailing spaces
s = '\n'.join([ln.rstrip() for ln in s.splitlines()]) + '\n'

p.write_text(s, encoding='utf-8')
print('Applied final pass 2')
