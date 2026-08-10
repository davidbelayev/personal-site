from pathlib import Path
p = Path('src/content/blog/security-plus-guide.md')
s = p.read_text(encoding='utf-8')
# Fix frontmatter closing
s = s.replace("direction: 'rtl'---\n\n", "direction: 'rtl'\n---\n\n")
# Restore bullets that were merged
s = s.replace('-יצירת', '\n- יצירת')
s = s.replace('-קניית', '\n- קניית')
s = s.replace('-הרשמה', '\n- הרשמה')
# Fix merged percentage examples
s = s.replace('streak 1/2Test 2:', 'streak 1/2\nTest 2:')
s = s.replace('streak 0/2Test 3:', 'streak 0/2\nTest 3:')
s = s.replace('streak 1/2Test 4:', 'streak 1/2\nTest 4:')
# Fix Donotgroup -> Do not group
s = s.replace('Donotgroup', 'Do not group')
# Fix cryptographyQuestions -> cryptography Questions
s = s.replace('cryptographyQuestions', 'cryptography Questions')
s = s.replace('threat actorsQuestions', 'threat actors Questions')
# Ensure blank line after frontmatter (if missing)
if s.startswith('---'):
    parts = s.split('\n')
    # ensure there's a blank line after the second '---'
    try:
        idx = parts.index('---', 1)
        if parts[idx+1].strip() != '':
            parts.insert(idx+1, '')
            s = '\n'.join(parts)
    except ValueError:
        pass
p.write_text(s, encoding='utf-8')
print('Final small fixes applied')
