import json
import os
T = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'titles.json')))
def full(book, ch):
    for v in T.values():
        if v['book'] == book and str(v['ch']) == str(ch):
            return f"{book} {ch} — {v['title']}" if str(ch).startswith('Appendix') else f"{book} ch {ch} — {v['title']}"
    raise KeyError((book, ch))
def L(xs): return '[' + ','.join(json.dumps(x, ensure_ascii=False) for x in xs) + ']'
CARDS = []
def card(id, n, k, p, enz, hi, mech, find, labs, buzz, src, tx, q, alias='', fa='', ref=None):
    CARDS.append(dict(id=id, n=n, k=k, p=p, enz=enz, hi=hi, mech=mech, find=find, labs=labs, buzz=buzz, src=src, tx=tx, q=q, alias=alias, fa=fa, ref=ref or []))
def card_js(c):
    head = (f'{c["id"]}:{{n:{json.dumps(c["n"], ensure_ascii=False)},' + (f'alias:{json.dumps(c["alias"], ensure_ascii=False)},' if c['alias'] else '') +
            f'k:"{c["k"]}",p:"{c["p"]}",enz:{json.dumps(c["enz"], ensure_ascii=False)},inh:"—",' + (f'fa:"{c["fa"]}",' if c['fa'] else '') + f'hi:{c["hi"]},')
    lines = [head, f' mech:{json.dumps(c["mech"], ensure_ascii=False)},', f' find:{L(c["find"])},', f' labs:{L(c["labs"])},', f' buzz:{L(c["buzz"])},']
    if c['src']: lines.append(f' src:{L(c["src"])},')
    tail = f' tx:{L(c["tx"])},q:{L(c["q"])}'
    if c['ref']:
        tail += ',\n ref:[' + ','.join('{' + ','.join(f'{k}:{json.dumps(r[k], ensure_ascii=False)}' for k in ('a','t','j','y','pmid','doi')) + '}' for r in c['ref']) + ']'
    lines.append(tail + '},')
    return '\n'.join(lines)
