# Case Studies

:::{Note}
**This documentation is up-to-date with v10.1.x!**
:::

## Crystal structure prediction of Li-N-H (fake formula)

```shell
(base) ➜  local_slurm_toml_vasp git:(devel) ✗ ls
INCAR_1        INCAR_3        POTCAR_H       POTCAR_N       machine-1.json ref_ene.txt
INCAR_2        INCAR_4        POTCAR_Li      input.toml     machine-2.json run.calypso.sh
```

input.toml example:

```toml

[CALYPSO]
SystemName = "Crystal-VASP CALYPSO config"
Seed = -1           # positive int number to set random seed for REPRODUCIBILITY,
                    # negetive to do not set it.
IType = 1           # or "CRYSTAL".
ICode = 1           # or "VASP".
IAlgo = 2           # or "LPSO".
IFit = 1            # or "ENTHALPY".
IDisp = 1           # or "CORE" means the build-in dispatcher by CALYPSO
                    # rather than third party libraries.

IRunner = 1         # normal mode of calypso.

ISim = 1            # or "BCM".
BlockMode = true    # block mode of calypso.
PickUp = false      # pick up the calculation whenever you want.

[CALYPSO.EVO]
NBest = 4
PSOratio = 0.4
PopSize = 10
MaxStep = 2

[CALYPSO.GENERATOR]
FormulaUnit = ["(LiH4)1-2(NH3)1-2",]
VolumeUnit = {Li=10, H=10, N=10}
DistanceOfIon = [["X",  "Li", "H", "N"],
                 ["Li",  1.0, 1.0,  1.0],
                 ["H",  1.0, 1.0,  1.0],
                 ["N", 1.0, 1.0,  1.0],]
SpaceGroup = [1, "2-30", 31, 32, "33-50", "51:231:1"]

[CALYPSO.OPT]
DFTInputPath = "."
JobFlow = ["opt", "opt", "opt", "scf"]
PpMap = {Li="POTCAR_Li", N="POTCAR_N", H="POTCAR_H"}

[CALYPSO.DISPATCHER]
# list your resoures here
MachineList = ["./machine-1.json", "./machine-2.json"]
TimeInterval = 3

[CALYPSO.DESCRIPTOR]
SimThreshold = 0.01

```

There are several ways to control and utilize the computational resources, by defining different combinations of `executor` and `scheduler` in `machine.json`.

### 1. Running CALYPSO in cluster with Slurm system in two queue using VASP

machine-1.json:

```json
{
    "name": "amd7513",

    "host": null,
    "port": null,
    "username": null,
    "password": null,
    "key_filename": null,

    "numb_cpu_per_node": 64,
    "numb_node": 1,
    "max_run_time": 100,

    "executor": "local",
    "scheduler": "slurm",
    "scheduler_envs": [],

    "remote_root": null,

    "machine_capacity": 4,
    "group_size": 1,
    "envs": [
        "source /data/env/compiler_intel-2021.3.0.sh",
        "source /data/env/mpi_intelmpi-2021.3.0.sh",
        "export CALYPSO_VASP_CMD='mpirun -n 64 /data/software/apps/vasp.6.1.0/bin/vasp_std'"
    ],
    "additional_head_settings": ["#SBATCH --exclude=node[49-50]"],
    "queue": "amd7513"
}
```

machine-2.json:

```json
{
    "name": "amd9654_1t",

    "host": null,
    "port": null,
    "username": null,
    "password": null,
    "key_filename": null,

    "numb_cpu_per_node": 64,
    "numb_node": 1,
    "max_run_time": 100,

    "executor": "local",
    "scheduler": "slurm",
    "scheduler_envs": [],

    "remote_root": null,

    "machine_capacity": 4,
    "group_size": 1,
    "envs": [
        "source /data/env/compiler_intel-2021.3.0.sh",
        "source /data/env/mpi_intelmpi-2021.3.0.sh",
        "export CALYPSO_VASP_CMD='mpirun -n 64 /data/software/apps/vasp.6.1.0/bin/vasp_std'"
    ],
    "additional_head_settings": ["#SBATCH --exclude=node[49-50]"],
    "queue": "amd9654_1t"
}
```

### 2. Running CALYPSO in local laptop or WorkStation using VASP

machine-1.json:

```json
{
    "name": "laptop",

    "host": null,
    "port": null,
    "username": null,
    "password": null,
    "key_filename": null,

    "numb_cpu_per_node": null,
    "numb_node": null,
    "max_run_time": 100,

    "executor": "local",
    "scheduler": "shell",
    "scheduler_envs": [],

    "remote_root": "/home/user/calypso/work_dir",

    "machine_capacity": 4,
    "group_size": 1,
    "envs": [
        "source /data/env/compiler_intel-2021.3.0.sh",
        "source /data/env/mpi_intelmpi-2021.3.0.sh",
        "export CALYPSO_VASP_CMD='mpirun -n 64 /data/software/apps/vasp.6.1.0/bin/vasp_std'"
    ],
    "additional_head_settings": [],
    "queue": null
}
```

### 3. Running CALYPSO in local laptop but send tasks into remote WorkStation using VASP

machine-1.json:

```json
{
    "name": "WorkStation",

    "host": "xxx.xxx.xxx.xxx",
    "port": 10086,
    "username": "username",
    "password": null,
    "key_filename": "key_file",

    "numb_cpu_per_node": null,
    "numb_node": null,
    "max_run_time": 100,

    "executor": "ssh",
    "scheduler": "shell",
    "scheduler_envs": [],

    "remote_root": "/home/remote/user/calypso/work_dir",

    "machine_capacity": 4,
    "group_size": 1,
    "envs": [
        "source /data/env/compiler_intel-2021.3.0.sh",
        "source /data/env/mpi_intelmpi-2021.3.0.sh",
        "export CALYPSO_VASP_CMD='mpirun -n 64 /data/software/apps/vasp.6.1.0/bin/vasp_std'"
    ],
    "additional_head_settings": [],
    "queue": null
}
```

### 4. Running CALYPSO in local laptop but send tasks into remote WorkStation and remote LSF cluster using VASP

machine-1.json:

```json
{
    "name": "WorkStation",

    "host": "xxx.xxx.xxx.xxx",
    "port": 10086,
    "username": "username",
    "password": null,
    "key_filename": "key_file",

    "numb_cpu_per_node": null,
    "numb_node": null,
    "max_run_time": 100,

    "executor": "ssh",
    "scheduler": "shell",
    "scheduler_envs": [],

    "remote_root": "/home/remote/user/calypso/work_dir",

    "machine_capacity": 4,
    "group_size": 1,
    "envs": [
        "source /data/env/compiler_intel-2021.3.0.sh",
        "source /data/env/mpi_intelmpi-2021.3.0.sh",
        "export CALYPSO_VASP_CMD='mpirun -n 64 /data/software/apps/vasp.6.1.0/bin/vasp_std'"
    ],
    "additional_head_settings": [],
    "queue": null
}
```

machine-2.json:

```json
{
    "name": "amd9654_1t",

    "host": "xxx.xxx.xxx.xxx",
    "port": 10086,
    "username": "username",
    "password": "xxxxxxxx",
    "key_filename": null,

    "numb_cpu_per_node": 64,
    "numb_node": 1,
    "max_run_time": 100,

    "executor": "ssh",
    "scheduler": "lsf",
    "scheduler_envs": [],

    "remote_root": "/remote/path/dir",

    "machine_capacity": 4,
    "group_size": 1,
    "envs": [
        "source /data/env/compiler_intel-2021.3.0.sh",
        "source /data/env/mpi_intelmpi-2021.3.0.sh",
        "export CALYPSO_VASP_CMD='mpirun -n 64 /data/software/apps/vasp.6.1.0/bin/vasp_std'"
    ],
    "additional_head_settings": ["#BSUB --exclude=node[49-50]"],
    "queue": "amd9654_1t"
}
```

