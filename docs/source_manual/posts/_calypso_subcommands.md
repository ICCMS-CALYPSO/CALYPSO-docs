# calypso.x subcommands

Utility subcommands of `calypso.x`, run as `calypso.x <subcommand> [options]`.

- [calypso.x subcommands](#calypsox-subcommands)
  - [supercell — expand a cell into a supercell](#supercell--expand-a-cell-into-a-supercell)
    - [supercell: Usage](#supercell-usage)
    - [supercell: Parameters](#supercell-parameters)
    - [supercell: Output files](#supercell-output-files)
    - [supercell: Examples](#supercell-examples)
      - [graphene: 2x2 in-plane supercell](#graphene-2x2-in-plane-supercell)
      - [H2O: 2x2x2 supercell](#h2o-2x2x2-supercell)
  - [cleave — generate a surface slab](#cleave--generate-a-surface-slab)
    - [cleave: Usage](#cleave-usage)
    - [cleave: Parameters](#cleave-parameters)
    - [cleave: Input files](#cleave-input-files)
    - [cleave: Output files](#cleave-output-files)
    - [cleave: Warnings (non-fatal)](#cleave-warnings-non-fatal)
    - [cleave: Errors (fatal — program stops)](#cleave-errors-fatal--program-stops)
    - [cleave: How H passivation works (`CapBondsWithH`)](#cleave-how-h-passivation-works-capbondswithh)
    - [cleave: Examples](#cleave-examples)
      - [diamond_111: C(111) slab from a CIF file (TOML mode)](#diamond_111-c111-slab-from-a-cif-file-toml-mode)
      - [TiO2_m5m20: (-5 -2 0) slab from a POSCAR (command-line mode)](#tio2_m5m20--5--2-0-slab-from-a-poscar-command-line-mode)
  - [mismatch — search lattice-matched interfaces](#mismatch--search-lattice-matched-interfaces)
    - [mismatch: Usage](#mismatch-usage)
    - [mismatch: Parameters](#mismatch-parameters)
    - [mismatch: TOML input](#mismatch-toml-input)
    - [mismatch: Output files](#mismatch-output-files)
    - [mismatch: Notes on `FlipSlab1Z`](#mismatch-notes-on-flipslab1z)
    - [mismatch: Errors (fatal — program stops)](#mismatch-errors-fatal--program-stops)
    - [mismatch: Examples](#mismatch-examples)
      - [rutile_anatase: rutile / anatase TiO2 (TOML mode)](#rutile_anatase-rutile--anatase-tio2-toml-mode)
      - [Ni_BN: h-BN monolayer on bulk Ni (TOML mode)](#ni_bn-h-bn-monolayer-on-bulk-ni-toml-mode)
      - [LCO_LPS: LiCoO2 / Li3PS4 (command-line mode)](#lco_lps-licoo2--li3ps4-command-line-mode)
      - [MXene_MoS2: MoS2 / Mo2CO2 monolayers (command-line mode)](#mxene_mos2-mos2--mo2co2-monolayers-command-line-mode)
  - [combine — stack two slabs into a heterostructure](#combine--stack-two-slabs-into-a-heterostructure)
    - [combine: Usage](#combine-usage)
    - [combine: Parameters](#combine-parameters)
    - [combine: TOML input](#combine-toml-input)
    - [combine: Output files](#combine-output-files)
    - [combine: Notes on `FlipSlab1Z`](#combine-notes-on-flipslab1z)
    - [combine: Errors (fatal — program stops)](#combine-errors-fatal--program-stops)
    - [combine: Examples](#combine-examples)
      - [rutile_anatase: stack a matched rutile / anatase pair](#rutile_anatase-stack-a-matched-rutile--anatase-pair)
      - [MoS2_MXene: stack monolayer MoS2 on Mo2CO2](#mos2_mxene-stack-monolayer-mos2-on-mo2co2)


## supercell — expand a cell into a supercell

Build a supercell from a structure file
(plugin: `calypso/plugins/cli_supercell.py`, backed by
`calypso.utils.supercell.SupercellExpanderIO`). `Selective Dynamics` flags are
copied to every image.

### supercell: Usage

```bash
# 2D: expand a and b, keep c
calypso.x supercell -p POSCAR.vasp -m 2 2 -s POSCAR_super.vasp

# 3D: expand a, b and c
calypso.x supercell -p POSCAR.vasp -m 2 2 2 -s POSCAR_super.vasp

# full 3x3 matrix (row-major)
calypso.x supercell -p POSCAR.vasp -m 2 1 0 -1 2 0 0 0 1
```

### supercell: Parameters

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--pcfilename`, `-p` | path | `POSCAR.vasp` | Input structure file. |
| `--matrix`, `-m` | 2, 3 or 9 ints | `1 1 1` | Expansion: `a b` (c kept), `a b c`, or a full 3x3 matrix `m11 m12 m13 m21 m22 m23 m31 m32 m33`. |
| `--scfilename`, `-s` | path | `POSCAR_super.vasp` | Output supercell file. |
| `--scformat`, `-f` | str | `vasp` | Output file format. |

### supercell: Output files

- **Supercell structure** — `--scfilename` (default `POSCAR_super.vasp`), in the
  format given by `--scformat`.

### supercell: Examples

The example files are in `example/cli_supercell/` of CALYPSO-Python.

#### graphene: 2x2 in-plane supercell

`-m 2 2` expands a and b and keeps c.

Input files (`example/cli_supercell/graphene/input_file/`):

```text
.
├── run_cli.sh
└── POSCAR.vasp
```

`run_cli.sh`:

```bash
#! /bin/bash

calypso.x supercell \
    -p POSCAR.vasp \
    -m 2 2 \
    -s POSCAR_super.vasp
```

:::{dropdown} POSCAR.vasp
```text
graphene
1.0
   1.2336456308015413   -2.1367369110836267    0.0000000000000000
   1.2336456308015413    2.1367369110836267    0.0000000000000000
   0.0000000000000000    0.0000000000000000    7.8030730000000004
C
2
direct
   0.0000000000000000    0.0000000000000000    0.2500000000000000
   0.3333333333333333    0.6666666666666666    0.2500000000000000
```
:::

Run `bash run_cli.sh`; afterwards the folder contains (`example/cli_supercell/graphene/output_file/`):

```text
.
├── run_cli.sh
├── POSCAR.vasp
└── POSCAR_super.vasp  # supercell
```

#### H2O: 2x2x2 supercell

The `Selective Dynamics` flags of the input are copied to every image.

Input files (`example/cli_supercell/H2O/input_file/`):

```text
.
├── run_cli.sh
└── POSCAR.vasp
```

`run_cli.sh`:

```bash
#! /bin/bash

calypso.x supercell \
    -p POSCAR.vasp \
    -m 2 2 2 \
    -s POSCAR_super.vasp
```

:::{dropdown} POSCAR.vasp
```text
H  O
1.0
        7.1974005699         0.0000000000         0.0000000000
        0.0000000000         6.9269595146         0.0000000000
        0.0000000000         0.0000000000         6.0000000000
    H    O
    2    1
Selective Dynamics
Direct
     0.583182871         0.433090448         0.500000000  F T T
     0.416817158         0.566909552         0.500000000  F F T
     0.450148702         0.433090448         0.500000000  T F F
```
:::

Run `bash run_cli.sh`; afterwards the folder contains (`example/cli_supercell/H2O/output_file/`):

```text
.
├── run_cli.sh
├── POSCAR.vasp
└── POSCAR_super.vasp  # supercell
```

---

## cleave — generate a surface slab

Generate a surface slab from a bulk crystal structure
(plugin: `calypso/plugins/cli_cleave.py`, backed by
`calypso.utils.cleave.CleaveSurfaceIO`).

Two input modes are supported:

1. **Direct parameters** — pass every parameter on the command line.
2. **TOML file** — write parameters into a TOML file and pass `--input`.
   When `--input` is supplied, all other flags are ignored.

### cleave: Usage

```bash
# Mode 1: direct command-line parameters
calypso.x cleave --spacegroup 227 \
    --latticeparameters 3.5668 3.5668 3.5668 90 90 90 \
    --irreducibleatoms "C 0.0 0.0 0.0" \
    --millerindex 1 1 1 --numlayers 6

# Mode 2: TOML file
calypso.x cleave --input input.toml
```

### cleave: Parameters

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

### cleave: Input files

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

### cleave: Output files

Running `cleave` writes three files (the slab next to where you point
`--cleavefilepath`, the two side-car files in the same directory):

- **Slab structure** — `CleaveFilePath` (default `POSCAR_{millerindex}_slab.vasp`),
  in the format given by `CleaveFileFormat`.
- **`uv.csv`** — the in-plane surface lattice vectors `u` and `v`.
- **`wb-surfgin.toml`** — a summary of every parameter used for the run,
  reusable directly as `--input`.

### cleave: Warnings (non-fatal)

These are emitted via Python `warnings.warn` (`UserWarning`). They print a
message but the run continues and a slab is still produced.

| Condition | Message | Effect |
|-----------|---------|--------|
| `NumRelaxedLayers > NumLayers` | *One of the relaxed layers is bigger than total layers, will set relax_layer to layer.* | `num_relaxed_layers` is clamped down to `num_layers`. Detected up-front from the input parameters. |
| Supercell ran out of atoms before reaching `NumLayers` | *Requested too many layers; reduced to N layers (ran out of atoms in the supercell).* | The slab is built with the achievable number of layers `N` (see `num_layers_out`) instead of the requested `NumLayers`. Increase `SlabTotalThick`, or request fewer layers, to avoid it. |
| The above happened **and** `CapBondsWithH` is set | *Cannot passivate dangling bonds with H when the layer count was reduced.* | A second warning, alerting that passivation may be unreliable for the reduced slab. |

### cleave: Errors (fatal — program stops)

These raise an exception and abort the `cleave` run; no slab is written.

| Exception | When | Message / cause |
|-----------|------|-----------------|
| `RuntimeError` | Intermediate supercell exceeds 100 000 atoms | *Surface generation failed: supercell too large (intermediate supercell exceeds 100 000 atoms). Try a smaller slab depth or a different Miller index.* |
| `RuntimeError` | Reconstructed surface basis vectors are degenerate | *There are serious problems with the reconstructed surface basis vectors, typically caused by two basis vectors aligned in the same direction. Please check the MatrixNotation control parameter.* |
| `ValueError` | `--usefile` set but `--filepath` missing | *'file_path' (FilePath) must be provided when use_file=True.* |
| `ValueError` | Direct mode (`--usefile` not set) with missing/invalid inputs | Reported for any of: `SpaceGroup` not in 1–230, `LatticeParameters` missing, `IrreducibleAtoms` missing. |
| `ValueError` | `LatticeParameters` cannot form a valid cell | *Invalid LatticeParameters …: could not build lattice matrix.* |

### cleave: How H passivation works (`CapBondsWithH`)

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

### cleave: Examples

The example files are in `example/cli_cleave_surface/` of CALYPSO-Python.

#### diamond_111: C(111) slab from a CIF file (TOML mode)

The CIF symmetry is read directly (`FileSymmetry = true`) and the bottom surface is capped with H (`CapBondsWithH = true`).

Input files (`example/cli_cleave_surface/diamond_111/input_file/`):

```text
.
├── input.toml
├── run_cli.sh
└── diamond.cif
```

`input.toml`:

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

`run_cli.sh`:

```bash
#! /bin/bash

calypso.x cleave --input input.toml
```

:::{dropdown} diamond.cif
```text
data_C
_audit_creation_date              2025-10-24
_audit_creation_method            'Materials Studio'
_symmetry_space_group_name_H-M    'FD-3M'
_symmetry_Int_Tables_number       227
_symmetry_cell_setting            cubic
loop_
_symmetry_equiv_pos_as_xyz
  x,y,z
  -x,-y+1/2,z+1/2
  -x+1/2,y+1/2,-z
  x+1/2,-y,-z+1/2
  z,x,y
  z+1/2,-x,-y+1/2
  -z,-x+1/2,y+1/2
  -z+1/2,x+1/2,-y
  y,z,x
  -y+1/2,z+1/2,-x
  y+1/2,-z,-x+1/2
  -y,-z+1/2,x+1/2
  y+3/4,x+1/4,-z+3/4
  -y+1/4,-x+1/4,-z+1/4
  y+1/4,-x+3/4,z+3/4
  -y+3/4,x+3/4,z+1/4
  x+3/4,z+1/4,-y+3/4
  -x+3/4,z+3/4,y+1/4
  -x+1/4,-z+1/4,-y+1/4
  x+1/4,-z+3/4,y+3/4
  z+3/4,y+1/4,-x+3/4
  z+1/4,-y+3/4,x+3/4
  -z+3/4,y+3/4,x+1/4
  -z+1/4,-y+1/4,-x+1/4
  -x+1/4,-y+1/4,-z+1/4
  x+1/4,y+3/4,-z+3/4
  x+3/4,-y+3/4,z+1/4
  -x+3/4,y+1/4,z+3/4
  -z+1/4,-x+1/4,-y+1/4
  -z+3/4,x+1/4,y+3/4
  z+1/4,x+3/4,-y+3/4
  z+3/4,-x+3/4,y+1/4
  -y+1/4,-z+1/4,-x+1/4
  y+3/4,-z+3/4,x+1/4
  -y+3/4,z+1/4,x+3/4
  y+1/4,z+3/4,-x+3/4
  -y+1/2,-x,z+1/2
  y,x,z
  -y,x+1/2,-z+1/2
  y+1/2,-x+1/2,-z
  -x+1/2,-z,y+1/2
  x+1/2,-z+1/2,-y
  x,z,y
  -x,z+1/2,-y+1/2
  -z+1/2,-y,x+1/2
  -z,y+1/2,-x+1/2
  z+1/2,-y+1/2,-x
  z,y,x
  x,y+1/2,z+1/2
  -x,-y,z
  -x+1/2,y,-z+1/2
  x+1/2,-y+1/2,-z
  z,x+1/2,y+1/2
  z+1/2,-x+1/2,-y
  -z,-x,y
  -z+1/2,x,-y+1/2
  y,z+1/2,x+1/2
  -y+1/2,z,-x+1/2
  y+1/2,-z+1/2,-x
  -y,-z,x
  y+3/4,x+3/4,-z+1/4
  -y+1/4,-x+3/4,-z+3/4
  y+1/4,-x+1/4,z+1/4
  -y+3/4,x+1/4,z+3/4
  x+3/4,z+3/4,-y+1/4
  -x+3/4,z+1/4,y+3/4
  -x+1/4,-z+3/4,-y+3/4
  x+1/4,-z+1/4,y+1/4
  z+3/4,y+3/4,-x+1/4
  z+1/4,-y+1/4,x+1/4
  -z+3/4,y+1/4,x+3/4
  -z+1/4,-y+3/4,-x+3/4
  -x+1/4,-y+3/4,-z+3/4
  x+1/4,y+1/4,-z+1/4
  x+3/4,-y+1/4,z+3/4
  -x+3/4,y+3/4,z+1/4
  -z+1/4,-x+3/4,-y+3/4
  -z+3/4,x+3/4,y+1/4
  z+1/4,x+1/4,-y+1/4
  z+3/4,-x+1/4,y+3/4
  -y+1/4,-z+3/4,-x+3/4
  y+3/4,-z+1/4,x+3/4
  -y+3/4,z+3/4,x+1/4
  y+1/4,z+1/4,-x+1/4
  -y+1/2,-x+1/2,z
  y,x+1/2,z+1/2
  -y,x,-z
  y+1/2,-x,-z+1/2
  -x+1/2,-z+1/2,y
  x+1/2,-z,-y+1/2
  x,z+1/2,y+1/2
  -x,z,-y
  -z+1/2,-y+1/2,x
  -z,y,-x
  z+1/2,-y,-x+1/2
  z,y+1/2,x+1/2
  x+1/2,y,z+1/2
  -x+1/2,-y+1/2,z
  -x,y+1/2,-z+1/2
  x,-y,-z
  z+1/2,x,y+1/2
  z,-x,-y
  -z+1/2,-x+1/2,y
  -z,x+1/2,-y+1/2
  y+1/2,z,x+1/2
  -y,z+1/2,-x+1/2
  y,-z,-x
  -y+1/2,-z+1/2,x
  y+1/4,x+1/4,-z+1/4
  -y+3/4,-x+1/4,-z+3/4
  y+3/4,-x+3/4,z+1/4
  -y+1/4,x+3/4,z+3/4
  x+1/4,z+1/4,-y+1/4
  -x+1/4,z+3/4,y+3/4
  -x+3/4,-z+1/4,-y+3/4
  x+3/4,-z+3/4,y+1/4
  z+1/4,y+1/4,-x+1/4
  z+3/4,-y+3/4,x+1/4
  -z+1/4,y+3/4,x+3/4
  -z+3/4,-y+1/4,-x+3/4
  -x+3/4,-y+1/4,-z+3/4
  x+3/4,y+3/4,-z+1/4
  x+1/4,-y+3/4,z+3/4
  -x+1/4,y+1/4,z+1/4
  -z+3/4,-x+1/4,-y+3/4
  -z+1/4,x+1/4,y+1/4
  z+3/4,x+3/4,-y+1/4
  z+1/4,-x+3/4,y+3/4
  -y+3/4,-z+1/4,-x+3/4
  y+1/4,-z+3/4,x+3/4
  -y+1/4,z+1/4,x+1/4
  y+3/4,z+3/4,-x+1/4
  -y,-x,z
  y+1/2,x,z+1/2
  -y+1/2,x+1/2,-z
  y,-x+1/2,-z+1/2
  -x,-z,y
  x,-z+1/2,-y+1/2
  x+1/2,z,y+1/2
  -x+1/2,z+1/2,-y
  -z,-y,x
  -z+1/2,y+1/2,-x
  z,-y+1/2,-x+1/2
  z+1/2,y,x+1/2
  x+1/2,y+1/2,z
  -x+1/2,-y,z+1/2
  -x,y,-z
  x,-y+1/2,-z+1/2
  z+1/2,x+1/2,y
  z,-x+1/2,-y+1/2
  -z+1/2,-x,y+1/2
  -z,x,-y
  y+1/2,z+1/2,x
  -y,z,-x
  y,-z+1/2,-x+1/2
  -y+1/2,-z,x+1/2
  y+1/4,x+3/4,-z+3/4
  -y+3/4,-x+3/4,-z+1/4
  y+3/4,-x+1/4,z+3/4
  -y+1/4,x+1/4,z+1/4
  x+1/4,z+3/4,-y+3/4
  -x+1/4,z+1/4,y+1/4
  -x+3/4,-z+3/4,-y+1/4
  x+3/4,-z+1/4,y+3/4
  z+1/4,y+3/4,-x+3/4
  z+3/4,-y+1/4,x+3/4
  -z+1/4,y+1/4,x+1/4
  -z+3/4,-y+3/4,-x+1/4
  -x+3/4,-y+3/4,-z+1/4
  x+3/4,y+1/4,-z+3/4
  x+1/4,-y+1/4,z+1/4
  -x+1/4,y+3/4,z+3/4
  -z+3/4,-x+3/4,-y+1/4
  -z+1/4,x+3/4,y+3/4
  z+3/4,x+1/4,-y+3/4
  z+1/4,-x+1/4,y+1/4
  -y+3/4,-z+3/4,-x+1/4
  y+1/4,-z+1/4,x+1/4
  -y+1/4,z+3/4,x+3/4
  y+3/4,z+1/4,-x+3/4
  -y,-x+1/2,z+1/2
  y+1/2,x+1/2,z
  -y+1/2,x,-z+1/2
  y,-x,-z
  -x,-z+1/2,y+1/2
  x,-z,-y
  x+1/2,z+1/2,y
  -x+1/2,z,-y+1/2
  -z,-y+1/2,x+1/2
  -z+1/2,y,-x+1/2
  z,-y,-x
  z+1/2,y+1/2,x
_cell_length_a                    3.5668
_cell_length_b                    3.5668
_cell_length_c                    3.5668
_cell_angle_alpha                 90.0000
_cell_angle_beta                  90.0000
_cell_angle_gamma                 90.0000
loop_
_atom_site_label
_atom_site_type_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_U_iso_or_equiv
_atom_site_adp_type
_atom_site_occupancy
C1     C     0.00000   0.00000   0.00000   0.00000  Uiso   1.00
loop_
_geom_bond_atom_site_label_1
_geom_bond_atom_site_label_2
_geom_bond_distance
_geom_bond_site_symmetry_2
_ccdc_geom_bond_type
C1     C1      1.544   14    S
C1     C1      1.544   16_445 S
C1     C1      1.544   13_454 S
C1     C1      1.544   15_544 S
```
:::

Run `bash run_cli.sh`; afterwards the folder contains (`example/cli_cleave_surface/diamond_111/output_file/`):

```text
.
├── input.toml
├── run_cli.sh
├── diamond.cif
├── POSCAR_111_slab.vasp  # surface slab
├── uv.csv                # in-plane surface vectors u, v
└── wb-surfgin.toml       # summary of the parameters used
```

#### TiO2_m5m20: (-5 -2 0) slab from a POSCAR (command-line mode)

The symmetry of `TiO2.vasp` is detected automatically.

Input files (`example/cli_cleave_surface/TiO2_m5m20/input_file/`):

```text
.
├── run_cli.sh
└── TiO2.vasp
```

`run_cli.sh`:

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

:::{dropdown} TiO2.vasp
```text
anatanse-opt
1.0
        3.9033000469         0.0000000000         0.0000000000
        0.0000000000         3.9033000469         0.0000000000
        0.0000000000         0.0000000000         9.6996002197
   Ti    O
    4    8
Direct
     0.500000000         0.500000000         0.000000000
     0.000000000         0.000000000         0.500000000
     0.500000000         0.000000000         0.250000000
     0.000000000         0.500000000         0.750000000
     0.500000000         0.500000000         0.207849979
     0.000000000         0.000000000         0.707849979
     0.500000000         0.000000000         0.457849979
     0.000000000         0.500000000         0.957849979
     0.000000000         0.500000000         0.542150021
     0.500000000         0.000000000         0.042150021
     0.000000000         0.000000000         0.292150021
     0.500000000         0.500000000         0.792150021
```
:::

Run `bash run_cli.sh`; afterwards the folder contains (`example/cli_cleave_surface/TiO2_m5m20/output_file/`):

```text
.
├── run_cli.sh
├── TiO2.vasp
├── POSCAR_m5m20_slab.vasp  # surface slab
├── uv.csv                  # in-plane surface vectors u, v
└── wb-surfgin.toml         # summary of the parameters used
```

---

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

### mismatch: Usage

```bash
# Mode 1: direct command-line parameters
calypso.x mismatch -f1 lat1.cif -f2 lat2.cif \
    --filesymmetry1 --filesymmetry2 \
    --maxmiller 5 --maxarea 200 --maxmismatch 0.05 -o ./interface

# Mode 2: TOML file
calypso.x mismatch --input mismatch.toml
```

### mismatch: Parameters

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

### mismatch: TOML input

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

### mismatch: Output files

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

### mismatch: Notes on `FlipSlab1Z`

`slab2` is placed below and `slab1` above. With `FlipSlab1Z=true` (the default),
`slab1` is mirrored within its occupied z range before stacking. This is useful
when the upper slab should be turned over so its interface side faces downward
and its outer/passivated side faces the vacuum. Set `FlipSlab1Z=false` to stack
`slab1` without this z inversion.

### mismatch: Errors (fatal — program stops)

| Exception | When |
|-----------|------|
| `FileNotFoundError` | `--input` given but the TOML file does not exist. |
| `ValueError` | Direct mode without both `--filepath1` and `--filepath2`. |
| `ValueError` | A `--SpecifyingMillerIndex*` list whose length is not a multiple of 3. |
| `KeyError` | TOML missing `[CRYSTAL1]` / `[CRYSTAL2]`, or either missing `FilePath`. |

### mismatch: Examples

The example files are in `example/cli_mismatch/` of CALYPSO-Python.

#### rutile_anatase: rutile / anatase TiO2 (TOML mode)

Both crystals are read from CIF files with their symmetry.

Input files (`example/cli_mismatch/rutile_anatase/input_file/`):

```text
.
├── mismatch.toml
├── run_cli.sh
├── anatase.cif
└── rutile.cif
```

`mismatch.toml`:

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

`run_cli.sh`:

```bash
#! /bin/bash

calypso.x mismatch --input mismatch.toml
```

:::{dropdown} anatase.cif
```text
data_anatanse-opt
_audit_creation_date              2015-11-18
_audit_creation_method            'Materials Studio'
_symmetry_space_group_name_H-M    'I41/AMD'
_symmetry_Int_Tables_number       141
_symmetry_cell_setting            tetragonal
loop_
_symmetry_equiv_pos_as_xyz
  x,y,z
  -x+1/2,-y+1/2,z+1/2
  -y,x+1/2,z+1/4
  y+1/2,-x,z+3/4
  -x+1/2,y,-z+3/4
  x,-y+1/2,-z+1/4
  y+1/2,x+1/2,-z+1/2
  -y,-x,-z
  -x,-y+1/2,-z+1/4
  x+1/2,y,-z+3/4
  y,-x,-z
  -y+1/2,x+1/2,-z+1/2
  x+1/2,-y+1/2,z+1/2
  -x,y,z
  -y+1/2,-x,z+3/4
  y,x+1/2,z+1/4
  x+1/2,y+1/2,z+1/2
  -x,-y,z
  -y+1/2,x,z+3/4
  y,-x+1/2,z+1/4
  -x,y+1/2,-z+1/4
  x+1/2,-y,-z+3/4
  y,x,-z
  -y+1/2,-x+1/2,-z+1/2
  -x+1/2,-y,-z+3/4
  x,y+1/2,-z+1/4
  y+1/2,-x+1/2,-z+1/2
  -y,x,-z
  x,-y,z
  -x+1/2,y+1/2,z+1/2
  -y,-x+1/2,z+1/4
  y+1/2,x,z+3/4
_cell_length_a                    3.9033
_cell_length_b                    3.9033
_cell_length_c                    9.6996
_cell_angle_alpha                 90.0000
_cell_angle_beta                  90.0000
_cell_angle_gamma                 90.0000
loop_
_atom_site_label
_atom_site_type_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_U_iso_or_equiv
_atom_site_adp_type
_atom_site_occupancy
Ti1    Ti   -0.50000   0.50000   1.00000   0.01267  Uiso   1.00
O1     O    -0.50000   0.50000   1.20785   0.01267  Uiso   1.00
loop_
_geom_bond_atom_site_label_1
_geom_bond_atom_site_label_2
_geom_bond_distance
_geom_bond_site_symmetry_2
_ccdc_geom_bond_type
Ti1    O1      2.016   .     S
Ti1    O1      2.016   8_557 S
Ti1    Ti1     3.113   3     S
Ti1    Ti1     3.113   4_454 S
Ti1    Ti1     3.113   4_354 S
Ti1    Ti1     3.113   3_565 S
Ti1    O1      1.994   6_557 S
Ti1    O1      1.994   4_454 S
Ti1    O1      1.994   4_354 S
Ti1    O1      1.994   6_567 S
O1     Ti1     1.994   3     S
O1     Ti1     1.994   3_565 S
```
:::

:::{dropdown} rutile.cif
```text
data_rutile-opt
_audit_creation_date              2015-11-18
_audit_creation_method            'Materials Studio'
_symmetry_space_group_name_H-M    'P42/MNM'
_symmetry_Int_Tables_number       136
_symmetry_cell_setting            tetragonal
loop_
_symmetry_equiv_pos_as_xyz
  x,y,z
  -x,-y,z
  -y+1/2,x+1/2,z+1/2
  y+1/2,-x+1/2,z+1/2
  -x+1/2,y+1/2,-z+1/2
  x+1/2,-y+1/2,-z+1/2
  y,x,-z
  -y,-x,-z
  -x,-y,-z
  x,y,-z
  y+1/2,-x+1/2,-z+1/2
  -y+1/2,x+1/2,-z+1/2
  x+1/2,-y+1/2,z+1/2
  -x+1/2,y+1/2,z+1/2
  -y,-x,z
  y,x,z
_cell_length_a                    4.6953
_cell_length_b                    4.6953
_cell_length_c                    3.0442
_cell_angle_alpha                 90.0000
_cell_angle_beta                  90.0000
_cell_angle_gamma                 90.0000
loop_
_atom_site_label
_atom_site_type_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_U_iso_or_equiv
_atom_site_adp_type
_atom_site_occupancy
Ti1    Ti    0.00000   0.00000  -0.00000   0.01267  Uiso   1.00
O1     O     0.30533   0.30533  -0.00000   0.01267  Uiso   1.00
```
:::

Run `bash run_cli.sh`; afterwards the folder contains (`example/cli_mismatch/rutile_anatase/output_file/`):

```text
.
├── mismatch.toml
├── run_cli.sh
├── anatase.cif
├── rutile.cif
├── matched_lattices.csv             # list of the matched pairs
├── wb-mismatch.toml                 # summary of the parameters used
└── matched_supercells/              # one folder per match
    ├── pair_1/
    │   ├── combined_interface.vasp  # stacked interface
    │   ├── lat1_supercell.vasp      # slab of crystal 1
    │   └── lat2_supercell.vasp      # slab of crystal 2
    ├── pair_2/
    │   ├── combined_interface.vasp  # stacked interface
    │   ├── lat1_supercell.vasp      # slab of crystal 1
    │   └── lat2_supercell.vasp      # slab of crystal 2
    └── pair_3/
        ├── combined_interface.vasp  # stacked interface
        ├── lat1_supercell.vasp      # slab of crystal 1
        └── lat2_supercell.vasp      # slab of crystal 2
```

#### Ni_BN: h-BN monolayer on bulk Ni (TOML mode)

The Miller indices of both crystals are fixed with `SpecifyingMillerIndex`.

Input files (`example/cli_mismatch/Ni_BN/input_file/`):

```text
.
├── mismatch.toml
├── run_cli.sh
├── BN.vasp
└── Ni.vasp
```

`mismatch.toml`:

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

`run_cli.sh`:

```bash
#! /bin/bash

calypso.x mismatch --input mismatch.toml
```

:::{dropdown} BN.vasp
```text
B2 N2
1.0
        2.5159442425         0.0000000000         0.0000000000
       -1.2579721212         2.1788716285         0.0000000000
        0.0000000000         0.0000000000         7.2582530975
    B    N
    1    1
Direct
     0.000000000         0.000000000         0.250000000
     0.666666670         0.333333330         0.250000000
```
:::

:::{dropdown} Ni.vasp
```text
Ni
1.0
        3.5239999294         0.0000000000         0.0000000000
        0.0000000000         3.5239999294         0.0000000000
        0.0000000000         0.0000000000         3.5239999294
   Ni
    4
Direct
     0.000000000         0.000000000         0.000000000
     0.000000000         0.500000000         0.500000000
     0.500000000         0.000000000         0.500000000
     0.500000000         0.500000000         0.000000000
```
:::

Run `bash run_cli.sh`; afterwards the folder contains (`example/cli_mismatch/Ni_BN/output_file/`):

```text
.
├── mismatch.toml
├── run_cli.sh
├── BN.vasp
├── Ni.vasp
├── matched_lattices.csv             # list of the matched pairs
├── wb-mismatch.toml                 # summary of the parameters used
└── matched_supercells/              # one folder per match
    ├── pair_1/
    │   ├── combined_interface.vasp  # stacked interface
    │   ├── lat1_supercell.vasp      # slab of crystal 1
    │   └── lat2_supercell.vasp      # slab of crystal 2
    ├── pair_2/
    │   ├── combined_interface.vasp  # stacked interface
    │   ├── lat1_supercell.vasp      # slab of crystal 1
    │   └── lat2_supercell.vasp      # slab of crystal 2
    └── pair_3/
        ├── combined_interface.vasp  # stacked interface
        ├── lat1_supercell.vasp      # slab of crystal 1
        └── lat2_supercell.vasp      # slab of crystal 2
```

#### LCO_LPS: LiCoO2 / Li3PS4 (command-line mode)

Both crystals are read from CIF files with their symmetry.

Input files (`example/cli_mismatch/LCO_LPS/input_file/`):

```text
.
├── run_cli.sh
├── lat1.cif
└── lat2.cif
```

`run_cli.sh`:

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

:::{dropdown} lat1.cif
```text
data_LiCoO2-opt
_audit_creation_date              2017-10-16
_audit_creation_method            'Materials Studio'
_symmetry_space_group_name_H-M    'R-3M'
_symmetry_Int_Tables_number       166
_symmetry_cell_setting            trigonal
loop_
_symmetry_equiv_pos_as_xyz
  x,y,z
  -y,x-y,z
  -x+y,-x,z
  y,x,-z
  x-y,-y,-z
  -x,-x+y,-z
  -x,-y,-z
  y,-x+y,-z
  x-y,x,-z
  -y,-x,z
  -x+y,y,z
  x,x-y,z
  x+2/3,y+1/3,z+1/3
  -y+2/3,x-y+1/3,z+1/3
  -x+y+2/3,-x+1/3,z+1/3
  y+2/3,x+1/3,-z+1/3
  x-y+2/3,-y+1/3,-z+1/3
  -x+2/3,-x+y+1/3,-z+1/3
  -x+2/3,-y+1/3,-z+1/3
  y+2/3,-x+y+1/3,-z+1/3
  x-y+2/3,x+1/3,-z+1/3
  -y+2/3,-x+1/3,z+1/3
  -x+y+2/3,y+1/3,z+1/3
  x+2/3,x-y+1/3,z+1/3
  x+1/3,y+2/3,z+2/3
  -y+1/3,x-y+2/3,z+2/3
  -x+y+1/3,-x+2/3,z+2/3
  y+1/3,x+2/3,-z+2/3
  x-y+1/3,-y+2/3,-z+2/3
  -x+1/3,-x+y+2/3,-z+2/3
  -x+1/3,-y+2/3,-z+2/3
  y+1/3,-x+y+2/3,-z+2/3
  x-y+1/3,x+2/3,-z+2/3
  -y+1/3,-x+2/3,z+2/3
  -x+y+1/3,y+2/3,z+2/3
  x+1/3,x-y+2/3,z+2/3
_cell_length_a                    2.8212
_cell_length_b                    2.8212
_cell_length_c                    14.1681
_cell_angle_alpha                 90.0000
_cell_angle_beta                  90.0000
_cell_angle_gamma                 120.0000
loop_
_atom_site_label
_atom_site_type_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_U_iso_or_equiv
_atom_site_adp_type
_atom_site_occupancy
Li1    Li    0.00000   0.00000   0.50000   0.01267  Uiso   1.00
Co1    Co    0.66667   0.33333   0.33333   0.01267  Uiso   1.00
O1     O     0.66667   0.33333   0.59348   0.01267  Uiso   1.00
```
:::

:::{dropdown} lat2.cif
```text
data_Li3PS4-opt
_audit_creation_date              2017-10-16
_audit_creation_method            'Materials Studio'
_symmetry_space_group_name_H-M    'PNMA'
_symmetry_Int_Tables_number       62
_symmetry_cell_setting            orthorhombic
loop_
_symmetry_equiv_pos_as_xyz
  x,y,z
  -x+1/2,-y,z+1/2
  -x,y+1/2,-z
  x+1/2,-y+1/2,-z+1/2
  -x,-y,-z
  x+1/2,y,-z+1/2
  x,-y+1/2,z
  -x+1/2,y+1/2,z+1/2
_cell_length_a                    13.0669
_cell_length_b                    8.0991
_cell_length_c                    6.2530
_cell_angle_alpha                 90.0000
_cell_angle_beta                  90.0000
_cell_angle_gamma                 90.0000
loop_
_atom_site_label
_atom_site_type_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_U_iso_or_equiv
_atom_site_adp_type
_atom_site_occupancy
Li1    Li   -0.16695   0.96733  -0.60975   0.01267  Uiso   1.00
S9     S    -0.34637   0.96376  -0.72928   0.01267  Uiso   1.00
Li9    Li   -0.50000  -0.00000  -0.50000   0.01267  Uiso   1.00
P1     P    -0.41040   0.75000  -0.84658   0.01267  Uiso   1.00
S1     S    -0.39904   0.75000  -0.17207   0.01267  Uiso   1.00
S5     S     0.44016   0.75000  -0.72634   0.01267  Uiso   1.00
```
:::

Run `bash run_cli.sh`; afterwards the folder contains (`example/cli_mismatch/LCO_LPS/output_file/`):

```text
.
├── run_cli.sh
├── lat1.cif
├── lat2.cif
├── matched_lattices.csv             # list of the matched pairs
├── wb-mismatch.toml                 # summary of the parameters used
└── matched_supercells/              # one folder per match
    ├── pair_1/
    │   ├── combined_interface.vasp  # stacked interface
    │   ├── lat1_supercell.vasp      # slab of crystal 1
    │   └── lat2_supercell.vasp      # slab of crystal 2
    ├── pair_2/
    │   ├── combined_interface.vasp  # stacked interface
    │   ├── lat1_supercell.vasp      # slab of crystal 1
    │   └── lat2_supercell.vasp      # slab of crystal 2
    └── pair_3/
        ├── combined_interface.vasp  # stacked interface
        ├── lat1_supercell.vasp      # slab of crystal 1
        └── lat2_supercell.vasp      # slab of crystal 2
```

#### MXene_MoS2: MoS2 / Mo2CO2 monolayers (command-line mode)

The layer plane of both monolayers is fixed to (0 0 1).

Input files (`example/cli_mismatch/MXene_MoS2/input_file/`):

```text
.
├── run_cli.sh
├── Mo2CO2.vasp
└── MoS2.vasp
```

`run_cli.sh`:

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

:::{dropdown} Mo2CO2.vasp
```text
POSCAR
   1.00000000000000
     2.8713901549661016   -0.0000000000004610    0.0000000000000000
    -1.4356950774334485    2.4866968183927578    0.0000000000000000
    -0.0000000000000000   -0.0000000000000000   29.9981157952378261
   Mo   C    O
     2     1     2
Direct
  0.6666666870000029  0.3333333429999996  0.4540913541341994
  0.3333333129999971  0.6666666269999979  0.5459086458658006
 -0.0000000000000000  0.0000000000000000  0.5000000000000000
  0.0000000000000000  0.0000000000000000  0.5865507526397682
 -0.0000000000000000 -0.0000000000000000  0.4134492473602318

  0.00000000E+00  0.00000000E+00  0.00000000E+00
  0.00000000E+00  0.00000000E+00  0.00000000E+00
  0.00000000E+00  0.00000000E+00  0.00000000E+00
  0.00000000E+00  0.00000000E+00  0.00000000E+00
  0.00000000E+00  0.00000000E+00  0.00000000E+00
```
:::

:::{dropdown} MoS2.vasp
```text
MoS2
1.0
        3.1621000767         0.0000000000         0.0000000000
       -1.5810500383         2.7384589957         0.0000000000
        0.0000000000         0.0000000000        30.4978008270
   Mo    S
    1    2
Direct
     0.666666985         0.333332986         0.500000000
     0.000000000         0.000000000         0.448559999
     0.000000000         0.000000000         0.551440001
```
:::

Run `bash run_cli.sh`; afterwards the folder contains (`example/cli_mismatch/MXene_MoS2/output_file/`):

```text
.
├── run_cli.sh
├── Mo2CO2.vasp
├── MoS2.vasp
├── matched_lattices.csv             # list of the matched pairs
├── wb-mismatch.toml                 # summary of the parameters used
└── matched_supercells/              # one folder per match
    ├── pair_1/
    │   ├── combined_interface.vasp  # stacked interface
    │   ├── lat1_supercell.vasp      # slab of crystal 1
    │   └── lat2_supercell.vasp      # slab of crystal 2
    ├── pair_2/
    │   ├── combined_interface.vasp  # stacked interface
    │   ├── lat1_supercell.vasp      # slab of crystal 1
    │   └── lat2_supercell.vasp      # slab of crystal 2
    └── pair_3/
        ├── combined_interface.vasp  # stacked interface
        ├── lat1_supercell.vasp      # slab of crystal 1
        └── lat2_supercell.vasp      # slab of crystal 2
```

---

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

### combine: Usage

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

### combine: Parameters

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

### combine: TOML input

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

### combine: Output files

- **Combined structure** — `OutputFile`, in the format specified by
  `OutputFormat`.
- **`wb-combine.toml`** — a summary of the effective parameters used, written
  next to `OutputFile`.

Path fields written to `wb-combine.toml` are absolute paths, including
`STRUCTURE1.FilePath`, `STRUCTURE2.FilePath`, and `COMBINE.OutputFile`. The
summary file intentionally does not include `WriteSummary`.

Each slab's selective-dynamics mask is carried through into the combined
structure unchanged.

### combine: Notes on `FlipSlab1Z`

With `FlipSlab1Z=true` (default), structure 1 is mirrored in z within its own
occupied thickness before it is placed above structure 2. Set it to `false` if
the two slabs have already been oriented exactly as desired.

### combine: Errors (fatal — program stops)

| Exception | When |
|-----------|------|
| `FileNotFoundError` | `--input` given but the TOML file does not exist. |
| `ValueError` | Direct mode without both `--filepath1` and `--filepath2`. |
| `KeyError` | TOML missing `[STRUCTURE1]` / `[STRUCTURE2]`, or either missing `FilePath`. |

### combine: Examples

The example files are in `example/cli_combine/` of CALYPSO-Python.

#### rutile_anatase: stack a matched rutile / anatase pair

The two slabs are a matched pair from `mismatch`.

Input files (`example/cli_combine/rutile_anatase/input_file/`):

```text
.
├── combine.toml
├── run_cli.sh
├── anatase_slab.vasp
└── rutile_slab.vasp
```

`combine.toml`:

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

`run_cli.sh`:

```bash
#! /bin/bash

calypso.x combine --input combine.toml
```

:::{dropdown} anatase_slab.vasp
```text
CalyData_O104Ti65
1.0
     11.709900000000       7.806600000000       0.000000000000
     -7.806600000000      11.709900000000       0.000000000000
      0.000000000000       0.000000000000      24.699600000000
O Ti
104 65
Direct
   0.1153846154    0.9230769231    0.5785827244
   0.0384615385    0.3076923077    0.5785827244
   0.1923076923    0.5384615385    0.5785827244
   0.3461538462    0.7692307692    0.5785827244
   0.2692307692    0.1538461538    0.5785827244
   0.4230769231    0.3846153846    0.5785827244
   0.5769230769    0.6153846154    0.5785827244
   0.7307692308    0.8461538462    0.5785827244
   0.5000000000    0.0000000000    0.5785827244
   0.6538461538    0.2307692308    0.5785827244
   0.8076923077    0.4615384615    0.5785827244
   0.9615384615    0.6923076923    0.5785827244
   0.8846153846    0.0769230769    0.5785827244
   0.0384615385    0.8076923077    0.5135118844
   0.1153846154    0.4230769231    0.5135118844
   0.2692307692    0.6538461538    0.5135118844
   0.4230769231    0.8846153846    0.5135118844
   0.1923076923    0.0384615385    0.5135118844
   0.3461538462    0.2692307692    0.5135118844
   0.5000000000    0.5000000000    0.5135118844
   0.6538461538    0.7307692308    0.5135118844
   0.8076923077    0.9615384615    0.5135118844
   0.5769230769    0.1153846154    0.5135118844
   0.7307692308    0.3461538462    0.5135118844
   0.8846153846    0.5769230769    0.5135118844
   0.9615384615    0.1923076923    0.5135118844
   0.0769230769    0.6153846154    0.4804070455
   0.2307692308    0.8461538462    0.4804070455
   0.0000000000    0.0000000000    0.4804070455
   0.1538461538    0.2307692308    0.4804070455
   0.3076923077    0.4615384615    0.4804070455
   0.4615384615    0.6923076923    0.4804070455
   0.6153846154    0.9230769231    0.4804070455
   0.3846153846    0.0769230769    0.4804070455
   0.5384615385    0.3076923077    0.4804070455
   0.6923076923    0.5384615385    0.4804070455
   0.8461538462    0.7692307692    0.4804070455
   0.7692307692    0.1538461538    0.4804070455
   0.9230769231    0.3846153846    0.4804070455
   0.1153846154    0.9230769231    0.4153362054
   0.0384615385    0.3076923077    0.4153362054
   0.1923076923    0.5384615385    0.4153362054
   0.3461538462    0.7692307692    0.4153362054
   0.2692307692    0.1538461538    0.4153362054
   0.4230769231    0.3846153846    0.4153362054
   0.5769230769    0.6153846154    0.4153362054
   0.7307692308    0.8461538462    0.4153362054
   0.5000000000    0.0000000000    0.4153362054
   0.6538461538    0.2307692308    0.4153362054
   0.8076923077    0.4615384615    0.4153362054
   0.9615384615    0.6923076923    0.4153362054
   0.8846153846    0.0769230769    0.4153362054
   0.0000000000    0.5000000000    0.3822313665
   0.1538461538    0.7307692308    0.3822313665
   0.3076923077    0.9615384615    0.3822313665
   0.0769230769    0.1153846154    0.3822313665
   0.2307692308    0.3461538462    0.3822313665
   0.3846153846    0.5769230769    0.3822313665
   0.5384615385    0.8076923077    0.3822313665
   0.4615384615    0.1923076923    0.3822313665
   0.6153846154    0.4230769231    0.3822313665
   0.7692307692    0.6538461538    0.3822313665
   0.9230769231    0.8846153846    0.3822313665
   0.6923076923    0.0384615385    0.3822313665
   0.8461538462    0.2692307692    0.3822313665
   0.0769230769    0.6153846154    0.3171605265
   0.2307692308    0.8461538462    0.3171605265
   0.0000000000    0.0000000000    0.3171605265
   0.1538461538    0.2307692308    0.3171605265
   0.3076923077    0.4615384615    0.3171605265
   0.4615384615    0.6923076923    0.3171605265
   0.6153846154    0.9230769231    0.3171605265
   0.3846153846    0.0769230769    0.3171605265
   0.5384615385    0.3076923077    0.3171605265
   0.6923076923    0.5384615385    0.3171605265
   0.8461538462    0.7692307692    0.3171605265
   0.7692307692    0.1538461538    0.3171605265
   0.9230769231    0.3846153846    0.3171605265
   0.0384615385    0.8076923077    0.2840556875
   0.1153846154    0.4230769231    0.2840556875
   0.2692307692    0.6538461538    0.2840556875
   0.4230769231    0.8846153846    0.2840556875
   0.1923076923    0.0384615385    0.2840556875
   0.3461538462    0.2692307692    0.2840556875
   0.5000000000    0.5000000000    0.2840556875
   0.6538461538    0.7307692308    0.2840556875
   0.8076923077    0.9615384615    0.2840556875
   0.5769230769    0.1153846154    0.2840556875
   0.7307692308    0.3461538462    0.2840556875
   0.8846153846    0.5769230769    0.2840556875
   0.9615384615    0.1923076923    0.2840556875
   0.0000000000    0.5000000000    0.2189848475
   0.1538461538    0.7307692308    0.2189848475
   0.3076923077    0.9615384615    0.2189848475
   0.0769230769    0.1153846154    0.2189848475
   0.2307692308    0.3461538462    0.2189848475
   0.3846153846    0.5769230769    0.2189848475
   0.5384615385    0.8076923077    0.2189848475
   0.4615384615    0.1923076923    0.2189848475
   0.6153846154    0.4230769231    0.2189848475
   0.7692307692    0.6538461538    0.2189848475
   0.9230769231    0.8846153846    0.2189848475
   0.6923076923    0.0384615385    0.2189848475
   0.8461538462    0.2692307692    0.2189848475
   0.0384615385    0.8076923077    0.5951351439
   0.1153846154    0.4230769231    0.5951351439
   0.2692307692    0.6538461538    0.5951351439
   0.4230769231    0.8846153846    0.5951351439
   0.1923076923    0.0384615385    0.5951351439
   0.3461538462    0.2692307692    0.5951351439
   0.5000000000    0.5000000000    0.5951351439
   0.6538461538    0.7307692308    0.5951351439
   0.8076923077    0.9615384615    0.5951351439
   0.5769230769    0.1153846154    0.5951351439
   0.7307692308    0.3461538462    0.5951351439
   0.8846153846    0.5769230769    0.5951351439
   0.9615384615    0.1923076923    0.5951351439
   0.1153846154    0.9230769231    0.4969594649
   0.0384615385    0.3076923077    0.4969594649
   0.1923076923    0.5384615385    0.4969594649
   0.3461538462    0.7692307692    0.4969594649
   0.2692307692    0.1538461538    0.4969594649
   0.4230769231    0.3846153846    0.4969594649
   0.5769230769    0.6153846154    0.4969594649
   0.7307692308    0.8461538462    0.4969594649
   0.5000000000    0.0000000000    0.4969594649
   0.6538461538    0.2307692308    0.4969594649
   0.8076923077    0.4615384615    0.4969594649
   0.9615384615    0.6923076923    0.4969594649
   0.8846153846    0.0769230769    0.4969594649
   0.0769230769    0.6153846154    0.3987837860
   0.2307692308    0.8461538462    0.3987837860
   0.0000000000    0.0000000000    0.3987837860
   0.1538461538    0.2307692308    0.3987837860
   0.3076923077    0.4615384615    0.3987837860
   0.4615384615    0.6923076923    0.3987837860
   0.6153846154    0.9230769231    0.3987837860
   0.3846153846    0.0769230769    0.3987837860
   0.5384615385    0.3076923077    0.3987837860
   0.6923076923    0.5384615385    0.3987837860
   0.8461538462    0.7692307692    0.3987837860
   0.7692307692    0.1538461538    0.3987837860
   0.9230769231    0.3846153846    0.3987837860
   0.0000000000    0.5000000000    0.3006081070
   0.1538461538    0.7307692308    0.3006081070
   0.3076923077    0.9615384615    0.3006081070
   0.0769230769    0.1153846154    0.3006081070
   0.2307692308    0.3461538462    0.3006081070
   0.3846153846    0.5769230769    0.3006081070
   0.5384615385    0.8076923077    0.3006081070
   0.4615384615    0.1923076923    0.3006081070
   0.6153846154    0.4230769231    0.3006081070
   0.7692307692    0.6538461538    0.3006081070
   0.9230769231    0.8846153846    0.3006081070
   0.6923076923    0.0384615385    0.3006081070
   0.8461538462    0.2692307692    0.3006081070
   0.0384615385    0.8076923077    0.2024324281
   0.1153846154    0.4230769231    0.2024324281
   0.2692307692    0.6538461538    0.2024324281
   0.4230769231    0.8846153846    0.2024324281
   0.1923076923    0.0384615385    0.2024324281
   0.3461538462    0.2692307692    0.2024324281
   0.5000000000    0.5000000000    0.2024324281
   0.6538461538    0.7307692308    0.2024324281
   0.8076923077    0.9615384615    0.2024324281
   0.5769230769    0.1153846154    0.2024324281
   0.7307692308    0.3461538462    0.2024324281
   0.8846153846    0.5769230769    0.2024324281
   0.9615384615    0.1923076923    0.2024324281
```
:::

:::{dropdown} rutile_slab.vasp
```text
CalyData_O144Ti72
1.0
     14.085900000000       0.000000000000       0.000000000000
      0.000000000000      14.085900000000       0.000000000000
      0.000000000000       0.000000000000      25.654700000000
O Ti
144 72
Direct
   0.1017766667    0.1017766667    0.6102078761
   0.1017766667    0.4351100000    0.6102078761
   0.1017766667    0.7684433333    0.6102078761
   0.4351100000    0.1017766667    0.6102078761
   0.4351100000    0.4351100000    0.6102078761
   0.4351100000    0.7684433333    0.6102078761
   0.7684433333    0.1017766667    0.6102078761
   0.7684433333    0.4351100000    0.6102078761
   0.7684433333    0.7684433333    0.6102078761
   0.2315566667    0.2315566667    0.6102078761
   0.2315566667    0.5648900000    0.6102078761
   0.2315566667    0.8982233333    0.6102078761
   0.5648900000    0.2315566667    0.6102078761
   0.5648900000    0.5648900000    0.6102078761
   0.5648900000    0.8982233333    0.6102078761
   0.8982233333    0.2315566667    0.6102078761
   0.8982233333    0.5648900000    0.6102078761
   0.8982233333    0.8982233333    0.6102078761
   0.0648900000    0.2684433333    0.5508776170
   0.0648900000    0.6017766667    0.5508776170
   0.0648900000    0.9351100000    0.5508776170
   0.3982233333    0.2684433333    0.5508776170
   0.3982233333    0.6017766667    0.5508776170
   0.3982233333    0.9351100000    0.5508776170
   0.7315566667    0.2684433333    0.5508776170
   0.7315566667    0.6017766667    0.5508776170
   0.7315566667    0.9351100000    0.5508776170
   0.2684433333    0.0648900000    0.5508776170
   0.2684433333    0.3982233333    0.5508776170
   0.2684433333    0.7315566667    0.5508776170
   0.6017766667    0.0648900000    0.5508776170
   0.6017766667    0.3982233333    0.5508776170
   0.6017766667    0.7315566667    0.5508776170
   0.9351100000    0.0648900000    0.5508776170
   0.9351100000    0.3982233333    0.5508776170
   0.9351100000    0.7315566667    0.5508776170
   0.1017766667    0.1017766667    0.4915473578
   0.1017766667    0.4351100000    0.4915473578
   0.1017766667    0.7684433333    0.4915473578
   0.4351100000    0.1017766667    0.4915473578
   0.4351100000    0.4351100000    0.4915473578
   0.4351100000    0.7684433333    0.4915473578
   0.7684433333    0.1017766667    0.4915473578
   0.7684433333    0.4351100000    0.4915473578
   0.7684433333    0.7684433333    0.4915473578
   0.2315566667    0.2315566667    0.4915473578
   0.2315566667    0.5648900000    0.4915473578
   0.2315566667    0.8982233333    0.4915473578
   0.5648900000    0.2315566667    0.4915473578
   0.5648900000    0.5648900000    0.4915473578
   0.5648900000    0.8982233333    0.4915473578
   0.8982233333    0.2315566667    0.4915473578
   0.8982233333    0.5648900000    0.4915473578
   0.8982233333    0.8982233333    0.4915473578
   0.0648900000    0.2684433333    0.4322170986
   0.0648900000    0.6017766667    0.4322170986
   0.0648900000    0.9351100000    0.4322170986
   0.3982233333    0.2684433333    0.4322170986
   0.3982233333    0.6017766667    0.4322170986
   0.3982233333    0.9351100000    0.4322170986
   0.7315566667    0.2684433333    0.4322170986
   0.7315566667    0.6017766667    0.4322170986
   0.7315566667    0.9351100000    0.4322170986
   0.2684433333    0.0648900000    0.4322170986
   0.2684433333    0.3982233333    0.4322170986
   0.2684433333    0.7315566667    0.4322170986
   0.6017766667    0.0648900000    0.4322170986
   0.6017766667    0.3982233333    0.4322170986
   0.6017766667    0.7315566667    0.4322170986
   0.9351100000    0.0648900000    0.4322170986
   0.9351100000    0.3982233333    0.4322170986
   0.9351100000    0.7315566667    0.4322170986
   0.1017766667    0.1017766667    0.3728868394
   0.1017766667    0.4351100000    0.3728868394
   0.1017766667    0.7684433333    0.3728868394
   0.4351100000    0.1017766667    0.3728868394
   0.4351100000    0.4351100000    0.3728868394
   0.4351100000    0.7684433333    0.3728868394
   0.7684433333    0.1017766667    0.3728868394
   0.7684433333    0.4351100000    0.3728868394
   0.7684433333    0.7684433333    0.3728868394
   0.2315566667    0.2315566667    0.3728868394
   0.2315566667    0.5648900000    0.3728868394
   0.2315566667    0.8982233333    0.3728868394
   0.5648900000    0.2315566667    0.3728868394
   0.5648900000    0.5648900000    0.3728868394
   0.5648900000    0.8982233333    0.3728868394
   0.8982233333    0.2315566667    0.3728868394
   0.8982233333    0.5648900000    0.3728868394
   0.8982233333    0.8982233333    0.3728868394
   0.0648900000    0.2684433333    0.3135565803
   0.0648900000    0.6017766667    0.3135565803
   0.0648900000    0.9351100000    0.3135565803
   0.3982233333    0.2684433333    0.3135565803
   0.3982233333    0.6017766667    0.3135565803
   0.3982233333    0.9351100000    0.3135565803
   0.7315566667    0.2684433333    0.3135565803
   0.7315566667    0.6017766667    0.3135565803
   0.7315566667    0.9351100000    0.3135565803
   0.2684433333    0.0648900000    0.3135565803
   0.2684433333    0.3982233333    0.3135565803
   0.2684433333    0.7315566667    0.3135565803
   0.6017766667    0.0648900000    0.3135565803
   0.6017766667    0.3982233333    0.3135565803
   0.6017766667    0.7315566667    0.3135565803
   0.9351100000    0.0648900000    0.3135565803
   0.9351100000    0.3982233333    0.3135565803
   0.9351100000    0.7315566667    0.3135565803
   0.1017766667    0.1017766667    0.2542263211
   0.1017766667    0.4351100000    0.2542263211
   0.1017766667    0.7684433333    0.2542263211
   0.4351100000    0.1017766667    0.2542263211
   0.4351100000    0.4351100000    0.2542263211
   0.4351100000    0.7684433333    0.2542263211
   0.7684433333    0.1017766667    0.2542263211
   0.7684433333    0.4351100000    0.2542263211
   0.7684433333    0.7684433333    0.2542263211
   0.2315566667    0.2315566667    0.2542263211
   0.2315566667    0.5648900000    0.2542263211
   0.2315566667    0.8982233333    0.2542263211
   0.5648900000    0.2315566667    0.2542263211
   0.5648900000    0.5648900000    0.2542263211
   0.5648900000    0.8982233333    0.2542263211
   0.8982233333    0.2315566667    0.2542263211
   0.8982233333    0.5648900000    0.2542263211
   0.8982233333    0.8982233333    0.2542263211
   0.0648900000    0.2684433333    0.1948960619
   0.0648900000    0.6017766667    0.1948960619
   0.0648900000    0.9351100000    0.1948960619
   0.3982233333    0.2684433333    0.1948960619
   0.3982233333    0.6017766667    0.1948960619
   0.3982233333    0.9351100000    0.1948960619
   0.7315566667    0.2684433333    0.1948960619
   0.7315566667    0.6017766667    0.1948960619
   0.7315566667    0.9351100000    0.1948960619
   0.2684433333    0.0648900000    0.1948960619
   0.2684433333    0.3982233333    0.1948960619
   0.2684433333    0.7315566667    0.1948960619
   0.6017766667    0.0648900000    0.1948960619
   0.6017766667    0.3982233333    0.1948960619
   0.6017766667    0.7315566667    0.1948960619
   0.9351100000    0.0648900000    0.1948960619
   0.9351100000    0.3982233333    0.1948960619
   0.9351100000    0.7315566667    0.1948960619
   0.0000000000    0.0000000000    0.6102078761
   0.0000000000    0.3333333333    0.6102078761
   0.0000000000    0.6666666667    0.6102078761
   0.3333333333    0.0000000000    0.6102078761
   0.3333333333    0.3333333333    0.6102078761
   0.3333333333    0.6666666667    0.6102078761
   0.6666666667    0.0000000000    0.6102078761
   0.6666666667    0.3333333333    0.6102078761
   0.6666666667    0.6666666667    0.6102078761
   0.1666666667    0.1666666667    0.5508776170
   0.1666666667    0.5000000000    0.5508776170
   0.1666666667    0.8333333333    0.5508776170
   0.5000000000    0.1666666667    0.5508776170
   0.5000000000    0.5000000000    0.5508776170
   0.5000000000    0.8333333333    0.5508776170
   0.8333333333    0.1666666667    0.5508776170
   0.8333333333    0.5000000000    0.5508776170
   0.8333333333    0.8333333333    0.5508776170
   0.0000000000    0.0000000000    0.4915473578
   0.0000000000    0.3333333333    0.4915473578
   0.0000000000    0.6666666667    0.4915473578
   0.3333333333    0.0000000000    0.4915473578
   0.3333333333    0.3333333333    0.4915473578
   0.3333333333    0.6666666667    0.4915473578
   0.6666666667    0.0000000000    0.4915473578
   0.6666666667    0.3333333333    0.4915473578
   0.6666666667    0.6666666667    0.4915473578
   0.1666666667    0.1666666667    0.4322170986
   0.1666666667    0.5000000000    0.4322170986
   0.1666666667    0.8333333333    0.4322170986
   0.5000000000    0.1666666667    0.4322170986
   0.5000000000    0.5000000000    0.4322170986
   0.5000000000    0.8333333333    0.4322170986
   0.8333333333    0.1666666667    0.4322170986
   0.8333333333    0.5000000000    0.4322170986
   0.8333333333    0.8333333333    0.4322170986
   0.0000000000    0.0000000000    0.3728868394
   0.0000000000    0.3333333333    0.3728868394
   0.0000000000    0.6666666667    0.3728868394
   0.3333333333    0.0000000000    0.3728868394
   0.3333333333    0.3333333333    0.3728868394
   0.3333333333    0.6666666667    0.3728868394
   0.6666666667    0.0000000000    0.3728868394
   0.6666666667    0.3333333333    0.3728868394
   0.6666666667    0.6666666667    0.3728868394
   0.1666666667    0.1666666667    0.3135565803
   0.1666666667    0.5000000000    0.3135565803
   0.1666666667    0.8333333333    0.3135565803
   0.5000000000    0.1666666667    0.3135565803
   0.5000000000    0.5000000000    0.3135565803
   0.5000000000    0.8333333333    0.3135565803
   0.8333333333    0.1666666667    0.3135565803
   0.8333333333    0.5000000000    0.3135565803
   0.8333333333    0.8333333333    0.3135565803
   0.0000000000    0.0000000000    0.2542263211
   0.0000000000    0.3333333333    0.2542263211
   0.0000000000    0.6666666667    0.2542263211
   0.3333333333    0.0000000000    0.2542263211
   0.3333333333    0.3333333333    0.2542263211
   0.3333333333    0.6666666667    0.2542263211
   0.6666666667    0.0000000000    0.2542263211
   0.6666666667    0.3333333333    0.2542263211
   0.6666666667    0.6666666667    0.2542263211
   0.1666666667    0.1666666667    0.1948960619
   0.1666666667    0.5000000000    0.1948960619
   0.1666666667    0.8333333333    0.1948960619
   0.5000000000    0.1666666667    0.1948960619
   0.5000000000    0.5000000000    0.1948960619
   0.5000000000    0.8333333333    0.1948960619
   0.8333333333    0.1666666667    0.1948960619
   0.8333333333    0.5000000000    0.1948960619
   0.8333333333    0.8333333333    0.1948960619
```
:::

Run `bash run_cli.sh`; afterwards the folder contains (`example/cli_combine/rutile_anatase/output_file/`):

```text
.
├── combine.toml
├── run_cli.sh
├── anatase_slab.vasp
├── rutile_slab.vasp
├── rutile_anatase_interface.vasp  # stacked interface
└── wb-combine.toml                # summary of the parameters used
```

#### MoS2_MXene: stack monolayer MoS2 on Mo2CO2

Both inputs are single layers with vacuum.

Input files (`example/cli_combine/MoS2_MXene/input_file/`):

```text
.
├── combine.toml
├── run_cli.sh
├── Mo2CO2.vasp
└── MoS2.vasp
```

`combine.toml`:

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

`run_cli.sh`:

```bash
#! /bin/bash

calypso.x combine --input combine.toml
```

:::{dropdown} Mo2CO2.vasp
```text
CalyData_C9O18Mo18
1.0
      4.307085232441       7.460090455117       0.000000000000
     -4.307085232441       7.460090455117       0.000000000000
      0.000000000000       0.000000000000      20.192718999706
C O Mo
9 18 18
Direct
   0.0000000000    0.0000000000    0.3761929981
   0.0000000000    0.3333333333    0.3761929981
   0.0000000000    0.6666666667    0.3761929981
   0.3333333333    0.0000000000    0.3761929981
   0.3333333333    0.3333333333    0.3761929981
   0.3333333333    0.6666666667    0.3761929981
   0.6666666667    0.0000000000    0.3761929981
   0.6666666667    0.3333333333    0.3761929981
   0.6666666667    0.6666666667    0.3761929981
   0.0000000000    0.0000000000    0.5047719923
   0.0000000000    0.3333333333    0.5047719923
   0.0000000000    0.6666666667    0.5047719923
   0.3333333333    0.0000000000    0.5047719923
   0.3333333333    0.3333333333    0.5047719923
   0.3333333333    0.6666666667    0.5047719923
   0.6666666667    0.0000000000    0.5047719923
   0.6666666667    0.3333333333    0.5047719923
   0.6666666667    0.6666666667    0.5047719923
   0.0000000000    0.0000000000    0.2476140038
   0.0000000000    0.3333333333    0.2476140038
   0.0000000000    0.6666666667    0.2476140038
   0.3333333333    0.0000000000    0.2476140038
   0.3333333333    0.3333333333    0.2476140038
   0.3333333333    0.6666666667    0.2476140038
   0.6666666667    0.0000000000    0.2476140038
   0.6666666667    0.3333333333    0.2476140038
   0.6666666667    0.6666666667    0.2476140038
   0.1111111111    0.1111111111    0.4443944560
   0.1111111111    0.4444444444    0.4443944560
   0.1111111111    0.7777777778    0.4443944560
   0.4444444444    0.1111111111    0.4443944560
   0.4444444444    0.4444444444    0.4443944560
   0.4444444444    0.7777777778    0.4443944560
   0.7777777778    0.1111111111    0.4443944560
   0.7777777778    0.4444444444    0.4443944560
   0.7777777778    0.7777777778    0.4443944560
   0.2222222222    0.2222222222    0.3079915402
   0.2222222222    0.5555555556    0.3079915402
   0.2222222222    0.8888888889    0.3079915402
   0.5555555556    0.2222222222    0.3079915402
   0.5555555556    0.5555555556    0.3079915402
   0.5555555556    0.8888888889    0.3079915402
   0.8888888889    0.2222222222    0.3079915402
   0.8888888889    0.5555555556    0.3079915402
   0.8888888889    0.8888888889    0.3079915402
```
:::

:::{dropdown} MoS2.vasp
```text
CalyData_S14Mo7
1.0
      6.324200153348       5.476917991417       0.000000000000
     -1.581050038337       8.215376987125       0.000000000000
      0.000000000000       0.000000000000      18.137613810077
S Mo
14 7
Direct
   0.0952380952    0.3809523810    0.4486595588
   0.5238095238    0.0952380952    0.4486595588
   0.3809523810    0.5238095238    0.4486595588
   0.2380952381    0.9523809524    0.4486595588
   0.8095238095    0.2380952381    0.4486595588
   0.6666666667    0.6666666667    0.4486595588
   0.9523809524    0.8095238095    0.4486595588
   0.0952380952    0.3809523810    0.2756702206
   0.5238095238    0.0952380952    0.2756702206
   0.3809523810    0.5238095238    0.2756702206
   0.2380952381    0.9523809524    0.2756702206
   0.8095238095    0.2380952381    0.2756702206
   0.6666666667    0.6666666667    0.2756702206
   0.9523809524    0.8095238095    0.2756702206
   0.0476190476    0.1904761905    0.3621648897
   0.3333333333    0.3333333333    0.3621648897
   0.1904761905    0.7619047619    0.3621648897
   0.7619047619    0.0476190476    0.3621648897
   0.6190476190    0.4761904762    0.3621648897
   0.4761904762    0.9047619048    0.3621648897
   0.9047619048    0.6190476190    0.3621648897
```
:::

Run `bash run_cli.sh`; afterwards the folder contains (`example/cli_combine/MoS2_MXene/output_file/`):

```text
.
├── combine.toml
├── run_cli.sh
├── Mo2CO2.vasp
├── MoS2.vasp
├── MoS2_MXene_interface.vasp  # stacked interface
└── wb-combine.toml            # summary of the parameters used
```
