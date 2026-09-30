# Quick Start

:::{Note}
**This documentation is up-to-date with v10.1.x!**
:::

We describe here in details an example on how to run
structure prediction by CALYPSO.

Here, VASP code and MLP (CHGNET) was used for geometric structure optimization and total energy calculations.

## Preparing input file

There are two type of files calypso needed to run:

```bash
> ls
input.toml  machine.json
```
### Brief Introduction to **input.toml**

The input file of CALYPSO is named as **input.toml**, one can find more information about toml in [this website](https://toml.io/cn/). Here is an example of input file:

```toml
# Template CALYPSO config
# The key is case-insensitive

[CALYPSO]
SystemName = "Crystal-MLP CALYPSO config"
Seed = -1
IType = 1
ICode = 15
IAlgo = 2
IFit = 1
IDisp = 1

IRunner = 1

ISim = 1
BlockMode = true
PickUp = false

[CALYPSO.EVO]
NBest = 4
PSOratio = 0.4
PopSize = 4
MaxStep = 2

[CALYPSO.GENERATOR]
FormulaUnit = ["(LiH4)1-2(NH3)1-2",]
VolumeUnit = {Li=10, H=10, N=10}
DistanceOfIon = [["X",  "B", "O", "Mg"],
                 ["B",  1.0, 1.0,  1.0],
                 ["O",  1.0, 1.0,  1.0],
                 ["Mg", 1.0, 1.0,  1.0],]
SpaceGroup = ["2-230"]

[CALYPSO.OPT]
DFTInputPath = "."
JobFlow = ["opt"]

MLPType = "chgnet"
MLPKwargs = {"model"="0.3.0", "check_cuda_mem"=true, "on_isolated_atoms"="warn"}

OptAlgo = "LBFGS"
OptStep = 10
TrajFile = "traj.traj"
Pstress = 0.0001
Fmax = 0.1

[CALYPSO.DISPATCHER]
MachineList = ["./machine-1.json", "./machine-2.json"]
TimeInterval = 3

[CALYPSO.DESCRIPTOR]
SimThreshold = 0.1
```

The parameters have been divided into different parts according to its functionality.

#### Part 1. CALYPSO

The first part is *CALYPSO*. All the basic setting of CALYPSO are defined here. 

In this example, we set

- `SystemName = "Crystal-MLP CALYPSO config"` is a comment line, just leave something for you.
- `Seed = -1` for controlling whether the calculation is reproducible, the minus value is not reproducible.
- `IType = 1` for crystal structure prediction.
- `ICode = 15` for choosing MLP as the calculator to evaluate total energy of given structures.
- `IAlgo = 2` for choosing LPSO as evolution algorithm.
- `IFit = 1` for choosing ENTHALPY as the fitness.
- `IDisp = 1` for choosing build-in dispatcher for dispatching jobs.
- `IRunner = 1` for choosing normal mode or split mode.
- `ISim = 1` for choosing BCM as structure fingerprint.
- `BlockMode = true` for population-based mode.
   We will release the *computational-pool-based* mode in very next release.
- `PickUp = false` for starting a new calculation.
   *Different from the past, calypso now can pick up the calculation without any other setting but only this key.*

#### Part 2. EVO

The parameters defined in `EVO` is mean to control the evolution-related settings.

In this example, we set
- `NBest = 4` for controlling the number of Pbest structure in PES. The default setting is enough.
- `PSOratio = 0.4` for deciding the percentage of the structures of PSO-generated structures in `popsize` of one population.
- `PopSize = 4` for controlling the number of structures in one population/step.
- `MaxStep = 2` for controlling the maximum number of generations to be executed for the entire structure prediction simulation.

#### Part 3. GENERATOR

In this part, the parameters will control how to generate structures in detail.

- `FormulaUnit = ["(LiH4)1-2(NH3)1-2",]` for predicting Li-N-H compound which contains $LiH_4$ unit in the range of 1 to 2 and $NH_3$ unit in the range. This is much more flexible than before.
- `VolumeUnit = {Li=10, H=10, N=10}` represents for the volume per atom of each element.
- `DistanceOfIon = [["X",  "B", "O", "Mg"], ["B",  1.0, 1.0,  1.0], ["O",  1.0, 1.0,  1.0], ["Mg", 1.0, 1.0,  1.0],]` represents for the minimum distance constrain. One can also leave these parameters when focusing on other chemical system because CALYPSO will automatically give a reasonable estimated value (basically using covalent radius).
- `SpaceGroup = ["2-230]` denotes the possible range of space group number.


#### Part 4. OPT

The `OPT` part is designed to control the calculator. Now the supported calculator includes VASP and MLPs (CHGNET, M3GNET, DP, DPA2).

- `DFTInputPath = "."` the path for providing the necessary input files.
- `JobFlow = ["opt"]` for defining the work flow of each structure, one opt is enough when using mlp, and VASP can be ["opt", "opt", "opt", "scf"]
- `MLPType = "chgnet"` for choosing the type of MLP. Now we support chgnet, m3gnet, dp, dpa2
- `MLPKwargs = {"model"="0.3.0", "check_cuda_mem"=true, "on_isolated_atoms"="warn"}` for defining the MLP parameters.
- `OptAlgo = "LBFGS"` for defining the optimization algo when using mlp.
- `OptStep = 10` for constraint the opt step when using mlp.
- `TrajFile = "traj.traj"` for save the trajectory when using mlp.
- `Pstress = 0.001` for constraint the pressure in GPa when using mlp.
- `Fmax = 0.1` to determine the convergence criteria when using mlp.

#### Part 5. DISPATCHER

`DISPATCHER` part is designed to command the job with computational resources, which can also be utilized itself.

- `MachineList = ["./machine-1.json", "./machine-2.json"]` to define the computational resources. In this example, we have two resources, we can consider them as two queue or two machine.
- `TimeInterval = 3` to determine how often dispatcher will update the job state.

#### Part 6. DESCRIPTOR

`DESCRIPTOR` part is designed to control the type of descriptor.
- `SimThreshold = 0.1` to distinguish if two structures are similar. BCM and CCF are support. Default is BCM.

For more specific explanation, please reference to `Input Parameters` part.

### reference entries for calculating convexhull

In the process of structure evolution, the structure will be sorted by fitness. If fitness is **ENTHALPY** and the **ref_ene.txt** exists, the energy (enthalpy) above hull will be calculated and the top `PSOratio` percent of structure will be considered as parent to evolute the next generation structures.

Also, when analyzing the results, **ref_ene.txt** is needed to calculated energy (enthalpy) above hull.

One can simply provide a fake reference entries with fake energy if you don't have it.

For example:

```bash
formula enthalpy_per_atom label
Li 0 element_Li
N 0 element_N
H 0 element_H
```

### machine file

```bash
{
    "name": "6123",

    # only for ssh
    "host": "xxx.xxx.xxx.xxx",
    "port": xxx,
    "username": "USERNAME",
    "password": null,  # null or "PASSWORD"
    "key_filename": "IDENTITY_FILENAME",  # identity filename if password null, example: /home/<USERNAME>/.ssh/id_rsa

    # define the computation resources
    "numb_cpu_per_node": 64,
    "numb_node": 1,
    "max_run_time": 10,  # time limit for each job.

    # define how to reach the machine
    "executor": "SSH",  # need ssh, we can set it local.
    "scheduler": "shell",  # consider it as a local worker station such as 6123 or 6022 or inside the node. We also support slurm, lsf.
    "scheduler_envs": [],  # only for lsf, ignore for other type.

    # to control where to conduct the calculation, null means in results/opt_task/*/
    "remote_root": "/home/wangzy/tmp/mlp",

    "machine_capacity": 5,  # max job number, only can be submitted or queued below this number.
    "group_size": 1,  # how many jobs are put in one submission and they will share the computational resources defined in upside.
    "envs": [
        "export PATH=xxx",
        "source /opt/intel/oneapi/setvars.sh --force >> env",
        "module load xxx",
        "export CALYPSO_MLP_CMD='/home/wangzy/soft/anaconda3/envs/chgnet/bin/python'"
    ],
    "additional_head_settings": ["#SLURM --nodelist=[a11]"],    # only for slurm or lsf.
    "queue": null  # only for slurm or lsf.
}
```

## Submit CALYPSO job

Since we have abstract the dispatcher (we called it Orchestrator, shorted as orch.) into a separate tool which can reaches the different mode by combinations of `executor` and `scheduler`.

| num  | executor  | scheduler | meaning                                           |
|------|-----------|-----------|---------------------------------------------------|
| 1    | ssh       | shell     | send jobs to another machine by ssh               |
| 2    | ssh       | slurm     | send jobs to another cluster with slurm system    |
| 3    | ssh       | lsf       | send jobs to another cluster with lsf system      |
| 4    | local     | shell     | running jobs in current local machine             |
| 5    | local     | slurm     | running jobs in current cluster with slurm system |
| 6    | local     | lsf       | running jobs in current cluster with lsf system   |

### How to submit CALYPSO job in workstation

In workstation, you can let calculation start in this current workstation `executor = local` and `scheduler = shell` or you can send task to other reachable machine through orch by setting `executor = ssh` and `scheduler = slurm`.

After setting these parameters, you can submit job by following scripts:

```bash
conda activate calypso
nohup calypso.x > caly.log 2>&1 &
```

If you submit several calypso jobs, you can use this script to recognize where the calypso jobs belong.

```bash
#!/bin/bash

printf "%s               %20s               %20s   \n" name PID work_path
for i in `ps aux | grep calypso.x | grep -v grep | awk '{print $2}'`
do
        work_path=$(pwdx $i)
        work_path=`echo ${work_path} | cut -d ':' -f 2`
        # echo -e "$i               ${work_path}        calypso.x"
        printf "%-20s               %-3d               %-30s   \n" calypso.x ${i} ${work_path} 
done

for i in `ps aux | grep calypso.x | grep -v grep | awk '{print $2}'`
do
        work_path=$(pwdx $i)
        work_path=`echo ${work_path} | cut -d ':' -f 2`
        # echo -e "$i               $work_path        calypso.x"
        printf "%-20s               %-3d               %-30s   \n" calypso.x ${i} ${work_path} 
done
```

### How to submit CALYPSO job in cluster

In cluster, we can submit CALYPSO job by setting `executor = local` and `scheduler = slurm` to submit jobs, but you may also find that we have to submit task into main node.

There is a way to avoid submitting calypso.x into main node: put calypso.x into a slurm submit script and change `executor = local` and `scheduler = shell`.

By doing this, you will lose the chance to use plenty of computational resources but only can use what you have apply.

Here is the example of submitting calypso into compute node (it's not recommend):

```bash
> cat run.sh
#!/bin/sh
#SBATCH  --job-name=pythontest
#SBATCH  --partition=wyc
#SBATCH  --nodes=1
#SBATCH  --ntasks=48
#SBATCH  --ntasks-per-node=48
#SBATCH  --exclusive

ulimit -s unlimited
ulimit -u unlimited

export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1

source /work/env/oneapi-2022.2.0

source /work/home/wangzhy/soft/anaconda3/bin/activate /work/home/wangzhy/soft/anaconda3/envs/calypso

calypso.x > caly.log 2>&1
```

after preparing the environment and input files, one can submit calypso job by 

```bash
sbatch run.sh
```

## Analysis Results

When CALYPSO is running, the *results* directory contains the following files / directories:

```bash
> cd results
> ls *
calydatabase.db  descriptor.pkl  ini.json  opt.json

opt_task:
0  1  10  11  12  13  14  15  16  17  18  19  2  20  21  22  23  24  25  26  27  28  29  3  30  31  32  33  34  35  36  37  38  39  4  5  6  7  8  9
```
- **database.db**: the process of CALYPSO is stored in this db file.
- **descriptor.pkl**: the descriptor file containing the fingerprint of all structures.
- **ini.json**: all initial structures are stored in this file.
- **opt.json**: all optimized structures are stored in this file.
- **opt_task**: all optimization tasks are stored in this directory.

When the first generation is done, one can go into the *results* directory to analysis the results by:

One can obtain POSCAR in specific tolerance by

```bash
> pycak --vasp -m 0.1 0.3
> tree .
.
├── Analysis_Output.csv
├── database.db
├── caly_structs.0.1
│   ├── UCell.0.caly_1.vasp
│   ├── UCell.1.caly_2.vasp
│   ├── UCell.2.caly_0.vasp
│   └── UCell.3.caly_3.vasp
├── caly_structs.0.3
│   ├── UCell.0.caly_1.vasp
│   ├── UCell.1.caly_2.vasp
│   ├── UCell.2.caly_0.vasp
│   └── UCell.3.caly_3.vasp
├── descriptor.pkl
├── ini.json
├── opt.json
└── opt_task
    ├── 0
    │   ├── caly_ini.xyz
    │   ├── caly_opt.pkl
    │   ├── calypso_check_mlp.py
    │   ├── calypso_run_mlp.py
    │   ├── command
    │   ├── err
    │   ├── gentype
    │   ├── out
    │   └── traj.traj
    ├── 1
    │   ├── caly_ini.xyz
    │   ├── caly_opt.pkl
    │   ├── calypso_check_mlp.py
    │   ├── calypso_run_mlp.py
    │   ├── command
    │   ├── err
    │   ├── gentype
    │   ├── out
    │   └── traj.traj
    ├── 2
    │   ├── caly_ini.xyz
    │   ├── caly_opt.pkl
    │   ├── calypso_check_mlp.py
    │   ├── calypso_run_mlp.py
    │   ├── command
    │   ├── err
    │   ├── gentype
    │   ├── out
    │   └── traj.traj
    ├── 3
    │   ├── caly_ini.xyz
    │   ├── caly_opt.pkl
    │   ├── calypso_check_mlp.py
    │   ├── calypso_run_mlp.py
    │   ├── command
    │   ├── err
    │   ├── gentype
    │   ├── out
    │   └── traj.traj
    ├── 4
    │   ├── caly_ini.xyz
    │   ├── caly_opt.pkl
    │   ├── calypso_check_mlp.py
    │   ├── calypso_run_mlp.py
    │   ├── command
    │   ├── err
    │   ├── gentype
    │   ├── out
    │   └── traj.traj
    ├── 5
    │   ├── caly_ini.xyz
    │   ├── caly_opt.pkl
    │   ├── calypso_check_mlp.py
    │   ├── calypso_run_mlp.py
    │   ├── command
    │   ├── err
    │   ├── gentype
    │   └── out
    └── 6
        ├── caly_ini.xyz
        ├── caly_opt.pkl
        ├── calypso_check_mlp.py
        ├── calypso_run_mlp.py
        ├── command
        ├── err
        ├── gentype
        ├── out
        └── traj.traj
```

The enthalpy of each structure are stored in **Analysis_Output.csv**

```bash
> cat Analysis_Output.csv
 idx   caly_name      formula       enth_per_atom   enth_above_hull   volume_per_atom   density   min_dis  spg(0.1)  spgnum(0.1) natom(0.1) spg(0.3)  spgnum(0.3) natom(0.3)
  0    caly_1         H14Li2N2         -0.594            1.401             6.846         8.181     0.839   P6/mmm        191         9     P6/mmm        191         9     
  1    caly_2         H7Li1N1           0.045            1.515             8.536         3.281     1.598   P6/mmm        191         9     P6/mmm        191         9     
  2    caly_0         H14Li2N2          0.511            1.585             9.695         5.777     1.722   F-43m         216         72    F-43m         216         72    
  3    caly_3         H14Li2N2          1.131            1.688            11.007         5.088     1.338   Pnnn           48         18    Pnnn           48         18 
```
