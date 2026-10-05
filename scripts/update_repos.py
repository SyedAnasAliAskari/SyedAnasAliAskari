import json, os, re, urllib.request
from pathlib import Path
USER='SyedAnasAliAskari'
req=urllib.request.Request(f'https://api.github.com/users/{USER}/repos?sort=pushed&per_page=100',headers={'Accept':'application/vnd.github+json','User-Agent':'profile-readme-action'})
with urllib.request.urlopen(req, timeout=20) as r: repos=json.load(r)
repos=[x for x in repos if not x.get('fork') and x['name'] != USER][:6]
lines=['<table><tr>']
for i,r in enumerate(repos):
    if i and i%3==0: lines.append('</tr><tr>')
    desc=(r.get('description') or 'Public GitHub project').replace('|','·')
    lang=r.get('language') or 'Repository'
    lines.append(f'<td width="33%" valign="top"><b><a href="{r["html_url"]}">{r["name"]}</a></b><br><sub>{lang}</sub><br><br>{desc}</td>')
lines.append('</tr></table>')
block='\n'.join(lines)
p=Path('README.md'); text=p.read_text(encoding='utf-8')
text=re.sub(r'<!-- AUTO-REPOS:START -->.*?<!-- AUTO-REPOS:END -->',f'<!-- AUTO-REPOS:START -->\n{block}\n<!-- AUTO-REPOS:END -->',text,flags=re.S)
p.write_text(text,encoding='utf-8')
