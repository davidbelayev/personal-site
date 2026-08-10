from pathlib import Path
import re
p = Path('src/content/blog/security-plus-guide.md')
s = p.read_text(encoding='utf-8')
# remove unicode isolate/control chars commonly displayed as visible glyphs
for ch in ['\u2066','\u2067','\u2068','\u2069','\u206A','\u206B','\u206C','\u206D','\u206E','\u206F']:
    s = s.replace(ch, '')
# Also remove literal glyphs if present
s = s.replace('⁦','').replace('⁩','').replace('⁧','').replace('⁨','').replace('⁩','')
# Ensure space after markdown headings markers
s = re.sub(r'^(#{1,6})([^ \n#])', r'\1 \2', s, flags=re.MULTILINE)
# Insert space between Hebrew and Latin/digits/symbols where missing
he = '\u0590-\u05FF\uFB1D-\uFB4F'
# Build patterns using evaluated unicode ranges
pattern1 = rf'([{he}])([A-Za-z0-9@#%&\+\-_=:/\.\,\$\(\)\[\\\\])'
pattern2 = rf'([A-Za-z0-9@#%&\+\-_=:/\.\,\$\(\)\[\\\\])([{he}])'
s = re.sub(pattern1, r'\1 \2', s)
s = re.sub(pattern2, r'\1 \2', s)
# Fix common English concatenations that lost spaces (theofficial -> the official)
s = s.replace('theofficial', 'the official')
s = s.replace('practice-test', 'practice-test')
# Clean up spaces before punctuation
s = re.sub(r' +([.,:;!?%])', r'\1', s)
# Collapse multiple spaces (but preserve newlines)
s = re.sub(r'(?<=\S) {2,}(?=\S)', ' ', s)
# Trim trailing spaces on lines
s = '\n'.join([ln.rstrip() for ln in s.splitlines()]) + '\n'

p.write_text(s, encoding='utf-8')
print('Final cleanup applied to', p)
