# CALYPSO Parameters

:::{Note}
**This documentation is up-to-date with v10.1.x!**
:::

Inputs and outputs.

- [CALYPSO Parameters](#calypso-parameters)
  - [CALYPSO Inputs —— toml](#calypso-inputs--toml)
    - [Common parameters in `CALYPSO` block](#common-parameters-in-calypso-block)
      - [**`Systemname`**](#systemname)
      - [**`Seed`**](#seed)
      - [**`IType`**](#itype)
      - [**`ICode`**](#icode)
      - [**`IAlgo`**](#ialgo)
      - [**`IDisp`**](#idisp)
      - [**`IFit`**](#ifit)
      - [**`IRunner`**](#irunner)
      - [**`ISim`**](#isim)
      - [**`BlockMode`**](#blockmode)
      - [**`PickUp`**](#pickup)
    - [Parameters for evolution in `CALYPSO.EVO` block](#parameters-for-evolution-in-calypsoevo-block)
      - [**`NBest`**](#nbest)
      - [**`PsoRatio`**](#psoratio)
      - [**`SabcRatio`**](#sabcratio)
      - [**`PopSize`**](#popsize)
      - [**`MaxStep`**](#maxstep)
      - [**`Temperature`**](#temperature)
    - [Parameters for generator in `CALYPSO.GENERATOR` block](#parameters-for-generator-in-calypsogenerator-block)
      - [basic parameters for each type of crystal structure prediction](#basic-parameters-for-each-type-of-crystal-structure-prediction)
      - [**`FormulaUnit`**](#formulaunit)
      - [**`MaxNumAtom`**](#maxnumatom)
      - [**`VolumeUnit`**](#volumeunit)
      - [**`DistanceOfIon`**](#distanceofion)
      - [**`SpaceGroup`**](#spacegroup)
      - [**`PrototypePath`**](#prototypepath)
      - [**`PrototypeRatio`**](#prototyperatio)
      - [bulk detail parameters](#bulk-detail-parameters)
      - [**`LengthMaxRatio`**](#lengthmaxratio)
      - [**`LengthMinRatio`**](#lengthminratio)
      - [Extra Parameters for layer structure prediction](#extra-parameters-for-layer-structure-prediction)
      - [**`Thicknesses`**](#thicknesses)
      - [**`Area`**](#area)
      - [**`Gaps`**](#gaps)
      - [Extra Parameters for cluster structure prediction](#extra-parameters-for-cluster-structure-prediction)
      - [**`Vacancy`**](#vacancy)
      - [**`cluster_type`**](#cluster_type)
      - [Extra Parameters for molecule structure prediction](#extra-parameters-for-molecule-structure-prediction)
      - [**`MoleculesPath`**](#moleculespath)
      - [Extra Parameters for surface structure prediction](#extra-parameters-for-surface-structure-prediction)
      - [**`AdsorptionStyle`**](#adsorptionstyle)
      - [**`AdsorptionSymmetry`**](#adsorptionsymmetry)
      - [**`SubstratePath`**](#substratepath)
      - [**`Supercell`**](#supercell)
      - [**`RangeOfZAxis`**](#rangeofzaxis)
      - [**`PointPath`**](#pointpath)
      - [**`MoleculesPath`**](#moleculespath-1)
      - [**`FixSiteC`**](#fixsitec)
      - [**`TranslateAtomPosition`**](#translateatomposition)
      - [**`RotateAtomPosition`**](#rotateatomposition)
      - [Extra Parameters for interface structure prediction](#extra-parameters-for-interface-structure-prediction)
      - [**`Substrate1Path`**](#substrate1path)
      - [**`Substrate2Path`**](#substrate2path)
      - [**`InterfaceThickness`**](#interfacethickness)
      - [**`ForbiThickness`**](#forbithickness)
      - [**`InternalThickness`**](#internalthickness)
      - [**`RandScheme`**](#randscheme)
      - [**`TwinInterface`**](#twininterface)
      - [**`InterfaceTranslation`**](#interfacetranslation)
      - [**`TranslationLimitA`**](#translationlimita)
      - [**`TranslationLimitB`**](#translationlimitb)
      - [**`CoordinateNumber`**](#coordinatenumber)
    - [Parameters for optimization in `CALYPSO.OPT` block](#parameters-for-optimization-in-calypsoopt-block)
      - [**`DFTInputPath`**](#dftinputpath)
      - [**`JobFlow`**](#jobflow)
      - [**`PpMap`**](#ppmap)
      - [**`ShareFiles`**](#sharefiles)
      - [**`CustomizableScript`**](#customizablescript)
      - [**`RunCustomizableScriptCMD`**](#runcustomizablescriptcmd)
      - [Extra Parameters MLP calculator](#extra-parameters-mlp-calculator)
      - [**`MLPType`**](#mlptype)
      - [**`MLPKwargs`**](#mlpkwargs)
      - [**`OptAlgo`**](#optalgo)
      - [**`OptStep`**](#optstep)
      - [**`TrajFile`**](#trajfile)
      - [**`Pstress`**](#pstress)
      - [**`Fmax`**](#fmax)
      - [**`MLPKeepSym`**](#mlpkeepsym)
      - [**`UcfMask`**](#ucfmask)
    - [Parameters for dispatcher in `CALYPSO.DISPATCHER` block](#parameters-for-dispatcher-in-calypsodispatcher-block)
      - [**`MachineList`**](#machinelist)
      - [**`TimeInterval`**](#timeinterval)
      - [**`TmpPath`**](#tmppath)
    - [Parameters for descriptor in `CALYPSO.DESCRIPTOR` block](#parameters-for-descriptor-in-calypsodescriptor-block)
      - [**`SimThreshold`**](#simthreshold)
  - [CALYPSO Outputs](#calypso-outputs)
  - [Analysis of Results](#analysis-of-results)
  - [Orchestrator —— CALYPSO task dispatcher](#orchestrator--calypso-task-dispatcher)
    - [common parameters](#common-parameters)
      - [**`name`**](#name)
    - [executor and related parameters](#executor-and-related-parameters)
      - [**`executor`**](#executor)
      - [**`host`**](#host)
      - [**`port`**](#port)
      - [**`username`**](#username)
      - [**`password`**](#password)
      - [**`key_filename`**](#key_filename)
      - [**`remote_root`**](#remote_root)
    - [scheduler and related parameters](#scheduler-and-related-parameters)
      - [**`scheduler`**](#scheduler)
      - [**`queue`**](#queue)
      - [**`numb_node`**](#numb_node)
      - [**`numb_cpu_per_node`**](#numb_cpu_per_node)
      - [**`max_run_time`**](#max_run_time)
      - [**`max_retry`**](#max_retry)
      - [**`machine_capacity`**](#machine_capacity)
      - [**`group_size`**](#group_size)
      - [**`envs`**](#envs)
      - [**`additional_head_settings`**](#additional_head_settings)
      - [**`scheduler_envs`**](#scheduler_envs)


## CALYPSO Inputs —— toml

Main input files, named as **`input.toml`**, which contains all necessary parameters for the
structure prediction. This files consists of input tags that can be given in any order,
or be omitted while the default values are used. below we offer a quick view of the
syntax of the tags:

1. the general syntax is consistence with **`toml`** , one can find more information about this format file here.
2. the labels are case-insensitive.
3. all text following the "#" character is taken as comment.
4. logical values can be given as t (or true), or f (or false).
5. null is allowed.

below are brief descriptions on necessary input parameters.

### Common parameters in `CALYPSO` block

#### **`Systemname`**

```text
SystemName = string
```

A description string of the targeted system(max. 40 characters).

Default: CALYPSO

#### **`Seed`**

```text
seed = integer
```

Positive int number to set random seed for REPRODUCIBILITY, negative to do not set it.

Default: -1

#### **`IType`**

```text
IType = int or string
```

Control the type of structures to be generated.

| IType int | IType string | Module                                      |
|:----------|:-------------|:--------------------------------------------|
| 1         | `CRYSTAL`    | Crystal structure prediction                |
| 2         | `CLUSTER`    | Cluster structure prediction                |
| 3         | `MOLECULAR`  | Molecular crystal structure prediction      |
| 4         | `LAYER`      | Layer (including film) structure prediction |
| 5         | `SURFACE`    | Surface or adsorption structure prediction  |
| 6         | `INTERFACE`  | Interface structure prediction              |

One can use int or string to specify the type of structure prediction. But if string is used,
it must be uppercase.

Default: 1

#### **`ICode`**

```text
ICode = integer or string
```

Defines which code to be used for local structure optimization during the structure prediction.

:1: VASP
:3: GULP
:4: PWSCF
:9: LAMMPS
:11: ARES  # ARES2026
:15: MLP
:16: MlpVasp  # prerelax with MLP and then VASP

Default: 1

#### **`IAlgo`**

```text
IAlgo = integer or string
```

Defines which PSO algorithm to be adopted in the simulation.

:1: global PSO algorithm
:2: local PSO algorithm
:3: ABC algorithm with symmetry

Default: 2

#### **`IDisp`**

```text
 IDisp = integer or string
```
:1: ORCH

The build-in task dispatcher by CALYPSO, other third party libraries will be implemented.

Default: 1

#### **`IFit`**

```text
IFit = integer or string
```

Defining the fitness to determine the evolution structure of the population.

:1: ENTHALPY
:2: HARDNESS
:3: GIBBS

Default: 1

#### **`IRunner`**

```text
IRunner = int
```

Define the style of running calypso.

:1: automatically run
:2: manually run each step (split mode)

Default: 1

#### **`ISim`**

```text
ISim = int or string
```

Define the descriptor of structures, it will be used to determine whether two structures are similar.

:0: NAN
:1: BCM
:2: CCF

BCM is faster than CCF, so we suggest to use BCM for most cases.
if encountering the similarity warning when generating structures, one should decrease the value of `SimThreshold` or turn off the similarity compare by setting `ISim = 0`.

Default: 1

#### **`BlockMode`**

```text
BlockMode = bool
```

Define the evolution way.

:true: evolution will be performed after each generation is done.
:false: evolution will be performed once each structures local optimization is done.

:::{warning}
Now we only support the blockmode = true.
:::

Default: true

#### **`PickUp`**

```text
PickUp = bool
```

Whether to pick up a calculation. Now CALYPSO support pickup in any stage, just turn this on.

Another interesting thing is that, `pickup` can not only pick up an aborted CALYPSO task, but also can "pick up" a finished CALYPSO task with a new changed `MaxStep`, which can allow you to keep the evolution information you don't want to drop and continue to run.

:true: pickup the old calculation.
:false: restart a new calculation.


Default: false

### Parameters for evolution in `CALYPSO.EVO` block

#### **`NBest`**

```text
NBest = int
```

Defines how many parts the PES will be separated and PSO will move to the closest one to generate the next structure.

In global PSO, `NBest` is equal to 1.

Default: 4

#### **`PsoRatio`**

```text
PsoRatio = float
```

Defines what percentage of the structures per generation should be produced by PSO.

The rest of structures will then be randomly generated with symmetry constraints.

Default: 0.6

#### **`SabcRatio`**

```text
Sabcratio = list of float
```

Define the percentage of scouts, employees, and onlookers, in which:

- scouts choose a different space groups
- onlookers choose a different combination of the wyckoff positions
- employees choose different atomic coordinates of the wyckoff positions

Please make sure the sum of three float number should equal to 1.0.

Default: [0.3, 0.2, 0.5]

#### **`PopSize`**

```text
PopSize = integer
```

The population size, i.e., the total number of structures per generation.

Normally, a larger population size is needed for a larger system. Very large population
size should be used for simulations of automatic variation of chemical compositions.

Default: 10

#### **`MaxStep`**

```text
MaxStep = integer
```

The maximum number of generations to be executed for the entire structure prediction simulation.

Typically, a larger number of generations are needed for a larger system.

Default: 2

#### **`Temperature`**

```text
Temperature = 300
```

The temperature value when considering Gibbs free energy (`IFit = 3`). The algorithm can be found [here](https://doi.org/10.1038/s41467-018-06682-4).

The unit is Kelvin.

Default: 300


### Parameters for generator in `CALYPSO.GENERATOR` block

#### basic parameters for each type of crystal structure prediction

#### **`FormulaUnit`**

```text
FormulaUnit = list of string
```

For example, if we set `FormulaUnit = ['(LiH4)1-2(NH3)3-4']`, it means that we want to predict LiH4-NH3 structure, within the range of 1 to 2, and 3 to 4, respectively.

In Crystal Structure prediction, the length of FormulaUnit is 1. But for layer structure prediction, the length of FormulaUnit is equal to the number of layers.

There is no default. you must define it.

#### **`MaxNumAtom`**

```text
MaxNumAtom = integer
```

The maximal number of atoms allowed in the simulation cell.

Default: 100

#### **`VolumeUnit`**

```text
VolumeUnit = dict of string and int
```

Custom volume of each unit. Set 0 or leave empty means calculated by covalent radii (only available for single element), which is 1.3*(4/3)πr^3.

For example, `VolumeUnit = {Li=10, H=10, N=10}` mean volume of atom Li, H, and N are equal to 10.

:::{warning}
The key of dict in toml is no need to add quote for string.
:::

Default: {} <=> (1.3*(4/3)π(covalent radii)^3)

#### **`DistanceOfIon`**

```text
DistanceOfIon = list or dict
```

Minimal inter atomic distances (in unit of angstrom) in a format of ***(n+1)x(n+1)*** matrix or in a format of dict.

for example, `DistanceOfIon = [["X", "Li", "H", "N"], ["Li",  1.0, 1.0,  1.0], ["H",  1.0, 1.0,  1.0], ["N", 1.0, 1.0,  1.0],]]` is equal to `DistanceOfIon = {Li: 0.5, N: 0.5, H: 0.5}`.

Default: {} <=> covalent radii

#### **`SpaceGroup`**

```text
SpaceGroup = list of int and string
```

Defines the range of space groups to be considered.

The rule of specific space group is :

1. one single integer means a single space group number
2. "int1-int2" means space group number ranging from int1 to int2
3. "int1:int2:int3" means space group number ranging from int1 to int2 with step size int3. [int1, int2)

:::{note}
  There are some differences when choosing different structure generating method.

  - crystal (`IType = 1`): `SpaceGroup` ranging from 1 to 230
  - cluster (`IType = 2`): `SpaceGroup` ranging from 1 to 31
  - molecular crystal (`IType = 3`): `SpaceGroup` ranging from 1 to 230
  - layer (`IType = 4`): `SpaceGroup` ranging from 1 to 17 for **multi-layer**, ranging from 1-230 for **single layer**.
:::

Default: [1, "2-210", "211:231:1"]

#### **`PrototypePath`**
```text
PrototypePath = list of string
```

The provided path which containing the prototype structures (end with .vasp).

For example, `PrototypePath = ["path/to/vasp/poscar"]`. In the very beginning, the code will parser the provided path and save them into `~/.cache/calypso/prototype` naming as `{number of atoms}.csv`. And all the structures with same number of atoms will save here.

There is no default value. You must supply this variable if you want to use it.

#### **`PrototypeRatio`**
```text
PrototypeRatio = float
```

The ratio of prototype-base-generated structures in random-generated structures.

Default: 0.0

#### bulk detail parameters

#### **`LengthMaxRatio`**
```text
LengthMaxRatio = float
```

The max ratio of the length of a, b, c.

Default: 5.0

#### **`LengthMinRatio`**
```text
LengthMinRatio = float
```

The min ratio of the length of a, b, c.

Default: 1.0

#### Extra Parameters for layer structure prediction

#### **`Thicknesses`**

```text
Thicknesses = list of float
```

The thicknesses of thin films (in unit of angstrom).

The length of `Thicknesses` is equal to the length of `FormulaUnit`

There is no default value. You must supply this variable if `IType = 4`.

#### **`Area`**

```text
Area = float
```

The area (in unit of angstrom^2) per formula unit.

If you cannot provide a good estimation on the area, please use the default value.
The program will automatically generate an estimated area by using the ionic radii of given atoms.

There is no default value. You must supply this variable if `IType = 4`.

#### **`Gaps`**

```text
Gaps = list of float
```

The gap between two layers, i.e., the interlayer distance (in unit of angstrom). The length of Gaps should be equal to the length of `FormulaUnit`. And the last value of `Gaps` is always the vacancy value.

For example, the `FormulaUnit = ["MoS2", "CrI3"]`, the gap can be set as `Gaps = [2, 10]`, which means the distance between two "MoS2" layer is 2 angstrom, and the vacancy is 10 angstrom.

There is no default value. You must supply this variable if `IType = 4`.

#### Extra Parameters for cluster structure prediction

#### **`Vacancy`**

```text
Vacancy = list of float
```

The isolated cluster is placed into an orthorhombic box where the periodic boundary
condition is applied.

This variable defines the separations (in unit of angstrom) between the studied cluster
and its nearest-neighboring periodic images. It should be large enough to ensure that
interactions between the studied cluster and its nearest-neighboring images are negligible.

For cluster structure prediction, we do not recommend the use of VASP for the structure
optimization for large systems since computationally VASP calculations are very expensive.

Default: [10.0 10.0 10.0]

#### **`cluster_type`**

```text
ClusterType = string 
```

:normal: the core-shell type cluster
:cage: the cage cluster
:plane: the plane cluster

Default: normal

#### Extra Parameters for molecule structure prediction

#### **`MoleculesPath`**

```text
MoleculesPath = dict of string
```

The path of molecules. And the molecular name in `FormulaUnit` will be parsed by this key.

For example, if we have `FormulaUnit = ["{Water}4"]`, then `MoleculesPath = {'Water'='./H2O.xyz'}`, so that Water will be parsed as H2O.

Default: {}


#### Extra Parameters for surface structure prediction

#### **`AdsorptionStyle`**

```text
AdsorptionStyle = integer
```

Determines which method should be adopted for generation of adsorption structures in the simulation cell.

| AdsorptionStyle int | AdsorptionStyle string | Method                                                        |
|:--------------------|:-----------------------|:--------------------------------------------------------------|
| 1                   | `UAS`                  | Unfixed adsorption sites.<br>Random generations of structures.|
| 2                   | `FAS`                  | Fixed adsorption sites.<br>Generating structures with fixed positions of adatom.              

Default: 1

#### **`AdsorptionSymmetry`**

```text
AdsorptionSymmetry = bool
```

A Boolean parameter governs the activation of the symmetry search in structure generation.

If True, the 2D space group is randomly chosen from the crystal system associated with the lattice of the provided substrate.

Default: True

#### **`SubstratePath`**

```text
SubstratePath = string
```

The file path for the substrate file.

The `selective dynamics` feature is also supported, allowing for control the respective coordinates of substrate atoms will be allowed to change during the ionic relaxation.

:::{warning}
Only the VASP format is accepted, with `.vasp` suffix.
:::

There is no default value. You must supply substrate file and its path if you want to use surface module.

#### **`Supercell`**

```text
Supercell = list of list of integer
```

This 2x2 matrix is used to define the substrate. Whose lattice vectors can be obtained via multiplying this matrix by the ideal lattice vectors.

Default = [[1, 0], [0, 1]]

#### **`RangeOfZAxis`**

```text
RangeOfZAxis = list of float
```

Defines the range of distances between the 2D layer and adatoms. Two integers of this parameters specify the maximal and minimal distance, respectively.

Default: [1.7, 1.2]

#### **`PointPath`**

```text
PointPath = string
```

Path for the fixed adsorption sites file.

Site coordinates are based on the substrate's lattice and `supercell` parameter.

The Z-coordinate of points are excluded; only the XY coordinates are recorded.

There is no default value. You must supply point file and path if you are using `AdsorptionStyle = 2`.

Two file formats are supported:

- VASP-like format

- JSON format

Both allow for coordinates to be specified in either `Direct` or `Cartesian` format.

:::{warning}
The lattice parameters must be identical to those of the substrate.
:::

**VASP-like format (POINT.vasp)**

```text
points
1.0
        2.4593999386         0.0000000000         0.0000000000
       -1.2296999693         2.1299028249         0.0000000000
        0.0000000000         0.0000000000        15.0000000000
  H O OH
  1 1 1
Direct
     0.666666687         0.333333343         0.500000000
     0.333333313         0.666666627         0.500000000
     0.666666687         0.333333343         0.500000000
```

- Scaling factor support 1.0 only.

- Species names support species of atoms or functional group or molecule.

- The selective dynamics format of POSCAR is not supported.

**JSON format (POINT.json)**

```js
{
    "coordinate system": "Direct",
        "point":
        {
            "H": [[0.666666687, 0.333333343, 0.500000000]],
            "O": [[0.333333313, 0.666666627, 0.500000000]],
            "OH": [[0.666666687, 0.333333343, 0.500000000]]
        }
}
```

- Do not provided substrate lattice in this format.

#### **`MoleculesPath`**

```text
MoleculesPath = dict of string
```

The path of molecules. And the molecular name in FormulaUnit will be parsed by this key.

For example, if we have `FormulaUnit = ["(H)2{OH}2{H2O}4"]`, then `MoleculesPath = {'OH' = './OH.xyz', 'H2O' = './H2O.xyz'}`, so that H2O molecular file will be parsed as H2O.xyz and OH functional group will be parsed as OH.xyz.

:::{warning}
Only the XYZ format is accepted, with `.xyz` suffix.
:::

There is no default value. You must supply moleculer files and paths when the system contains molecules or functional groups within the `FormulateUnit`.

#### **`FixSiteC`**

```text
FixSiteC = bool
```

| FixSitesC | Method |
|:----------|:-----------------------------------------------------------------------------------|
| `True`    | The Z-coordinate of the adatom is fixed to the mean value of `RangeOfZAxis`.       |
| `False`   |  The Z-coordinate of the adatom is randomly sampled from the `RangeOfZAxis` range. |          

Default: False

#### **`TranslateAtomPosition`**

Apply a random translation on the symmetric sites to generate the adsorption sites or not.

Take no effect if `AdsorptionSymmetry=False`.

```text
TranslateAtomPosition = bool
```

Default: True

#### **`RotateAtomPosition`**

Whether to rotate the adatom sites about the Z-axis by a random angle and the molecule/functional group about its first atom by a random angle.

Take no effect if `AdsorptionSymmetry=False`.

```text
RotateAtomPosition = bool
```

Default: True

#### Extra Parameters for interface structure prediction

#### **`Substrate1Path`**

```text
Substrate1Path = string
```

The file path for the first substrate slab file.

The `selective dynamics` feature is supported: atoms with fixed coordinates in the POSCAR
will be treated as frozen during the interface search.

:::{warning}
Only the VASP format is accepted, with `.vasp` suffix.
:::

There is no default value. You must supply this parameter for interface prediction.

#### **`Substrate2Path`**

```text
Substrate2Path = string
```

The file path for the second substrate slab file.

Same format requirements as `Substrate1Path`.

There is no default value. You must supply this parameter for interface prediction.

#### **`InterfaceThickness`**

```text
InterfaceThickness = float
InterfaceThickness = [float, float]
```

Specifies the thickness of the interface region (in unit of angstrom) in which the
interface atoms are placed.

When a single value is provided, it is used as both the minimum and maximum thickness.
When a two-element list is provided, it specifies `[min_thickness, max_thickness]`,
and the actual thickness is optimized as a PSO variable.

Default: [3.0, 3.0]

#### **`ForbiThickness`**

```text
ForbiThickness = float
```

Specifies the stand-off distance (in unit of angstrom) applied symmetrically on both
sides of the interface region: between the topmost atomic layer of the lower substrate
and the bottom boundary of the generation region, and equivalently between the bottom
atomic layer of the upper substrate and the top boundary of the generation region.
Interface atoms are forbidden from being placed within this margin.

Default: 0.0

#### **`InternalThickness`**

```text
InternalThickness = float
```

Specifies the depth (in unit of angstrom) by which the generation region extends into
each substrate, applied symmetrically on both sides: the bottom of the generation region
penetrates downward into the lower substrate by this amount, and the top of the generation
region penetrates upward into the upper substrate by the same amount. This parameter acts
in the opposite sense to `ForbiThickness`: rather than excluding atoms near the substrate
surface, it allows atoms to be placed partially within the substrate layers.

Default: 0.0

#### **`RandScheme`**

```text
RandScheme = integer
```

Determines which structure generation method should be used for the interface atoms.

| RandScheme | Method                                              |
|:----------:|:----------------------------------------------------|
|     0      | Random generation of structures                     |
|     1      | Structure generation with 2D symmetry constraints   |
|     2      | Structure generation with bonding constraints (requires `CoordinateNumber`) |

Default: 1

#### **`TwinInterface`**

```text
TwinInterface = integer
```

Selects the interface structural model.

| TwinInterface | Model                                                        |
|:-------------:|:-------------------------------------------------------------|
|       0       | Single-slab model                                            |
|       1       | Inversion-symmetric model with two equivalent interfaces     |
|       2       | Mirror-symmetric model with two equivalent interfaces        |

Default: 0

#### **`InterfaceTranslation`**

```text
InterfaceTranslation = string
```

Enables rigid-body translation between the two bulk phases and specifies the
translation direction(s).

| Value  | Meaning                                          |
|:------:|:-------------------------------------------------|
| `""`   | No rigid-body translation                        |
| `"a"`  | Translation along the *a* lattice vector         |
| `"b"`  | Translation along the *b* lattice vector         |
| `"ab"` | Translation on the lateral (*a*–*b*) plane       |

Default: `""` (disabled)

#### **`TranslationLimitA`**

```text
TranslationLimitA = [float, float]
```

Specifies the range `[min, max]` (in unit of angstrom) of the rigid-body translation
along the *a* direction. Only takes effect when `InterfaceTranslation` contains `"a"` and `"ab"`.

Default: [0.0, 1.5]

#### **`TranslationLimitB`**

```text
TranslationLimitB = [float, float]
```

Specifies the range `[min, max]` (in unit of angstrom) of the rigid-body translation
along the *b* direction. Only takes effect when `InterfaceTranslation` contains `"b"` and `"ab"`.

Default: [0.0, 1.5]

#### **`CoordinateNumber`**

```text
CoordinateNumber = list of list
```

Defines bonding constraints for interface structure generation. Only required when
`RandScheme = 2`.

Each entry is a 6-element list:
`[central element, neighbor element, maximum growth coordination number, maximum bonding coordination number, minimum distance, maximum distance]`

| Field                       | Type    | Description                                                        |
|:----------------------------|:--------|:-------------------------------------------------------------------|
| Central element             | string  | Element symbol of the central atom                                 |
| Neighbor element            | string  | Element symbol of the neighboring atom                             |
| Maximum growth coordination number  | integer | Upper limit on the coordination number used during structure growth; 0 means no such neighboring atoms are considered  |
| Maximum bonding coordination number | integer | Upper limit on the coordination number used for bond formation; 0 means no such neighboring atoms are considered       |
| Minimum distance            | float   | Inner radius of the nearest-neighbor shell (angstrom)              |
| Maximum distance            | float   | Outer radius of the nearest-neighbor shell (angstrom)              |

For example:

```toml
CoordinateNumber = [['Ti', 'Ti', 0, 0, 2.5, 2.5],
                    ['O',  'O',  0, 0, 1.8, 2.3],
                    ['Ti', 'O',  6, 0, 1.8, 2.5],
                    ['O',  'Ti', 3, 0, 1.8, 2.5]]
```

There is no default value. You must supply this parameter when `RandScheme = 2`.

### Parameters for optimization in `CALYPSO.OPT` block

#### **`DFTInputPath`**

```text
DFTInputPath = string
```

The Path that contains the input files for the DFT code.

If one using MLP with model file, it also should be saved in here.

Default: "./"

#### **`JobFlow`**

```text
JobFlow = list of string
```

Define the sequence of calculation to be conducted. The number of input files should also be equal to the length of JobFlow.

default: ["opt", "opt", "opt"]

#### **`PpMap`**

```text
PpMap = list of string
```

Define the path of pseudopotential files and their corresponding element mapping. Only work for VASP for now.

For example, `PpMap = {Li: "POTCAR_Li", Mg: "mmm"}`

There is no default value. One must set it manually.

#### **`ShareFiles`**

```text
ShareFiles = list of string
```

the absolute path of model of other files need to be copied into the real calculation directory. 

For example , if one using VASP as calculator and considering vdw functional which definitely needs the vdw_kernel.bindat file, one can put the path of kernel file in `ShareFiles` to make sure the kernel will be used in each structure optimization.

Another example is that one can put the path of model here if using mlp as calculator.

Default: []

#### **`CustomizableScript`**

```text
CustomizableScript: str
```

`CustomizableScript` value must be an absolute path that point to a script.

While you can use this code to run your own, the output must conform to the format
and file names of the `ICode` you select. For instance, an `ICode` of 1 (VASP) requires
VASP-compatible (name and format) output. Documentation with more details will be provided soon.

Default: None

#### **`RunCustomizableScriptCMD`**

```text
RunCustomizableScriptCMD: str
```

Default: None

You only provide this when your `CustomizableScript` value is not `None`.
**CAUTION**: `RunCustomizableScriptCMD` value must use the script provided by `CustomizableScript`, more specifically,
`RunCustomizableScriptCMD` value must include the customizable script name, not the full path in `CustomizableScript`.
For instance, if `CustomizableScript` value is `/path/to/customizable_run_flow.sh`, `RunCustomizableScriptCMD` value can
be `bash customizable_run_flow.sh $CALYPSO_MLP_CMD`. It can't be `bash /path/to/customizable_run_flow.sh $CALYPSO_MLP_CMD`,
because during calculation, CALYPSO may move the given customizable script to another place or even a different machine,
its path is not stable, but the script name is stable.

#### Extra Parameters MLP calculator

#### **`MLPType`**

```text
MLPType = "dp"
```

:dp: deep potential
:deepmd: deep potential
:dpa: deep potential
:dpa2: deep potential
:m3gnet:
:chgnet:
:mace_mp:
:mace_off:
:gulp:
:emt:
:lj:
:morse:

Choose which type of mlp will be used.

There is no default value. One must set it manually.

#### **`MLPKwargs`**

```text
MLPKwargs = {"model"="M3GNet-MP-2021.2.8-PES"}
```

The parameters of mlp initialization.
chgnet: {"model"="0.3.0", "check_cuda_mem"=true, "on_isolated_atoms"="warn"}
dp: {"model": "path/to/model"}

Default: {}

#### **`OptAlgo`**

```text
OptAlgo = string
```

The algorithm of optimization.

:LBFGS:
:FIRE:
:BFGS:

Default: "LBFGS"

#### **`OptStep`**

```text
OptStep = int
```

The number of step of optimization.

Default: 1000

#### **`TrajFile`**

```text
TrajFile = string
```

The filename of optimization trajectory.

Default: traj.traj

#### **`Pstress`**

```text
Pstress = float
```

The pressure of when conducting mlp structure optimization.
in GPa

Default: 0.0

#### **`Fmax`**

```text
Fmax = float
```

The coverage condition. The optimization will stop when all the force of each atom is smaller than Fmax.

Default: 0.1

#### **`MLPKeepSym`**

```text
MKPKeepSym = bool
```

Whether to keep symmetry when using mlp to conducting optimization.

Default: false

:::{warning}
Take no effect if any atoms or lattice is fixed. e.g. `selective dynamics` [in substratepath](#substratepath) or [UcfMask](#ucfmask).
:::


#### **`UcfMask`**

None or a list of booleans, indicating which of the six independent components of the strain are relaxed.

See [ase.filters.UnitCellFilter](https://ase-lib.org/ase/filters.html#ase.filters.UnitCellFilter) `mask` parameter.

```text
UcfMask = list of bool
```

Default: None

:::{warning}
Ensure `ase` library version 3.26 for machine learning potential compatibility; other versions may cause optimization errors.
:::


### Parameters for dispatcher in `CALYPSO.DISPATCHER` block

#### **`MachineList`**

```text
MachineList = list of string
```

These parameters define the available computational resources. For example, you are using the cluster with two queues that can be used, then can choose to set up at most two `machine.json` to perform structure optimization,  in very parallel way.

`MachineList = ["./machine-1.json", "/machine-2.json"]`

There is no default value for `MachineList`. One must set it manually.

#### **`TimeInterval`**

```text
TimeInterval = int
```

How often the dispatcher will check the status of the jobs.

Default: 10

#### **`TmpPath`**

```text
TmpPath = string
```

The path to save the log file of Orchestrator (dispatcher).

Default: "BackStage"

### Parameters for descriptor in `CALYPSO.DESCRIPTOR` block

#### **`SimThreshold`**

```text
SimThreshold = float
```

Define the threshold of similarity between two structures. If the distance of two structures is less than the threshold, they are considered as the same structure.

Default: 0.01

## CALYPSO Outputs

All the major output files are listed in the folder of "**results**":

|       File Name       | Description                                                                                  |
|:---------------------:|:---------------------------------------------------------------------------------------------|
| `Analysis_Output.csv` | The results file of the predicted structures.                                                |
|     `database.db`     | Contains the intermediate parameters of CALYPSO.                                             |
|   `descriptor.pkl`    | Includes the information of the descriptor of each structures.                               |
|      `ini.json`       | Includes the initial structures information.                                                 |
|      `opt.json`       | Includes the optimized structures information and the corresponding energy, force and so on. |
|      `opt_task`       | All structures optimization are saved in this folder.                                        |

## Analysis of Results

CALYPSO calculations often generate a large number of structures. Therefore, it is essential to have a versatile tool for efficient data analysis.

Introducing the **CALYPSO ANALYSIS KIT (CAK)**, a tool designed for automatic structure analysis.

Once CALYPSO is installed, the `pycak` tool will be available for use from the command line.


```bash
> cd path-to-calculation/results
> pycak --help
usage: pycak [-h] [-d DIR] [--refene REFENE_FILE] [-m TOL [TOL ...]] [-a] [--reduce-sim] [--energy-threshold ENERGY_THRESHOLD] [--split-by-formula | --no-split-by-formula]
             [--out-root OUT_ROOT] [--pcell] [--ucell] [--vasp] [--synth] [--synth-model-dir SYNTHESISABILITY_MODEL_DIR] [--spap] [--spap-symprec SPAP_SYMPREC]
             [--spap-threshold SPAP_THRESHOLD] [--spap-r-cutoff SPAP_R_CUTOFF] [--spap-ilat {0,1,2}] [--spap-no-compare] [--spap-no-db] [--spap-cif] [--spap-poscar] [--skip-analyze]

CALYPSO Analysis Toolkits
-------------------------
Use `analyze` (default) to analyze CALYPSO results, or/and `spap` to run SPAP symmetry/similarity.

Examples:
    - pycak -m 0.1 0.01 -a --ucell --vasp
    - pycak -m 0.1 --ucell --vasp --split-by-formula --out-root by-formula
    - pycak -m 0.1 --ucell --vasp --refene ../ref_ene.txt
    - pycak --spap
    - pycak -m 0.01 --reduce-sim -a --spap --spap-poscar
    - pycak -m 0.1 0.01 0.3 --reduce-sim --spap --spap-poscar
    - pycak -m 0.1 0.01 0.3 --reduce-sim --vasp --split-by-formula --spap --spap-poscar --skip-analyze

Optional: analysis synthesisability
    This requires pytorch etc. being installed. See detailed instruction in
    <https://iccms-calypso.github.io/CALYPSO-Python/posts/_installation.html#installation>

Then download and decompress the model archive into the default cache directory:
    MODEL_ARCHIVE_URL=https://github.com/ICCMS-CALYPSO/open-resources/releases/download/CALYPSO-v10.0.0-alpha.1/synth-ckpt-v1.0.0.tar.gz
    PROJECT_CACHEDIR=${HOME}/.cache/calypso
    curl -L $MODEL_ARCHIVE_URL | tar -C $PROJECT_CACHEDIR -zxf -

options:
  -h, --help            show this help message and exit
  -d DIR, --results-dir DIR
                        path to the results directory (default: .)
  --refene REFENE_FILE  reference energy (enthalpy) for energy above hull (default: ../ref_ene.txt)
  -m TOL [TOL ...], --multi-tolerance TOL [TOL ...]
                        tolerances for analysising symmetry;
                        multiple values are acceptable; some useful
                        values: 1.0, 0.5, 0.1, 0.01, 0.001; (default: 0.1)
  -a, --all             analysis all structures; by default only the
                        50 lowest energy structures are considered
  --reduce-sim          reduce similarity using energy threshold
  --energy-threshold ENERGY_THRESHOLD
                        energy threshold (eV) of reducing similarity; below which
                        two structures are considered duplicates (default: 1e-3)
  --split-by-formula, --no-split-by-formula
                        also emit per-formula outputs in <out-root>/<formula>/ (default: False)
  --out-root OUT_ROOT   root directory to hold per-formula outputs (default: by_formula)

output format:
  --pcell               write primcell cell
  --ucell               write unit cell; If neither pcell nor ucell are specified,
                        ucell is switched on
  --vasp                write structure in vasp format

analysis synthesisability:
  --synth               whether to analyse synthesisability with machine learning model
  --synth-model-dir SYNTHESISABILITY_MODEL_DIR
                        directory to model parameters for synthesisability model
                        (default: /home/wangzy/.cache/calypso/synth-ckpt-v1.0.0)

SPAP (post-analysis):
  --spap                after analysis, run SPAP under each caly_structs.<tol>/spap_run/
  --spap-symprec SPAP_SYMPREC
                        this precision is used to analyze symmetry of atomic structures (default: 0.1)
  --spap-threshold SPAP_THRESHOLD
                        threshold for similar/dissimilar boundary (default: None)
  --spap-r-cutoff SPAP_R_CUTOFF
                        inter-atomic distances within this cut off radius will contribute to CCF (default: None)
  --spap-ilat {0,1,2}   this parameter controls which method will be used to deal with lattice for comparing structural similarity
                        0 do not change lattice;
                        1 equal particle number density;
                        2 try equal particle number density and equal lattice
  --spap-no-compare     not to compare similarity of structures  (default: False)
  --spap-no-db          not to write structures into ase (https://wiki.fysik.dtu.dk/ase/) database file (default: False)
  --spap-cif            write structures into cif files (default: False)
  --spap-poscar         write structures into files in VASP format (default: False)
  --skip-analyze        only run SPAP (assumes caly_structs.<tol>/ already exist) (default: False)

> pycak
```


An output file named "**Analysis_Output.dat**" will be generated. And the `ref_ene.txt` file should be considered cause the calypso will calculating the energy/enthalpy above the hull.

The `ref_ene.txt` file should have the following format:
```text
> cat ../ref_ene.txt 
formula enthalpy_per_atom label
La 13.06301 element_La
H  -0.55342 element_H
```

The results generated by `pycak` will appear as follows:

```text
> head -n 3 Analysis_Output.csv 
 idx   caly_name      formula       enth_per_atom   enth_above_hull       fitness       volume_per_atom   density   min_dis  spg(0.1)  spgnum(0.1) natom(0.1)
  0    caly_4403        H2La            3.322            0.000             3.322             6.206        12.568     1.622   P6/mmm        191         3     
  1    caly_4463        H4La            1.569            0.000             1.569             4.529        10.481     1.488   I4/mmm        139         10  
  2    caly_6283       H10La            0.330            0.000             0.330             2.992         7.516     1.131   Fm-3m         225         44    
  3    caly_2934        H4La            1.571            0.002             1.571             4.506        10.535     1.455   I4/mmm        139         10 
```
However, when the reference energy is set to 0, the `enth_per_atom` and `enth_above_hull` columns in **Analysis_Output.csv** will have identical values.

Duplicated structures can be eliminated using the `--reduce-sim` option. Structures can be saved in VASP format using the `--vasp` option and unit cells can be written with `--ucell`. Structures with different compositions will be separated into different directories by using the `--split-by-formula` option. Additionally, the structure prototype can be analyzed using the `--spap` option. After running this command, the structure prototype will be saved in different subdirectories. When using `--spap`, the options `--vasp` and `--split-by-formula` will also be activated.

The directory structure will look like this:

```bash
> pycak -m 0.1 0.01 0.3 --reduce-sim --vasp --split-by-formula --spap --spap-poscar
> pwd
/calypso/results

> ls
Analysis_Output.csv  by_formula/  caly_structs.0.01/  caly_structs.0.1/  caly_structs.0.3/  ini.json  opt.json

> ls by_formula 
H10La/  H2La/  H4La/  H6La/

> ls by_formula/H10La/
Analysis_Output.csv  caly_structs.0.01/  caly_structs.0.1/  caly_structs.0.3/

```

You can also skip the normal analysis process and directly analyze the structure prototype:
```bash
> pycak -m 0.1 0.01 0.3 --reduce-sim --vasp --split-by-formula --spap --spap-poscar --skip-analyze
```

For more information about the SPAP package, please refer to the [official documentation here](https://github.com/chuanxun/StructurePrototypeAnalysisPackage/).

## Orchestrator —— CALYPSO task dispatcher

To make CALYPSO more flexible, we develop a task dispatcher to help users to submit CALYPSO jobs in more ways.

Orchestrator mainly depends on an input file: `machine.json`, which defines how to reach the computational resources, and how to run calculation in these resources.

Here is the parameters of `machine.json`:

### common parameters

#### **`name`**

```text
name = string
```

Name of this computational resources, useful when you have multi-computational resources.

Default: "Machine"

### executor and related parameters

#### **`executor`**

```js
executor = "local" // or "ssh"
```

Where to conduct the calculation, we have `local` and `ssh` parameters.

When using `local`, the calculation will be performed in local machine.

When using `ssh`, the calculation will be performed in remote machine according to the provided `host`, `port`, `username` and `password` or `key_filename`.

After deciding the executor, some basic parameters are need to be set:

1. ssh related if chosen:

   - [host](#host)
   - [port](#port)
   - [username](#username)
   - [password](#password)
   - [key_filename](#key_filename)

2. a list for setting environment, e.g. `source` or `export` etc.:
   - [envs](#envs)


3. where to go:
   - [remote_root](#remote_root)

Default: "local"

#### **`host`**

```text
host = string
```

The host name of your machine, only work when `executor` is `ssh`.

for example:

`host = "127.0.0.1"`

Default: null

#### **`port`**

```text
port = string
```

The port of your machine, only work when `executor` is `ssh`.

for example:

`port = 22`

Default: null

#### **`username`**

```text
username = string
```

The username of your machine, only work when `executor` is `ssh`.

for example:

`username = 'wangzy'`

Default: null

#### **`password`**

```text
password = string
```

The password of your machine, only work when `executor` is `ssh`.

if one set `key_filename`, `password` will not work.

for example:

`password = 'password'`

Default: null

#### **`key_filename`**

```text
key_filename = string
```

The key file of your machine, only work when `executor` is `ssh`.

if one set `key_filename`, `password` will not work.

for example:

`key_filename = '/public/home/.ssh/id_rsa'`

Default: null


#### **`remote_root`**

```text
remote_root = string
```

Calculations of each structure will be conducted in `remote_root` if provided, otherwise, the calculation will be conducted in the "./results/opt_task/xxx" directory.

Default: null

### scheduler and related parameters
#### **`scheduler`**

```text
scheduler = string
```

We now support `pbs`, `slurm`, `lsf` and `shell`.

After choosing the scheduler, we should set three part of settings:

1. computational resources:

   - [queue](#queue)
   - [numb_node](#numb_node)
   - [numb_cpu_per_node](#numb_cpu_per_node)
   - [max_run_time](#max_run_time)
   - [machine_capacity](#machine_capacity)
   - [group_size](#group_size)

2. environment variables

   - [envs](#envs)
   - source (Deprecated Warning in V10.1.0)
   - module (Deprecated Warning in V10.1.0)

3. others

   - [additional_head_settings](#additional_head_settings)
   - [scheduler_envs](#scheduler_envs)

Here is the example of generated script for submitting job to scheduler Slurm:

```bash
#!/bin/bash
#SBATCH --job-name=sub_calypso-3.sh
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=1
#SBATCH --nodes=1
#SBATCH --partition=amd9654
#SBATCH --time=01:00:00
#SBATCH --output=sub_calypso-3.sh.log
#SBATCH --error=sub_calypso-3.sh.log


. /path/to/workplace/of/calypso/results/opt_task/3/calypso-3.sh > /path/to/workplace/of/calypso/results/opt_task/3/submit.log 2>&1;
```

One can add more additional scheduler settings with key: `additional_head_settings`. And if one did not set the `remote_root`, the calculation will be performed at `./results/opt_task/x/` where x denotes the structure number.

Default: "shell"

#### **`queue`**

```text
queue = string
```

The queue name of cluster, if it needs.

Default: null

#### **`numb_node`**

```text
numb_node = int
```

Specific the number of node.

for example:

`numb_node = 64`

Default: null


#### **`numb_cpu_per_node`**

```text
numb_cpu_per_node = int
```

Specific the number of cpu per node.

for example:

`numb_cpu_per_node = 64`

Default: null


#### **`max_run_time`**

```text
max_run_time = int or string
```

The max run time of each job.

If the value is string, it will be parsed into hour:minute:second.

if the value is int, it will be considered as seconds.

Default: "1:00:00"

#### **`max_retry`**

```text
max_retry = int
```

The max retry time of each job.

Default: 5


#### **`machine_capacity`**

```text
machine_capacity = string
```

Sometimes, we are allowed to submit tasks 
with no more than the limited number. In this case, can set `machine_capacity` to control the max number of tasks can be submitted in this computational resources.

After you set `machine_capacity`, the total number including running and waiting tasks is no more than this number.

`machine_capacity = 1`

Default: 1

#### **`group_size`**

```text
group_size = int
```

The `group_size` number of tasks will be packed together in one submission.

For example, We have generated 100 tasks, and we want to submit them in groups of 10. Then we can set `group_size` to 10. Each 10 tasks will occupy one node.

`group_size = 10`

Default: 1


#### **`envs`**

```js
envs = [string]
```

Some environment variables can be exported, whose command can be added here.

For example:

```js
envs = ["source /opt/intel/oneapi/setvars.sh"]
```

In current version of CALYPSO, environment variables for specific calculator must be set:

- For VASP calculation (`ICode` is `1`):

  ```js
  envs = [
    "source /opt/intel/oneapi/setvars.sh",
    "export CALYPSO_VASP_CMD='mpirun -np 32 /path/to/vasp_std'"
  ]
  ```

- For MLP calculation (`ICode` is `15`):

  ```js
  envs = ["export CALYPSO_MLP_CMD='/path/to/mlp/python'"]
  ```

- Use MLP + VASP calculation (`ICode` is `16`):
  ```js
  envs = [
    "source /opt/intel/oneapi/setvars.sh",
    "CALYPSO_MLP_CMD=/path/to/chgnet/python",
    "CALYPSO_VASP_CMD='mpirun -np 32 /path/to/vasp_std'"
  ]
  ```

Default: `[]`


#### **`additional_head_settings`**

```text
additional_head_settings = list of string
```

We will automatically generate the submit script according to `executor` and `scheduler`, but if you need some special setting, you should put them here.

For example:

`additional_head_settings = ["#SBATCH --exclude=node10"]`

Default: []

#### **`scheduler_envs`**

```text
scheduler_envs = list of string
```

Only work when using lsf. Because lsf somehow need its environment to submit/query/kill jobs.

Default: null
