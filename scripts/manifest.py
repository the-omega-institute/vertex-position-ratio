#!/usr/bin/env python3
"""Write or check SHA-256 hashes for the public package, excluding build outputs."""
import argparse
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as src:
        for block in iter(lambda: src.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()

def members():
    paths = [ROOT/name for name in ('.gitignore', 'README.md', 'LICENSE')]
    for folder in ('note', 'scripts', 'data'):
        paths.extend(p for p in (ROOT/folder).rglob('*')
                     if p.is_file() and '__pycache__' not in p.parts)
    return sorted(paths)

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', action='store_true', help='verify the existing manifest')
    args = ap.parse_args()
    manifest = ROOT/'SHA256SUMS'
    paths = members()
    if args.check:
        expected = dict(line.split('  ', 1)[::-1]
                        for line in manifest.read_text().splitlines())
        actual = {str(p.relative_to(ROOT)): digest(p) for p in paths}
        differences = sorted(name for name in expected.keys() | actual.keys()
                             if expected.get(name) != actual.get(name))
        if differences:
            raise SystemExit('Integrity check failed: '+', '.join(differences))
        print(f'Verified {len(actual)} package files')
    else:
        manifest.write_text(''.join(digest(p)+'  '+str(p.relative_to(ROOT))+'\n'
                                    for p in paths))
        print(f'Wrote hashes for {len(paths)} package files')

if __name__ == '__main__':
    main()
