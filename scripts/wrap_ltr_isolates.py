import re
from pathlib import Path

p = Path('src/content/blog/security-plus-guide.md')
s = p.read_text(encoding='utf-8')

# Split frontmatter
if s.startswith('---'):
    parts = s.split('---', 2)
    # parts: ['', '\n...front...', '\nbody...']
    if len(parts) >= 3:
        front = '---' + parts[1] + '---'
        body = parts[2]
    else:
        front = ''
        body = s
else:
    front = ''
    body = s

lines = body.splitlines(True)
out_lines = []
fence = False

# LRI and PDI
LRI = '\u2066'
PDI = '\u2069'

# regex to find LTR runs (letters, digits, common symbols), avoid wrapping standalone punctuation
ltr_re = re.compile(r'([A-Za-z0-9@#%&\+\-_=:\/\.\?,]+)')

for line in lines:
    # detect fenced code blocks
    if line.strip().startswith('```'):
        fence = not fence
        out_lines.append(line)
        continue
    if fence:
        out_lines.append(line)
        continue
    # process inline code by splitting on backticks
    parts = re.split(r'(`+)', line)
    for i in range(0, len(parts)):
        if parts[i].startswith('`'):
            # code delimiter or code content, leave as-is
            continue
        # Only process non-code parts (even indices)
        if i % 2 == 0:
            # Replace LTR runs that are not already wrapped
            def wrap(match):
                txt = match.group(1)
                if LRI in txt or PDI in txt:
                    return txt
                return LRI + txt + PDI
            parts[i] = ltr_re.sub(wrap, parts[i])
    out_lines.append(''.join(parts))

new_body = ''.join(out_lines)
new = front + new_body
p.write_text(new, encoding='utf-8')
print('Wrapped LTR runs in', p)
