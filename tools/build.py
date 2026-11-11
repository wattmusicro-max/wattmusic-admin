#!/usr/bin/env python3
"""Lipește modulele în ordinea din ORDINE.txt -> dist/<widget>.html (exact ce era în Elementor)."""
import os, hashlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = {'tm0admw': 'src/admin', 'tm0ofradm': 'src/oferte'}
os.makedirs(os.path.join(ROOT, 'dist'), exist_ok=True)
for wid, d in W.items():
    d = os.path.join(ROOT, d)
    names = [l.strip() for l in open(os.path.join(d, 'ORDINE.txt')) if l.strip()]
    out = ''.join(open(os.path.join(d, n), encoding='utf-8', newline='').read() for n in names)
    p = os.path.join(ROOT, 'dist', wid + '.html')
    open(p, 'w', encoding='utf-8', newline='').write(out)
    print(wid, len(out), hashlib.sha256(out.encode('utf-8')).hexdigest())
