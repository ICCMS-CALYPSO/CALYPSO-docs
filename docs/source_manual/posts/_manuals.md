# CALYPSO Manual

basic inputs and outputs

- [CALYPSO Manual](#calypso-manual)
  - [CALYPSO Inputs](#calypso-inputs)
    - [Common parameters](#common-parameters)
      - [**`systemname`**](#systemname)
      - [**`numberofspecies`**](#numberofspecies)
      - [**`nameofatoms`**](#nameofatoms)
      - [**`numberofatoms`**](#numberofatoms)
      - [**`numberofformula`**](#numberofformula)
      - [**`Volume`**](#volume)
      - [**`@DistanceOfIon`**](#distanceofion)
      - [**`Ialgo`**](#ialgo)
      - [**`ICode`**](#icode)
      - [**`NumberOfLocalOptim`**](#numberoflocaloptim)
      - [**`PsoRatio`**](#psoratio)
      - [**`PopSize`**](#popsize)
      - [**`Kgrid`** (deprecated)](#kgrid-deprecated)
      - [**`Command`**](#command)
      - [**`MaxStep`**](#maxstep)
      - [**`PickUp`**](#pickup)
      - [**`PickStep`**](#pickstep)
      - [**`MaxTime`**](#maxtime)
      - [**`LMC`**](#lmc)
    - [Parameters for structural prediction of two-dimensional layers](#parameters-for-structural-prediction-of-two-dimensional-layers)
      - [**`2D`**](#2d)
      - [**`LFilm`**](#lfilm)
      - [**`Thickness`**](#thickness)
      - [**`Area`**](#area)
      - [**`MultiLayer`**](#multilayer)
      - [**`DeltaZ`**](#deltaz)
      - [**`LayerGap`**](#layergap)
      - [**`VacuumGap`**](#vacuumgap)
      - [**`@LayerType`**](#layertype)
      - [**`LAtom_Dis`**](#latom_dis)
    - [Parameters for cluster structure prediction](#parameters-for-cluster-structure-prediction)
      - [**`Cluster`**](#cluster)
      - [**`Vacancy`**](#vacancy)
    - [Parameters for rigid Molecules prediction](#parameters-for-rigid-molecules-prediction)
      - [**`MOL`**](#mol)
      - [**`NumberOfTypeMolecule`**](#numberoftypemolecule)
      - [**`NumberOfMolecule`**](#numberofmolecule)
      - [**`DistOfMol`**](#distofmol)
    - [Parameters for with variational stoichiometry structure prediction](#parameters-for-with-variational-stoichiometry-structure-prediction)
      - [**`VSC`**](#vsc)
      - [**`MaxNumAtom`**](#maxnumatom)
      - [**`@CtrlRange`**](#ctrlrange)
    - [Parameters for surface reconstruction prediction](#parameters-for-surface-reconstruction-prediction)
      - [**`LSurface`**](#lsurface)
      - [**`SurfaceThickness`**](#surfacethickness)
      - [**`Substrate`** (surface)](#substrate-surface)
      - [**`SurfaceAStoms`**](#surfaceastoms)
      - [**`SpaceSaving`**](#spacesaving)
      - [**`ECR`**](#ecr)
    - [Parameters for automatic generate substrate](#parameters-for-automatic-generate-substrate)
      - [**`CifFilePath`**](#ciffilepath)
      - [**`MillerIndex`**](#millerindex)
      - [**`@MatrixNotation`**](#matrixnotation)
      - [**`SlabVacuumThick`**](#slabvacuumthick)
      - [**`SlabTopMost`**](#slabtopmost)
      - [**`SlabNumLayers`**](#slabnumlayers)
      - [**`NumRelaxedLayers`**](#numrelaxedlayers)
      - [**`CapBondsWithH`**](#capbondswithh)
    - [Parameters for solid-solid interfacial prediction](#parameters-for-solid-solid-interfacial-prediction)
      - [**`LSurface`** (deprecated)](#lsurface-deprecated)
      - [**`LInterface`**](#linterface)
      - [**`InterfaceTranslation`**](#interfacetranslation)
      - [**`TranslationLimitA`**](#translationlimita)
      - [**`TranslationLimitB`**](#translationlimitb)
      - [**`Rand_Scheme`**](#rand_scheme)
      - [**`Interface_thickness`**](#interface_thickness)
      - [**`@SURFACE_ATOMS`**](#surface_atoms)
      - [**`@COORDINATE_NUMBER`**](#coordinate_number)
      - [**`Substrate`** (interface)](#substrate-interface)
      - [**`Substrate2`**](#substrate2)
      - [**`Twin_Interface`**](#twin_interface)
    - [Parameters for inverse design of superhard materials](#parameters-for-inverse-design-of-superhard-materials)
      - [**`Hardness`**](#hardness)
    - [Parameters for atom or molecule adsorption of 2D layer materials](#parameters-for-atom-or-molecule-adsorption-of-2d-layer-materials)
      - [**`Adsorption`**](#adsorption)
      - [**`AdsorptionStyle`**](#adsorptionstyle)
      - [**`NumberOfTypeAtom`**](#numberoftypeatom)
      - [**`BothSide`**](#bothside)
      - [**`@Adatoms`**](#adatoms)
      - [**`@SuperCell`**](#supercell)
      - [**`RangeOfZAxis`**](#rangeofzaxis)
    - [Parameters for design of optical materials with desirable band gap](#parameters-for-design-of-optical-materials-with-desirable-band-gap)
      - [**`BandGapDesign`**](#bandgapdesign)
      - [**`TarBandGap`**](#tarbandgap)
    - [Parameters for special constraints](#parameters-for-special-constraints)
      - [**`SpeSpaceGroup`**](#spespacegroup)
      - [**`FixCell`**](#fixcell)
      - [**`FixAtom`**](#fixatom)
    - [Parameters for X-ray diffraction data assisted structural prediction](#parameters-for-x-ray-diffraction-data-assisted-structural-prediction)
      - [**`LXRD`**](#lxrd)
      - [**`WaveLength`**](#wavelength)
      - [**`RangeOf2Theta`**](#rangeof2theta)
      - [**`StandardPeakPosition`**](#standardpeakposition)
    - [Parameters for Prediction of Transition States in Solids](#parameters-for-prediction-of-transition-states-in-solids)
      - [**`LTranState`**](#ltranstate)
      - [**`NumberOfImages`**](#numberofimages)
  - [Other Inputs](#other-inputs)
  - [CALYPSO Outputs](#calypso-outputs)
  - [Analysis of Results](#analysis-of-results)
    - [Installation of CAK](#installation-of-cak)
    - [CAK Commands](#cak-commands)
    - [CAK Outputs](#cak-outputs)

## CALYPSO Inputs

the main input file named as **`input.dat`**, contains all necessary parameters for the
structure prediction. the file consists of input tags that can be given in any order,
or be omitted while the default values are used. below we offer a quick view of the
syntax of the tags:

1. the general syntax is **`tag labels = value1 value2 value3 ...`** for matrix input,
   it starts with `@tag` and ends with `@end`. values that are not specified in the
   `input.dat` file are assigned as default values. input values should be separated by space.
2. the labels are case-insensitive.
3. all text following the "#" character is taken as comment.
4. logical values can be given as t (or true), or f (or false).

below are brief descriptions on necessary input parameters.

### Common parameters

#### **`systemname`**

```text
systemname = string
```

A description string of the targeted system(max. 40 characters).

Default: calypso

#### **`numberofspecies`**

```text
numberofspecies = integer
```

Number of different atomic (or chemical) species in the system.

For example, it is "2" for MgB{sub}`2`.

There is no default. you must define it.

#### **`nameofatoms`**

```text
nameofatoms = string1 string2 string3 ...
```

Elemental symbols of each atomic species separated by space.

Taking MgB{sub}`2` and MgB{sub}`3` and MgSiO{sub}`3` as examples, one writes
"nameofatoms = Mg B" and "nameofatoms = Mg Si O", respectively.

There is no default. you must define it.

#### **`numberofatoms`**

```text
numberofatoms = integer1 integer2 integer3 ...
```

Number of atoms for each chemical species per formula unit.

Taking MgB{sub}`2` and MgSiO{sub}`3` as examples, one writes
"numberofatoms = 1 2" and "numberofatoms = 1 1 3", respectively.

There is no default. you must define it.

#### **`numberofformula`**

```text
numberofformula = integer1 integer2
```

Defining the number of formula units in the simulation cell.

*integer1* and *integer2* are the minimal and maximal number of formula units used in
the simulation cell, respectively.

If *integer1* equals to *integer2*, then only single choice of formula unit will be adopted.

For example, "NumberOfFormula = 4 4" indicates one single run of 4 formula units in your
simulation, while "NumberOfFormula = 1 4" indicates that four separate structure prediction
runs for 1, 2, 3, and 4 formula units, respectively, will be performed.

Default: 1 4

#### **`Volume`**

```text
Volume = real
```

The volume (in unit of angstrom^3) per formula unit.

If you cannot provide a good estimation on the volume, please use the default value.
The program will automatically generate an estimated volume by using the ionic radii of given atoms.

Default: 0

#### **`@DistanceOfIon`**

```text
@DistanceOfIon
real11   real12   real13   ...
real21   real22   real23   ...
real31   real32   real33   ...
...      ...      ...      ...
@End
```

Minimal interatomic distances (in unit of angstrom) in a format of ***nxn*** matrix.

The rank ***n*** of the matrix is determined by the "NumberOfSpecies".
If we take MgB{sub}`2` as an example with "NumberOfSpecies = 2",
the ***2x2*** matrix is defined as:

```text
@DistanceOfIon
d_Mg_Mg   d_Mg_B
d_B_Mg    d_B_B
@End
```

Here, d_Mg_Mg and d_Mg_B define the minimal Mg-Mg and Mg-B distances, respectively,
while d_B_Mg and d_B_B define the minimal B-Mg and B-B distances, respectively.

Default: 0.7

#### **`Ialgo`**

```text
Ialgo = integer
```

Defines which PSO algorithm to be adopted in the simulation.

:1: global PSO algorithm
:2: local PSO algorithm
:3: ABC algorithm with symmetry

Default: 2

#### **`ICode`**

```text
ICode = integer
```

Defines which code to be used for local structure optimization during the structure prediction.

:1: VASP
:2: SIESTA
:3: GULP
:4: PWSCF
:5: CASTEP
:6: CP2K
:7: Gaussian
:8: DFTB+
:9: LAMMPS

Default: 1

#### **`NumberOfLocalOptim`**

```text
NumberOfLocalOptim = integer
```

Defines how many times a structure should be optimized once it is generated during structure prediction.

The reason why we optimize the structure by several times is because the generated
structures are often far from their local minima. A single fine structure optimization
typically leads to a non-converged calculation. Our tests indicated that three or
four-steps optimizations of one structure are the best solution. During the course of
these multiple optimizations, the optimization degree should increase gradually:
coars->medium->fine. If one uses VASP for structure optimization, three or four input
INCAR files should be therefore provided. The same multiple-optimization procedure
applies also to the use of other optimization codes. More details can be found in
[examples](./_examples.md#crystal-structure-prediction).

Default: 4

#### **`PsoRatio`**

```text
PsoRatio = real
```

Defines what percentage of the structures per generation should be produced by PSO.

The rest of structures will then be randomly generated with symmetry constraints.

Default: 0.6

#### **`PopSize`**

```text
PopSize = integer
```

The population size, i.e., the total number of structures per generation.

Normally, a larger population size is needed for a larger system. Very large population
size should be used for simulations of automatic variation of chemical compositions.

Default: 30

#### **`Kgrid`** (deprecated)

```text
Kgrid = real_1   real_2
```

The precision of the *K*-point sampling for local geometric optimization for VASP,
Quantum-Espresso and DFTB+ codes.

The Brillouin zone sampling uses a grid of spacing
$2\pi\cdot\text{Kgrid}\cdot\mathring{A}^{-1}$.

*real_1* controls the precision of the first two or three local optimizations, and the
*real_2* with denser K-points controls the last optimization. The smaller value gives
finer optimization results. Note that this setting of Kgrid is only applicable to the
uses of VASP, DFTB+ and Quantum-Espresso codes. For uses of other *ab initio* codes
(e.g., CASTEP, CP2K, and Gaussian, etc.), please prepare appropriate Kgrid settings in
their input files.

Default: 0.12 0.06

#### **`Command`**

```text
Command = string
```

The command to submit structure optimization jobs in your computer.

*Default value:* submit.sh.

#### **`MaxStep`**

```text
MaxStep = integer
```

The maximum number of generations to be executed for the entire structure prediction simulation.

Typically, a larger number of generations are needed for a larger system.

Default: 50

#### **`PickUp`**

```text
PickUp = logical
```

If this variable is set as **True**, structure prediction will start from a specified
generation (see PickStep) where a previous structure prediction job was unexpectedly interrupted.

Default: False

#### **`PickStep`**

```text
PickStep = integer
```

At which generation the previously interrupted calculation should be re-started.

There is no default. If PickUp=True, you must define this variable.

#### **`MaxTime`**

```text
MaxTime = integer
```

The running wall-time limit (in unit of seconds) of one single structure optimization.

If the optimization time goes beyond MaxTime, the current structure optimization will be terminated.

Default: 7200

#### **`LMC`**

```text
LMC = logical
```

Determines whether the Metropolis criterion should be applied during the PSO structure evolution.

For cluster structure prediction, it is highly recommended to set this variable as "True".

Default: False

### Parameters for structural prediction of two-dimensional layers

Here are [Detailed Examples](./_examples.md#two-dimensional-structure-prediction)

#### **`2D`**

```text
2D = logical
```

Switcher to perform of 2-dimensional layer structure prediction or not.

Default: False

#### **`LFilm`**

```text
LFilm = logical
```

Switcher to perform of 2-dimensional thin film structure prediction

Default: False

#### **`Thickness`**

```text
Thickness = real
```

The thickness of thin film (in unit of angstrom).

There is no default. You must supply this variable if switch `LFilm` on.

#### **`Area`**

```text
Area = real
```

The area (in unit of angstrom^2) per formula unit.

If you cannot provide a good estimation on the area, please use the default value.
The program will automatically generate an estimated area by using the ionic radii of given atoms.

Default: 0.0

#### **`MultiLayer`**

```text
MultiLayer = integer
```

Defines the number of layers you would like to design.

Default: 1

#### **`DeltaZ`**

```text
DeltaZ = real
```

The distortion value (in unit of angstrom) along the ***c*** direction, i.e.,
perpendicular to the ***a-b*** plane of the layer.

If this parameter is set to be zero, then a strict flat layer will be designed.
Otherwise, a buckled layer is designed.

Default: 0.2

#### **`LayerGap`**

```text
LayerGap = real
```

The gap between two layers, i.e., the interlayer distance (in unit of angstrom).

If this parameter is set as zero, then one single layer will be designed.

Default: 5.0

#### **`VacuumGap`**

```text
VacuumGap = real
```

Defines the separations (in unit of angstrom) between the designed single layer (or
multi-layers) and its nearest-neighboring periodic images.

This value should be large enough to ensure that interactions between the designed layer
and its nearest-neighboring periodic images are negligible.

Default: 10.0

#### **`@LayerType`**

```text
@LayerType
integer11 integer12 integer13 ...
integer21 integer22 integer23 ...
@End
```

Design of multi-layers materials with desirable compositions in a format of ***m×n*** matrix.

The row (***m***) and column (***n***) ranks of the matrix are determined by the
"MultiLayer" and "NumberOfSpecies", respectively. For each row (i.e., each layer),
the matrix column values are defined as the number of atoms for each chemical species as
listed in the "NameOfAtoms".

We take the design of double layers of B-C-N materials as an example. Here we have

```text
MultiLayer      = 2
NumberOfSpecies = 3
NameOfAtoms     = B C N
```

If we purposely design the materials with the first layer having 6 C and 4 N atoms and
the second layer having 3 B, 4 C, and 7 N atoms. The ***2×3*** matrix can be written as follows:

```text
@LayerType
0 6 4
3 4 7
@End
```

There is no default. You must define these numbers.

#### **`LAtom_Dis`**

```text
LAtom_Dis = real
```

The minimal interatomic distance in unit of angstrom.

Default: 1.0

### Parameters for cluster structure prediction

Here are [Detailed Examples](./_examples.md#cluster-structure-prediction)

#### **`Cluster`**

```text
Cluster = logical
```

Switcher to perform a nanocluster structure prediction

Default: False

#### **`Vacancy`**

```text
Vacancy = real_1 real_2 real_3
```

The isolated cluster is placed into an orthorhombic box where the periodic boundary
condition is applied.

This variable defines the separations (in unit of angstrom) between the studied cluster
and its nearest-neighboring periodic images. It should be large enough to ensure that
interactions between the studied cluster and its nearest-neighboring images are negligible.

Default: 10.0 10.0 10.0

For cluster structure prediction, we do not recommend the use of VASP for the structure
optimization for large systems since computationally VASP calculations are very expensive.
**We recommend using SIESTA, CP2K, and Gaussian codes when cluster sizes are larger than 10 atoms.**

### Parameters for rigid Molecules prediction

Here are [Detailed Examples](./_examples.md#molecular-structure-prediction)

#### **`MOL`**

```text
MOL = logical
```

Switcher to perform structure prediction with fixed rigid molecules

This is a useful technique for structure design of molecular systems, especially when
rigid molecules are known constituent of certain structures. Note that a file named as
MOL is needed to define the rigid molecule.

Please refer to [examples](./_examples.md#molecular-structure-prediction) for settings of MOL.

Default: False

#### **`NumberOfTypeMolecule`**

```text
NumberOfTypeMolecule = integer
```

The number of different types of molecules in the simulation cell.

There is no default. You must supply this variable.

#### **`NumberOfMolecule`**

```text
NumberOfMolecule = integer1 integer2 ...
```

The number of molecules for different molecular species.

There is no default. You must supply this variable.

#### **`DistOfMol`**

```text
DistOfMol = real
```

The minimum distance (in unit of angstrom) between two rigid molecules.

Default: 1.5

### Parameters for with variational stoichiometry structure prediction

Here are [Detailed Examples](./_examples.md#variable-stoichiometry-structure-prediction)

#### **`VSC`**

```text
VSC = logical
```

Switcher to perform structure prediction of automatic variation of chemical compositions

This technique is designed to explore all possible stoichiometries for given binary
systems (e.g., A{sub}`x`B{sub}`y` system) at once. However, one has to take
his/her own risk for the use of this technique. The search space has been significantly
enlarged due to the existence of large number of possible stoichiometries. We highly
recommend separate simulations with fixed stoichiometries for confirmation of their results.

Default: False

#### **`MaxNumAtom`**

```text
MaxNumAtom = integer
```

The maximal number of atoms allowed in the simulation cell.

Default: 20

#### **`@CtrlRange`**

```text
@CtrlRange
integer11 integer12
integer21 integer22
@End
```

Defining the compositional range for each type of constituent atom in the binary
A{sub}`x`B{sub}`y` system.

For atom A, *x* varies from *integer*{sub}`11` to *integer*{sub}`12`, while
for atom B, *y* varies from *integer*{sub}`21` to *integer*{sub}`22`.

Default:

```text
@CtrlRange
1  6
1  6
@End
```

### Parameters for surface reconstruction prediction

Here are [Detailed Examples](./_examples.md#surface-structure-prediction)

#### **`LSurface`**

```text
LSurface = logical
```

The flag specifies whether surface reconstruction prediction will be performed.

Default: False

#### **`SurfaceThickness`**

```text
SurfaceThickness = real
```

This variable (in unit of angstrom) specifies the thickness of surface reconstruction,
and it should be set as a value slightly larger than the double distance of two adjacent
atomic layers in bulk materials.

Default: 3.0

#### **`Substrate`** (surface)

```text
Substrate = string
```

This variable allows the users to define their own substrates.

***string*** is the name of the user defined substrate file, which contains the
structure data of the substrate (i.e., lattice parameters and atomic positions).
Here, both POSCAR and cif file formats are supported.

For POSCAR file format, users can use '***Selective dynamics***' tag to define the
relaxable atomic layers, otherwise all the atoms in the substrate will remain un-relaxed
during surface reconstruction calculations.

For cif file format, users need to insert '_selective' tag beneath '_atom_site_fract_z',
and then include 'T' after atomic positions to define the relaxable atomic layers,
while 'F' for the unrelaxable bulk.

Please refer to [examples](./_examples.md#surface-structure-prediction) for more details.

By defining this variable to 'Automatic' or 'Auto', the substrate will be generated
automatically from its bulk structure. See below *controlling parameters* for generation
of *substrate* based on its bulk structure.

Default: SUBSTRATE.surf

#### **`SurfaceAStoms`**

```text
@SurfaceAtoms
string_11  integer_12
string_21  integer_22
...
@End
```

Defining the reconstructed surface region with desirable compositions in a format of ***mx2*** matrix.

The row (***m***) rank of the matrix is determined by "NumberOfSpecies". For each row,
the matrix contains two columns. The first column (***string***) is the elemental symbol
of each chemical species, followed by the number of atoms for such a chemical species
(***integer***).

Please refer to the [examples](./_examples.md#surface-structure-prediction) for more detailed setting of these parameters.

There is no default. You must supply this variable.

#### **`SpaceSaving`**

```text
SpaceSaving = logical
```

If this parameter is set as “**True**”, the output files for structure relaxation will be deleted.

Since the output files for structure relaxation are very large, it is desirable to save
the storage space in hard driver by deleting these redundant files. However, one might
set this parameter as "False" only in case of debugging the results.

Default: True

#### **`ECR`**

```text
ECR = logical
```

If this parameter is set as "True", only those initial structures that meet electron
counting rule are accepted.

For more information on electron counting rule, please refer to the paper by
Lu *et al.*, [Nat. Commun. 5, 3666 (2014)].
Note that ECR only works for semiconductors with large band gaps.

Default: False

### Parameters for automatic generate substrate

The controlling parameters below are used to generate substrate from bulk crystal
structure ONLY when `Substrate = Automatic`(or "Auto" for short).

#### **`CifFilePath`**

```text
CifFilePath = string
```

Specifies the name of crystal structure (in *CIF* format), whose surface structure
prediction is to be performed.

There is no default value.

#### **`MillerIndex`**

```text
MillerIndex = h k l
```

Defines the targeted surface as determined by the Miller indices h, k, and l for doing
surface reconstruction calculations.

For a known bulk structure, once the Miller indices are defined, CALYPSO will
automatically generate the idea surface structure denoted by lattice vectors
(*a*{sub}`1`, *a*{sub}`2`) ready for performing surface reconstruction
simulations.

See below tag of [MatrixNotation](#matrixnotation) for how to define a reconstructed
surface denoted by lattice vectors (*b*{sub}`1`, *b*{sub}`2`). CALYPSO also
supports the use of 4-numbered (***h k i l***) Miller index for hexagonal and
rhombohedral lattice systems. Here, the variable should be defined as
**MillerIndex = *h k i l.***

There is no default value.

#### **`@MatrixNotation`**

```text
@MatrixNotation
integer_11  integer_12
integer_21  integer_22
@End
```

This ***2x2*** matrix is used to define the reconstructed surface. Reconstructed surface
lattice vectors (*b*{sub}`1`, *b*{sub}`2`) can be obtained via multiplying this
matrix by the ideal surface lattice vectors (*a*{sub}`1`, *a*{sub}`2`).

$b1b2 = integer11 integer12 integer21 integer22 a1a2$

For example, for the reconstructed surface 1, the 2×2 matrix is written as *3002*, for the reconstructed surface 2, the 2×2 matrix is written as *111-1* .

There is no default value.

#### **`SlabVacuumThick`**

```text
SlabVacuumThick = real
```

This parameter (in units of angstrom) defines the vacuum region, where the whole slab
is separated from its periodic images.

Default: 10.0

#### **`SlabTopMost`**

```text
SlabTopMost = string
```

Control the topmost layer of the substrate that contains multi-elements.

For example, for a binary system of TiO{sub}`2`, this parameter should be defined as
"Ti" or "O". For single-element system, this parameter can be neglected.

Default: CALYPSO

#### **`SlabNumLayers`**

```text
SlabNumLayers = integer
```

Number of layers in the substrate.

Default : 6

#### **`NumRelaxedLayers`**

```text
NumRelaxedLayers = integer
```

Number of the relaxable layers in the substrate, must be smaller than [`SlabNumLayers`](#slabnumlayers).

Default: 2

#### **`CapBondsWithH`**

```text
CapBondsWithH = logical
```

Switcher to passivate the dangling bonds in the bottom side of the slab via
pseudo-hydrogen atoms.

Default: True

### Parameters for solid-solid interfacial prediction

Here are [Detailed Examples](./_examples.md#prediction-of-transition-states-in-solids)

#### **`LSurface`** (deprecated)

```text
LSurface = logical
```

Switcher to perform surface reconstruction prediction.
This parameter is set as "True" for interfacial structure prediction.

Default: False

#### **`LInterface`**

```text
LInterface = logical
```

Switcher to perform interface structure prediction.

Default: False

#### **`InterfaceTranslation`**

```text
InterfaceTranslation = logical
```

Determines the direction of the rigid-body displacement between two bulk phases.

If this parameter is set as "**a**" ("**b**"), the displacement is performed along the
direction of ***a*** (***b***) vector of simulated cell. "**ab**" represents that the
displacement is performed on lateral plane of interface.

Default: False

#### **`TranslationLimitA`**

```text
TranslationLimitA = real
```

Specifies the maximum rigid-body displacement (in unit of angstrom) along the
direction of *a* vector.

Default: 0

#### **`TranslationLimitB`**

```text
TranslationLimitB = real
```

Specifies the maximum rigid-body displacement (in unit of angstrom) along the
direction of *b* vector.

Default: 0

#### **`Rand_Scheme`**

```text
Rand_Scheme = integer
```

Determines which interface structure generation methods should be adopted.

| Rand_Scheme | Methods                                            |
|:-----------:|:---------------------------------------------------|
|      0      | Random generations of structures                   |
|      1      | Generating structures with 2D symmetry constraints |
|      2      | Generating structures with the bonding constraints |

Default: 1

#### **`Interface_thickness`**

```text
Interface_thickness = real
```

Specifies the thickness of interface region, in unit of angstrom.

#### **`@SURFACE_ATOMS`**

```text
@SURFACE_ATOMS  # |atomic symbol | count|   (CAN CHANGE TO INTERFACE_ATOMS)
string_11  integer_12
string_21  integer_22
@END
```

Defines the atomic compositions at interface region in a format of ***mx2*** matrix.

For each row, the matrix contains two columns. The first column (string) is the
elemental symbol of each chemical species, followed by the number of atoms for
such a chemical species (integer).

Please refer to the [Examples](./_examples.md#surface-structure-prediction) for
more detailed setting of these parameters.

There is no default. You must specify it.

#### **`@COORDINATE_NUMBER`**

```text
@COORDINATE_NUMBER
string_11  string_12  integer_13  real15  real_16
string_21  string_22  integer_23  real25  real_26
string_21  string_32  integer_33  real35  real_36
string_41  string_42  integer_43  real45  real_46
@END
```

This ***mx5*** parametric matrix controls the structure generation under the bonding
constraint, which is only required when the parameter of "RandScheme" is set to 3.

Here each atom is regarded as a central atom, and a nearest-neighbor shell of this atom
is defined. If a generated atom as a neighboring atom locates at this nearest-neighbor
shell, it is regarded as a coordinated atom of the central atom.

For each row, the 1st column (string) represents the elemental symbol of central atom.
The 2nd column (string) represents the elemental symbol of neighboring atom.
The 3rd column represents the maximum coordination number in the generation of interface structures.
The 4th and 5th column specify the minimum and maximum radius of the nearest-neighbor shell
(in unit of angstrom), respectively.

There is no default. You must specify it.

#### **`Substrate`** (interface)

```text
Substrate = string
```

Specifies the filename of the 1st slab model of bulk phase. (CAN CHANGE TO "BulkStructure")

Default: SUBSTRATE.surf

#### **`Substrate2`**

```text
Substrate2 = string
```

Specifies the filename of the 2nd slab model of bulk phase. (CAN CHANGE TO "BulkStructure2")

Default: SUBSTRATE2.surf

#### **`Twin_Interface`**

```text
Twin_Interface = integer
```

Determines which model should be adopted in the prediction of interface structure.

| Twin_Interface | model                                                       |
|:--------------:|:------------------------------------------------------------|
|       0        | Slab model                                                  |
|       1        | An inversion-symmetric model with two equivalent interfaces |
|       2        | A mirror-symmetric model with two equivalent interfaces     |

### Parameters for inverse design of superhard materials

Example is given in next section.

#### **`Hardness`**

```text
Hardness = logical
```

Switcher to perform structure design of superhard materials.

Here, we introduce an inverse-design scheme where "hardness" is used as the fitness
function, instead of "energy" in a standard structure prediction.

After the simulation of CALYPSO inverse-design of superhard materials, one can plot out
hardness values versus energy map to dig out the candidate superhard structures possessing
simultaneously high hardness and low energies.

For more details, please refer to the paper by Zhang *et al.*, J. Chem. Phys. 138, 114101 (2013).

Default: False

### Parameters for atom or molecule adsorption of 2D layer materials

Here are [Detailed Examples](./_examples.md#structure-prediction-of-atom-or-molecule-adsorption-of-2d-layer-material)

#### **`Adsorption`**

```text
Adsorption = logical
```

Switcher to perform 2D materials prediction with atom or molecule adsorption.

Default: False

#### **`AdsorptionStyle`**

```text
AdsorptionStyle = integer
```

Determines which method should be adopted for generation of adsorption structures in the simulation cell.

| AdsorptionStyle | method                                               |
|:---------------:|:-----------------------------------------------------|
|        1        | Random generations of structures                     |
|        2        | Generating structures with fixed positions of adatom |

Default: 1

#### **`NumberOfTypeAtom`**

```text
NumberOfTypeAtom = integer
```

Number of different types of adatoms in the simulation cell.

There is no default. You must specify this variable.

#### **`BothSide`**

```text
BothSide = logical
```

Switcher to adsorb the adatoms on both sides of a 2D layer or on single side.

Default: False

#### **`@Adatoms`**

```text
@Adatoms
string_11  integer_12  (integer_13)
string_21  integer_22  (integer_23)
...
End
```

Defines the adatoms in a format of ***mx2*** for `BothSide = F` or ***mx3*** matrix for `BothSide = T`.

The row (***m***) rank of the matrix is determined by [`NumberOfTypeAtom`](#numberoftypeatom).

When `BothSide = F`, the matrix contains two columns for each line.
The first column (***string***) is the elemental symbol of each adatom,
followed by the number of adatoms in the simulation cell (***integer***).

We take the ***4x4*** supercell of graphene adsorbing eight hydrogen atoms as an example.
The **1x2** matrix is defined as:

```text
@Adatoms
H  8
@End
```

Here, ***H*** is the elemental symbol of adatom, ***8*** indicates that 8 H atoms are
adsorbed for ***4x4*** supercell of graphene.

When `BothSide = T`, the matrix contains three columns for each line.
The first column (***string***) is the elemental symbol of each adatom.
The second column is the number of adatoms on one side.
The third column is the number of adatoms on the other side.

We take the ***4x4*** supercell of graphene adsorbing eight hydrogen atoms as an example.
The ***1x3*** matrix is defined as:

```text
@Adatoms
H  4  4
@End
```

Here, ***H*** is the elemental symbol of adatom, the first **4*** indicates that 4 H
atoms are adsorbed on one side of ***4x4*** supercell of graphene. the second **4**
indicates that 4 H atoms are adsorbed on the other side of ***4x4*** supercell of graphene.

There is no default. You must specify this variable.

#### **`@SuperCell`**

```text
SuperCell
integer_11  integer_12
integer_21  integer_22
End
```

This ***2x2*** matrix is used to define the substrate. Whose lattice vectors can be
obtained via multiplying this matrix by the ideal lattice vectors.

There is no default value.

#### **`RangeOfZAxis`**

```text
RangeOfZAxis = real_1 real_2
```

Defines the range of distances between the 2D layer and adatoms.

*real_1* and *real_2* specify the maximal and minimal distance, respectively.

Default: 1.7 1.2

### Parameters for design of optical materials with desirable band gap

Example is given in next section

#### **`BandGapDesign`**

```text
BandGapDesign = logical
```

Switcher to perform inverse design of optical materials with desirable band gap.

Default: False

#### **`TarBandGap`**

```text
TarBandGap = real
```

Defines the desirable band gap.

### Parameters for special constraints

Here are [Detailed Examples](./_examples.md#crystal-structure-prediction-with-fixed-cell-parameters-or-atomic-positions)

#### **`SpeSpaceGroup`**

```text
SpeSpaceGroup = integer1 integer2
```

Defines the space groups ranging from *integer1* to *integer2* for generation of structures.

If *integer*1 equals to *integer*2, structure generations will be confined to this specified
space group.

This option is particularly useful when one tries to perform a fixed space group calculation.

For a general structure prediction, please use the default value. All 230-space groups will
be allowed for generation of structures.

Default: 1 230

#### **`FixCell`**

```text
FixCell = logical
```

Switcher to perform the structure prediction with fixed cell parameters.

Note that a file named as **cell.dat** is needed to define the fixed cell parameters.

Please refer to [examples](./_examples.md#crystal-structure-prediction-with-fixed-cell-parameters-or-atomic-positions) for settings of **cell.dat**.

Default: False

#### **`FixAtom`**

```text
FixAtom = logical
```

Switcher to perform the structure prediction with fixed atomic positions.

Note that a file named as **cell.dat** is needed to define the fixed atomic positions.

Please refer to [examples](./_examples.md#crystal-structure-prediction-with-fixed-cell-parameters-or-atomic-positions) for settings of **cell.dat**.

Default: False

### Parameters for X-ray diffraction data assisted structural prediction

Example is given in next section

#### **`LXRD`**

```text
LXRD = logical
```

Switcher to perform the X-ray diffraction data assisted structural prediction.

A file named as **XRD.dat** containing the experimental XRD data should be provided.

Default: False

#### **`WaveLength`**

```text
WaveLength = real
```

Defines the wavelength used in the experimental XRD measurement.

There is no default. You must specify this variable.

#### **`RangeOf2Theta`**

```text
RangeOf2Theta = real1 real2
```

Defines the range of $2\theta$ angles from *real1* to *real2* for comparison with the experimental XRD data.

There is no default. You must specify this variable.

#### **`StandardPeakPosition`**

```text
StandardPeakPosition = real1 real2
```

Defines the position of characteristic peak of experimental XRD data in the $2\theta$
range from *real1* to *real2*.

The peak of experimental XRD with maximum intensity is selected as the characteristic peak.

There is no default. You must specify this variable.

### Parameters for Prediction of Transition States in Solids

Example is given in next section

#### **`LTranState`**

```text
LTranState = logical
```

Switcher to perform transition states prediction in solids.

Within this module, only VASP code can be used to perform local structure optimization
at the current stage. Note that a file named as **IF_struct.dat** is needed to provide
structural information for initial and final solid states.

Please refer to [examples](./_examples.md#prediction-of-transition-states-in-solids)
for settings of **IF_struct.dat**.

Default: False

#### **`NumberOfImages`**

```text
NumberOfImages = integer
```

Defines the number of images, which are used to sample the transition state by the
modified nudged elastic band method, for each trial transition path.

For the sake of simplicity, this parameter should be divided evenly by [`PopSize`](#popsize).
For example, if `PopSize = 30`, **NumberOfImages** can be chosen as 3, 5, or 6.

With our modified nudged elastic band method, the number of images for sampling the
transition state can be chosen as small as 3 for eight-atom silicon system.
A slightly larger **NumberOfImages** is expected for a more complex system.

There is no default. You must specify this variable.

## Other Inputs

| Local Optimization | Required Files                               |
|:-------------------|:---------------------------------------------|
| VASP               | `INCAR_*` and pseudopotential file `POTCAR`  |
| SIESTA             | `sinput_*` and pseudopotential files `*.psf` |
| GULP               | `ginput_*`                                   |
| CP2K               | `cp2k.inp_*`                                 |

## CALYPSO Outputs

All the major output files are listed in the folder of "**results**":

|      File Name      | Description                                                                                                            |
|:-------------------:|:-----------------------------------------------------------------------------------------------------------------------|
| `CALYPSO_input.dat` | Backup of the initial input file                                                                                       |
|    `similar.dat`    | Contains the geometrical structure parameters of predicted structures.                                                 |
|     `pso_ini_*`     | Includes the information of the initial structures of the *-th generation.                                             |
|     `pso_opt_*`     | Includes the enthalpy data and structural parameters of the geometrically optimized structures of the *-th generation. |
|     `pso_sor_*`     | The enthalpy data sorted in ascending order of the \*-th generation.                                                   |
|    `struct.dat`     | Necessary information for all predicted structures (the space group number, the volume, the number of atoms, etc.).    |

## Analysis of Results

CALYPSO calculations typically generate a large number of structures.
It is necessary to devise a versatile tool for data analyses.

Here we develop **CALYPSO ANALYSIS KIT (CAK)** allowing automatic structure analysis.

### Installation of CAK

CAK should be installed on a Linux or a Mac OS X system. Structure analysis through CAK
tool needs the use of mathematics lib of **numpy** package in Python. You might need to
link the path of Python to the variable 'PYBIN' in your Makefile. Installation of CAK is simple.

```bash
cd CALYPSO_ANALYSIS_KIT
make
```

Then add `source /path/caly.sh` in .bashrc.

### CAK Commands

Please go to the directory "**results**" and type '**cak.py**'.

```bash
cd path-to-calculation/results
cak.py
```

An output file named as "**Analysis_Output.dat**" will be generated.

By default, "Analysis_Output.dat" contains space-group and enthalpy information of 50
energetically best structures. Note that space groups of structures are determined with
a tolerance of 0.1 $\AA$ by default. Below we show several more advanced analyzing options.

Analysis, and output all structures generated by CALYPSO:

```bash
cak.py -a
```

Analysis, and output the specified number of best structures:

```bash
cak.py -n <integer>
```

Specify values ranging from 0.01 to 1.0 Å will be used as the tolerance for symmetry
analyses of given structures:

```bash
cak.py -t <real ...>
```

The default value is set as 0.1. Multi-tolerance values (separated by space) are allowed.

Output structure files with **CIF** format in directories of '**dir_n**'
(*n* indicates the tolerance value for symmetry analysis):

```bash
cak.py --cif -m <real ...>
```

Output structure files with **VASP POSCAR** format in directories of '**dir_n**'
(*n* indicates the tolerance value for symmetry analysis):

```bash
cak.py --vasp -m <real ...>
```

Output the primitive cells of structures:

```bash
cak.py --pri --vasp/cif
```

Plot the figure of lowest enthalpy as a function of generations:

```bash
cak.py -p
```

Output the structures in the descending order of hardness:

```bash
cak.py --hard
```

### CAK Outputs

(1) **Analysis_Output.dat**

At least three columns are present in this file by default.

The first column is the index of the structures sorted by enthalpies in the ascending
order (the numbers in bracket indicate the structure number out of all structures
generated in the CALYPSO calculation). The second column shows the enthalpy data.
The corresponding space-group numbers as obtained by the desirable tolerance value for
the structures are listed in the third column.

(2) **Convexhull.dat**

This file contains two columns. The first column shows various stoichiometries for a
given binary system. The second column presents the lowest enthalpy for each stoichiometry.

(3) **plot.dat**

This file contains two columns. The first column shows the generation number, while the
second gives the lowest enthalpy for each generation.

(4) **UCell_m_n.vasp**

This file contains the structure data in conventional cell in the POSCAR format of VASP.
*m* and *n* indicate the enthalpy ranking number and the space group number of the structure, respectively.

(5) **PCell_m_n.vasp**

This file contains the structure data in primitive cell in the POSCAR format of VASP.
*m* and *n* indicate the enthalpy ranking number and the space group number of the structure, respectively.

(7) **m_n.cif**

This file contains the structure data in conventional cell in the **.cif** format.
*m* and *n* indicate the enthalpy ranking number and the space group number of the structure, respectively.

(8) **m_n_p.cif**

This file contains the structure data within a primitive unit cell in the **.cif** format.
*m* and *n* indicate the enthalpy ranking number and the space group number of the structure, respectively.
