# python3 -I tools/reports.py            — list the question reports students sent ("⚑ Report a problem")
# python3 -I tools/reports.py --block nephro   — only one block
# python3 -I tools/reports.py --delete QREPORT-nephro-1760000000000-ab12cd   — remove one once it's handled
#
# shared/app.js writes each report as its own document, syncs/QREPORT-<block>-<time>-<random>, in the
# Firestore project sync.js uses (no PIN or personal data: block, question id, reason, note, the answer
# picked, the first 160 characters of the stem). This lists them newest first.
import json, re, sys, pathlib, argparse, urllib.request, urllib.parse
from datetime import datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
SYNC = (ROOT / 'sync.js').read_text(encoding='utf-8')
PROJECT = re.search(r"projectId:\s*'([^']+)'", SYNC).group(1)
KEY = re.search(r"apiKey:\s*'([^']+)'", SYNC).group(1)
BASE = f'https://firestore.googleapis.com/v1/projects/{PROJECT}/databases/(default)/documents/syncs'
WHY = {'key': 'answer key wrong', 'explain': 'explanation wrong/unclear', 'typo': 'typo/wording', 'other': 'other'}

def get(url):
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)

def reports():
    out, token = [], ''
    while True:
        q = {'key': KEY, 'pageSize': 300, 'mask.fieldPaths': ['kind', 'block', 'qid', 'reason', 'note', 'exam', 'sdl', 'picked', 'stem', '_createdAt']}
        if token: q['pageToken'] = token
        page = get(BASE + '?' + urllib.parse.urlencode(q, doseq=True))
        for d in page.get('documents', []):
            name = d['name'].rsplit('/', 1)[1]
            if not name.startswith('QREPORT-'): continue
            f = {k: (v.get('stringValue') or v.get('timestampValue') or '') for k, v in d.get('fields', {}).items()}
            f['id'] = name
            out.append(f)
        token = page.get('nextPageToken')
        if not token: break
    return sorted(out, key=lambda r: r.get('_createdAt', ''), reverse=True)

a = argparse.ArgumentParser()
a.add_argument('--block'); a.add_argument('--delete'); a.add_argument('--json', action='store_true')
o = a.parse_args()
if o.delete:
    if not o.delete.startswith('QREPORT-'): raise SystemExit('only QREPORT-… documents can be deleted here')
    req = urllib.request.Request(f'{BASE}/{urllib.parse.quote(o.delete)}?key={KEY}', method='DELETE')
    urllib.request.urlopen(req, timeout=30); print('deleted', o.delete); sys.exit()
rs = [r for r in reports() if not o.block or r.get('block') == o.block]
if o.json: print(json.dumps(rs, indent=1, ensure_ascii=False)); sys.exit()
if not rs: print('no reports'); sys.exit()
for r in rs:
    when = r.get('_createdAt', '')[:16].replace('T', ' ')
    print(f"{when}  {r.get('block'):<10} q {r.get('qid'):<8} exam {r.get('exam') or '-'} · SDL {r.get('sdl') or '-'}  "
          f"[{WHY.get(r.get('reason'), r.get('reason'))}]" + (f"  picked {r['picked']}" if r.get('picked') else ''))
    if r.get('note'): print('    note:', r['note'])
    print('    stem:', r.get('stem', ''))
    print('    id:  ', r['id'])
print(f'{len(rs)} report(s)')
