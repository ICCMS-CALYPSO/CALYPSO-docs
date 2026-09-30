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
