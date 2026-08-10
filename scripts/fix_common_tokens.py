from pathlib import Path
p = Path('src/content/blog/security-plus-guide.md')
s = p.read_text(encoding='utf-8')
replacements = {
    'Donotrestrict': 'Do not restrict',
    'test meonly': 'test me only',
    'test meonly': 'test me only',
    'Writeoriginal': 'Write original',
    'questionsthat': 'questions that',
    'havefour': 'have four',
    'at least50': 'at least 50',
    'at least50': 'at least 50',
    'up to100': 'up to 100',
    'at least50 multiple-choice': 'at least 50 multiple-choice',
    'at least50 multiple-choice': 'at least 50 multiple-choice',
    'at least50 multiple-choice questions.': 'at least 50 multiple-choice questions.',
    'at least50 multiple-choice questions': 'at least 50 multiple-choice questions',
    'up to100 questions': 'up to 100 questions',
    'havefour plausible': 'have four plausible',
}
for k,v in replacements.items():
    s = s.replace(k,v)
# remove space before hyphen when it's used as prefix/suffix (e.g., 'ב -CompTIA' -> 'ב-CompTIA')
import re
s = re.sub(r'\s-\s*', '-', s)
s = re.sub(r'\s-([A-Za-z])', r'-\1', s)
# replace multiple spaces
s = re.sub(r' {2,}', ' ', s)
# ensure a blank line before headings
s = re.sub(r'\n(##)', r'\n\n\1', s)
p.write_text(s, encoding='utf-8')
print('Applied common token fixes')
