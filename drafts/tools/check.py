# python3 -I check.py <module>   — validate a dynamic map module: problems (must fix) and layout warnings
import sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from dynlib import check
P, W, M, NEW = check(sys.argv[1])
print(f"{M.get('id')}: {len(NEW)} new cards, {len(M.get('nodes', []))} nodes, {len(M.get('dyn', {}).get('sites', []))} sites, {len(M.get('dyn', {}).get('flows', []))} flows")
for p in P: print('PROBLEM ', p)
for w in W: print('warning ', w)
print('OK' if not P else f'{len(P)} problems', '·', len(W), 'warnings')
