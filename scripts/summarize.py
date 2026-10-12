#!/usr/bin/env python3
"""Stream result rows into exact summaries and minimum-order witnesses."""
import csv, gzip, json
from collections import Counter
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def op(path):return gzip.open(path,'rt') if path.suffix=='.gz' else path.open()
def main():
    summaries=[];witness={}
    for kind in ('cubic','subcubic','connected'):
        # Prefer fresh plain CSVs per order, while retaining compressed orders
        # that were not regenerated during a partial enumeration.
        by_order={int(p.name.split('-')[1].split('.')[0]):p
                  for p in (ROOT/'data').glob(kind+'-*.csv.gz')}
        by_order.update({int(p.name.split('-')[1].split('.')[0]):p
                         for p in (ROOT/'data').glob(kind+'-*.csv')})
        paths=list(by_order.values())
        for path in sorted(paths,key=lambda p:int(p.name.split('-')[1].split('.')[0])):
            hist=Counter();count=0;extremal=[];ratio=Fraction(0)
            with op(path) as f:
                for r in csv.DictReader(f):
                    n,a,b=map(int,(r['n'],r['vp_minus'],r['vp']));hist[a,b]+=1;count+=1
                    q=Fraction(b,a)
                    if q>ratio:ratio=q;extremal=[r['graph6']]
                    elif q==ratio and len(extremal)<5:extremal.append(r['graph6'])
                    if kind=='connected' and (a,b) not in witness:witness[a,b]=r
            summaries.append(dict(kind=kind,n=n,count=count,max_ratio=str(ratio),
                                  extremal_graph6=extremal,pair_counts={f'{a},{b}':c for (a,b),c in sorted(hist.items())}))
    (ROOT/'data/summary.json').write_text(json.dumps(summaries,indent=2)+'\n')
    with (ROOT/'data/summary.csv').open('w') as f:
        w=csv.writer(f);w.writerow(['class','n','count','max_ratio','witness_graph6'])
        for r in summaries:w.writerow([r['kind'],r['n'],r['count'],r['max_ratio'],r['extremal_graph6'][0]])
    with (ROOT/'data/pair-witnesses.csv').open('w') as f:
        w=csv.writer(f);w.writerow(['a','b','minimum_order_through_9','graph6','p'])
        for (a,b),r in sorted(witness.items()):w.writerow([a,b,r['n'],r['graph6'],r['p']])
    print((ROOT/'data/summary.csv').read_text())
if __name__=='__main__':main()
