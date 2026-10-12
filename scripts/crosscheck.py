#!/usr/bin/env python3
"""Independent exhaustive-subset checks, and the credited tree formula."""
import csv, gzip, json
from pathlib import Path
from graphs import decode, local_numbers_bruteforce, position_numbers
ROOT=Path(__file__).resolve().parents[1]
def op(p):return gzip.open(p,'rt') if p.suffix=='.gz' else p.open()
def path_for(kind,n):
    p=ROOT/'data'/f'{kind}-{n}.csv'
    return p if p.exists() else p.with_suffix('.csv.gz')
def main():
    output=[];trees=0
    for n in range(1,7):
        with op(path_for('connected',n)) as f:
            for row in csv.DictReader(f):
                g=decode(row['graph6']);p=list(map(int,row['p'].split()))
                brute=local_numbers_bruteforce(g)
                assert brute['vp']==p
                output.append(dict(graph6=row['graph6'],n=n,**brute))
    with (ROOT/'data/local-small.json').open('w') as f:json.dump(output,f,indent=2)
    for n in range(3,11):
        with op(path_for('subcubic',n)) as f:
            for row in csv.DictReader(f):
                g=decode(row['graph6'])
                if sum(map(len,g))!=2*(n-1):continue
                leaves=sum(len(a)==1 for a in g)
                expected=[leaves-1 if len(a)==1 else leaves for a in g]
                assert list(map(int,row['p'].split()))==expected;trees+=1
    # Exact brute-force subset validation on up to five extremal cubic witnesses
    # per order through 20, as well as all cubic graphs through order 10.
    summary=json.loads((ROOT/'data/summary.json').read_text());checked=0
    for r in summary:
        if r['kind']!='cubic':continue
        chosen=set(r['extremal_graph6'])
        with op(path_for('cubic',r['n'])) as f:
            rows=[x for x in csv.DictReader(f) if r['n']<=10 or x['graph6'] in chosen]
        for row in rows:
            s=row['graph6'];g=decode(s);p=position_numbers(g);n=len(g)
            assert p==list(map(int,row['p'].split()))
            from graphs import bfs
            d=[bfs(g,u) for u in range(n)]
            # Branch over independent subsets of the comparability graph;
            # this uses no matching theorem or matching implementation.
            for root in range(n):
                vertices=[u for u in range(n) if u!=root]
                conflict=[0]*n
                for u in vertices:
                    for v in vertices:
                        if u!=v and (d[root][u]+d[u][v]==d[root][v] or d[root][v]+d[u][v]==d[root][u]):conflict[u]|=1<<v
                best=0
                def visit(mask,size):
                    nonlocal best
                    if size+mask.bit_count()<=best:return
                    if not mask:best=max(best,size);return
                    u=(mask&-mask).bit_length()-1;rest=mask&~(1<<u)
                    visit(rest&~conflict[u],size+1);visit(rest,size)
                visit(sum(1<<u for u in vertices),0)
                assert best==p[root]
            checked+=1
    report=dict(all_connected_subset_checks_through_6=len(output),
                subcubic_tree_checks_orders_3_through_10=trees,
                cubic_independent_subset_checks=checked)
    (ROOT/'data/crosscheck-report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))
if __name__=='__main__':main()
