# python3 -I shot.py <module> [--dyn o:drug:x,t:adh] [--look x0,y0,x1,y1] [--out file.png] [--dark] [--moving]
# builds a scratch copy of the site with your map and screenshots it with headless Chrome (whole map, or a region with --look)
import sys, argparse, pathlib
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from dynlib import site_for, shoot, SCRATCH, CHROME
if not CHROME: raise SystemExit('shot.py needs Chrome/Chromium on this machine — none found; check.py works without it')
a = argparse.ArgumentParser(); a.add_argument('mod'); a.add_argument('--dyn', default=''); a.add_argument('--look', default='')
a.add_argument('--out', default=''); a.add_argument('--dark', action='store_true'); a.add_argument('--moving', action='store_true')
a.add_argument('--nobuild', action='store_true')
o = a.parse_args()
if o.nobuild:
    import importlib; site = SCRATCH / o.mod; mid = importlib.import_module(o.mod).MAP['id']
else:
    site, M = site_for(o.mod); mid = M['id']
out = o.out or str(SCRATCH / f'{o.mod}-{(o.dyn or "default").replace(":", "_").replace(",", "+")}{"-look" if o.look else ""}{"-dark" if o.dark else ""}.png')
shoot(site, mid, out, o.dyn, o.look, still=not o.moving, dark=o.dark)
print(out)
