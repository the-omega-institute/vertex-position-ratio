#!/usr/bin/env python3
"""Compress the large enumeration files reproducibly, one file at a time."""
import gzip, shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
for kind in ('cubic','subcubic','connected'):
    for ext in ('csv','g6'):
        for p in sorted((ROOT/'data').glob(f'{kind}-*.{ext}')):
            with p.open('rb') as src, p.with_suffix(p.suffix+'.gz').open('wb') as out:
                with gzip.GzipFile(filename='',mode='wb',fileobj=out,mtime=0) as dst:
                    shutil.copyfileobj(src,dst,1024*1024)
            p.unlink()