### 5. Running CALYPSO in local laptop or WorkStation using MLP

Please note that `ICode` in `input.toml` must be **15** if one intends to use MLP.

machine-1.json:

```json
{
    "name": "laptop",

    "host": null,
    "port": null,
    "username": null,
    "password": null,
    "key_filename": null,

    "numb_cpu_per_node": null,
    "numb_node": null,
    "max_run_time": 100,

    "executor": "local",
    "scheduler": "shell",
    "scheduler_envs": [],

    "remote_root": "/home/user/calypso/work_dir",

    "machine_capacity": 4,
    "group_size": 1,
    "envs": ["export CALYPSO_MLP_CMD='/home/wangzy/softwares/miniconda3/envs/chgnet/bin/python'"],
    "additional_head_settings": [],
    "queue": null
}
```

ref_ene.txt:

```text
formula enthalpy_per_atom label
Li -1 element_Li
N -2 element_N
H -1.5 element_H
```

run.calypso.sh:

```text
#!/bin/bash

source /data/env/compiler_intel-2021.3.0.sh
source /data/env/mpi_intelmpi-2021.3.0.sh

source /data/home/wangzhenyu/softwares/miniconda3/bin/activate /data/home/wangzhenyu/softwares/miniconda3/envs/calypso

calypso.x > caly.log 2>&1
```

As you can see, CALYPSO will be submitted in login node by running `run.calypso.sh`. If you are not allowed to run process in login node, you can submit the `run.calypso.sh` to Slurm or PBS.

```text
#!/bin/bash
#SBATCH --job-name=VaspTest
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=1
#SBATCH --partition=amd9654

source /data/env/compiler_intel-2021.3.0.sh
source /data/env/mpi_intelmpi-2021.3.0.sh

source /data/home/wangzhenyu/softwares/miniconda3/bin/activate /data/home/wangzhenyu/softwares/miniconda3/envs/calypso

calypso.x > caly.log 2>&1
```
In this way, calypso will run in this compute node, but if your cluster is not allowed you to submit tasks in compute node with `sbatch` command, you may need to change the `scheduler` back to `shell` for normal mode.


## Molecule Crystal Prediction of $H_2O$

In this section, we use CALYPSO to predict the structure of $H_2O$ VIII. The following files are required:

```text
.
├── H2O.xyz
├── input.toml
└── machine-1.json
```

1. Molecular Structure Input (XYZ File)

   For molecular crystal prediction, an XYZ file is needed to store the molecular structure. Here, we use H2O.xyz to define the H₂O molecule structure:
   
   ```text
   3 
   H2O
   O 0.0 0.0 0.0
   H -0.895696 0.0 -0.454015
   H 0.895696 0.0 -0.454015
   ```

2. Task Configuration (input.toml)

   Next, we configure the prediction task in input.toml:
   
   ```toml
   [CALYPSO]
   # ...
   IType = 3           # For molecular crystal prediction
   # ...
   
   [CALYPSO.GENERATOR]
   FormulaUnit = "{H2O}4" # Curly brackets define a molecule unit
   VolumeUnit = {H2O=25}
   DistanceOfIon = [["X","H2O"],
                    ["H2O",1.2]]
   SpaceGroup = [141]
   GenerateMethod = "random"
   MoleculesPath = {'H2O'='./H2O.xyz'}
   LatticeMaxAttempts = 10
   OrbitalMaxAttempts = 10
   MaxTryPointEachOrb = 10
   
   [CALYPSO.EVO]
   NBest = 4
   PSOratio = 0 # Must be set to 0, as PSO evaluation is not supported
   ```

3. Explanation of Key Parameters

    - IType: Must be 3 to run molecular crystal prediction.
    - Molecular Labeling: The label `H2O` represents the water molecule.
    - Formula Unit Definition: `FormulaUnit = "{H2O}4"` specifies four $H_2O$ molecules in curly brackets.
    - Volume and Distance Configuration: Using the label, you can set parameters like volume, inter-molecular distance, and molecule paths.
    - PSO Ratio: PSOratio must be set to 0 because PSO evaluation is not supported.

This setup ensures the correct execution of the molecular crystal prediction for H₂O VIII using CALYPSO.


## Molecule Crystal Prediction of Fe-O-OH

Molecules can also be defined with other elements. In this example, we input `OH` as a unit along with the elements `Fe` and `O`.


```toml
[CALYPSO]
# ...
IType = 3           # For molecular crystal prediction
# ...

[CALYPSO.GENERATOR]
FormulaUnit = "(Fe)4(O)4{OH}4"
VolumeUnit = {Fe=15,O=15,OH=15}
DistanceOfIon = [["X", "Fe","O","OH"],
                 ["Fe", 1.2,1.2,1.2],
                 ["O",1.2,1.2,1.2],
                 ["OH",1.2,1.2,1.2]]
SpaceGroup = [62] 
GenerateMethod = "random"
MoleculesPath = {'OH'='./OH.xyz'}
LatticeMaxAttempts = 10
OrbitalMaxAttempts = 10
MaxTryPointEachOrb = 10

[CALYPSO.EVO]
NBest = 4
PSOratio = 0 # Must be set to 0, as PSO evaluation is not supported
```

and here is the `OH.xyz` file:

```text
2
HO
O 0 0 0
H 0 0 0.9
```

## Surface Structure Prediction

