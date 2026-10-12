#!/usr/bin/env python3
"""Sequential generation and analysis. No simultaneous worker processes."""
import argparse, json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--geng', required=True)
    ap.add_argument('--solver', required=True)
    ap.add_argument('--class', dest='kind', choices=['cubic', 'subcubic', 'connected'], required=True)
    ap.add_argument('--min-order', type=int, default=1)
    ap.add_argument('--max-order', type=int, required=True)
    args = ap.parse_args()
    if not 1 <= args.min_order <= args.max_order <= 62:
        ap.error('orders must satisfy 1 <= min-order <= max-order <= 62')
    (ROOT / 'data').mkdir(exist_ok=True)
    log = ROOT / 'data' / (args.kind + '-run.jsonl')
    records = {}
    if log.exists():
        for line in log.read_text().splitlines():
            record = json.loads(line)
            records[record['n']] = record
    for n in range(args.min_order, args.max_order+1):
        if args.kind == 'cubic' and (n < 4 or n % 2): continue
        stem = ROOT / 'data' / f'{args.kind}-{n}'
        options = ['-cq']
        if args.kind == 'cubic': options += ['-d3', '-D3']
        if args.kind == 'subcubic': options += ['-D3']
        with stem.with_suffix('.g6').open('w') as f:
            subprocess.run([args.geng, *options, str(n)], stdout=f, check=True)
        subprocess.run([args.solver, str(stem.with_suffix('.g6')), str(stem.with_suffix('.csv'))], check=True)
        record = dict(kind=args.kind, n=n, generation_options=[*options, str(n)])
        records[n] = record
        log.write_text(''.join(json.dumps(records[order])+'\n' for order in sorted(records)))
        print(json.dumps(record), flush=True)

if __name__ == '__main__': main()
