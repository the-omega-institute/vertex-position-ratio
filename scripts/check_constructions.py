#!/usr/bin/env python3
"""Finite checks of every edge, every claimed geodesic, and every selected vertex."""
import csv, json
from pathlib import Path
from constructions import original, subcubic, cubic, realize, fan
from graphs import bfs, position_numbers, local_numbers_bruteforce, encode
ROOT=Path(__file__).resolve().parents[1]

def check_family(kind,m):
    g,meta=globals()[kind](m)
    x,y,M=meta['x'],meta['y'],meta['M'];f=meta['f']
    dx=bfs(g,x);dy=bfs(g,y)
    assert min(dx)>=0 and len(f)==len(g)
    assert f[x]==0
    assert all(abs(f[u]-f[v])<=1 for u in range(len(g)) for v in g[u])
    assert len(set(meta['selected']))==(m*(m-1) if kind=='original' else m*m)
    assert all(dx[v]==M and f[v]==M for v in meta['selected'])
    covered=set()
    for p in meta['cover']:
        assert p[0]==y and len(p)==len(set(p))
        assert all(v in g[u] for u,v in zip(p,p[1:]))
        assert dy[p[-1]]==len(p)-1
        covered.update(p)
    assert len(covered)==len(g)
    degrees=[len(a) for a in g]
    if kind=='cubic':assert set(degrees)=={3}
    if kind=='subcubic':assert max(degrees)==3
    if kind=='original':
        # Each vertex has exactly one neighbor in the preceding y-layer.
        assert all(sum(dy[u]==dy[v]-1 for u in g[v])==1 for v in range(len(g)) if v!=y)
    return dict(family=kind,m=m,n=len(g),max_degree=max(degrees),sphere_radius=M,
                selected_count=len(meta['selected']),root_geodesic_cover=len(meta['cover']))

def main():
    records=[]
    # Deliberately sequential; adjacency lists and two BFS arrays only.
    for kind in ['original','subcubic','cubic']:
        for m in range(2,13):records.append(check_family(kind,m))
    for m in [20,40]:records.append(check_family('cubic',m))
    with (ROOT/'data/construction-checks.json').open('w') as f:json.dump(records,f,indent=2)
    realization_count=0
    with (ROOT/'data/realization-checks.csv').open('w') as f:
        w=csv.writer(f);w.writerow(['a','b','n','graph6','p'])
        for a in range(2,11):
            for b in range(a,3*a):
                g=realize(a,b);p=position_numbers(g)
                assert (min(p),max(p))==(a,b)
                w.writerow([a,b,len(g),encode(g),' '.join(map(str,p))])
                realization_count+=1
    fans=[]
    for n in range(2,9):
        p=local_numbers_bruteforce(fan(n))['monophonic']
        assert min(p)==2 and max(p)==n
        fans.append(dict(n=n,p=p))
    (ROOT/'data/fan-checks.json').write_text(json.dumps(fans,indent=2)+'\n')
    report=dict(construction_instances=len(records),realization_instances=realization_count,
                         fan_instances=len(fans))
    (ROOT/'data/construction-run.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))

if __name__=='__main__':main()
