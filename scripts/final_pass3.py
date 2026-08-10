from pathlib import Path
import re
p = Path('src/content/blog/security-plus-guide.md')
s = p.read_text(encoding='utf-8')
# Insert newline after words like Strong or Moderate when immediately followed by a digit
s = re.sub(r'(Strong|Moderate)(?=\d)', r'\1\n', s)
# Fix 'doesnotmean' -> 'does not mean'
s = s.replace('doesnotmean', 'does not mean')
# ensure space after em-dash sequences if missing
s = s.replace('—Mastery', '— Mastery')
# fix 'Test meonly' if still present
s = s.replace('Test meonly', 'Test me only')
# collapse multiple blank lines
s = re.sub(r'\n{3,}', '\n\n', s)

p.write_text(s, encoding='utf-8')
print('Applied final pass 3')
