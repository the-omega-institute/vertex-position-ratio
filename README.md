# Sharp growth of vertex-position ratios and realizable pairs

**Haobo Ma and Wenlin Zhang · 2026**

We prove that the largest ratio `vp(G)/vp^-(G)` among connected cubic graphs of order `n` is `Theta(n/log n)` for every sufficiently large even `n`, sharpening the negative answer to Problem 2.4 of Thankachy, Thomas, Chandran, Tuite, Di Stefano and Erskine, [*On the Vertex Position Number of Graphs*, arXiv:2209.00359v2](https://arxiv.org/abs/2209.00359v2). For connected graphs of maximum degree exactly `Delta`, the largest ratio is `Theta(n/(Delta+log n))`, uniformly for `3<=Delta<=n-1`; with maximum degree at most `Delta>=3`, it is `Theta(n/log n)`. The observer-based local monophonic-position and local mutual-visibility ratios are also unbounded, with the latter growing linearly along a connected cubic family. The realizable pairs `(vp^-,vp)=(a,b)` with `a<=2` are exactly `(1,1)`, `(1,2)` and `(2,b)` for `2<=b<=10`; every integer pair with `a>=2` and `a<=b<=3a-1` is realizable. The largest upper parameter in each row, `B(a)=max{vp(G):vp^-(G)=a}`, exists and satisfies `2^(a-1)<=B(a)<=(2a+1)4^a` for `a>=2`, so `B(a)=2^Theta(a)`.

Read the complete arguments in [the note (PDF)](note/note.pdf), or use [the TeX source](note/note.tex). This directory is the note-and-code package intended for <https://github.com/the-omega-institute/vertex-position-ratio>.

## Definitions and scope

Graphs are finite, simple, undirected and connected. For observer `x`, an `x`-position set contains no selected vertex on a shortest path from `x` to another selected vertex. Let `p_x(G)` be its maximum size. Then `vp^-(G)=min_x p_x(G)` and `vp(G)=max_x p_x(G)`. The minus sign denotes a minimum **over observers**, not the size of a smallest maximal set. The original definition gives `p_x(K_1)=1`; for a graph of order at least two, a maximum set can be chosen to exclude its observer.

The two local variants in Section 5 of the note exclude the observer and concern graphs of order at least two. Local monophonic position forbids another selected vertex on **any induced** observer-to-target path. Local mutual visibility requires **at least one shortest** observer-to-target path avoiding the other selected vertices; the note uses the standard term **vertex visibility** for this condition and writes its lower and upper parameters as `vv^-` and `vv`. It imposes this condition between the observer and each target, without requiring mutual visibility between selected vertices. Counting the observer in vertex visibility adds one to each observer value and preserves unboundedness.

## What is proved

- **General upper bounds:** writing `a=vp^-(G)` and `b=vp(G)`, every connected graph of order `n>=2` satisfies `b<=(2a+1)4^a` and `b/a<=4n/log_2 n`. The proof bounds geodesic antichains using a cover by shortest paths.
- **Connected cubic graphs:** the maximum ratio is `Theta(n/log n)` for every sufficiently large even `n`. The new family `C^(h)` has order `Theta(h*2^h)`, linearly many vertices in a position set for one observer, and a cover by `O(h)` geodesics from another. Padding attains every sufficiently large even order. In particular, `C^(10)` has 417,454 vertices, `vp>=8,160`, `vp^-<=96`, and ratio at least 85. These are proved bounds, not computed equalities for its global parameters.
- **Maximum degree:** for maximum degree at most `Delta>=3`, the maximum ratio is `Theta(n/log n)` for all sufficiently large `n`. For maximum degree exactly `Delta`, it is `Theta(n/(Delta+log n))`, uniformly for `3<=Delta<=n-1`, with absolute constants and a threshold independent of `Delta`. For maximum degree at most two, the maximum is 2 once `n>=3`.
- **Local monophonic position:** the fan `K_1 join P_n`, `n>=2`, has lower and upper values 2 and `n`, so its ratio is exactly `n/2`.
- **Local mutual visibility (vertex visibility):** for every `t>=1`, a connected cubic graph `D_t` has order `4t+2` and `vv(D_t)/vv^-(D_t)>=t/7`. Together with the general linear upper bound, this gives linear growth along the family.
- **Realizable pairs:** the pairs with `a<=2` are exactly `(1,1)`, `(1,2)` and `(2,b)` for `2<=b<=10`. Explicit 27-vertex subcubic graphs realize `(2,b)` for `6<=b<=10`, and the note proves that `a=2` forces `b<=10`. Every integer pair with `a>=2` and `a<=b<=3a-1` is realized, with diagonal pairs supplied by `K_(a+1)`. Section 4 separately credits the already known pairs `(a,6a-4)`, `a>=3`, to Lemma 2.3 of the cited paper.
- **Exponential row growth:** the maximum `B(a)=max{vp(G):vp^-(G)=a}` exists and satisfies `2^(a-1)<=B(a)<=(2a+1)4^a` for every `a>=2`, hence `B(a)=2^Theta(a)`.

The [pinned Lean source for the original unboundedness construction](https://github.com/the-omega-institute/trureturing/blob/9cba9d04fef654e1e09d10813836d884854c0b3f/D5/S3/Combinatorics/PositionSets/VertexPositionRatioRefutation.lean) formalizes the original family and its global bounds. The final note gives mathematical proofs of the sharp growth bounds, local-variant results, pair classification and exponential row bounds; these results are outside the scope of that Lean file. Preparing this package did not include a Lean build.

## What is computed

The packaged scripts and data retain the earlier enumeration and construction checks. They do not reproduce all of the additional computations reported in the final note. The archived enumeration uses nauty **2.9.1** `geng`, one representative per isomorphism class. Every observer of every generated graph is evaluated. Connectivity and the stated degree limits are the generation restrictions; no girth, bipartiteness, or stronger connectivity condition is imposed.

| Class | Orders | Total graph records | Maximum ratios by increasing order |
| --- | --- | ---: | --- |
| Connected cubic | 4, 6, ..., 20 | 556,471 | `1, 1, 4/3, 2, 2, 7/3, 8/3, 3, 3` |
| Connected | 1, 2, ..., 9 | 273,193 | `1, 1, 2, 2, 2, 2, 5/2, 5/2, 3` |
| Connected, maximum degree at most three | 1, 2, ..., 10 | 2,571 | `1, 1, 2, 2, 2, 2, 2, 5/2, 5/2, 5/2` |

The classes overlap: **832,235 records** across these searches do not mean that many distinct graphs in their union. Their result vectors contain **13,496,353 observer values**.

The connected search gives 27 distinct pairs, with minimum-order witnesses through order nine. For `(2,b)`, `b=2,3,4,5,6`, the minimum orders are `3,4,5,7,9`. In particular, an explicit nine-vertex graph realizes `(2,6)`, outside the interval supplied by the realization theorem. The cubic search also gives `(3,9)` at order 18.

The packaged check scripts reproduce these finite checks:

- All 35 construction certificates for the **earlier families**: each of the original, subcubic and cubic families for `m=2,...,12`, plus cubic `m=20,40`. Checks cover edge potentials, root geodesic covers, and selected sphere vertices. The earlier `C_40` has 427,670 vertices, 1,600 selected sphere vertices, and a cover by 384 root geodesics, giving a ratio at least `25/6`. The `cubic(m)` function in `scripts/constructions.py` generates this earlier family, not the final note's `C^(h)`.
- All 108 realization pairs with `2<=a<=10` and `a<=b<=3a-1`, using one admissible layer split for each off-diagonal pair; fans with path order `2,...,8`.
- Exhaustive subset checks on all 143 connected graphs through order six, including 142 nontrivial graphs for the literal local definitions; the tree formula on 81 subcubic trees of orders 3 through 10; and independent position-set subset checks on 50 cubic graphs (all 27 through order ten and 23 extremal representatives at larger orders).

Section 6 of the final note reports additional exact checks:

- Matching and independent recursive maximum-antichain search agree for every observer in the five 27-vertex witnesses, all 1,834 two-ray graphs with ray lengths one through four and every subset of allowed rungs, and all 27,476 connected labeled graphs of orders one through six (164,031 observer values in the last collection). Two-ray upper bounds also hold in 400 further sampled graphs with ray lengths five through fifteen. These labeled-graph checks are distinct from the packaged enumeration by isomorphism class.
- The nine-vertex `(2,6)` witness has independently recomputed observer vector `(4,2,3,6,3,3,5,4,4)`.
- Breadth-first searches, potential and geodesic-cover checks, and antichain checks using the shortest-path directed acyclic graph validate the new constructions for `h=8,9,10` and a padded `h=8` example. The cubic orders are 101,454, 204,158, 417,454 and 101,488, respectively.
- The exponential-row constructions are checked for `2<=a<=10`, all interval examples for `2<=a<=15`, and the visibility construction for `1<=t<=12` and `t=20,50,100`.

The programs and outputs for these additional checks are **not included in `scripts/` or `data/`**. The commands below reproduce the archived enumeration and the finite checks supplied with this package. The final note's all-parameter results follow from its proofs; its new finite checks do not claim minimum-order witnesses.

## What remains open

The sharp leading constants in the cubic and exact-maximum-degree growth estimates remain undetermined. For the higher pair rows, determine `B(a)` exactly for `a>=3` and decide whether every integer between `a` and `B(a)` is realizable. The exponential bounds and interval construction do not settle these questions. The archived maximum ratio of 3 through cubic order 20 is a statement about that finite range.

## Contents and data formats

| Location | Contents |
| --- | --- |
| `note/note.pdf`, `note/note.tex` | The final note, dated 13 October 2026, and its self-contained source |
| `scripts/position.cpp` | Exact C++17 vertex-position solver |
| `scripts/graphs.py`, `scripts/constructions.py` | Python graph utilities, the earlier original/subcubic/cubic families, interval realizations, and fans |
| `scripts/enumerate.py`, `scripts/setup_nauty.sh` | Sequential enumeration and a checksum-pinned local dependency build |
| `scripts/summarize.py`, `scripts/crosscheck.py`, `scripts/check_constructions.py` | Archived enumeration summaries, independent subset checks, and checks of the packaged constructions |
| `scripts/pack_data.py`, `scripts/manifest.py` | Deterministic compression and package integrity hashes |
| `data/{class}-{n}.g6.gz`, `data/{class}-{n}.csv.gz` | All enumeration inputs and per-observer outputs for the three classes |
| `data/summary.csv`, `data/summary.json` | Counts, exact ratio extrema, complete pair frequencies, and example extrema |
| `data/pair-witnesses.csv` | Minimum-order witnesses and their observer vectors |
| `data/realization-checks.csv`, `data/construction-checks.json` | Exact interval-realization values through `a=10` and certificate metadata for the earlier large families |
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

To regenerate every archived enumeration graph and result vector, plus the packaged checks:

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

The supplied final PDF is retained as the release artifact. Rebuilding may change PDF metadata and byte hashes while preserving the mathematical content.

## License

The note, documentation, and data are licensed under **CC BY 4.0**. Original code in `scripts/` is licensed under **MIT**. See [LICENSE](LICENSE) for the scope, CC BY 4.0 terms link, and full MIT text. Downloaded dependencies retain their own licenses.

## How to cite

```bibtex
@misc{MaZhang2026vp,
  author = {Haobo Ma and Wenlin Zhang},
  title = {Sharp growth of vertex-position ratios and realizable pairs},
  year = {2026},
  howpublished = {\url{https://github.com/the-omega-institute/vertex-position-ratio}},
  note = {Note and code}
}
```
