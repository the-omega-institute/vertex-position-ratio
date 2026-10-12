# Unbounded vertex-position ratios in cubic graphs and local position problems

**Haobo Ma and Wenlin Zhang · 2026**

We prove that the ratio `vp(G)/vp^-(G)` is unbounded over connected graphs, giving a negative answer to Problem 2.4 of Thankachy, Thomas, Chandran, Tuite, Di Stefano and Erskine, [*On the Vertex Position Number of Graphs*, arXiv:2209.00359v2](https://arxiv.org/abs/2209.00359v2). The ratio remains unbounded among connected cubic graphs, with a construction giving growth at least of order `n^(1/3)` along its orders. The corresponding ratios for observer-based local monophonic position and local mutual visibility are also unbounded. We realize every integer pair `(vp^-,vp)=(a,b)` with `a>=2` and `a<=b<=3a-1`, and classify the case `a=1` completely. Exact finite computations give additional pair witnesses and ratio extrema; the full pair classification and optimal growth as a function of cubic order remain open.

Read the complete arguments in [the note (PDF)](note/note.pdf), or use [the TeX source](note/note.tex). This directory is the note-and-code package intended for <https://github.com/the-omega-institute/vertex-position-ratio>.

## Definitions and scope

Graphs are finite, simple, undirected and connected. For observer `x`, an `x`-position set contains no selected vertex on a shortest path from `x` to another selected vertex. Let `p_x(G)` be its maximum size. Then `vp^-(G)=min_x p_x(G)` and `vp(G)=max_x p_x(G)`. The minus sign denotes a minimum **over observers**, not the size of a smallest maximal set. The original definition gives `p_x(K_1)=1`; for a graph of order at least two, a maximum set can be chosen to exclude its observer.

The two local variants in Section 4 of the note exclude the observer and concern graphs of order at least two. Local monophonic position forbids another selected vertex on **any induced** observer-to-target path. Local mutual visibility requires **at least one shortest** observer-to-target path avoiding the other selected vertices. It imposes this condition between the observer and each target. Counting the observer in local mutual visibility adds one to each observer value and preserves unboundedness.

## What is proved

- **Connected graphs:** the original family `G_m`, `m>=2`, has order `7m^2+5m+1`, `vp^-(G_m)<=2m+1`, and `vp(G_m)>=m(m-1)`. Hence its ratio is at least `m(m-1)/(2m+1)` and tends to infinity.
- **Cubic graphs:** let `k` be the least power of two at least `2m+1` and `N_m=3m^3+13m^2+13m+3+2k`. The connected cubic family `C_m` has order `2N_m+4k`, `vp^-(C_m)<=3k`, and `vp(C_m)>=m^2`. Its ratio is at least `m^2/(3k)`. These are bounds for the large graphs, rather than computed equalities for their global parameters.
- **Fixed maximum degree:** the maximum ratio for maximum degree at most two is 2. For every fixed degree ceiling at least three, the ratio is unbounded. The note also treats maximum degree exactly a fixed value greater than three.
- **Local variants:** the fan `K_1 join P_n`, `n>=2`, has lower and upper local monophonic numbers 2 and `n`. The original family `G_m` proves unbounded local mutual-visibility ratios.
- **Realizable pairs:** the only pairs with `a=1` are `(1,1)` and `(1,2)`. Every pair with `a>=2` and `a<=b<=3a-1` is realized, and every diagonal pair `(a,a)` is realized by `K_(a+1)`. Section 5 separately credits the already known pairs `(a,6a-4)`, `a>=3`, to Lemma 2.3 of the cited paper.

The [pinned Lean source for the original unboundedness construction](https://github.com/the-omega-institute/trureturing/blob/9cba9d04fef654e1e09d10813836d884854c0b3f/D5/S3/Combinatorics/PositionSets/VertexPositionRatioRefutation.lean) formalizes the original family and its global bounds. The cubic, local-variant, and realization results have complete mathematical proofs in the note. Their formalization is outside the scope of that Lean file. Preparing this package did not include a Lean build.

## What is computed

Enumeration uses nauty **2.9.1** `geng`, one representative per isomorphism class. Every observer of every generated graph is evaluated. Connectivity and the stated degree limits are the generation restrictions; no girth, bipartiteness, or stronger connectivity condition is imposed.

| Class | Orders | Total graph records | Maximum ratios by increasing order |
| --- | --- | ---: | --- |
| Connected cubic | 4, 6, ..., 20 | 556,471 | `1, 1, 4/3, 2, 2, 7/3, 8/3, 3, 3` |
| Connected | 1, 2, ..., 9 | 273,193 | `1, 1, 2, 2, 2, 2, 5/2, 5/2, 3` |
| Connected, maximum degree at most three | 1, 2, ..., 10 | 2,571 | `1, 1, 2, 2, 2, 2, 2, 5/2, 5/2, 5/2` |

The classes overlap: **832,235 records** across these searches do not mean that many distinct graphs in their union. Their result vectors contain **13,496,353 observer values**.

The connected search gives 27 distinct pairs, with minimum-order witnesses through order nine. For `(2,b)`, `b=2,3,4,5,6`, the minimum orders are `3,4,5,7,9`. In particular, an explicit nine-vertex graph realizes `(2,6)`, outside the interval supplied by the realization theorem. The cubic search also gives `(3,9)` at order 18.

The packaged check scripts reproduce these finite checks:

- All 35 construction certificates: each of the original, subcubic and cubic families for `m=2,...,12`, plus cubic `m=20,40`. Checks cover edge potentials, root geodesic covers, and selected sphere vertices. `C_40` has 427,670 vertices, 1,600 selected sphere vertices, and a cover by 384 root geodesics, giving a ratio at least `25/6`.
- All 108 realization pairs with `2<=a<=10` and `a<=b<=3a-1`, using one admissible layer split for each off-diagonal pair; fans with path order `2,...,8`.
- Exhaustive subset checks on all 143 connected graphs through order six, including 142 nontrivial graphs for the literal local definitions; the tree formula on 81 subcubic trees of orders 3 through 10; and independent position-set subset checks on 50 cubic graphs (all 27 through order ten and 23 extremal representatives at larger orders).

Section 6 of the corrected note also reports a separate independent review: a full antichain-search recomputation, all admissible layer splits through `a=15`, diagonal examples through `a=30`, and fans through path order ten. Those separate review programs and outputs are not included here. The commands below reproduce the archived enumeration and the finite checks supplied with this package; the all-parameter results follow from the note's proofs.

## What remains open

The optimal maximum ratio as a function of cubic order is open: our family gives an `Omega(n^(1/3))` lower bound along its orders, while the general upper bounds in the note can be linear in `n`. A finite maximum of 3 through cubic order 20 is a statement about that range. The full classification of pairs beyond the proved region and known families is also open, including whether `(2,b)` can be realized for any `b>=7`.

## Contents and data formats

| Location | Contents |
| --- | --- |
| `note/note.pdf`, `note/note.tex` | The corrected eight-page note and its self-contained source |
| `scripts/position.cpp` | Exact C++17 vertex-position solver |
| `scripts/graphs.py`, `scripts/constructions.py` | Python graph utilities and explicit constructions |
| `scripts/enumerate.py`, `scripts/setup_nauty.sh` | Sequential enumeration and a checksum-pinned local dependency build |
| `scripts/summarize.py`, `scripts/crosscheck.py`, `scripts/check_constructions.py` | Summaries, independent subset checks, and construction checks |
| `scripts/pack_data.py`, `scripts/manifest.py` | Deterministic compression and package integrity hashes |
| `data/{class}-{n}.g6.gz`, `data/{class}-{n}.csv.gz` | All enumeration inputs and per-observer outputs for the three classes |
| `data/summary.csv`, `data/summary.json` | Counts, exact ratio extrema, complete pair frequencies, and example extrema |
| `data/pair-witnesses.csv` | Minimum-order witnesses and their observer vectors |
| `data/realization-checks.csv`, `data/construction-checks.json` | Exact realization values and large-family certificate metadata |
| `data/fan-checks.json`, `data/local-small.json` | Finite local-variant values |
| `data/*-run.jsonl`, `data/construction-run.json`, `data/crosscheck-report.json` | Generation options and completed check counts |
| `LICENSE`, `.gitignore`, `SHA256SUMS` | Licensing, build exclusions, and release-file hashes |

Each enumeration CSV has columns `graph6,n,vp_minus,vp,p`. The space-separated `p` vector follows the graph6 vertex order `0,...,n-1`. The CSV retains every graph; `summary.json` retains at most five example extrema per order as well as **all** pair frequencies. Ratios are stored as exact fractions. Run records contain generation options and check scope, without machine-specific resource measurements.

`local-small.json` retains the archived optional singleton convention `[1]` for both local variants. The literal observer-excluding definitions would give zero on `K_1`; the note's local theorems and local ratios apply to graphs of order at least two. The ordinary vertex-position singleton value is 1.

## Reproduce

Run every command below from the directory containing this README. Computation uses Python **3.10 or later**, the standard library, and a C++17 compiler. Full graph generation additionally needs `curl`, `tar`, `make`, and a C compiler. The note build needs Tectonic or a LaTeX installation with the packages listed in `note/note.tex`. Poppler is optional for PDF inspection.

First verify the supplied package:

```sh
python3 scripts/manifest.py --check
```

To summarize and check the supplied compressed data, without downloading dependencies or compiling a solver:

```sh
python3 scripts/summarize.py
python3 scripts/crosscheck.py
python3 scripts/check_constructions.py
```

To regenerate every graph and every result vector:

```sh
sh scripts/setup_nauty.sh
mkdir -p tools
c++ -O3 -std=c++17 scripts/position.cpp -o tools/position

python3 scripts/enumerate.py --geng tools/nauty2_9_1/geng --solver tools/position --class cubic --max-order 20
python3 scripts/enumerate.py --geng tools/nauty2_9_1/geng --solver tools/position --class connected --max-order 9
python3 scripts/enumerate.py --geng tools/nauty2_9_1/geng --solver tools/position --class subcubic --max-order 10

python3 scripts/summarize.py
python3 scripts/crosscheck.py
python3 scripts/check_constructions.py
python3 scripts/pack_data.py
python3 scripts/manifest.py --check
```

`setup_nauty.sh` downloads the official `nauty2_9_1.tar.gz`, verifies SHA-256 `488fa906d10a372c72d2364c5dee48e0f7307004fbe52c2bce50c52de8cd873e`, and builds `geng` under `tools/`. The generation commands are `geng -cq -d3 -D3 n` for cubic graphs, `geng -cq n` for connected graphs, and `geng -cq -D3 n` for subcubic graphs. Cubic enumeration skips odd orders and orders below four. Generation of each input finishes before its analysis starts.

Enumeration overwrites plain graph/result files and replaces the corresponding per-order metadata without duplicating records. Summaries select fresh plain files per order when present and otherwise read compressed files. Compression writes gzip streams with an empty filename and zero timestamp, then removes the plain intermediates. Checks overwrite their corresponding reports and certificates. If you intentionally modify package contents, refresh and check the manifest with:

```sh
python3 scripts/manifest.py
python3 scripts/manifest.py --check
```

The exact solver uses BFS distances and maximum matching on **all strict comparable pairs** of the geodesic order, giving `p_x=(n-1)-matching_size` for `n>=2`. It treats `K_1` separately as 1. The direct chain-cover/antichain proof is in Section 6 of the note. The C++ graph6 parser supports orders 1 through 62 and rejects disconnected graphs. Large-family checks use adjacency lists and root-distance arrays to verify certificates rather than compute their exact global extrema. Keep Python assertions enabled when running checks.

To rebuild the note without replacing the supplied PDF:

```sh
mkdir -p tmp/pdfs
tectonic --keep-logs -o tmp/pdfs note/note.tex
```

Alternatively:

```sh
mkdir -p tmp/pdfs
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp/pdfs note/note.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=tmp/pdfs note/note.tex
```

Optional visual inspection of the rebuilt PDF:

```sh
pdfinfo tmp/pdfs/note.pdf
pdftoppm -r 110 -png tmp/pdfs/note.pdf tmp/pdfs/page
```

The supplied corrected PDF is retained as the release artifact. Rebuilding may change PDF metadata and byte hashes while preserving the mathematical content.

## License

The note, documentation, and data are licensed under **CC BY 4.0**. Original code in `scripts/` is licensed under **MIT**. See [LICENSE](LICENSE) for the scope, CC BY 4.0 terms link, and full MIT text. Downloaded dependencies retain their own licenses.

## How to cite

```bibtex
@misc{MaZhang2026vp,
  author = {Haobo Ma and Wenlin Zhang},
  title = {Unbounded vertex-position ratios in cubic graphs and local position problems},
  year = {2026},
  howpublished = {\url{https://github.com/the-omega-institute/vertex-position-ratio}},
  note = {Note and code}
}
```
