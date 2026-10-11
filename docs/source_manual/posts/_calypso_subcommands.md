# calypso.x subcommands

- [supercell — expand a cell into a supercell](#supercell)
  - [Usage](#supercell-usage)
  - [Parameters](#supercell-parameters)
  - [Output files](#supercell-output-files)
  - [Examples](#supercell-examples)
- [cleave — generate a surface slab](#cleave)
  - [Usage](#cleave-usage)
  - [Parameters](#cleave-parameters)
  - [Input files](#cleave-input-files)
  - [Output files](#cleave-output-files)
  - [Warnings (non-fatal)](#cleave-warnings)
  - [Errors (fatal — program stops)](#cleave-errors)
  - [How H passivation works (`CapBondsWithH`)](#cleave-how-h-passivation-works)
  - [Examples](#cleave-examples)
- [mismatch — search lattice-matched interfaces](#mismatch)
  - [Usage](#mismatch-usage)
  - [Parameters](#mismatch-parameters)
  - [TOML input](#mismatch-toml-input)
  - [Output files](#mismatch-output-files)
  - [Notes on `FlipSlab1Z`](#mismatch-notes-on-flipslab1z)
  - [Errors (fatal — program stops)](#mismatch-errors)
  - [Examples](#mismatch-examples)
- [combine — stack two slabs into a heterostructure](#combine)
  - [Usage](#combine-usage)
  - [Parameters](#combine-parameters)
  - [TOML input](#combine-toml-input)
  - [Output files](#combine-output-files)
  - [Notes on `FlipSlab1Z`](#combine-notes-on-flipslab1z)
  - [Errors (fatal — program stops)](#combine-errors)
  - [Examples](#combine-examples)

---

(supercell)=
## supercell — expand a cell into a supercell

Build a supercell from a structure file
(plugin: `calypso/plugins/cli_supercell.py`, backed by
`calypso.utils.supercell.SupercellExpanderIO`). `Selective Dynamics` flags are
copied to every image.

(supercell-usage)=
### Usage

```bash
# 2D: expand a and b, keep c
calypso.x supercell -p POSCAR.vasp -m 2 2 -s POSCAR_super.vasp

# 3D: expand a, b and c
calypso.x supercell -p POSCAR.vasp -m 2 2 2 -s POSCAR_super.vasp

# full 3x3 matrix (row-major)
calypso.x supercell -p POSCAR.vasp -m 2 1 0 -1 2 0 0 0 1
```

(supercell-parameters)=
### Parameters

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--pcfilename`, `-p` | path | `POSCAR.vasp` | Input structure file. |
| `--matrix`, `-m` | 2, 3 or 9 ints | `1 1 1` | Expansion: `a b` (c kept), `a b c`, or a full 3x3 matrix `m11 m12 m13 m21 m22 m23 m31 m32 m33`. |
| `--scfilename`, `-s` | path | `POSCAR_super.vasp` | Output supercell file. |
| `--scformat`, `-f` | str | `vasp` | Output file format. |

(supercell-output-files)=
### Output files

- **Supercell structure** — `--scfilename` (default `POSCAR_super.vasp`), in the
  format given by `--scformat`.

(supercell-examples)=
### Examples

Input and output files are in `example/cli_supercell/` of CALYPSO-Python.

**graphene** — 2x2 in-plane supercell of graphene (`-m 2 2` keeps c).

`input_file/run_cli.sh`:

```bash
#! /bin/bash

calypso.x supercell \
    -p POSCAR.vasp \
    -m 2 2 \
    -s POSCAR_super.vasp
```

Output: `output_file/POSCAR_super.vasp` (C8).

**H2O** — 2x2x2 supercell; the `Selective Dynamics` flags of the input are kept.

`input_file/run_cli.sh`:

```bash
#! /bin/bash

calypso.x supercell \
    -p POSCAR.vasp \
    -m 2 2 2 \
    -s POSCAR_super.vasp
```

Output: `output_file/POSCAR_super.vasp` (H16O8).


---

(cleave)=
## cleave — generate a surface slab

Generate a surface slab from a bulk crystal structure
(plugin: `calypso/plugins/cli_cleave.py`, backed by
`calypso.utils.cleave.CleaveSurfaceIO`).

Two input modes are supported:

1. **Direct parameters** — pass every parameter on the command line.
2. **TOML file** — write parameters into a TOML file and pass `--input`.
   When `--input` is supplied, all other flags are ignored.

(cleave-usage)=
### Usage

```bash
# Mode 1: direct command-line parameters
calypso.x cleave --spacegroup 227 \
    --latticeparameters 3.5668 3.5668 3.5668 90 90 90 \
    --irreducibleatoms "C 0.0 0.0 0.0" \
    --millerindex 1 1 1 --numlayers 6

# Mode 2: TOML file
calypso.x cleave --input input.toml
```

(cleave-parameters)=
### Parameters

| Flag | TOML key | Type | Default | Description |
|------|----------|------|---------|-------------|
| `--input`, `-i` | — | path | `None` | Read all parameters from a TOML file. When set, other flags are ignored. |
| `--usefile` | `UseFile` | flag | `False` | Read the bulk structure from `--filepath` instead of `--latticeparameters`. |
| `--filepath`, `-f` | `FilePath` | path | `None` | Input structure file (POSCAR, CIF, …). Required when `--usefile` is set. |
| `--filesymmetry` | `FileSymmetry` | flag | `False` | With `--usefile`: if set, treat the file as a CIF and read symmetry directly; otherwise use the standard reader and auto-detect symmetry. |
| `--symprec` | `SymPrec` | float | `1e-5` | Symmetry-detection tolerance (Å). |
| `--spacegroup`, `-sg` | `SpaceGroup` | int | `1` | International Tables space-group number (1–230). |
| `--latticeparameters`, `-lp` | `LatticeParameters` | 6 floats | `None` | Cell parameters `a b c alpha beta gamma` (Å, degrees). Required when `--usefile` is not set. |
| `--irreducibleatoms`, `-ia` | `IrreducibleAtoms` | strings | `None` | Inequivalent atoms as quoted `"symbol x y z"` tokens, e.g. `"O 0.0 0.0 0.0" "Ti 0.0 0.0 0.7"`. Required when `--usefile` is not set. |
| `--millerindex`, `-m` | `MillerIndex` | 3 or 4 ints | `0 0 1` | Miller indices: 3 values (hkl) or 4 values (hkil). |
| `--matrixnotation`, `-mn` | `MatrixNotation` | 4 ints | `1 0 0 1` | Surface reconstruction matrix, row-major (a11 a12 a21 a22). |
| `--vacuumthick` | `VacuumThick` | float | `20.0` | Vacuum thickness (Å). |
| `--slabdepth` | `SlabDepth` | float | `0.0` | Depth from the top surface (Å). |
| `--slabtotalthick` | `SlabTotalThick` | float | `100.0` | Total slab thickness (Å). |
| `--numlayers`, `-nl` | `NumLayers` | int | `6` | Number of atomic layers in the slab. |
| `--numrelaxedlayers` | `NumRelaxedLayers` | int | `2` | Number of top layers left free (selective dynamics). Clamped to `NumLayers` if larger. |
| `--slabtolerance` | `SlabTolerance` | float | `0.5` | Layer-detection tolerance (Å). |
| `--capbondswithh` | `CapBondsWithH` | flag | `False` | Passivate dangling bonds on the bottom surface with hydrogen. |
| `--cleavefilepath`, `-o` | `CleaveFilePath` | path | auto | Output slab file. Default: `POSCAR_{millerindex}_slab.vasp`. |
| `--cleavefileformat` | `CleaveFileFormat` | str | `vasp` | Output file format (e.g. `vasp`, `extxyz`). |

(cleave-input-files)=
### Input files

- **Direct mode** (`--usefile` not set): no input file; the structure is built
  from `--spacegroup`, `--latticeparameters` and `--irreducibleatoms`.
- **File mode** (`--usefile`): a structure file given by `--filepath`
  (POSCAR / CIF / any reader-supported format). With `--filesymmetry` the file
  must be a CIF whose symmetry is read directly.
- **TOML mode** (`--input`): a TOML file whose keys are the *TOML key* column
  above. Example:

  ```toml
  SpaceGroup        = 227
  LatticeParameters = [3.5668, 3.5668, 3.5668, 90.0, 90.0, 90.0]
  IrreducibleAtoms  = [["C", 0.0, 0.0, 0.0]]
  MillerIndex       = [1, 1, 1]
  MatrixNotation    = [[2, 0], [0, 1]]
  VacuumThick       = 20.0
  SlabTotalThick    = 100.0
  NumLayers         = 6
  NumRelaxedLayers  = 2
  SlabTolerance     = 0.5
  CapBondsWithH     = true
  CleaveFilePath    = "POSCAR_111_slab.vasp"
  CleaveFileFormat  = "vasp"
  ```

(cleave-output-files)=
### Output files

Running `cleave` writes three files (the slab next to where you point
`--cleavefilepath`, the two side-car files in the same directory):

- **Slab structure** — `CleaveFilePath` (default `POSCAR_{millerindex}_slab.vasp`),
  in the format given by `CleaveFileFormat`.
- **`uv.csv`** — the in-plane surface lattice vectors `u` and `v`.
- **`wb-surfgin.toml`** — a summary of every parameter used for the run,
  reusable directly as `--input`.

(cleave-warnings)=
### Warnings (non-fatal)

These are emitted via Python `warnings.warn` (`UserWarning`). They print a
message but the run continues and a slab is still produced.

| Condition | Message | Effect |
|-----------|---------|--------|
| `NumRelaxedLayers > NumLayers` | *One of the relaxed layers is bigger than total layers, will set relax_layer to layer.* | `num_relaxed_layers` is clamped down to `num_layers`. Detected up-front from the input parameters. |
| Supercell ran out of atoms before reaching `NumLayers` | *Requested too many layers; reduced to N layers (ran out of atoms in the supercell).* | The slab is built with the achievable number of layers `N` (see `num_layers_out`) instead of the requested `NumLayers`. Increase `SlabTotalThick`, or request fewer layers, to avoid it. |
| The above happened **and** `CapBondsWithH` is set | *Cannot passivate dangling bonds with H when the layer count was reduced.* | A second warning, alerting that passivation may be unreliable for the reduced slab. |

(cleave-errors)=
### Errors (fatal — program stops)

These raise an exception and abort the `cleave` run; no slab is written.

| Exception | When | Message / cause |
|-----------|------|-----------------|
| `RuntimeError` | Intermediate supercell exceeds 100 000 atoms | *Surface generation failed: supercell too large (intermediate supercell exceeds 100 000 atoms). Try a smaller slab depth or a different Miller index.* |
| `RuntimeError` | Reconstructed surface basis vectors are degenerate | *There are serious problems with the reconstructed surface basis vectors, typically caused by two basis vectors aligned in the same direction. Please check the MatrixNotation control parameter.* |
| `ValueError` | `--usefile` set but `--filepath` missing | *'file_path' (FilePath) must be provided when use_file=True.* |
| `ValueError` | Direct mode (`--usefile` not set) with missing/invalid inputs | Reported for any of: `SpaceGroup` not in 1–230, `LatticeParameters` missing, `IrreducibleAtoms` missing. |
| `ValueError` | `LatticeParameters` cannot form a valid cell | *Invalid LatticeParameters …: could not build lattice matrix.* |

(cleave-how-h-passivation-works)=
### How H passivation works (`CapBondsWithH`)

When `CapBondsWithH` is enabled, dangling bonds on the **bottom** side of the
slab are saturated with hydrogen by the Fortran routine `capbond_with_h`. The
algorithm uses covalent radii (one value per element, passed in from the Python
side; the pairwise sums are formed in Fortran):

1. **Find the broken bonds.** For every surface atom *i* in the slab and every
   atom *j* that was cut away just below it (including its periodic images in
   the *a*/*b* directions, `-1..1`), the pair is considered bonded when their
   distance is below a cutoff scaled from the covalent radii:

   ```
   max_bond_len = 1.2 * (cov_radii[i] + cov_radii[j])
   ```

   The factor `max_ratio = 1.2` (20 % tolerance) is the bonding criterion. Each
   such broken *i–j* bond becomes one passivating H atom, so the count of added
   H atoms is determined here first.

2. **Place each H atom.** The H replacing the removed neighbour *j* is put on
   the *i→j* direction, but at a shortened, element-dependent **X–H bond
   length**:

   ```
   h_bond_len = 0.8 * (cov_radii[i] + cov_radii[H])
   ```

   i.e. 0.8 × the sum of the surface atom's and hydrogen's covalent radii.
   The H is moved along the original bond direction to this distance from
   atom *i* (`move_along`).

3. **Pseudo-hydrogen charge.** To keep the slab charge-neutral, each cap is
   assigned a fractional ("pseudo-hydrogen") charge derived from the broken
   bond:

   ```
   charge = 2.0 - decomposed_charge(ele_i, ele_j)
   ```

   The cap's element label is chosen from this charge:

   | charge | label |
   |--------|-------|
   | 0.25 | `H.25` |
   | 0.5  | `H.5`  |
   | 0.75 | `H.75` |
   | 1.0  | `H` (ordinary hydrogen) |
   | 1.25 | `H1.25` |
   | 1.5  | `H1.5` |
   | other | `H_s` (generic pseudo-H) |

   So a plain `H` label means a charge-1.0 (normal covalent) cap, whereas
   labels such as `H.5` / `H1.25` are pseudo-hydrogens carrying the indicated
   partial charge.

4. **Bookkeeping.** The capped atoms are tagged in `subpos_type` as type `3`
   (relaxed surface = `1`, bulk = `2`, pseudo-H = `3`); in the output slab the
   bulk and pseudo-H atoms are fixed (selective dynamics), the top relaxed
   layers are free.

The number of H atoms added is printed at run time
(`Number of passivation H atoms: …`). Note the warning above: if the layer
count had to be reduced, passivation may be unreliable for that slab.

(cleave-examples)=
### Examples

Input and output files are in `example/cli_cleave_surface/` of CALYPSO-Python.

**diamond_111** — C(111) slab from a CIF file with symmetry, H-capped bottom
surface (TOML mode).

`input_file/run_cli.sh`:

```bash
#! /bin/bash

calypso.x cleave --input input.toml
```

`input_file/input.toml`:

```toml
# Test 1: Diamond C(111) surface
# space_group=227 (Fd-3m), a=3.5668 Å
# miller=(1,1,1), recon_mat=[[2,0],[0,1]], cap_bonds_with_h=True

MillerIndex       = [1, 1, 1]
MatrixNatation    = [[1, 0], [0, 1]]

VacuumThick       = 20.0
SlabDepth         = 0.0
SlabTotalThick    = 100.0
NumLayers         = 6
NumRelaxedLayers  = 2
SlabTolerance     = 0.5
CapBondsWithH     = true

UseFile           = true
FilePath          = "diamond.cif"
FileSymmetry      = true
SymPrec           = 1e-5
CleaveFilePath    = "POSCAR_111_slab.vasp"
CleaveFileFormat  = "vasp"
```

Output: `POSCAR_111_slab.vasp`, `uv.csv`, `wb-surfgin.toml`.

**TiO2_m5m20** — (-5 -2 0) slab of TiO2 read from a POSCAR (command-line mode).

`input_file/run_cli.sh`:

```bash
#!/bin/bash
# Test 2: TiO2 rutile(-5-20) surface
# space_group=141 (I4_1/amd), a=b=3.9033 Å, c=9.6996 Å
# 2 irreducible atoms: Ti(-0.5, 0.5, 1.0), O(-0.5, 0.5, 1.20785)
# miller=(-5,-2,0), recon_mat=[[1,0],[0,1]], cap_bonds_with_h=False

calypso.x cleave \
    --millerindex -5 -2 0 \
    --matrixnotation 1 0 0 1 \
    --vacuumthick 15.0 \
    --slabtotalthick 100.0 \
    --numlayers 5 \
    --numrelaxedlayers 5 \
    --slabtolerance 0.5 \
    --usefile \
    --filepath ./TiO2.vasp \
    --cleavefileformat vasp
```

Output: `POSCAR_m5m20_slab.vasp`, `uv.csv`, `wb-surfgin.toml`.


---

(mismatch)=
## mismatch — search lattice-matched interfaces

Search lattice-matched supercell interfaces between two crystals via the
CALYPSO mismatch module. For each accepted match, the two
crystals are cleaved to slabs, expanded to matched in-plane supercells, and
optionally stacked into a combined interface.

Two input modes are supported:

1. **Direct parameters** — pass parameters on the command line.
2. **TOML file** — write parameters into a three-section TOML file and pass
   `--input`. When `--input` is supplied, other command-line flags are ignored.

The input TOML file is user-controlled. If you run with command-line flags,
CALYPSO does **not** create `mismatch.toml`. In both modes, CALYPSO writes a
separate full parameter summary named `wb-mismatch.toml` under `OutputDir`.

(mismatch-usage)=
### Usage

```bash
# Mode 1: direct command-line parameters
calypso.x mismatch -f1 lat1.cif -f2 lat2.cif \
    --filesymmetry1 --filesymmetry2 \
    --maxmiller 5 --maxarea 200 --maxmismatch 0.05 -o ./interface

# Mode 2: TOML file
calypso.x mismatch --input mismatch.toml
```

(mismatch-parameters)=
### Parameters

The TOML file has `[CRYSTAL1]` for the upper crystal, `[CRYSTAL2]` for the
lower crystal, `[MATCHING]` for search/output parameters, and an optional
`[COMBINE]` table for combined-interface stacking parameters. Section and key
names are case-insensitive. Stacking keys may be written in `[MATCHING]` or
`[COMBINE]`; `[COMBINE]` is clearer when using TOML.

**Input mode**

| Flag | TOML key | Type | Default | Description |
|------|----------|------|---------|-------------|
| `--input`, `-i` | — | path | `None` | Read parameters from a TOML file. When set, other flags are ignored. |

**Crystal files and slab generation** (`[CRYSTAL1]` / `[CRYSTAL2]`)

| Flag | TOML key | Type | Default | Description |
|------|----------|------|---------|-------------|
| `--filepath1`, `-f1` / `--filepath2`, `-f2` | `FilePath` | path | required | Upper / lower crystal structure file. |
| `--filesymmetry1` / `--filesymmetry2` | `FileSymmetry` | bool | `false` | Treat the file as a CIF and keep its recorded space group instead of re-detecting symmetry. |
| `--symprec1` / `--symprec2` | `SymPrec` | float | `1e-5` | Symmetry-detection tolerance (Angstrom). |
| TOML only | `UseSymmetry` | bool | `true` | Use spglib symmetry reduction. Set `false` to keep every atom as P1, useful for supercells that must not be reduced. |
| `--numlayers1` / `--numlayers2` | `NumLayers` | int | `6` | Number of atomic layers in each slab. |
| `--numrelaxedlayers1` / `--numrelaxedlayers2` | `NumRelaxedLayers` | int | all layers | Number of top layers left free. Omit to relax all layers. |
| `--slabtolerance1` / `--slabtolerance2` | `SlabTolerance` | float | `0.5` | Layer-detection tolerance (Angstrom). |
| `--capbondswithh1` / `--capbondswithh2` | `CapBondsWithH` | bool | `false` | Passivate dangling bonds with pseudo-H. This is opt-in; enable only for systems where pseudo-H passivation is appropriate. |
| `--vacuumthick1` / `--vacuumthick2` | `VacuumThick` | float | `15.0` | Vacuum thickness for the individual slabs (Angstrom). |
| `--slabdepth1` / `--slabdepth2` | `SlabDepth` | float | `0.0` | Slab depth from the top surface (Angstrom). |
| `--SpecifyingMillerIndex1` / `--SpecifyingMillerIndex2` | `SpecifyingMillerIndex` | list | auto | Fix Miller indices instead of searching. CLI uses flat triplets, e.g. `1 0 0 0 0 1`; TOML uses list of triplets, e.g. `[[1, 1, 0], [1, 0, 0]]`. |

**Search parameters** (`[MATCHING]`)

| Flag | TOML key | Type | Default | Description |
|------|----------|------|---------|-------------|
| `--maxmiller`, `-mm` | `MaxMiller` | int | `2` | Maximum absolute Miller index to search. |
| `--maxarea`, `-ma` | `MaxArea` | float | `200.0` | Maximum supercell area (Angstrom^2). |
| `--maxmismatch`, `-mx` | `MaxMismatch` | float | `0.05` | Maximum mismatch value, 0-1. |
| `--eqvahkl` / `--noeqvahkl` | `EqvaHkl` | bool | `true` | Skip crystallographically equivalent HKLs. |
| `--elihkl` | `EliHkl` | bool | `false` | Only consider `i<j` HKL pairs. |
| `--maxresults`, `-mr` | `MaxResults` | int | `100` | Maximum number of returned matches. |
| `--slabthick` | `SlabThick` | float | `30.0` | Shared upper bound on slab thickness (Angstrom). |

**Output and stacking** (`[MATCHING]` / `[COMBINE]`)

| Flag | TOML key | Type | Default | Description |
|------|----------|------|---------|-------------|
| `--outputdir`, `-o` | `OutputDir` | path | `.` | Output root directory. In `wb-mismatch.toml`, this is recorded as an absolute path. |
| `--nowritepairs` | `WritePairs` | bool | `true` | Disable writing `matched_supercells/pair_N/` directories. |
| `--nowritecombined` | `WriteCombined` | bool | `true` | Disable writing `combined_interface.vasp` for each pair. |
| `--deltaz` | `DeltaZ` | float | `2.5` | Interlayer gap between the two slabs (Angstrom). |
| `--vacuum` | `Vacuum` | float | `15.0` | Vacuum for the combined structure when `Typ=1` (Angstrom). |
| `--deltax` / `--deltay` | `DeltaX` / `DeltaY` | float | `0.0` | Lateral shift of the upper slab (Angstrom). |
| `--typ` | `Typ` | int | `1` | Combined cell type: `1` = slab + vacuum, `2` = periodic crystal along c. |
| `--flip-slab1-z` / `--no-flip-slab1-z` | `FlipSlab1Z` | bool | `true` | Mirror the upper slab (`slab1`) along z before stacking, so its outer surface can face the vacuum and the opposite side faces the interface. |
| `--pairformat` | `PairFormat` | str | `vasp` | Output structure format for pair directories. |

(mismatch-toml-input)=
### TOML input

```toml
[CRYSTAL1]
FilePath              = "rutile.cif"
FileSymmetry          = true
SymPrec               = 1e-5
UseSymmetry           = true
NumLayers             = 2
NumRelaxedLayers      = 1
SlabTolerance         = 0.5
CapBondsWithH         = false
VacuumThick           = 15.0
SlabDepth             = 0.0
SpecifyingMillerIndex = [[0, 0, 1]]

[CRYSTAL2]
FilePath              = "anatase.cif"
FileSymmetry          = true
SymPrec               = 1e-5
UseSymmetry           = true
NumLayers             = 2
SlabTolerance         = 0.5
CapBondsWithH         = false
VacuumThick           = 15.0
SlabDepth             = 0.0
SpecifyingMillerIndex = [[0, 0, 1]]

[MATCHING]
MaxMiller     = 3
MaxArea       = 150.0
MaxMismatch   = 0.05
EqvaHkl       = true
EliHkl        = false
MaxResults    = 10
SlabThick     = 30.0
OutputDir     = "./output_file"
WritePairs    = true
WriteCombined = true
PairFormat    = "vasp"

[COMBINE]
DeltaZ     = 2.5
Vacuum     = 15.0
DeltaX     = 0.0
DeltaY     = 0.0
Typ        = 1
FlipSlab1Z = true
```

(mismatch-output-files)=
### Output files

Written under `OutputDir`:

- **`matched_lattices.csv`** — accepted matches, including `hkl1` / `hkl2`,
  in-plane vectors, areas, and mismatch values.
- **`matched_supercells/pair_N/`** — one directory per match when
  `WritePairs=true`, containing `lat1_supercell.vasp`, `lat2_supercell.vasp`,
  and, when `WriteCombined=true`, `combined_interface.vasp`.
- **`wb-mismatch.toml`** — a complete summary of the effective parameters used
  for the run. It is always written when mismatch runs successfully, regardless
  of whether the input came from command-line flags or `mismatch.toml`.

Path fields written to `wb-mismatch.toml` are absolute paths, including
`CRYSTAL1.FilePath`, `CRYSTAL2.FilePath`, `MATCHING.OutputDir`, and
`MATCHING.CsvPath`. This distinguishes the user input TOML (`mismatch.toml`,
only present if the user supplied one) from CALYPSO's generated summary file
(`wb-mismatch.toml`).

(mismatch-notes-on-flipslab1z)=
### Notes on `FlipSlab1Z`

`slab2` is placed below and `slab1` above. With `FlipSlab1Z=true` (the default),
`slab1` is mirrored within its occupied z range before stacking. This is useful
when the upper slab should be turned over so its interface side faces downward
and its outer/passivated side faces the vacuum. Set `FlipSlab1Z=false` to stack
`slab1` without this z inversion.

(mismatch-errors)=
### Errors (fatal — program stops)

| Exception | When |
|-----------|------|
| `FileNotFoundError` | `--input` given but the TOML file does not exist. |
| `ValueError` | Direct mode without both `--filepath1` and `--filepath2`. |
| `ValueError` | A `--SpecifyingMillerIndex*` list whose length is not a multiple of 3. |
| `KeyError` | TOML missing `[CRYSTAL1]` / `[CRYSTAL2]`, or either missing `FilePath`. |

(mismatch-examples)=
### Examples

Input and output files are in `example/cli_mismatch/` of CALYPSO-Python. Every
example writes `matched_lattices.csv`, `wb-mismatch.toml` and
`matched_supercells/pair_N/` (`lat1_supercell.vasp`, `lat2_supercell.vasp`,
`combined_interface.vasp`) for the three best matches.

**rutile_anatase** — rutile / anatase TiO2 from CIF files (TOML mode).

`input_file/run_cli.sh`:

```bash
#! /bin/bash

calypso.x mismatch --input mismatch.toml
```

`input_file/mismatch.toml`:

```toml
# Example: rutile TiO2 / anatase TiO2 lattice matching (TOML mode)
# Reference params from example_rutile_anatase/input_mismatch.dat:
#   MaximumArea = 200.0, MaximumMismatchValue = 0.05, MaximumMillerIndex = 5
#
# Section / key names are case-insensitive. Bulk crystals: keep symmetry
# reduction on (UseSymmetry = true, the default).

[CRYSTAL1]
FilePath         = "rutile.cif"   # rutile TiO2 (SG 136)
FileSymmetry     = true
SymPrec          = 1e-5
UseSymmetry      = true
NumLayers        = 8
NumRelaxedLayers = 2
SlabTolerance    = 0.5
CapBondsWithH    = false
VacuumThick      = 15.0
SlabDepth        = 0.0

[CRYSTAL2]
FilePath         = "anatase.cif"  # anatase TiO2 (SG 141)
FileSymmetry     = true
SymPrec          = 1e-5
UseSymmetry      = true
NumLayers        = 8
NumRelaxedLayers = 2
SlabTolerance    = 0.5
CapBondsWithH    = false
VacuumThick      = 15.0
SlabDepth        = 0.0

[MATCHING]
MaxMiller     = 5
MaxArea       = 200.0
MaxMismatch   = 0.05
MaxResults    = 3
SlabThick     = 30.0
OutputDir     = "."
WritePairs    = true
WriteCombined = true
PairFormat    = "vasp"

# Stacking parameters for the combined interface of each pair.
# Optional: omit to keep the mismatch defaults.
[COMBINE]
DeltaZ = 2.5
Vacuum = 15.0
DeltaX = 0.0
DeltaY = 0.0
Typ    = 1
FlipSlab1Z = true
```

**Ni_BN** — h-BN monolayer on bulk Ni with fixed Miller indices (TOML mode).

`input_file/run_cli.sh`:

```bash
#! /bin/bash

calypso.x mismatch --input mismatch.toml
```

`input_file/mismatch.toml`:

```toml
# Example: BN monolayer / Ni bulk interface (TOML mode)
#
# Crystal 1 (BN) is a monolayer; crystal 2 (Ni) is a bulk FCC conventional
# cell (4 atoms, space group 225). Both crystals go through normal symmetry
# detection (UseSymmetry = true, the default) and are cleaved internally via
# NumLayers/SpecifyingMillerIndex. Inputs are VASP POSCARs (no symmetry
# records).
#
# Section / key names are case-insensitive.

[CRYSTAL1]
FilePath              = "BN.vasp"   # monolayer h-BN
FileSymmetry          = false
SymPrec               = 1e-5
UseSymmetry           = true
NumLayers             = 1
NumRelaxedLayers      = 1
SlabTolerance         = 0.5
CapBondsWithH         = false
VacuumThick           = 15.0
SlabDepth             = 0.0
SpecifyingMillerIndex = [[0, 0, 1]]

[CRYSTAL2]
FilePath              = "Ni.vasp"   # Ni bulk conventional cell (FCC, SG 225)
FileSymmetry          = false
SymPrec               = 1e-5
UseSymmetry           = true
NumLayers             = 4
NumRelaxedLayers      = 2
SlabTolerance         = 0.5
CapBondsWithH         = false
VacuumThick           = 15.0
SlabDepth             = 0.0
SpecifyingMillerIndex = [[1, 1, 0], [1, 0, 0]]

[MATCHING]
MaxMiller     = 5
MaxArea       = 100.0
MaxMismatch   = 0.10
MaxResults    = 3
SlabThick     = 30.0
OutputDir     = "."
WritePairs    = true
WriteCombined = true
PairFormat    = "vasp"

# Stacking parameters for the combined interface of each pair.
[COMBINE]
DeltaZ = 3.0
Vacuum = 15.0
DeltaX = 0.0
DeltaY = 0.0
Typ    = 1
```

**LCO_LPS** — LiCoO2 / Li3PS4 from CIF files (command-line mode).

`input_file/run_cli.sh`:

```bash
#! /bin/bash
# LiCoO2 (LCO) / Li3PS4 (LPS) lattice matching — command-line mode.
# Both inputs are CIFs with symmetry records, so --filesymmetry1/2 is set.

calypso.x mismatch \
    -f1 lat1.cif -f2 lat2.cif \
    --filesymmetry1 --filesymmetry2 \
    --symprec1 1e-5 --symprec2 1e-5 \
    --maxmiller 5 --maxarea 100.0 --maxmismatch 0.10 --maxresults 3 \
    --slabthick 30.0 \
    --numlayers1 8 --numlayers2 8 \
    --numrelaxedlayers1 2 --numrelaxedlayers2 2 \
    --slabtolerance1 0.5 --slabtolerance2 0.5 \
    --vacuumthick1 15.0 --vacuumthick2 15.0 \
    --slabdepth1 0.0 --slabdepth2 0.0 \
    --outputdir . \
    --deltaz 2.5 --vacuum 15.0 --typ 1 --pairformat vasp
```

**MXene_MoS2** — MoS2 / Mo2CO2 monolayers, layer plane fixed to (0 0 1)
(command-line mode).

`input_file/run_cli.sh`:

```bash
#! /bin/bash
# 2-D heterostructure: monolayer MoS2 / Mo2CO2 MXene — command-line mode.
# Inputs are VASP POSCARs (no symmetry records); space group is auto-detected.
# For a 2-D stack we fix the layer plane via --SpecifyingMillerIndex1/2 0 0 1
# instead of using a 2-D flag.

calypso.x mismatch \
    -f1 MoS2.vasp -f2 Mo2CO2.vasp \
    --symprec1 1e-5 --symprec2 1e-5 \
    --SpecifyingMillerIndex1 0 0 1 --SpecifyingMillerIndex2 0 0 1 \
    --maxmiller 5 --maxarea 100.0 --maxmismatch 0.10 --maxresults 3 \
    --slabthick 30.0 \
    --numlayers1 3 --numlayers2 5 \
    --numrelaxedlayers1 3 --numrelaxedlayers2 5 \
    --slabtolerance1 0.5 --slabtolerance2 0.5 \
    --vacuumthick1 15.0 --vacuumthick2 15.0 \
    --slabdepth1 0.0 --slabdepth2 0.0 \
    --outputdir . \
    --deltaz 3.0 --vacuum 15.0 --typ 1 --pairformat vasp
```


---

(combine)=
## combine — stack two slabs into a heterostructure

Stack two already lattice-matched slabs into one heterostructure interface.
Structure 2 is placed below, structure 1 is placed above, and the two are
separated by `DeltaZ`. The in-plane `(a, b)` lattice is taken from structure 2;
only the stacking direction is rebuilt.

Two input modes are supported:

1. **Direct parameters** — pass parameters on the command line.
2. **TOML file** — write parameters into a TOML file and pass `--input`. When
   `--input` is supplied, other command-line flags are ignored.

The input TOML file is user-controlled. If you run with command-line flags,
CALYPSO does **not** create `combine.toml`. In both modes, CALYPSO writes a
separate summary named `wb-combine.toml` next to the output structure unless
summary writing is disabled by the Python API.

(combine-usage)=
### Usage

```bash
# Mode 1: direct command-line parameters
calypso.x combine -f1 lat1_supercell.vasp -f2 lat2_supercell.vasp \
    --deltaz 2.5 --vacuum 15 --typ 1 -o combined_interface.vasp

# Disable the default z flip of the upper slab
calypso.x combine -f1 lat1_supercell.vasp -f2 lat2_supercell.vasp \
    --no-flip-slab1-z -o combined_interface.vasp

# Mode 2: TOML file
calypso.x combine --input combine.toml
```

(combine-parameters)=
### Parameters

The TOML file has `[STRUCTURE1]` for the upper slab, `[STRUCTURE2]` for the
lower slab, and `[COMBINE]` for stacking/output parameters. Section and key
names are case-insensitive.

| Flag | TOML key | Type | Default | Description |
|------|----------|------|---------|-------------|
| `--input`, `-i` | — | path | `None` | Read parameters from a TOML file. When set, other flags are ignored. |
| `--filepath1`, `-f1` | `[STRUCTURE1] FilePath` | path | required | Upper slab file. |
| `--filepath2`, `-f2` | `[STRUCTURE2] FilePath` | path | required | Lower slab file. |
| `--deltaz` | `[COMBINE] DeltaZ` | float | `2.5` | Interlayer gap between the two slabs (Angstrom). |
| `--vacuum` | `[COMBINE] Vacuum` | float | `15.0` | Total vacuum when `Typ=1`, split above and below the stack. |
| `--deltax` | `[COMBINE] DeltaX` | float | `0.0` | In-plane x shift of the upper slab (Angstrom). |
| `--deltay` | `[COMBINE] DeltaY` | float | `0.0` | In-plane y shift of the upper slab (Angstrom). |
| `--typ` | `[COMBINE] Typ` | int | `1` | Combined cell type: `1` = slab + vacuum, `2` = periodic crystal along c. |
| `--flip-slab1-z` / `--no-flip-slab1-z` | `[COMBINE] FlipSlab1Z` | bool | `true` | Mirror the upper slab along z before stacking. |
| `--output`, `-o` | `[COMBINE] OutputFile` | path | `combined_interface.vasp` | Output structure file. |
| `--outputformat` | `[COMBINE] OutputFormat` | str | `vasp` | Output structure format. |

`WriteSummary` is not written into `wb-combine.toml`. It is only an internal
Python API switch controlling whether the summary file is generated.

(combine-toml-input)=
### TOML input

```toml
[STRUCTURE1]
FilePath = "lat1_supercell.vasp"   # upper slab

[STRUCTURE2]
FilePath = "lat2_supercell.vasp"   # lower slab

[COMBINE]
DeltaZ       = 3.0
Vacuum       = 15.0
DeltaX       = 0.0
DeltaY       = 0.0
Typ          = 1
FlipSlab1Z   = true
OutputFile   = "combined_interface.vasp"
OutputFormat = "vasp"
```

(combine-output-files)=
### Output files

- **Combined structure** — `OutputFile`, in the format specified by
  `OutputFormat`.
- **`wb-combine.toml`** — a summary of the effective parameters used, written
  next to `OutputFile`.

Path fields written to `wb-combine.toml` are absolute paths, including
`STRUCTURE1.FilePath`, `STRUCTURE2.FilePath`, and `COMBINE.OutputFile`. The
summary file intentionally does not include `WriteSummary`.

Each slab's selective-dynamics mask is carried through into the combined
structure unchanged.

(combine-notes-on-flipslab1z)=
### Notes on `FlipSlab1Z`

With `FlipSlab1Z=true` (default), structure 1 is mirrored in z within its own
occupied thickness before it is placed above structure 2. Set it to `false` if
the two slabs have already been oriented exactly as desired.

(combine-errors)=
### Errors (fatal — program stops)

| Exception | When |
|-----------|------|
| `FileNotFoundError` | `--input` given but the TOML file does not exist. |
| `ValueError` | Direct mode without both `--filepath1` and `--filepath2`. |
| `KeyError` | TOML missing `[STRUCTURE1]` / `[STRUCTURE2]`, or either missing `FilePath`. |

(combine-examples)=
### Examples

Input and output files are in `example/cli_combine/` of CALYPSO-Python.

**rutile_anatase** — stack a matched rutile / anatase pair from `mismatch`.

`input_file/run_cli.sh`:

```bash
#! /bin/bash

calypso.x combine --input combine.toml
```

`input_file/combine.toml`:

```toml
# Example: combine two lattice-matched slabs into an interface.
#
# The two input slabs come from a `mismatch` run on rutile / anatase TiO2
# (one matched pair's lat1_supercell.vasp / lat2_supercell.vasp). This is the
# typical combine workflow: first run `mismatch` to find a matched pair, then
# `combine` to stack the two substrate supercells with the desired gap/vacuum.
#
# Section / key names are case-insensitive.

[STRUCTURE1]
FilePath = "rutile_slab.vasp"    # upper slab (matched rutile supercell)

[STRUCTURE2]
FilePath = "anatase_slab.vasp"   # lower slab (matched anatase supercell)

[COMBINE]
DeltaZ       = 2.5
Vacuum       = 15.0
DeltaX       = 0.0
DeltaY       = 0.0
Typ          = 1                 # 1 = slab + vacuum, 2 = crystal
OutputFile   = "rutile_anatase_interface.vasp"
OutputFormat = "vasp"
```

Output: `rutile_anatase_interface.vasp`, `wb-combine.toml`.

**MoS2_MXene** — stack monolayer MoS2 on Mo2CO2.

`input_file/run_cli.sh`:

```bash
#! /bin/bash

calypso.x combine --input combine.toml
```

`input_file/combine.toml`:

```toml
# Example: vertical stacking of monolayer MoS2 on Mo2CO2 MXene
#
# Both inputs are single layers (c ~ 30 Å, already with vacuum). combine simply
# stacks STRUCTURE2 (lower) and STRUCTURE1 (upper) along c, separated by DeltaZ,
# and centres the stack in the cell. Section / key names are case-insensitive.

[STRUCTURE1]
FilePath = "MoS2.vasp"     # upper layer

[STRUCTURE2]
FilePath = "Mo2CO2.vasp"   # lower layer

[COMBINE]
DeltaZ       = 3.0                       # interlayer gap (Å)
Vacuum       = 15.0                      # total vacuum (typ=1), split above/below
DeltaX       = 0.0
DeltaY       = 0.0
Typ          = 1                         # 1 = slab + vacuum, 2 = crystal
OutputFile   = "MoS2_MXene_interface.vasp"
OutputFormat = "vasp"
```

Output: `MoS2_MXene_interface.vasp`, `wb-combine.toml`.
