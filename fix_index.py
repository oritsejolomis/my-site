from pathlib import Path

p = Path('index.html')
text = p.read_text(encoding='utf-8')
start = text.index('<style>')
end = text.index('</style>', start) + len('</style>')
replacement = '  <link rel="stylesheet" href="styles.css">\n'
p.write_text(text[:start] + replacement + text[end:], encoding='utf-8')
