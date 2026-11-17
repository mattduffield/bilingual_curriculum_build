"""Rebuild the handout and runbook HTML/PDF from markdown (same look as the multimodal_ai handouts).
usage: python3 build.py"""
import re, subprocess
style = re.search(r'<style>.*?</style>', open('../multimodal_ai/SETUP-GUIDE.html').read(), re.S).group(0)
extra = """<style>
ul.task-list{list-style:none;margin-left:2pt}
ul.task-list li label{display:inline}
ul.task-list li{margin-bottom:3pt}
.box{display:inline-block;width:7.5pt;height:7.5pt;border:1pt solid #0b5394;border-radius:1.5pt;margin-right:5pt;vertical-align:-0.5pt}
.box.done{background:#0b5394}
pre code{background:none;padding:0;border-radius:0;font-size:1em}
pre{break-inside:avoid}
</style>"""
for name in ['WALKTHROUGH', 'PROMPTS', 'SHOW-GUIDE', 'TEACHER-WORKFLOW', 'LIVE-RUNBOOK', 'SETUP-GUIDE']:
    body = subprocess.run(['pandoc', '-f', 'gfm', '-t', 'html5', '--wrap=none', name + '.md'], capture_output=True, text=True).stdout
    body = re.sub(r'<hr />\s*<p><em>(Full Stack Devs PDX[^<]*)</em></p>\s*$', r'<div class="foot">\1</div>', body.strip())
    # WeasyPrint renders form checkboxes as blocks; draw inline boxes instead
    body = re.sub(r'<input type="checkbox" checked="" />', '<span class="box done"></span>', body)
    body = re.sub(r'<input type="checkbox" />', '<span class="box"></span>', body)
    open(name + '.html', 'w').write('<!DOCTYPE html><html><head><meta charset="UTF-8">' + style + extra + '</head><body>\n' + body + '\n</body></html>\n')
    subprocess.run(['weasyprint', name + '.html', name + '.pdf'], stderr=subprocess.DEVNULL)
    pages = subprocess.run(['pdfinfo', name + '.pdf'], capture_output=True, text=True).stdout
    print(name + '.pdf', re.search(r'Pages:\s+(\d+)', pages).group(1), 'pages')

# One printable review pack: walkthrough, prompts, runbook, attendee handout, then the brief
parts = ['WALKTHROUGH.pdf', 'PROMPTS.pdf', 'SHOW-GUIDE.pdf', 'TEACHER-WORKFLOW.pdf', 'LIVE-RUNBOOK.pdf', 'SETUP-GUIDE.pdf', 'project-brief.pdf']
subprocess.run(['pdfunite'] + parts + ['PRINT-PACK.pdf'], check=True)
pages = subprocess.run(['pdfinfo', 'PRINT-PACK.pdf'], capture_output=True, text=True).stdout
print('PRINT-PACK.pdf', re.search(r'Pages:\s+(\d+)', pages).group(1), 'pages')