The input files of the cases below are in `example/surface-mlp/` of CALYPSO-Python. All cases use
CHGNet (`ICode = 15`) and the same settings outside `[CALYPSO.GENERATOR]`. See
[Input parameters](_input_parameters.md#extra-parameters-for-surface-structure-prediction)
for every surface parameter.

(surface-common-files)=
### Common files

Every surface case uses the same `machine-1.json` and `run.calypso.sh`. Replace the
`/path/to/...` placeholders by your own environments.

`machine-1.json`:

```json
{
    "name": "local",
    "executor": "local",
    "scheduler": "shell",
    "scheduler_envs": [],
    "remote_root": null,
    "machine_capacity": 1,
    "group_size": 1,
    "envs": ["export CALYPSO_MLP_CMD='/path/to/envs/chgnet/bin/python'"],
    "additional_head_settings": [],
    "queue": null
}
```

`run.calypso.sh`:

```bash
#!/bin/bash

source /path/to/anaconda3/bin/activate /path/to/anaconda3/envs/calypso
calypso.x > caly.log 2>&1 &
```

(surface-case-1)=
### 1. H and OH on graphene, unfixed sites

Two H atoms on the upper side and one OH on the lower side of a 2x2 graphene substrate; OH rotates freely (`MolRotate = true`).

Files in `example/surface-mlp/C8_H2_OH1_unfixed_sites/`:

```text
.
├── input.toml
├── machine-1.json
├── run.calypso.sh
├── SUB.vasp
└── OH.xyz
```

`SUB.vasp`:

```text
graphine
1.0
        2.4593999386         0.0000000000         0.0000000000
       -1.2296999693         2.1299028249         0.0000000000
        0.0000000000         0.0000000000        15.0000000000
  C
  2
  Selective Dynamics
Direct
  0.666666687         0.333333343         0.500000000 T T T
  0.333333313         0.666666627         0.500000000 T T T
```

`OH.xyz`:

```text
2
HO
O 0 0 0
H 0 0 0.9
```

`machine-1.json` and `run.calypso.sh`: see [common files](#surface-common-files).

`input.toml`:

```toml
[CALYPSO]
SystemName = "Graphene_H_OH_unfixed_sites"
Seed = -1            # positive: fixed random seed for reproducibility; negative: not set
IType = 5            # surface
ICode = 15           # MLP
IAlgo = 2            # local PSO
IFit = 1             # enthalpy
IDisp = 1            # built-in dispatcher
IRunner = 1          # run automatically
ISim = 1             # BCM similarity descriptor
BlockMode = true     # wait for the whole generation before evolving
PickUp = false       # start a new calculation

[CALYPSO.EVO]
NBest = 4
PSOratio = 0.6       # ratio of structures generated by PSO
PopSize = 5          # structures per generation
MaxStep = 2          # number of generations

[CALYPSO.GENERATOR]
AdsorptionStyle = 1                # unfixed adsorption sites
FormulaUnit = ["(H)2", "{OH}1"]    # [upper side, lower side]
DistanceOfIon = [["X",  "C", "H", "OH"],
                 ["C",  1.0, 1.2, 1.2],
                 ["H",  1.2, 1.2, 1.2],
                 ["OH", 1.2, 1.2, 1.2]]
AdsorptionSymmetry = true          # symmetric adsorption sites
SubstratePath = "./SUB.vasp"       # graphene
Supercell = [[2, 0], [0, 2]]       # 2x2 substrate
RangeOfZAxis = [1.7, 1.2]          # adsorption height range
MoleculesPath = {"OH" = "./OH.xyz"}
FixSiteC = false                   # sample the height within RangeOfZAxis
TranslateAtomPosition = false      # no random translation of the sites
RotateAtomPosition = false         # no random rotation of the sites
MolRotate = true                   # molecules rotate freely about their first atom

[CALYPSO.OPT]
JobFlow = ["opt"]
MLPType = "chgnet"   # MLP: chgnet, m3gnet, dpa2, ...
MLPKwargs = {"model"="0.3.0", "check_cuda_mem"=false, "on_isolated_atoms"="warn"}
OptAlgo = "LBFGS"    # LBFGS, BFGS, FIRE
OptStep = 100        # maximal optimization steps
TrajFile = "traj.traj"
Pstress = 0          # GPa
Fmax = 0.01          # eV/angstrom
MLPKeepSym = false   # keep symmetry during optimization
UcfMask = [false, false, false, false, false, false]   # false: keep the substrate cell fixed

[CALYPSO.DISPATCHER]
MachineList = ["./machine-1.json"]
TimeInterval = 3     # seconds between job checks
TmpPath = "BackStage"

[CALYPSO.DESCRIPTOR]
SimThreshold = 0.01  # similarity threshold
```

(surface-case-2)=
### 2. H and O on graphene, fixed sites

`AdsorptionStyle = 2` places H and O only on the sites listed in `point.json`; the names `H` and `O` in `point.json` are the units of `FormulaUnit`.

Files in `example/surface-mlp/C8_H1_O1_fixed_sites/`:

```text
.
├── input.toml
├── machine-1.json
├── run.calypso.sh
├── SUB.vasp
└── point.json
```

`SUB.vasp`:

```text
graphine
1.0
        2.4593999386         0.0000000000         0.0000000000
       -1.2296999693         2.1299028249         0.0000000000
        0.0000000000         0.0000000000        15.0000000000
  C
  2
  Selective Dynamics
Direct
  0.666666687         0.333333343         0.500000000 T T T
  0.333333313         0.666666627         0.500000000 T T T
```

`point.json`:

```js
{
    "coordinate system": "Direct",
    "point":{
    "H":[[0.666670024,         0.333330005,         0.500000000],
        [0.333330005,         0.666670024,         0.500000000]],
    "O":[[0.465000004,         0.491389990,         0.500000000]]
    }
}
```

`machine-1.json` and `run.calypso.sh`: see [common files](#surface-common-files).

`input.toml`:

```toml
[CALYPSO]
SystemName = "Graphene_H_O_fixed_sites"
Seed = -1            # positive: fixed random seed for reproducibility; negative: not set
IType = 5            # surface
ICode = 15           # MLP
IAlgo = 2            # local PSO
IFit = 1             # enthalpy
IDisp = 1            # built-in dispatcher
IRunner = 1          # run automatically
ISim = 1             # BCM similarity descriptor
BlockMode = true     # wait for the whole generation before evolving
PickUp = false       # start a new calculation

[CALYPSO.EVO]
NBest = 4
PSOratio = 0.6       # ratio of structures generated by PSO
PopSize = 5          # structures per generation
MaxStep = 2          # number of generations

[CALYPSO.GENERATOR]
AdsorptionStyle = 2                # fixed adsorption sites from PointPath
FormulaUnit = ["(H)1(O)1"]
DistanceOfIon = [["X", "C", "H", "O"],
                 ["C", 1.0, 1.2, 1.2],
                 ["H", 1.2, 1.2, 1.2],
                 ["O", 1.2, 1.2, 1.2]]
AdsorptionSymmetry = true          # symmetric adsorption sites
SubstratePath = "./SUB.vasp"       # graphene
Supercell = [[2, 0], [0, 2]]       # 2x2 substrate
RangeOfZAxis = [1.7, 1.2]          # adsorption height range
PointPath = "./point.json"         # candidate adsorption sites
FixSiteC = false                   # sample the height within RangeOfZAxis
TranslateAtomPosition = false      # no random translation of the sites
RotateAtomPosition = false         # no random rotation of the sites

[CALYPSO.OPT]
JobFlow = ["opt"]
MLPType = "chgnet"   # MLP: chgnet, m3gnet, dpa2, ...
MLPKwargs = {"model"="0.3.0", "check_cuda_mem"=false, "on_isolated_atoms"="warn"}
OptAlgo = "LBFGS"    # LBFGS, BFGS, FIRE
OptStep = 100        # maximal optimization steps
TrajFile = "traj.traj"
Pstress = 0          # GPa
Fmax = 0.01          # eV/angstrom
MLPKeepSym = false   # keep symmetry during optimization
UcfMask = [false, false, false, false, false, false]   # false: keep the substrate cell fixed

[CALYPSO.DISPATCHER]
MachineList = ["./machine-1.json"]
TimeInterval = 3     # seconds between job checks
TmpPath = "BackStage"

[CALYPSO.DESCRIPTOR]
SimThreshold = 0.01  # similarity threshold
```

(surface-case-3)=
### 3. Three boron slabs in one cell (multi-surface)

`SUB.vasp` holds three borophene slabs; the last column is the slab index (1 = bottom). `FormulaUnit` and `RangeOfZAxis` give one `[upper, lower]` pair per slab. At the start CALYPSO writes the slabs to `POSCAR_0.vasp`, `POSCAR_1.vasp` and `POSCAR_2.vasp` for checking.

Files in `example/surface-mlp/B8_H2_B8_H3_OH1_B8_O2_multi_surf/`:

```text
.
├── input.toml
├── machine-1.json
├── run.calypso.sh
├── SUB.vasp
└── OH.xyz
```

:::{dropdown} SUB.vasp
```text
B
   1.000
    5.0588002205000002    0.0000000000000000    0.0000000000000000
   -2.5294001102000001    4.3810495035999999    0.0000000000000000
    0.0000000000000000    0.0000000000000000   30.0000000000000000
   B
   24
Selective Dynamics
Direct
    0.3323099910000000    0.0000000000000000    0.6000000240000000    F  F  F    3
    0.6676899790000000    0.0000000000000000    0.6000000240000000    F  F  F    3
    0.0000000000000000    0.3323099910000000    0.6000000240000000    F  F  F    3
    0.3323099910000000    0.3323099910000000    0.6000000240000000    F  F  F    3
    0.6666700240000000    0.3333300050000000    0.6054199930000000    F  F  F    3
    0.0000000000000000    0.6676899790000000    0.6000000240000000    F  F  F    3
    0.3333300050000000    0.6666700240000000    0.5945799950000000    F  F  F    3
    0.6676899790000000    0.6676899790000000    0.6000000240000000    F  F  F    3
    0.3323099910000000    0.0000000000000000    0.2690199910000000    F  F  F    1
    0.6676899790000000    0.0000000000000000    0.2690199910000000    F  F  F    1
    0.0000000000000000    0.3323099910000000    0.2690199910000000    F  F  F    1
    0.3323099910000000    0.3323099910000000    0.2690199910000000    F  F  F    1
    0.6666700240000000    0.3333300050000000    0.2744399910000000    F  F  F    1
    0.0000000000000000    0.6676899790000000    0.2690199910000000    F  F  F    1
    0.3333300050000000    0.6666700240000000    0.2636100050000000    F  F  F    1
    0.6676899790000000    0.6676899790000000    0.2690199910000000    F  F  F    1
    0.3323099910000000    0.0000000000000000    0.4662800130000000    F  F  F    2
    0.6676899790000000    0.0000000000000000    0.4662800130000000    F  F  F    2
    0.0000000000000000    0.3323099910000000    0.4662800130000000    F  F  F    2
    0.3323099910000000    0.3323099910000000    0.4662800130000000    F  F  F    2
    0.6666700240000000    0.3333300050000000    0.4716899990000000    F  F  F    2
    0.0000000000000000    0.6676899790000000    0.4662800130000000    F  F  F    2
    0.3333300050000000    0.6666700240000000    0.4608600140000000    F  F  F    2
    0.6676899790000000    0.6676899790000000    0.4662800130000000    F  F  F    2
```
:::

`OH.xyz`:

```text
2
HO
O 0 0 0
H 0 0 0.9
```

`machine-1.json` and `run.calypso.sh`: see [common files](#surface-common-files).

`input.toml`:

```toml
[CALYPSO]
SystemName = "Borophene_multi_surface_H_OH_O"
Seed = -1            # positive: fixed random seed for reproducibility; negative: not set
IType = 5            # surface
ICode = 15           # MLP
IAlgo = 2            # local PSO
IFit = 1             # enthalpy
IDisp = 1            # built-in dispatcher
IRunner = 1          # run automatically
ISim = 1             # BCM similarity descriptor
BlockMode = true     # wait for the whole generation before evolving
PickUp = false       # start a new calculation

[CALYPSO.EVO]
NBest = 4
PSOratio = 0.6       # ratio of structures generated by PSO
PopSize = 5          # structures per generation
MaxStep = 2          # number of generations

[CALYPSO.GENERATOR]
AdsorptionStyle = 1                # unfixed adsorption sites
FormulaUnit = [["(H)2{OH}1", ""],     # slab 1: [upper, lower]
               ["(H)3", "{OH}1"],      # slab 2
               ["", "(O)2"]]           # slab 3
DistanceOfIon = [["X",  "B", "O", "H", "OH"],
                 ["B",  1.2, 1.3, 1.4, 1.5],
                 ["O",  1.3, 1.1, 1.2, 1.3],
                 ["H",  1.4, 1.2, 1.6, 1.7],
                 ["OH", 1.5, 1.3, 1.7, 1.6]]
AdsorptionSymmetry = true          # symmetric adsorption sites
SubstratePath = "./SUB.vasp"       # three slabs, last column = slab index
MoleculesPath = {"OH" = "./OH.xyz"}
RangeOfZAxis = [[[1.0, 1.3], []],     # same layout as FormulaUnit
                [[1.0, 1.3], [1.4, 1.3]],
                [[], [1.3, 1.4]]]
FixSiteC = false                   # sample the height within RangeOfZAxis
TranslateAtomPosition = false      # no random translation of the sites
RotateAtomPosition = false         # no random rotation of the sites
MolRotate = true                   # molecules rotate freely about their first atom

[CALYPSO.OPT]
JobFlow = ["opt"]
MLPType = "chgnet"   # MLP: chgnet, m3gnet, dpa2, ...
MLPKwargs = {"model"="0.3.0", "check_cuda_mem"=false, "on_isolated_atoms"="warn"}
OptAlgo = "LBFGS"    # LBFGS, BFGS, FIRE
OptStep = 100        # maximal optimization steps
TrajFile = "traj.traj"
Pstress = 0          # GPa
Fmax = 0.01          # eV/angstrom
MLPKeepSym = false   # keep symmetry during optimization
UcfMask = [false, false, false, false, false, false]   # false: keep the substrate cell fixed

[CALYPSO.DISPATCHER]
MachineList = ["./machine-1.json"]
TimeInterval = 3     # seconds between job checks
TmpPath = "BackStage"

[CALYPSO.DESCRIPTOR]
SimThreshold = 0.01  # similarity threshold
```

(surface-case-4)=
### 4. Diamond (111) reconstruction, automatic substrate

`SubstratePath = "Automatic"` cleaves the substrate from bulk diamond, so no substrate file is needed. The substrate carbon and the adsorbed carbon are listed separately in `DistanceOfIon`.

Files in `example/surface-mlp/diamond_111_C4_unfixed_sites/`:

```text
.
├── input.toml
├── machine-1.json
└── run.calypso.sh
```

`machine-1.json` and `run.calypso.sh`: see [common files](#surface-common-files).

`input.toml`:

```toml
[CALYPSO]
SystemName = "Diamond111_C4_reconstruction"
Seed = -1            # positive: fixed random seed for reproducibility; negative: not set
IType = 5            # surface
ICode = 15           # MLP
IAlgo = 2            # local PSO
IFit = 1             # enthalpy
IDisp = 1            # built-in dispatcher
IRunner = 1          # run automatically
ISim = 1             # BCM similarity descriptor
BlockMode = true     # wait for the whole generation before evolving
PickUp = false       # start a new calculation

[CALYPSO.EVO]
NBest = 4
PSOratio = 0.6       # ratio of structures generated by PSO
PopSize = 5          # structures per generation
MaxStep = 2          # number of generations

[CALYPSO.GENERATOR]
AdsorptionStyle = 1                # unfixed adsorption sites
FormulaUnit = ["(C)4"]
DistanceOfIon = [["X", "C", "H", "C"],   # substrate C, H, adsorbed C
                 ["C", 1.0, 1.2, 1.2],
                 ["H", 1.2, 1.2, 1.2],
                 ["C", 1.2, 1.2, 1.2]]
AdsorptionSymmetry = true          # symmetric adsorption sites
SubstratePath = "Automatic"        # cleave diamond (111), see CLEAVE
Supercell = [[1, 0], [0, 1]]
RangeOfZAxis = [3.2, 1.2]          # adsorption height range
FixSiteC = false                   # sample the height within RangeOfZAxis
TranslateAtomPosition = false      # no random translation of the sites
RotateAtomPosition = false         # no random rotation of the sites

[CALYPSO.GENERATOR.CLEAVE]
MillerIndex = [1, 1, 1]            # diamond (111)
MatrixNotation = [[2, 0], [0, 1]]  # 2x1 surface cell
SpaceGroup = 227
LatticeParameters = [3.5668, 3.5668, 3.5668, 90.0, 90.0, 90.0]
IrreducibleAtoms = [['C', 0.0, 0.0, 0.0]]
CapBondsWithH = true               # H caps the bottom surface

[CALYPSO.OPT]
JobFlow = ["opt"]
MLPType = "chgnet"   # MLP: chgnet, m3gnet, dpa2, ...
MLPKwargs = {"model"="0.3.0", "check_cuda_mem"=false, "on_isolated_atoms"="warn"}
OptAlgo = "LBFGS"    # LBFGS, BFGS, FIRE
OptStep = 100        # maximal optimization steps
TrajFile = "traj.traj"
Pstress = 0          # GPa
Fmax = 0.01          # eV/angstrom
MLPKeepSym = false   # keep symmetry during optimization
UcfMask = [false, false, false, false, false, false]   # false: keep the substrate cell fixed

[CALYPSO.DISPATCHER]
MachineList = ["./machine-1.json"]
TimeInterval = 3     # seconds between job checks
TmpPath = "BackStage"

[CALYPSO.DESCRIPTOR]
SimThreshold = 0.01  # similarity threshold
```

(surface-case-5)=
### 5. Borophene covering Ag(100) (2D, full coverage)

`SurfaceGenerationMode = "2D"` with `Coverage = "Full"` builds a B8 layer on the whole Ag(100) 2x2 cell; Ag(100) is cleaved automatically.

Files in `example/surface-mlp/Ag_100_B8_side_2D_full/`:

```text
.
├── input.toml
├── machine-1.json
└── run.calypso.sh
```

`machine-1.json` and `run.calypso.sh`: see [common files](#surface-common-files).

`input.toml`:

```toml
[CALYPSO]
SystemName = "Ag100_B8_2D_full"
Seed = -1            # positive: fixed random seed for reproducibility; negative: not set
IType = 5            # surface
ICode = 15           # MLP
IAlgo = 2            # local PSO
IFit = 1             # enthalpy
IDisp = 1            # built-in dispatcher
IRunner = 1          # run automatically
ISim = 1             # BCM similarity descriptor
BlockMode = true     # wait for the whole generation before evolving
PickUp = false       # start a new calculation

[CALYPSO.EVO]
NBest = 4
PSOratio = 0.6       # ratio of structures generated by PSO
PopSize = 5          # structures per generation
MaxStep = 2          # number of generations

[CALYPSO.GENERATOR]
SurfaceGenerationMode = "2D"       # a boron layer covering the substrate
FormulaUnit = ["(B)8"]
DistanceOfIon = [["X",  "Ag", "B"],   # substrate first, then seed
                 ["Ag", 2.8,  2.0],
                 ["B",  2.0,  1.5]]
SubstratePath = "Automatic"        # cleave Ag(100), see CLEAVE
RangeOfZAxis = [2.0, 2.4]          # gap between substrate top and layer bottom

[CALYPSO.GENERATOR.CLEAVE]
MillerIndex = [1, 0, 0]            # Ag(100)
MatrixNotation = [[2, 0], [0, 2]]  # 2x2 surface cell
SpaceGroup = 225                   # fcc Ag
LatticeParameters = [4.10, 4.10, 4.10, 90.0, 90.0, 90.0]
IrreducibleAtoms = [['Ag', 0.0, 0.0, 0.0]]
CapBondsWithH = false

[CALYPSO.GENERATOR.2D]
Coverage = "Full"                  # layer uses the whole substrate cell
Thicknesses = [0]                  # atomically flat
SpaceGroup = ["1-80"]              # layer groups
Gaps = [15]

[CALYPSO.OPT]
JobFlow = ["opt"]
MLPType = "chgnet"   # MLP: chgnet, m3gnet, dpa2, ...
MLPKwargs = {"model"="0.3.0", "check_cuda_mem"=false, "on_isolated_atoms"="warn"}
OptAlgo = "LBFGS"    # LBFGS, BFGS, FIRE
OptStep = 100        # maximal optimization steps
TrajFile = "traj.traj"
Pstress = 0          # GPa
Fmax = 0.01          # eV/angstrom
MLPKeepSym = false   # keep symmetry during optimization
UcfMask = [false, false, false, false, false, false]   # false: keep the substrate cell fixed

[CALYPSO.DISPATCHER]
MachineList = ["./machine-1.json"]
TimeInterval = 3     # seconds between job checks
TmpPath = "BackStage"

[CALYPSO.DESCRIPTOR]
SimThreshold = 0.01  # similarity threshold
```

(surface-case-6)=
### 6. Boron island on Ag(100) (2D, island)

A finite B6 flake of 25 angstrom^2 with a buckling up to 0.2 angstrom on Ag(100).

Files in `example/surface-mlp/Ag_100_B6_side_2D/`:

```text
.
├── input.toml
├── machine-1.json
└── run.calypso.sh
```

`machine-1.json` and `run.calypso.sh`: see [common files](#surface-common-files).

`input.toml`:

```toml
[CALYPSO]
SystemName = "Ag100_B6_2D_island"
Seed = -1            # positive: fixed random seed for reproducibility; negative: not set
IType = 5            # surface
ICode = 15           # MLP
IAlgo = 2            # local PSO
IFit = 1             # enthalpy
IDisp = 1            # built-in dispatcher
IRunner = 1          # run automatically
ISim = 1             # BCM similarity descriptor
BlockMode = true     # wait for the whole generation before evolving
PickUp = false       # start a new calculation

[CALYPSO.EVO]
NBest = 4
PSOratio = 0.6       # ratio of structures generated by PSO
PopSize = 5          # structures per generation
MaxStep = 2          # number of generations

[CALYPSO.GENERATOR]
SurfaceGenerationMode = "2D"       # a 2D boron island on the substrate
FormulaUnit = ["(B)6"]
DistanceOfIon = [["X",  "Ag", "B"],   # substrate first, then seed
                 ["Ag", 2.8,  2.0],
                 ["B",  2.0,  1.5]]
SubstratePath = "Automatic"        # cleave Ag(100), see CLEAVE
RangeOfZAxis = [2.0, 2.4]          # gap between substrate top and layer bottom

[CALYPSO.GENERATOR.CLEAVE]
MillerIndex = [1, 0, 0]            # Ag(100)
MatrixNotation = [[2, 0], [0, 2]]  # 2x2 surface cell
SpaceGroup = 225                   # fcc Ag
LatticeParameters = [4.10, 4.10, 4.10, 90.0, 90.0, 90.0]
IrreducibleAtoms = [['Ag', 0.0, 0.0, 0.0]]
CapBondsWithH = false

[CALYPSO.GENERATOR.2D]
Area = 25                          # island area (angstrom^2)
Thicknesses = [0.2]                # buckling up to 0.2 angstrom
SpaceGroup = ["1-80"]              # layer groups
Gaps = [15]

[CALYPSO.OPT]
JobFlow = ["opt"]
MLPType = "chgnet"   # MLP: chgnet, m3gnet, dpa2, ...
MLPKwargs = {"model"="0.3.0", "check_cuda_mem"=false, "on_isolated_atoms"="warn"}
OptAlgo = "LBFGS"    # LBFGS, BFGS, FIRE
OptStep = 100        # maximal optimization steps
TrajFile = "traj.traj"
Pstress = 0          # GPa
Fmax = 0.01          # eV/angstrom
MLPKeepSym = false   # keep symmetry during optimization
UcfMask = [false, false, false, false, false, false]   # false: keep the substrate cell fixed

[CALYPSO.DISPATCHER]
MachineList = ["./machine-1.json"]
TimeInterval = 3     # seconds between job checks
TmpPath = "BackStage"

[CALYPSO.DESCRIPTOR]
SimThreshold = 0.01  # similarity threshold
```

(surface-case-7)=
### 7. (BN)6 cluster on Ag(100)

`SurfaceGenerationMode = "Cluster"` generates a B6N6 cluster (volume from `VolumeUnit`) and puts it on Ag(100), cleaved automatically.

Files in `example/surface-mlp/Ag_100_B6N6_side_Cluster/`:

```text
.
├── input.toml
├── machine-1.json
└── run.calypso.sh
```

`machine-1.json` and `run.calypso.sh`: see [common files](#surface-common-files).

`input.toml`:

```toml
[CALYPSO]
SystemName = "Ag100_B6N6_Cluster"
Seed = -1            # positive: fixed random seed for reproducibility; negative: not set
IType = 5            # surface
ICode = 15           # MLP
IAlgo = 2            # local PSO
IFit = 1             # enthalpy
IDisp = 1            # built-in dispatcher
IRunner = 1          # run automatically
ISim = 1             # BCM similarity descriptor
BlockMode = true     # wait for the whole generation before evolving
PickUp = false       # start a new calculation

[CALYPSO.EVO]
NBest = 4
PSOratio = 0.6       # ratio of structures generated by PSO
PopSize = 5          # structures per generation
MaxStep = 2          # number of generations

[CALYPSO.GENERATOR]
SurfaceGenerationMode = "Cluster"  # a (BN)6 cluster on the substrate
FormulaUnit = ["(BN)6"]
VolumeUnit = {"N" = 5.0, "B" = 5.0}  # volume per atom of the normal cluster
DistanceOfIon = [["X",  "Ag", "B", "N"],   # substrate first, then seed
                 ["Ag", 1.8,  1.6, 1.6],
                 ["B",  1.6,  1.2, 1.2],
                 ["N",  1.6,  1.2, 1.2]]
SubstratePath = "Automatic"        # cleave Ag(100), see CLEAVE
RangeOfZAxis = [3.0, 1.2]          # gap between substrate top and cluster bottom

[CALYPSO.GENERATOR.CLEAVE]
MillerIndex = [1, 0, 0]            # Ag(100)
MatrixNotation = [[2, 0], [0, 2]]  # 2x2 surface cell
SpaceGroup = 225                   # fcc Ag
LatticeParameters = [4.10, 4.10, 4.10, 90.0, 90.0, 90.0]
IrreducibleAtoms = [['Ag', 0.0, 0.0, 0.0]]
CapBondsWithH = false

[CALYPSO.GENERATOR.CLUSTER]
ClusterType = "normal"             # normal, cage, plane
SpaceGroup = ["1-31"]              # point groups
GenerateMethod = "fortran"
Vacancy = [15.0, 15.0, 15.0]       # vacuum around the generated cluster

[CALYPSO.OPT]
JobFlow = ["opt"]
MLPType = "chgnet"   # MLP: chgnet, m3gnet, dpa2, ...
MLPKwargs = {"model"="0.3.0", "check_cuda_mem"=false, "on_isolated_atoms"="warn"}
OptAlgo = "LBFGS"    # LBFGS, BFGS, FIRE
OptStep = 100        # maximal optimization steps
TrajFile = "traj.traj"
Pstress = 0          # GPa
Fmax = 0.01          # eV/angstrom
MLPKeepSym = false   # keep symmetry during optimization
UcfMask = [false, false, false, false, false, false]   # false: keep the substrate cell fixed

[CALYPSO.DISPATCHER]
MachineList = ["./machine-1.json"]
TimeInterval = 3     # seconds between job checks
TmpPath = "BackStage"

[CALYPSO.DESCRIPTOR]
SimThreshold = 0.01  # similarity threshold
```

## Interface Structure Prediction

The input files are in `example/interface-mlp/` of CALYPSO-Python. Every case searches a TiO4
interface layer between a rutile slab (`SUB1.vasp`, lower slab, keeps its lattice)
and an anatase slab (`SUB2.vasp`, upper slab). See
[Input parameters](_input_parameters.md#extra-parameters-for-interface-structure-prediction)
for every interface parameter.

(interface-common-files)=
### Common files

Every interface case uses the same `machine-1.json` and `run.calypso.sh`. Replace
the `/path/to/...` placeholders by your own environments.

`machine-1.json`:

```json
{
    "name": "local",
    "executor": "local",
    "scheduler": "shell",
    "scheduler_envs": [],
    "remote_root": null,
    "machine_capacity": 1,
    "group_size": 1,
    "envs": ["export CALYPSO_MLP_CMD='/path/to/envs/chgnet/bin/python'"],
    "additional_head_settings": [],
    "queue": null
}
```

`run.calypso.sh`:

```bash
#!/bin/bash

source /path/to/anaconda3/bin/activate /path/to/anaconda3/envs/calypso
calypso.x > caly.log 2>&1 &
```

(interface-case-1)=
### 1. Symmetric generation

`RandScheme = 1` generates the interface atoms with 2D symmetry.

Files in `example/interface-mlp/rutile_anatanse_tio4_symmetry/`:

```text
.
├── input.toml
├── machine-1.json
├── run.calypso.sh
├── SUB1.vasp
└── SUB2.vasp
```

:::{dropdown} SUB1.vasp (rutile, lower slab)
```text
rutile
   1.000
    9.3906002045000001    0.0000000000000000    0.0000000000000000
    0.0000000000000000    5.5958018303000001    0.0000000000000000
    0.0000000000000000    0.0000000000000000   17.5543136597000000
   O    Ti
    8    8
Direct
    0.3473350000000000    0.7850331200000000    0.3859111300000000
    0.8473349999999999    0.7850331200000000    0.3859111300000000
    0.4026650000000000    0.2850331200000000    0.3859111300000000
    0.9026650000000001    0.2850331200000000    0.3859111300000000
    0.0973350000000000    0.0109192000000000    0.3292585900000000
    0.5973349999999999    0.0109192000000000    0.3292585900000000
    0.1526650000000000    0.5109192000000000    0.3292585900000000
    0.6526650000000001    0.5109192000000000    0.3292585900000000
    0.2500000000000000    0.5000000000000000    0.4303394500000000
    0.7500000000000000    0.5000000000000000    0.4303394500000000
    0.0000000000000000    0.0000000000000000    0.4303394500000000
    0.5000000000000000    0.0000000000000000    0.4303394500000000
    0.2500000000000000    0.7959523200000000    0.2848302800000000
    0.7500000000000000    0.7959523200000000    0.2848302800000000
    0.0000000000000000    0.2959523200000000    0.2848302800000000
    0.5000000000000000    0.2959523200000000    0.2848302800000000
```
:::

:::{dropdown} SUB2.vasp (anatase, upper slab)
```text
anatanse
   1.000
    8.2801496926000002   -4.8497996119000000    0.0000000000000000
    2.7600501230000001    4.8497995127999998    0.0000000000000000
    0.0000000000000000    0.0000000000000000   20.5200996398999997
   O    Ti
   20   10
Direct
    0.6460750000000000    0.0617750000000000    0.5126729400000000
    0.1460750000000000    0.5617750000000000    0.5126729400000000
    0.8539250000000000    0.4382250000000000    0.5126729400000000
    0.3539250000000000    0.9382250000000000    0.5126729400000000
    0.3960750000000000    0.3117750000000000    0.4454205800000000
    0.8960750000000000    0.8117750000000000    0.4454205800000000
    0.1039250000000000    0.1882250000000000    0.4454205800000000
    0.6039250000000000    0.6882250000000000    0.4454205800000000
    0.8960750000000000    0.3117750000000000    0.3781682300000000
    0.3960750000000000    0.8117750000000000    0.3781682300000000
    0.6039250000000000    0.1882250000000000    0.3781682300000000
    0.1039250000000000    0.6882250000000000    0.3781682300000000
    0.1460750000000000    0.0617750000000000    0.3109158800000000
    0.6460750000000000    0.5617750000000000    0.3109158800000000
    0.3539250000000000    0.4382250000000000    0.3109158800000000
    0.8539250000000000    0.9382250000000000    0.3109158800000000
    0.6460750000000000    0.0617750000000000    0.2436635300000000
    0.1460750000000000    0.5617750000000000    0.2436635300000000
    0.8539250000000000    0.4382250000000000    0.2436635300000000
    0.3539250000000000    0.9382250000000000    0.2436635300000000
    0.2500000000000000    0.2500000000000000    0.5126729400000000
    0.7500000000000000    0.7500000000000000    0.5126729400000000
    0.5000000000000000    0.0000000000000000    0.4454205800000000
    0.0000000000000000    0.5000000000000000    0.4454205800000000
    0.0000000000000000    0.0000000000000000    0.3781682300000000
    0.5000000000000000    0.5000000000000000    0.3781682300000000
    0.7500000000000000    0.2500000000000000    0.3109158800000000
    0.2500000000000000    0.7500000000000000    0.3109158800000000
    0.2500000000000000    0.2500000000000000    0.2436635300000000
    0.7500000000000000    0.7500000000000000    0.2436635300000000
```
:::

`machine-1.json` and `run.calypso.sh`: see [common files](#interface-common-files).

`input.toml`:

```toml
[CALYPSO]
SystemName = "Rutile_Anatase_TiO4_symmetry"
Seed = -1            # positive: fixed random seed for reproducibility; negative: not set
IType = 6            # interface
ICode = 15           # MLP
IAlgo = 2            # local PSO
IFit = 1             # enthalpy
IDisp = 1            # built-in dispatcher
IRunner = 1          # run automatically
ISim = 1             # BCM similarity descriptor
BlockMode = true     # wait for the whole generation before evolving
PickUp = false       # start a new calculation

[CALYPSO.EVO]
NBest = 4
PSOratio = 0.6       # ratio of structures generated by PSO
PopSize = 5          # structures per generation
MaxStep = 2          # number of generations

[CALYPSO.GENERATOR]
FormulaUnit = ["(Ti)1(O)4"]        # atoms of the interface region
DistanceOfIon = [["X",  "Ti", "O"],
                 ["Ti", 1.5,  1.4],
                 ["O",  1.4,  1.2]]
Substrate1Path = "./SUB1.vasp"     # rutile slab
Substrate2Path = "./SUB2.vasp"     # anatase slab
RandScheme = 1                     # 2D symmetry
InterfaceThickness = [4.0, 4.0]    # thickness of the interface region (angstrom)
InternalThickness = 0              # depth into the slabs (angstrom)
ForbiThickness = 0                 # gap kept free next to the slabs (angstrom)
InterfaceTranslation = ""          # no slab translation
TwinInterface = 0                  # single interface

[CALYPSO.OPT]
JobFlow = ["opt"]
MLPType = "chgnet"   # MLP: chgnet, m3gnet, dpa2, ...
MLPKwargs = {"model"="0.3.0", "check_cuda_mem"=false, "on_isolated_atoms"="warn"}
OptAlgo = "LBFGS"    # LBFGS, BFGS, FIRE
OptStep = 100        # maximal optimization steps
TrajFile = "traj.traj"
Pstress = 0          # GPa
Fmax = 0.01          # eV/angstrom
MLPKeepSym = false   # keep symmetry during optimization
UcfMask = [true, true, true, true, true, true]   # true: relax the cell with the interface

[CALYPSO.DISPATCHER]
MachineList = ["./machine-1.json"]
TimeInterval = 3     # seconds between job checks
TmpPath = "BackStage"

[CALYPSO.DESCRIPTOR]
SimThreshold = 0.01  # similarity threshold
```

(interface-case-2)=
### 2. Random generation with slab translation

`RandScheme = 0` with an interface thickness optimized between 4 and 5 angstrom; the upper slab is translated in the ab plane within `TranslationLimitA` / `TranslationLimitB`.

Files in `example/interface-mlp/rutile_anatanse_tio4_random_translation/`:

```text
.
├── input.toml
├── machine-1.json
├── run.calypso.sh
├── SUB1.vasp
└── SUB2.vasp
```

`SUB1.vasp` and `SUB2.vasp`: same as in [case 1](#interface-case-1).

`machine-1.json` and `run.calypso.sh`: see [common files](#interface-common-files).

`input.toml`:

```toml
[CALYPSO]
SystemName = "Rutile_Anatase_TiO4_random_translation"
Seed = -1            # positive: fixed random seed for reproducibility; negative: not set
IType = 6            # interface
ICode = 15           # MLP
IAlgo = 2            # local PSO
IFit = 1             # enthalpy
IDisp = 1            # built-in dispatcher
IRunner = 1          # run automatically
ISim = 1             # BCM similarity descriptor
BlockMode = true     # wait for the whole generation before evolving
PickUp = false       # start a new calculation

[CALYPSO.EVO]
NBest = 4
PSOratio = 0.6       # ratio of structures generated by PSO
PopSize = 5          # structures per generation
MaxStep = 2          # number of generations

[CALYPSO.GENERATOR]
FormulaUnit = ["(Ti)1(O)4"]        # atoms of the interface region
DistanceOfIon = [["X",  "Ti", "O"],
                 ["Ti", 1.5,  1.4],
                 ["O",  1.4,  1.2]]
Substrate1Path = "./SUB1.vasp"     # rutile slab
Substrate2Path = "./SUB2.vasp"     # anatase slab
RandScheme = 0                     # random generation
InterfaceThickness = [4.0, 5.0]    # thickness of the interface region (angstrom)
InternalThickness = 0              # depth into the slabs (angstrom)
ForbiThickness = 0                 # gap kept free next to the slabs (angstrom)
InterfaceTranslation = "ab"        # translate the slabs in the ab plane
TranslationLimitA = [0, 1.2]       # range along a (angstrom)
TranslationLimitB = [0.5, 1.2]     # range along b (angstrom)
TwinInterface = 0                  # single interface

[CALYPSO.OPT]
JobFlow = ["opt"]
MLPType = "chgnet"   # MLP: chgnet, m3gnet, dpa2, ...
MLPKwargs = {"model"="0.3.0", "check_cuda_mem"=false, "on_isolated_atoms"="warn"}
OptAlgo = "LBFGS"    # LBFGS, BFGS, FIRE
OptStep = 100        # maximal optimization steps
TrajFile = "traj.traj"
Pstress = 0          # GPa
Fmax = 0.01          # eV/angstrom
MLPKeepSym = false   # keep symmetry during optimization
UcfMask = [true, true, true, true, true, true]   # true: relax the cell with the interface

[CALYPSO.DISPATCHER]
MachineList = ["./machine-1.json"]
TimeInterval = 3     # seconds between job checks
TmpPath = "BackStage"

[CALYPSO.DESCRIPTOR]
SimThreshold = 0.01  # similarity threshold
```

(interface-case-3)=
### 3. Bonding constraints, inversion twin

`RandScheme = 2` grows the interface with the `CoordinateNumber` constraints; `TwinInterface = 1` builds two interfaces related by inversion.

Files in `example/interface-mlp/rutile_anatanse_tio4_bonding_constraints_inversion_twin/`:

```text
.
├── input.toml
├── machine-1.json
├── run.calypso.sh
├── SUB1.vasp
└── SUB2.vasp
```

`SUB1.vasp` and `SUB2.vasp`: same as in [case 1](#interface-case-1).

`machine-1.json` and `run.calypso.sh`: see [common files](#interface-common-files).

`input.toml`:

```toml
[CALYPSO]
SystemName = "Rutile_Anatase_TiO4_inversion_twin"
Seed = -1            # positive: fixed random seed for reproducibility; negative: not set
IType = 6            # interface
ICode = 15           # MLP
IAlgo = 2            # local PSO
IFit = 1             # enthalpy
IDisp = 1            # built-in dispatcher
IRunner = 1          # run automatically
ISim = 1             # BCM similarity descriptor
BlockMode = true     # wait for the whole generation before evolving
PickUp = false       # start a new calculation

[CALYPSO.EVO]
NBest = 4
PSOratio = 0.6       # ratio of structures generated by PSO
PopSize = 5          # structures per generation
MaxStep = 2          # number of generations

[CALYPSO.GENERATOR]
FormulaUnit = ["(Ti)1(O)4"]        # atoms of the interface region
DistanceOfIon = [["X",  "Ti", "O"],   # RandScheme = 2 generates with CoordinateNumber
                 ["Ti", 1.5,  1.4],   # (below); the PSO evolution (PSOratio > 0)
                 ["O",  1.4,  1.2]]   # needs the minimal distances
Substrate1Path = "./SUB1.vasp"     # rutile slab
Substrate2Path = "./SUB2.vasp"     # anatase slab
RandScheme = 2                     # bonding constraints
InterfaceThickness = [4.0, 4.0]    # thickness of the interface region (angstrom)
InternalThickness = 0              # depth into the slabs (angstrom)
ForbiThickness = 0                 # gap kept free next to the slabs (angstrom)
InterfaceTranslation = ""          # no slab translation
TwinInterface = 1                  # two interfaces related by inversion
CoordinateNumber = [['Ti', 'Ti', 0, 0, 2.5, 2.5],   # [center, neighbor, growth CN,
                    ['O',  'O',  0, 0, 1.8, 2.3],   #  bonding CN, d_min, d_max]
                    ['Ti', 'O',  6, 0, 1.8, 2.5],
                    ['O',  'Ti', 3, 0, 1.8, 2.5]]

[CALYPSO.OPT]
JobFlow = ["opt"]
MLPType = "chgnet"   # MLP: chgnet, m3gnet, dpa2, ...
MLPKwargs = {"model"="0.3.0", "check_cuda_mem"=false, "on_isolated_atoms"="warn"}
OptAlgo = "LBFGS"    # LBFGS, BFGS, FIRE
OptStep = 100        # maximal optimization steps
TrajFile = "traj.traj"
Pstress = 0          # GPa
Fmax = 0.01          # eV/angstrom
MLPKeepSym = false   # keep symmetry during optimization
UcfMask = [true, true, true, true, true, true]   # true: relax the cell with the interface

[CALYPSO.DISPATCHER]
MachineList = ["./machine-1.json"]
TimeInterval = 3     # seconds between job checks
TmpPath = "BackStage"

[CALYPSO.DESCRIPTOR]
SimThreshold = 0.01  # similarity threshold
```

(interface-case-4)=
### 4. Bonding constraints, mirror twin

Same as case 3 with `TwinInterface = 2` (two interfaces related by a mirror).

Files in `example/interface-mlp/rutile_anatanse_tio4_bonding_constrains_mirror_twin/`:

```text
.
├── input.toml
├── machine-1.json
├── run.calypso.sh
├── SUB1.vasp
└── SUB2.vasp
```

`SUB1.vasp` and `SUB2.vasp`: same as in [case 1](#interface-case-1).

`machine-1.json` and `run.calypso.sh`: see [common files](#interface-common-files).

`input.toml`:

```toml
[CALYPSO]
SystemName = "Rutile_Anatase_TiO4_mirror_twin"
Seed = -1            # positive: fixed random seed for reproducibility; negative: not set
IType = 6            # interface
ICode = 15           # MLP
IAlgo = 2            # local PSO
IFit = 1             # enthalpy
IDisp = 1            # built-in dispatcher
IRunner = 1          # run automatically
ISim = 1             # BCM similarity descriptor
BlockMode = true     # wait for the whole generation before evolving
PickUp = false       # start a new calculation

[CALYPSO.EVO]
NBest = 4
PSOratio = 0.6       # ratio of structures generated by PSO
PopSize = 5          # structures per generation
MaxStep = 2          # number of generations

[CALYPSO.GENERATOR]
FormulaUnit = ["(Ti)1(O)4"]        # atoms of the interface region
DistanceOfIon = [["X",  "Ti", "O"],   # RandScheme = 2 generates with CoordinateNumber
                 ["Ti", 1.5,  1.4],   # (below); the PSO evolution (PSOratio > 0)
                 ["O",  1.4,  1.2]]   # needs the minimal distances
Substrate1Path = "./SUB1.vasp"     # rutile slab
Substrate2Path = "./SUB2.vasp"     # anatase slab
RandScheme = 2                     # bonding constraints
InterfaceThickness = [4.0, 4.0]    # thickness of the interface region (angstrom)
InternalThickness = 0              # depth into the slabs (angstrom)
ForbiThickness = 0                 # gap kept free next to the slabs (angstrom)
InterfaceTranslation = ""          # no slab translation
TwinInterface = 2                  # two interfaces related by a mirror
CoordinateNumber = [['Ti', 'Ti', 0, 0, 2.5, 2.5],   # [center, neighbor, growth CN,
                    ['O',  'O',  0, 0, 1.8, 2.3],   #  bonding CN, d_min, d_max]
                    ['Ti', 'O',  6, 0, 1.8, 2.5],
                    ['O',  'Ti', 3, 0, 1.8, 2.5]]

[CALYPSO.OPT]
JobFlow = ["opt"]
MLPType = "chgnet"   # MLP: chgnet, m3gnet, dpa2, ...
MLPKwargs = {"model"="0.3.0", "check_cuda_mem"=false, "on_isolated_atoms"="warn"}
OptAlgo = "LBFGS"    # LBFGS, BFGS, FIRE
OptStep = 100        # maximal optimization steps
TrajFile = "traj.traj"
Pstress = 0          # GPa
Fmax = 0.01          # eV/angstrom
MLPKeepSym = false   # keep symmetry during optimization
UcfMask = [true, true, true, true, true, true]   # true: relax the cell with the interface

[CALYPSO.DISPATCHER]
MachineList = ["./machine-1.json"]
TimeInterval = 3     # seconds between job checks
TmpPath = "BackStage"

[CALYPSO.DESCRIPTOR]
SimThreshold = 0.01  # similarity threshold
```
