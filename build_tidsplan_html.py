#!/usr/bin/env python3
"""Lager tidsplan.html (liggende tidslinje) fra tidsplan.md. Chromium -> PDF."""
import re, html

SRC, OUT = "tidsplan.md", "tidsplan.html"


def strip_md(s):
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s.strip())
    s = re.sub(r'\*(.+?)\*', r'\1', s)
    return html.escape(s.replace('`', '').strip())


lines = open(SRC, encoding='utf-8').read().split('\n')
header, rows, in_t = None, [], False
for ln in lines:
    s = ln.strip()
    if s.startswith('|') and 'Kl.' in s and 'Hendelse' in s:
        header = [c.strip() for c in s.strip('|').split('|')]; in_t = True; continue
    if in_t:
        if not s.startswith('|'):
            break
        if re.match(r'^\|[\s\-:|]+\|$', s):
            continue
        rows.append([c for c in s.strip('|').split('|')])

widths = ['6%', '38%', '14%', '8%', '34%']
th = ''.join(f'<th style="width:{widths[j] if j < len(widths) else "auto"}">{strip_md(h)}</th>'
             for j, h in enumerate(header))
trs = []
for cells in rows:
    major = cells[0].strip().startswith('**')
    tds = ''.join(f'<td>{strip_md(cells[j]) if j < len(cells) else ""}</td>'
                  for j in range(len(header)))
    trs.append(f'<tr class="{"major" if major else ""}">{tds}</tr>')

doc = f"""<!doctype html><html lang="no"><head><meta charset="utf-8">
<style>
@page {{ size: A4 landscape; margin: 11mm; }}
body {{ font-family: Calibri, 'Segoe UI', Arial, sans-serif; color:#111; }}
h1 {{ font-size: 16pt; margin: 0 0 6px; }}
.sub {{ color:#666; font-size:9pt; margin:0 0 8px; }}
table {{ width:100%; border-collapse:collapse; font-size:8.7pt; }}
th {{ background:#404040; color:#fff; text-align:left; padding:4px 5px; }}
td {{ border:1px solid #cfcfcf; padding:2.5px 5px; vertical-align:top; }}
tr.major td {{ background:#f3dcdc; font-weight:bold; }}
tr:nth-child(even):not(.major) td {{ background:#f7f7f7; }}
</style></head><body>
<h1>Tidsplan &ndash; Anders &amp; Michelles bryllup</h1>
<p class="sub">26. juni 2026 &middot; Maarud G&aring;rd &middot; Toastmaster: Fredrik</p>
<table><thead><tr>{th}</tr></thead><tbody>{''.join(trs)}</tbody></table>
</body></html>"""

open(OUT, 'w', encoding='utf-8').write(doc)
print(f"Skrev {OUT} ({len(rows)} rader)")
