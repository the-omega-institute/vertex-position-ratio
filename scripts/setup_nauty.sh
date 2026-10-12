#!/bin/sh
# Local dependency build only; no installation or repository operations.
set -eu
cd "$(dirname "$0")/.."
mkdir -p tools
curl -L --fail https://pallini.di.uniroma1.it/nauty2_9_1.tar.gz -o tools/nauty2_9_1.tar.gz
python3 - <<'PY'
import hashlib
from pathlib import Path
actual=hashlib.sha256(Path('tools/nauty2_9_1.tar.gz').read_bytes()).hexdigest()
expected='488fa906d10a372c72d2364c5dee48e0f7307004fbe52c2bce50c52de8cd873e'
if actual!=expected:raise SystemExit('nauty source archive checksum mismatch')
PY
tar -xzf tools/nauty2_9_1.tar.gz -C tools
cd tools/nauty2_9_1
./configure
make -j1 geng
