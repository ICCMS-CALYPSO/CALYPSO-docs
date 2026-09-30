# Examples

- [Examples](#examples)
  - [Crystal Structure Prediction](#crystal-structure-prediction)
  - [Two-Dimensional Structure Prediction](#two-dimensional-structure-prediction)
  - [Cluster Structure Prediction](#cluster-structure-prediction)
    - [Tutorial for B6 clusters](#tutorial-for-b6-clusters)
    - [Tutorial for Ti4 clusters](#tutorial-for-ti4-clusters)
    - [Tutorial for B12 clusters](#tutorial-for-b12-clusters)
  - [Molecular Structure Prediction](#molecular-structure-prediction)
  - [Variable Stoichiometry Structure Prediction](#variable-stoichiometry-structure-prediction)
  - [Surface Structure Prediction](#surface-structure-prediction)
    - [Diamond (111) surface reconstruction prediction](#diamond-111-surface-reconstruction-prediction)
    - [Hydrogenated diamond (100) surface reconstruction](#hydrogenated-diamond-100-surface-reconstruction)
    - [Crystal lattice matches of two graphene](#crystal-lattice-matches-of-two-graphene)
    - [Interface structure prediction of SIGMA5(210) grain boundary of rutile TiO2](#interface-structure-prediction-of-sigma5210-grain-boundary-of-rutile-tio2)
  - [Design of Superhard Materials](#design-of-superhard-materials)
  - [Structure prediction of atom or molecule adsorption of 2D layer material](#structure-prediction-of-atom-or-molecule-adsorption-of-2d-layer-material)
  - [Design of Optical Materials with Desirable Electronic Band Gap](#design-of-optical-materials-with-desirable-electronic-band-gap)
  - [Crystal Structure Prediction with Fixed Cell Parameters or Atomic Positions](#crystal-structure-prediction-with-fixed-cell-parameters-or-atomic-positions)
  - [Structural Prediction via X-ray Diffraction Data](#structural-prediction-via-x-ray-diffraction-data)
  - [Prediction of Transition States in Solids](#prediction-of-transition-states-in-solids)
  - [Accelerating Structure Prediction by Machine Learning Potentials (MLP)](#accelerating-structure-prediction-by-machine-learning-potentials-mlp)
    - [Constructing training (and testing) data set](#constructing-training-and-testing-data-set)
    - [Fitting MLP](#fitting-mlp)
    - [Structure prediction assisted by MLP](#structure-prediction-assisted-by-mlp)

:::{warning}
**KGrid** parameter is no longer taking effect in **`input.dat`**, and removed from all
following examples. You should specify it according to the different local optimization software.

Taking VASP for example, set **KSPACING** in **`INCAR`**, or give **`KPOINTS`** file.
:::

## Crystal Structure Prediction

This section is to show the examples for the three-dimensional crystal structure
prediction using CALYPSO code.

We take the structure prediction of cubic boron nitride (cBN) as an example.
Here, VASP code was used for geometry optimization and enthalpy calculations.

CALYPSO input file **`input.dat`** and VASP input files of **`INCAR_*`** and
pseudopotential file of **`POTCAR`** are needed.

The following files should be present in the working directory:

| **Files** | **Description**                                                  |
|-----------|------------------------------------------------------------------|
| calypso.x | The executable file for running CALYPSO program                  |
| input.dat | The input file of CALYPSO containing controllable key parameters |
| INCAR_*   | Input files for VASP                                             |
| POTCAR    | Pseudopotential file for VASP                                    |
| submit.sh | Job submission file                                              |

**`calypso.x`** can be downloaded in the webpage of <http://www.calypso.cn>
according to different operating systems.

Parameters in **input.dat** are shown below:

```text
SystemName = BN
NumberOfSpecies = 2
NameOfAtoms = B N
NumberOfAtoms = 1 1
NumberOfFormula = 1 1
Volume = 20.0
@DistanceOfIon
1.0 0.8
0.8 0.8
@End
Ialgo = 2
PsoRatio = 0.6
PopSize = 30
ICode = 1
NumberOfLocalOptim = 4
Kgrid = 0.12 0.06
Command = sh submit.sh
MaxStep = 30
```

For VASP, the number of **`INCAR_*`** (INCAR_1, INCAR_2, ...) files should be in
accordance with the setting tag **`NumberOfLocalOptim`**.

In this example, four INCAR files are used for structure relaxation:

**INCAR_1** and **INCAR_2** files are used to perform very coarse structure relaxation with
the fixed volume, and **INCAR_3** and **INCAR_4** files are used to perform full structure
relaxation (i.e., variable lattice parameters, variable volumes, and variable atomic
coordinates) with medium and accurate precision, respectively.

> INCAR_1

```text
SYSTEM = local optimization
PREC = LOW
EDIFF = 3e-2
IBRION = 2
ISIF = 2
NSW = 40
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.5
LWAVE = FALSE
LCHARG = FALSE
ISTART = 0
PSTRESS = 3000
EDIFFG = -4e-2
```

> INCAR_2

```text
SYSTEM = local optimization
PREC = Normal
EDIFF = 2e-2
IBRION = 2
ISIF = 4
NSW = 40
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.2
LWAVE = FALSE
LCHARG = FALSE
PSTRESS = 3000
EDIFFG = -4e-1
```

> INCAR_3

```text
SYSTEM = local optimization
PREC = Normal
EDIFF = 2e-4
IBRION = 1
ISIF = 3
NSW = 40
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.1
LWAVE = FALSE
LCHARG = FALSE
PSTRESS = 3000
EDIFFG = 2e-3
```

> INCAR_4

```text
SYSTEM = local optimization
ENCUT = 600
EDIFF = 1e-5
IBRION = 2
ISIF = 3
NSW = 80
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.1
LWAVE = FALSE
LCHARG = FALSE
PSTRESS = 3000
EDIFFG = 2e-3
```

:::{hint}
Multi-optimization strategy for structure relaxation is strongly suggested
:::

**`POTCAR`** should be provided.

:::{important}
**ATTENTION!!!** The order of elements in POTCAR must be identical to the element order
in the setting tag of **NameOfAtoms**.
:::

**`submit.sh`** is the job submission file for the VASP calculations.
Here is an example of *submit.sh*:

```bash
#!/bin/bash
mpdboot
mpiexec -n 12 vasp_std > vasp.log 2>&1
```

For using VASP software to optimize generated structures, CALYPSO supports accelerating structure search by modifying submit.sh file in Version 7.3.6. Here are the examples of *submit.sh*.

```bash
#!/bin/sh
nohup  ./badopt.py &> badopt.log &
for(( i=1; i<=3; i++ ));
do
        cp INCAR_$i INCAR
        if [[ "$i" == "3" ]]
        then
          sg=`./sym.py`
        fi
        if [[ "$sg" == "1" ||  "$sg" == "610612509" ]]
        then
          break
        fi
        if [[ "$i" == "3" ]]
        then
          nohup ./sym_split.py &> sym.log &
        fi
        killall -9 vasp_std
        mpirun -np 36  /data/software/vasp.5.4.1/bin/vasp_std > vasp.log_$i
        cp CONTCAR POSCAR
done
killall -9 python
```

Three scripts (badopt.py, sym.py and sym_split.py) are used to accelerate structure search. 

badopt.py: check the error information during VASP structure optimization.

sym.py: check the space group of the structures after VASP structure optimization with low precision. If the space group is P1, the last structure optimization with high precision will be not carried out.

sym_split.py: check the space group of the structures during VASP structure optimization with high precision. If the space group is P1, the structure optimization will stop.

Users can choose any one of three scripts by according to own requirements. For using this submit.sh file to accelerate structure search, “NumberOfLocalOptim” in the input.dat file should be set as “1”. It's required to install numpy for your python environment. 

The following is the script to run structure optimizations using VASP for accelerate structure search using CALYPSO split mode:

```bash
#!/bin/sh
#BSUB -n 36
#BSUB -R 'span[ptile=36]'
#BSUB -q mym4
#BSUB -o %J.out

cp ../badopt.py .
nohup  ./badopt.py &> badopt.log &
for(( i=1; i<=3; i++ ));
do
        cp INCAR_$i INCAR
        cp CONTCAR POSCAR
        if [[ "$sg" == "1" ||  "$sg" == "610612509" ]]
        then
          cp ../sym.py .
          sg=`./sym.py`
        fi
        if [[ "$sg" == "1" ]]
        then
          break
        fi
        if [[ "$i" == "3" ]]
        then
          cp ../sym_split.py .
          nohup ./sym_split.py &> sym.log &
        fi
        killall -9 vasp_std
        mpirun -np 36  /data/software/vasp.5.4.1/bin/vasp_std > vasp.log_$i
done
killall -9 python
```

Once all input files are ready, you can simply type

```bash
./calypso.x > caly.log &
```

to execute the CALYPSO in the sequential mode.
Or you can write this command into the *pbs* script and submit it in a queue system.

CALYPSO run will generate the **`results`** folder in the current directory you have specified.
The *results* folder contains all the outputs files of CALYPSO.

To analyze the results, please simply type the following commands:

```bash
cd results
cak.py --cif
```

The index of the structures sorted by enthalpies in the ascending order will present in
the **`Analysis_Output.dat`** file, and all predicted structure files by CALYPSO with
cif formats are shown in the **`dir_0.1`** directory.

Please see [here](./_manuals.md#analysis-of-results) for more information about the analyses of CALYPSO results.

## Two-Dimensional Structure Prediction

This section is to show the examples for the two-dimensional structure prediction using CALYPSO code.

We take the structure prediction of B{sub}`3`N{sub}`2` two-dimensional system as an example.
Here, VASP code was used for geometry optimization and enthalpy calculations.

CALYPSO input file of **`input.dat`** and VASP input files of **`INCAR_*`** and
pseudopotential file of **`POTCAR`** are needed.

The following files should be present in the working directory:

| Files     | Description                                                      |
|-----------|------------------------------------------------------------------|
| calypso.x | The executable file for running CALYPSO program                  |
| input.dat | The input file of CALYPSO containing controllable key parameters |
| INCAR_*   | Input files for VASP                                             |
| POTCAR    | Pseudopotential for VASP                                         |
| submit.sh | Job submission file                                              |

**`calypso.x`** can be downloaded according to different operating systems.

Parameters in **input.dat** are shown below:

```text
SystemName = B3N2
NumberOfSpecies = 2
NameOfAtoms = B N
NumberOfAtoms = 3 2
Ialgo = 2
PsoRatio = 0.6
PopSize = 20
ICode = 1
NumberOfLocalOptim = 3
Command = sh submit.sh
MaxStep = 50
2D = T
MultiLayer = 2
Area = 14
DeltaZ = 0
LayerGap = 5
VacuumGap = 5
@LayerType
1 1
2 1
@End
LAtom_Dis = 1.4
```

For VASP, the number of **`INCAR_*`** (INCAR_1, INCAR_2, ...) files should be in
accordance with the setting tag **`NumberOfLocalOptim`**.

In this example, we use three INCAR files for structure relaxation.
**INCAR_1** and **INCAR_2** are used to perform very coarse structure relaxation keeping the volume fixed,
**INCAR_3** is used to** perform full structure relaxation with accurate precision.

> INCAR_1

```text
SYSTEM = B3N2
PREC = LOW
EDIFF = 3e-3
IBRION = 2
ISIF = 2
NSW = 50
ISMEAR = 1 ; SIGMA = 0.2
POTIM = 0.5
LWAVE = FALSE
LCHARG = FALSE
PSTRESS = 0.001
EDIFFG = 4e-2
```

> INCAR_2

```text
SYSTEM = B3N2
PREC = LOW
EDIFF = 2e-3
IBRION = 2
ISIF = 4
NSW = 50
ISMEAR = 1 ; SIGMA = 0.2
POTIM = 0.2
LWAVE = FALSE
LCHARG = FALSE
PSTRESS = 0.001
EDIFFG = 1e-2
```

> INCAR_3

```text
SYSTEM = B3N2
PREC = Accurate
ENCUT = 400
EDIFF = 2e-4
IBRION = 2
ISIF = 3
NSW = 60
ISMEAR = 1 ; SIGMA = 0.2
POTIM = 0.1
LWAVE = FALSE
LCHARG = FALSE
PSTRESS = 0.001
EDIFFG = 1e-4
```

:::{hint}
Multi-optimization strategy for structure relaxation is strongly suggested
:::

**`POTCAR`** should be provided.

:::{important}
**ATTENTION!!!** The order of elements in POTCAR must be identical to the element order
in the setting tag of **NameOfAtoms**.
:::

**`submit.sh`** is the job submission file for performing the VASP calculations.
Here is an example of *submit.sh*:

```bash
#!/bin/bash
mpdboot
mpiexec -n 12 vasp_std > vasp.log 2>&1
```

Once all input files are ready, you can just type

```bash
./calypso.x > caly.log &
```

to execute the CALYPSO in the sequential mode.
Or you can write this command into the *pbs* script and submit it.

CALYPSO will generate the **`results`** folder, which contains all outputs files.
To analyze the results of CALYPSO, just type following command:

```bash
cd results
cak.py --cif
```

The index of the structures sorted by enthalpies in the ascending order is presented in
**`Analysis_Output.dat`** file, and these newly predicted structure files with cif
format are shown in **`dir_0.1`** directory.

Please see [here](./_manuals.md#analysis-of-results) for more information about the analyses of CALYPSO results.

## Cluster Structure Prediction

This section is to show the examples for the cluster structure prediction using CALYPSO code.

[Here](#tutorial-for-b6-clusters) an example for boron clusters that composed of 6 atoms
(B{sub}`6`) is presented. Gaussian09 code was used for geometry optimization and energy calculations.

[Here](#tutorial-for-ti4-clusters) an example for Ti{sub}`4` clusters is given, and
the local optimization is performed by VASP.

Finally, [here](#tutorial-for-b12-clusters) an example for B{sub}`12` clusters is provided.
The CP2K code was used for geometry optimization and energy calculations.

### Tutorial for B6 clusters

In this tutorial, a CALYPSO structure search for B{sub}`6` clusters is presented.
The local structure optimizations are performed by Gaussian09 code,
so you have to install the Gaussian09 in your machine.

The following files should be present in the working directory:

| Files     | Description                                                      |
|-----------|------------------------------------------------------------------|
| calypso.x | The executable file for running CALYPSO program                  |
| input.dat | The input file of CALYPSO containing controllable key parameters |
| gsinput_* | Input files for Gaussian                                         |
| submit.sh | Job submission file                                              |

**`calypso.x`** can be downloaded according to different operating systems.

Parameters in **`input.dat`** are shown below:

```text
SystemName = B6Cluster
NumberOfSpecies = 1
NameOfAtoms = B
NumberOfAtoms = 6
NumberOfFormula = 1 1
@DistanceOfIon
1.7
@End
Ialgo = 2
PsoRatio = 0.8
PopSize = 20
ICode = 7
NumberOfLocalOptim = 2
Command = sh submit.sh
MaxStep = 50
LMC = T
Cluster= T
Vacancy = 15 15 15
```

For Gaussian, the number of **`gsinput_*`** (gsinput_1 and gsinput_2) should be in
accordance with the setting tag **`NumberOfLocalOptim`**.

In this example, we use two **gsinput_\*** files for structure relaxation.
The **gsinput_1** is used to perform very coarse structure relaxation,
and **gsinput_2** is used to perform structure relaxation with medium precision.
During the structure relaxation, **gsinput_\*** files will be copied to **gsinput**,
and atomic coordinates will be automatically attached by CALYPSO.

> gsinput_1

```text
%chk=calypso.chk
%nprocs=12
%Mem=12GB
#p RHF/PBEPBE/3-21G
SCF=(fermi,MaxCycle=565,conver=4)
OPT=(Redundant,MaxCycle=50,MaxStep=29,loose)
NoSymm

dr38 Geometry Optimization

0 1

```

> gsinput_2

```text
%chk=calypso.chk
%nprocs=12
%Mem=12GB
#p RHF/PBEPBE/3-21G
SCF=(xqc,MaxCycle=565,conver=5)
OPT=(Redundant,MaxCycle=1500,MaxStep=29,loose)
NoSymm

dr38 Geometry Optimization

0 1

```

:::{hint}
We strongly suggest that you use the multi-stage strategy for structure relaxation.
:::

**`submit.sh`** is the job submission file for the Gaussian calculation:

Here is an example of **submit.sh**:

```bash
#!/bin/bash
g09 < gsinput > gsoutput
```

Once all the input files are ready, you can just type

```bash
./calypso.x > caly.log &
```

to execute the CALYPSO in the sequential mode.
Or you can write this command into the *pbs* script and submit it.

CALYPSO will generate the **`results`** folder, which contains all most the output files.

To analyze the results, just type following command:

```bash
cd results
cak.py –cif
```

The index of the structures sorted by energies in the ascending order is presented in
**`Analysis_Output.dat`** file, and these newly predicted structure files with cif
format are shown in **`dir_origin`** directory.

Please see [here](./_manuals.md#analysis-of-results) for more information about the analyses of CALYPSO results.

### Tutorial for Ti4 clusters

In this tutorial, a CALYPSO structure search for Ti{sub}`4` clusters is presented.
The local structural optimizations are performed by VASP,
so you have to install the VASP code in your machine.

All the reference files can be found in **Path-to-CALYPSO/Example/Ti4_VASP**.

The following files should be present in the working directory:

| Files     |                           Description                            |
|:----------|:----------------------------------------------------------------:|
| calypso.x |         The executable file for running CALYPSO program          |
| input.dat | The input file of CALYPSO containing controllable key parameters |
| INCAR_*   |                       Input files for VASP                       |
| POTCAR    |                     Pseudopotential for VASP                     |
| submit.sh |                       Job submission file                        |

**`calypso.x`** can be downloaded according to different operating systems.

Parameters in **`input.dat`** are shown below:

```text
SystemName Ti
NumberOfSpecies = 1
NameOfAtoms = Ti
NumberOfAtoms = 4
NumberOfFormula = 1 1
@DistanceOfIon
2.6
@End
Ialgo = 2
PsoRatio = 0.8
ICode = 1
NumberOfLocalOptim = 1
Command = sh submit.sh
MaxStep = 50
LMC = T
Cluster = T
Vacancy = 12 12 12
```

In this example, geometry optimization is performed by VASP code and only one input file
for VASP (named **`INCAR_1`**) is needed.

> INCAR_1

```text
SYSTEM = Ti
PREC = Accurate
ENCUT = 300
EDIFF = 1e-4
IBRION = 2
ISIF = 2
NSW = 1000
ISMEAR = 0 ; SIGMA = 0.0001
POTIM = 0.1
LWAVE = FALSE
LCHARG = FALSE
EDIFFG = -0.01
ISPIN = 2
ISYM = 0
```

**`POTCAR`** should be provided.

**`submit.sh`** is the job submission file for performing the VASP calculations.
Here is an example of *submit.sh*:

```bash
#!/bin/bash
mpdboot
mpiexec -n 12 vasp_std > vasp.log 2>&1
```

Once all the input files are ready, you can just type

```bash
./calypso.x > caly.log &
```

to execute the CALYPSO in the sequential mode.
Or you can write this command into the *pbs* script and submit it.

CALYPSO will generate the “**results**” folder, which contains all most the output files.
To analyze the CALYPSO results, just type following command:

```bash
cd results
cak.py --cif
```

The index of the structures sorted by energies in the ascending order is presented in
**`Analysis_Output.dat`** file, and these newly predicted structure files with cif
format are shown in **`dir_0.1`** directory.

Please see [here](./_manuals.md#analysis-of-results) for more information about the analyses of CALYPSO results.

### Tutorial for B12 clusters

In this tutorial, a CALYPSO structure search for B{sub}`12` clusters is presented.
The local structural optimizations are performed by CP2K,
so you have to install the CP2K code in your machine.

All the reference files can be found in **Path-to-CALYPSO/Example/B12_cp2k**.

The following files should be present in the working directory:

| Files             |                           Description                            |
|:------------------|:----------------------------------------------------------------:|
| calypso.x         |         The executable file for running CALYPSO program          |
| EMSL\_BASIS\_SETS |                    Basis sets files for CP2K                     |
| POTENTIAL         |                  Pseudopotential files for CP2K                  |
| input.dat         | The input file of CALYPSO containing controllable key parameters |
| cp2k.inp\_\*      |                       Input files for CP2K                       |
| submit.sh         |                       Job submission file                        |

The **calypso.x** can be downloaded according to different operating system.

Parameters in **`input.dat`** are shown for the B{sub}`12` cluster:

```text
SystemName = B
NumberOfSpecies = 1
NameOfAtoms = B
NumberOfFormula = 1 1
@DistanceOfIon
1.7
@End
Ialgo = 2
PsoRatio = 0.8
PopSize = 30
ICode = 6
NumberOfLocalOptim = 1
Command = sh submit.sh
MaxStep = 50
LMC = T
Cluster = T
Vacancy = 12 12 12
```

In this example, geometry optimization is performed by CP2K code and only one input
file for CP2K (named as **`cp2k.inp_1`**) is needed.
During the structure relaxation, it will be renamed as **cp2k.inp**,
and atomic coordinates will be automatically inserted into this file (behind the marker line “########”).

> cp2k.inp_1

```text
&FORCE_EVAL
  METHOD QS
  &DFT
    BASIS_SET_FILE_NAME EMSL_BASIS_SETS
    POTENTIAL_FILE_NAME POTENTIAL
    &MGRID
      CUTOFF 250
      REL_CUTOFF 50
    &END MGRID
        &QS
      EPS_DEFAULT 1.0E-10

        &END QS
    &POISSON
        PSOLVER MT
    &END POISSON
    &SCF
      SCF_GUESS ATOMIC
      &OT ON
        MINIMIZER DIIS
      &END OT
      MAX_SCF 100
      EPS_SCF 1.0E-5
      &PRINT
        &RESTART OFF
        &END
      &END
    &END SCF
    &XC
      &XC_FUNCTIONAL PBE
      &END XC_FUNCTIONAL
    &END XC
  &END DFT
  &SUBSYS
########
    &KIND B
      BASIS_SET 6-311Gxx
      POTENTIAL GTH-PBE-q3
    &END KIND
  &END SUBSYS
&END FORCE_EVAL
&GLOBAL
  PROJECT cp2k
  RUN_TYPE GEOMETRY_OPTIMIZATION
  PRINT_LEVEL LOW
  &TIMINGS
    THRESHOLD 0.000001
  &END
&END GLOBAL
&MOTION
  &GEO_OPT
    OPTIMIZER BFGS
    MAX_ITER  1000
    MAX_FORCE 0.00045
    RMS_FORCE 0.0003
  &END GEO_OPT
&END MOTION
```

The users should provide the **`EMSL_BASIS_SETS`** and **`POTENTIAL`** files,
which contain the basis set and pseudopotential for running CP2K code.

**`submit.sh`** is the job submission file for performing the CP2K calculations.
Here is an example of submit.sh:

```bash
#!/bin/bash
mpirun.lsf cp2k.popt -i cp2k.inp > out.cp2k 2>&1
```

Once all the input files are ready, you can just type

```bash
./calypso.x > caly.log &
```

to execute the code in the sequential mode.
Or you can write this command into the *pbs* script and submit it.

CALYPSO will generate the “**results**” folder in current directory, which contains all
most the outputs files of CALYPSO. To analyze the results, just type following command:

```bash
cd results
cak.py  --cif
```

The index of the structures sorted by energies in the ascending order is presented in
**`Analysis_Output.dat`** file, and these newly predicted structure files with cif
format are shown in **`dir_orign`** directory.

Please see [here](./_manuals.md#analysis-of-results) for more information about the analyses of CALYPSO results.

## Molecular Structure Prediction

This section is to show the example for the structure prediction with fixed rigid molecules using CALYPSO code.

Here, **SIESTA** code was used for geometry optimization and enthalpy calculations.

The CALYPSO input file of **`input.dat`**, rigid molecular structure information
file of **`MOL`**, SIESTA input files of **`sinput_*`** and pseudopotential file
of **`*.psf`** are needed.

The following files should be present in the working directory:

| Files     | Description                                                      |
|-----------|------------------------------------------------------------------|
| calypso.x | The executable file for running CALYPSO program                  |
| input.dat | The input file of CALYPSO containing controllable key parameters |
| sinput_*  | Input files for SIESTA                                           |
| MOL       | Rigid molecular structure information with Z\_Matrix format      |
| *.psf     | Pseudopotential for SIESTA                                       |
| submit.sh | Job submission file                                              |

**`calypso.x`** can be downloaded according to different operating systems.

Parameters in **`input.dat`** for the CH{sub}`4` system are shown below:

```text
SystemName = CH4
NumberOfSpecies = 2
NameOfAtoms = C H
NumberOfAtoms = 1 4
NumberOfFormula = 1 1
Volume = 60
@DistanceOfIon
1.0 1.0
1.0 1.0
@End
Ialgo = 2
PsoRatio = 0.6
PopSize = 20
ICode = 2
NumberOfLocalOptim = 3
Kgrid = 0.1 0.07
Command = sh submit.sh
MaxStep = 50
Mol = T
NumberOfTypeMolecule = 1
NumberOfMolecule = 2
DistOfMol = 1.5
```

**`MOL`** file contains the rigid molecular structure information with Z_Matrix format.

The Z_matrix is a way to represent a system built of atoms with internal coordinates.
It provides a description of each atom in a molecule in terms of its atomic type, bond length, bond angle, and dihedral angle.

> The detailed descriptions about Z-Matrix can be found in [here](http://en.wikipedia.org/wiki/Z-matrix_(chemistry>)).

**`MOL`** example of CH4 is shown below:

this the internal coordinate title and no need to write in MOL file

```text
Nspecie   I J K   R      A      T   ifr ifa ift
```

this is what the file contains

```text
5
1         0 0 0   0.0   0.0    0.0   1   1   1
2         1 0 0   1.044 0.0    0.0   0   1   1
2         1 2 0   1.044 109.48 0.0   0   0   1
2         1 2 3   1.044 109.48 120   0   0   0
2         1 2 3   1.044 109.48 120   0   0   0
```

The first line gives the total number of the atoms in the rigid molecular structure information and the following lines give the internal coordinates of each atom.

The internal coordinates consist of ten parts:

Nspecie (*integer*)
: the species number of the atom.

I, J, K (*integer*)
: atomic order in molecule is used to define the internal coordinates for current atomic coordinates

R (*real*)
: bond length of current atom with respect to *I* atom.

A (*real*)
: bond angle of current atom with respect to *I* and *J* atoms.

T (*real*)
: dihedral angle of current atom with respect to *I*, *J* and *K* atoms.

ifr, ifa, ift (*integer*)
: flags that indicate whether *r*, *a*, and *t* should be varied during local structural relaxation.
  0 for fixed and 1 for varying.

For SIESTA, the number of **`sinput_*`** (sinput_1, sinput_2, ...) should be in
accordance with the setting tag of *NumberOfLocalOptim*.

In this example, we use three SIESTA input files for structure relaxation.
**`sinput_1`** and **`sinput_2`** are used to perform very coarse structure relaxation,
while **`sinput_3`** is used to perform full structure relaxation with accurate precision.

> sinput_1

```text
SystemName siesta
SystemLabel siesta
NumberOfSpecies 2
NumberOfAtoms  10
%block ChemicalSpeciesLabel
1    6 C
2    1 H
%endblock ChemicalSpeciesLabel
PAO.BasisSize   SZ
kgrid_cutoff    8.0 Ang
MeshCutoff      80 Ry
PAO.EnergyShift 0.02 Ry
XC.functional           GGA
XC.authors              PBE
MaxSCFIterations        100
DM.MixingWeight         0.150
DM.Tolerance            1.d-4
DM.NumberPulay          5      
# Relaxation, smearing, etc.
ElectronicTemperature   3000 K
MD.TypeOfRun            cg     
Optim.Broyden           .true.
MD.VariableCell         .true.
MD.ConstantVolume       .false.
MD.MaxForceTol          1d-3 eV/Ang
MD.NumCGsteps           5
Use-Save-CG             .true.
Use-Save-XV             .true.
MD.Broyden.Initial.Inverse.Jacobian 0.20
MD.RemoveIntramolecularPressure .true.
MD.TargetPressure       100.0 GPa
ZM.ForceTolLen 0.04 eV/Ang
ZM.ForceTolAng 0.0001 eV/deg
ZM.MaxDisplLen 0.1 Ang
ZM.MaxDisplAng 20.0 deg
AtomicCoordinatesFormat NotScaledCartesianAng
%include Zmatrix.data
%block MM.Potentials
1 1 C6 16.292 0.5
2 2 C6  0.735 0.5
1 2 C6  3.185 0.5
%endblock MM.Potentials
```

> sinput_2

```text
SystemName siesta
SystemLabel siesta
NumberOfSpecies 2
NumberOfAtoms   10
%block ChemicalSpeciesLabel
1    6 C
2    1 H
%endblock ChemicalSpeciesLabel
PAO.BasisSize   SZ
%endblock PAO.BasisSizes
kgrid_cutoff    8.0 Ang
MeshCutoff      80 Ry
PAO.EnergyShift 0.01 Ry
XC.functional           GGA
XC.authors              PBE
MaxSCFIterations        100
DM.MixingWeight         0.150
DM.Tolerance            1.d-5
DM.NumberPulay          5    
ElectronicTemperature   3000 K
MD.TypeOfRun            cg    
Optim.Broyden           .true.
MD.VariableCell         .true.
MD.ConstantVolume       .false.
MD.MaxForceTol          2d-5 eV/Ang
MD.NumCGsteps           40
Use-Save-CG             .true.
Use-Save-XV             .true.
MD.Broyden.Initial.Inverse.Jacobian 0.20
MD.RemoveIntramolecularPressure .true.
MD.TargetPressure       100.000010 GPa
ZM.ForceTolLen 0.04 eV/Ang
ZM.ForceTolAng 0.0001 eV/deg
ZM.MaxDisplLen 0.1 Ang
ZM.MaxDisplAng 20.0 deg
AtomicCoordinatesFormat NotScaledCartesianAng
%include Zmatrix.data
%block MM.Potentials
1 1 C6 16.292 1.392
2 2 C6  0.735 2.025
1 2 C6  3.185 1.649
%endblock MM.Potentials
```

> sinput_3

```text
SystemName siesta
SystemLabel siesta
NumberOfSpecies 2
NumberOfAtoms   10
%block ChemicalSpeciesLabel
1    6 C
2    1 H
%endblock ChemicalSpeciesLabel
PAO.BasisSize   DZ
kgrid_cutoff    8.0 Ang
MeshCutoff      80 Ry
PAO.EnergyShift 0.002 Ry
XC.functional           GGA
XC.authors              PBE
MaxSCFIterations        100
DM.MixingWeight         0.150
DM.Tolerance            1.d-5
DM.NumberPulay          5     
ElectronicTemperature   3000 K
MD.TypeOfRun            cg     
Optim.Broyden           .false.
MD.VariableCell         .true.
MD.ConstantVolume       .false.
MD.MaxForceTol          2d-5 eV/Ang
MD.NumCGsteps           60
Use-Save-CG             .true.
Use-Save-XV             .true.
MD.RemoveIntramolecularPressure .true.
MD.TargetPressure       100.000010 GPa
ZM.ForceTolLen 0.04 eV/Ang
ZM.ForceTolAng 0.0001 eV/deg
ZM.MaxDisplLen 0.1 Ang
ZM.MaxDisplAng 20.0 deg
AtomicCoordinatesFormat NotScaledCartesianAng
%include Zmatrix.data
%block MM.Potentials
1 1 C6 16.292 1.392
2 2 C6  0.735 2.025
1 2 C6  3.185 1.649
%endblock MM.Potentials
```

:::{hint}
Multi-optimization strategy for structure relaxation is strongly suggested
:::

The psedopotential files **`*.psf`** (C.psf and H.psf in this case) should be provided by the user.

**`submit.sh`** is the job submission file for performing the SIESTA calculation.
Here is an example of submit.sh:

```bash
#!/bin/bash
siesta < siesta.fdf > siesta.out
```

:::{important}
the SIESTA output file should be named as "siesta.out"
:::

Once all the input files are ready, you can just type

```bash
./calypso.x > caly.log &
```

to execute the CALYPSO code in the sequential mode.
Or you can write this command into the *pbs* script and submit it.

CALYPSO will generate the **`results`** folder, which contains all the output files of
CALYPSO. To analyze the CALYPSO results, just type following command:

```bash
cd results
cak.py  --cif
```

The index of the structures sorted by enthalpies in the ascending order is presented in
**`Analysis_Output.dat`** file, and these newly predicted structure files with cif
format are shown in **`dir_0.1`** directory.

Please see [here](./_manuals.md#analysis-of-results) for more information about the analyses of CALYPSO results.

## Variable Stoichiometry Structure Prediction

This section is to show the example for variable stoichiometry structure prediction using
CALYPSO code. Here, VASP code was used for geometry optimization and enthalpy calculations.

The CALYPSO input file of **`input.dat`**, VASP input files of **`INCAR_*`** and
pseudopotential file of **`POTCAR`** are needed.

The following files should be present in the working directory:

| File:     | Description                                                      |
|:----------|:-----------------------------------------------------------------|
| calypso.x | The executable file for running CALYPSO program                  |
| input.dat | The input file of CALYPSO containing controllable key parameters |
| INCAR_*   | Input files for VASP                                             |
| POTCAR    | Pseudopotential for VASP                                         |
| submit.sh | Job submission file                                              |

**`calypso.x`** can be downloaded according to different operating systems.

Parameters in **`input.dat`** are shown for the LiH system:

```text
########### The Parameters of CALYPSO #############
# A string of one or several words contain a descriptive 
# name of the system (max. 40 characters).
SystemName = LiH
# Number of different atomic species in the simulation, 
# where it has two type elements (B and N).
NumberOfSpecies = 2
# Element symbols of the different chemical species. 
NameOfAtoms = Li H
# The range of formula unit per cell in your simulation.
NumberOfFormula = 1 1
# The volume of 1 f.u. unit=angstrom^3. 
Volume = 5.0
# Minimal distances between atoms of each chemical species. 
@DistanceOfIon
 1.0 0.8
 0.8 0.8
@End
# It determines which algorithm should be adopted in the simulation.
Ialgo = 2
# The proportion of the structures generated by PSO 
# against the new structures in each generation.
PsoRatio = 0.6
# The population size. Normally, it is larger for larger systems.
PopSize = 30
# It determines which local optimization program 
# should be used in the simulation.
ICode = 1
# The Number of local optimization for each structure.
NumberOfLocalOptim = 4
# It is the k-point sampling solution in local optimization. 
# Kgrid = 0.12 0.06
# The script for submitting local optimization calculations.
Command = sh submit.sh
# The Max step for iteration
MaxStep =30
# If True, Variational Stoichiometry structure prediction is performed
VSC=T
VSCEnergy= 0 0
# The Max Number of Atoms in unit cell
MaxNumAtom=20
# The Variation Range for each type atom 
@CtrlRange
1 1
1 7
@End
#################### End Parameters #######################
```

For VASP, the number of **`INCAR_*`** (INCAR_1, INCAR_2, ...) is in accordance with the
setting tag of *NumberOfLocalOptim*.

In this example, we use four INCAR files for structure relaxation.
**`INCAR_1`** and **`INCAR_2`** are used to perform very crude structure relaxation
keeping the volume fixed, **`INCAR_3`** is used to perform full structure relaxation
with medium precision, while **`INCAR_4`** is used to perform very accurate calculation.

> INCAR_1

```text
SYSTEM = local optimization
PREC = LOW
EDIFF = 3e-2
IBRION = 2
ISIF = 2
NSW = 40
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.50
LWAVE = FALSE
LCHARG = FALSE
ISTART = 0
PSTRESS = 3000
EDIFFG = -4e-2
```

> INCAR_2

```text
SYSTEM = local optimization
PREC = Normal
EDIFF = 2e-2
IBRION = 2
ISIF = 4
NSW = 40
ISMEAR = 0 
SIGMA = 0.05
POTIM = 0.2
LWAVE = FALSE
LCHARG = FALSE
PSTRESS = 3000
EDIFFG = -1e-2
```

> INCAR_3

```text
SYSTEM = local optimization
PREC = Normal
EDIFF = 2e-4
IBRION = 1
ISIF = 3
NSW = 40
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.1
LWAVE = FALSE
LCHARG = FALSE
PSTRESS = 3000
EDIFFG = 1e-3
```

> INCAR_4

```text
SYSTEM = local optimization
ENCUT = 600
EDIFF = 1e-5
IBRION = 2
ISIF = 3
NSW = 80
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.1
LWAVE = FALSE
LCHARG = FALSE
PSTRESS = 3000
EDIFFG = 1e-4
```

:::{hint}
Multi-optimization strategy for structure relaxation is strongly suggested
:::

**`POTCAR`** should be provided.

:::{important}
**ATTENTION!!!** The order of elements in POTCAR must be identical to the element order
in the setting tag of **NameOfAtoms**.
:::

**`submit.sh`** is the submission job file for performing the VASP calculations.

Here is an example of submit.sh:

```bash
#!/bin/bash
mpdboot
mpiexec -n 12 vasp_std > vasp.log 2>&1
```

Once all input files are ready, you can just type

```bash
./calypso.x > caly.log &
```

to execute the CALYPSO code in the sequential mode.
Or you can write this command into the *pbs* script and submit it.

CALYPSO will generate the **`results`** folder, which contains all the output files of CALYPSO.
To analyze the results, just type following command:

```bash
cd results
cak.py --cif
```

The index of the structures sorted by enthalpies in the ascending order is presented in **`./dir_Li*H*/Analysis_Output.dat`** file, and these newly predicted structure files
with cif format are shown in **`dir_0.1`** directory.

## Surface Structure Prediction

This section introduces the surface structure prediction module. It includes a
description of the required input files, a typical run of the program, and result analysis.

:::{note}
This part of CALYPSO package is currently in the early stage of development, there might
be large changes on the control parameters and output files in the following versions.

For surface structure prediction, DFTB+ and VASP package are supported for local optimization by now.
:::

This section will give a general introduction to the files used to run the program in the first place,
then a relatively detailed description of each file, followed by two example runs of the program via
VASP and DFTB+ packages.

The most important input files are: **`input.dat`** (control parameters),
**`SUBSTRATE.surf`** (the structure files of substrate, both cif and VASP POSCAR format are supported),
and input files for VASP/DFTB+. Most of the output files reside in **`results`** directory.

### Diamond (111) surface reconstruction prediction

This subsection will introduce how to predict the (111) surface reconstruction of diamond
using VASP as the local relaxation code.

In this example, the substrate will be generated automatically from crystal structures.

To perform surface structure prediction, one needs to create a directory and prepare the following files:

| File      | Description                                                          |
|:----------|:---------------------------------------------------------------------|
| calypso.x | The executable file for running CALYPSO program                      |
| input.dat | The input file of CALYPSO specifying the controllable key parameters |
| INCAR_*   | Input files for VASP                                                 |
| POTCAR    | Pseudopotential for VASP                                             |
| submit.sh | Job submission file                                                  |

**`calypso.x`** can be downloaded according to operating system.

**`input.dat`** specifies all the control parameters that tell the program how to do
the job of global surface structure search.

Most of the parameters have default values and do not need to be changed.
Here is an example for diamond (111) surface reconstruction prediction:

```text
LSurface    = T  # Surface reconstruction predictions
ICode        = 1  #VASP
Kgrid        = 0.2 
PopSize      = 20
MaxStep      = 30
PsoRatio     = 0.6
SurfaceThickness = 2.0
#|atomic symbol|count|
@SurfaceAtoms 
C    4   
@End
#--------------------------------------------------
#Following parameters are used to build 
#the surface from bulk crystal info reconstruction symmetry
Substrate  = Automatic
@MatrixNotation             
2     0
0     1
@End
UseCifFile = T         
CifFilePath = dia-vasp.cif
MillerIndex = 1 1 1 
SlabDepth = 0.0            
SlabNumLayers = 6
NumRelaxedLayers = 2
CapBondsWithH = T
```

Note that the **Substrate** tag is specified to "Automatic", which means the substrate
will be generated from the bulk crystal.

**`INCAR_*`**, **`POTCAR-*`** files must present in the current work directory for VASP users.

*INCAR_1* and *INCAR_2* are the central input files for VASP.
The structures will be relaxed by a set of relatively low precision control parameters in
*INCAR_1* first; then the coarsely relaxed structures will be further relaxed by a set of
relatively high-precision parameters in *INCAR_2*.

> INCAR_1

```text
PREC   = LOW
EDIFF  = 3e-2
EDIFFG = -4e-2
IBRION = 2
ISIF   = 0
NSW    = 45
ISMEAR = 0 ; SIGMA = 0.05
POTIM  = 0.050
LWAVE  = FALSE
LCHARG = FALSE
ISTART = 0
```

> INCAR_2

```text
ENCUT  = 500
EDIFF  = 1e-4
EDIFFG = 1e-3
IBRION = 2
ISIF   = 0
NSW    = 100
ISMEAR = 0; SIGMA = 0.05
POTIM  = 0.0300
LCHARG = FALSE
LWAVE  = FALSE
ISTART = 0
```

Users do NOT need to cat *POTCAR* of each atomic species together.
The program will do the job automatically.
However, one has to copy POTCAR for each element to this directory and rename it to
**POTCAR-\*** format, while the star (*) stands for the name of the element.

Taking surface structures constructed by C and H atoms for example, one needs to copy
POTCAR of C and H to this directory and rename them to **POTCAR-C** and **POTCAR-H**, respectively.
For pseudo-hydrogens with fractional valence electrons, such as Z=0.75, its POTCAR should
be renamed to **POTCAR-H.75**.

**`submit.sh`** is the script for local relaxation via VASP. Here is an example:

```bash
mpiexec -n 12 vasp_std > vasp.log 2>&1
```

Once all the input files are ready, you may run the structure prediction via the
following command, or alternatively, put this execution command into a job submission script.

```bash
./calypso.x >  caly.log &
```

The result analysis process of surface structure prediction is similar to the crystal
structure predictions. You may run the following commands:

```bash
cd results
cak.py --cif 
```

and will see the surface formation enthalpy order of predicted structures in
**`Analysis_Output.dat`** file, and these newly predicted structure files with cif
format can be found in **`dir_0.1`** directory.

Please see [here](./_manuals.md#analysis-of-results) for more information about the analyses of CALYPSO results.

### Hydrogenated diamond (100) surface reconstruction

Example to perform hydrogenated diamond (100) surface reconstruction prediction using
predefined substrate file and DFTB+ local relaxation will be demonstrated in this subsection.

Files needed to run this example are listed below:

| File              | Description                                                          |
|:------------------|:---------------------------------------------------------------------|
| calypso.x         | The executable file for running CALYPSO program                      |
| input.dat         | The input file of CALYPSO specifying the controllable key parameters |
| SUBSTRATE.surf    | Substrate file (cif and POSCAR formatted are supported)              |
| DFTB+ input files | dftb_in.hsd_PRE_1, dftb_in.hsd_PRE_2, SK files                       |
| submit.sh         | A script to run VASP or DFTB+.                                       |

**`calypso.x`** can be downloaded according to different operating systems.

**`input.dat`** contains all the parameters to run the surface structure predictions.

In this example, we show how to control the program to adopt user specified substrate
and use DFTB+ code to relax structures locally. Here is an example:

```text
LSurface     = T  # Surface reconstruction predictions
ICode        = 8  # DFTB+
Kgrid        = 0.2 
PopSize      = 20
MaxStep      = 30
PsoRatio     = 0.6
SurfaceThickness = 2.0
@SurfaceAtoms #|atomic symbol|count|
C    4   
H    4
@End
Substrate  = SUBSTRATE.surf
```

**`SUBSTRATE.surf`** is an optional user defined substrate file. The surface will be
generated on top of this substrate. Both VASP and CIF files can be recognized by CALYPSO.

One can set the **Substrate** control parameter in **input.dat** to "Auto" or "Automatic" in order to generate substrate automatically via crystal info.

Please see previous example for more information.

For VASP format, chemical symbols should be inserted just before the line of the numbers of atoms.

```text
Diamond-100
1.00000
   5.054258   0.000000   0.000000
   0.000000   5.054258   0.000000
   0.000000   0.000000  19.467375
   H   C
   8  24
Selective dynamics
Direct
 0.10783118      0.00000000      0.21796252   F   F   F
 0.10783118      0.50000000      0.21796252   F   F   F
 0.60783118      0.00000000      0.21796252   F   F   F
 0.60783118      0.50000000      0.21796252   F   F   F
 0.39216882      0.00000000      0.21796252   F   F   F
 0.39216882      0.50000000      0.21796252   F   F   F
 0.89216882      0.00000000      0.21796252   F   F   F
 0.89216882      0.50000000      0.21796252   F   F   F
 0.25000000      0.25000000      0.48632006   T   T   T
 ...
```

Besides, CIF format is also supported. However, one needs to add **_selective** tag to
specify which atoms are allowed to relax. Please see the following example file:

```text
data_Surf
_amcsd_formula_title          "H8C48"
_symmetry_Int_Tables_number   1
_cell_length_a                5.052205
_cell_length_b                5.052205
_cell_length_c                19.824233
_cell_angle_alpha             90.000000
_cell_angle_beta              90.000000
_cell_angle_gamma             90.000000
 
loop_
_space_group_symop_operation_xyz
x,y,z
loop_
_atom_site_label
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_selective
C        0.00000000  0.25000000  0.74778343   T
C        0.00000000  0.75000000  0.74778343   T
C        0.50000000  0.25000000  0.74778343   T
C        0.50000000  0.75000000  0.74778343   T
C        0.25000000  0.25000000  0.70273190   T
C        0.25000000  0.75000000  0.70273190   T
C        0.75000000  0.25000000  0.70273190   T
C        0.75000000  0.75000000  0.70273190   T
C        0.25000000  0.50000000  0.65768037   F
C        0.75000000  0.00000000  0.65768037   F
C        0.25000000  0.00000000  0.65768037   F
...
```

DFTB+ input files of hsd formated are needed to relax structures

**`dftb_in.hsd_PRE_1`** and **`dftb_in.hsd_PRE_2`**, control parameters line between
"####" will be filled automatically via the program and users shouldn't change these values.

Besides, users should provide Slater-Koster (SK) files for DFTB+ calculation
(Some SK files can be found in this link: <http://www.dftb.org/parameters/>).

**`submit.sh`** is the submission job file for perform the DFTB+ calculation.
Here is an example of submit.sh:

```bash
#!/bin/bash
export OMP_NUM_THREADS=4
/share/apps/dftb+ > dftb.log 2>&1
```

Once all the input files are ready, you may run the structure prediction via the
following command, or alternatively, put this execution command into a job submit script.

```bash
./calypso.x >  caly.log &
```

The result analysis process of surface structure prediction is similar to the crystal
structure predictions. You may run the following commands:

```bash
cd results
cak.py --cif 
```

and will see the surface formation enthalpy order of predicted structures in
**`Analysis_Output.dat`** file, and these newly predicted structure files with cif
format can be found in **`dir_0.1`** directory.

Please see [here](./_manuals.md#analysis-of-results) for more information about the analyses of CALYPSO results.

### Crystal lattice matches of two graphene

This subsection will introduce how to search the matched lattice for two materials
which is used for building the simulated model for interface structure prediction.

This is an example for matching the lattices for graphene asymmetric grain boundary.
The slab model with the optimally matched lattice adopted in the interface structure
prediction will be generated automatically from graphene bulk structure.

| File:              | Description                                                                                                                             |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| calypso.x          | The executable file of CALYPSO program to cleave the surface (i.e. create the primitive vectors of surface) with specified miller index |
| input.dat.ini      | The pre-input file to generate the input.dat file of CALYPSO specifying the controllable key parameters                                 |
| lat1.cif, lat2.cif | Structure files of bulk crystal in cif format with symmetry information                                                                 |
| input_mismatch.dat | Input files of lattice match toolkit                                                                                                    |
| gen_slab_model.sh  | The script for calling calypso.x                                                                                                        |
| mismatch-zur.x     | The executable file of lattice match toolkit                                                                                            |

**`calypso.x`** can be downloaded according to different operating systems.

**`input.dat.ini`** contains all the parameters of *calypso.x* to cleave the surface.
Here is an example:

```text
LSurface         = T
ICode            = 1
Kgrid         = 0.1
PopSize     = 40
MaxStep     = 10
Pre_surf_relax=F

Surface_thickness = 1.5
ForbiThickness    = 0.50000000
SPACESAVING = T
@SURFACE_ATOMS  # |atomic symbol|count|
C  4
@END

#used to build the surface from bulk info
#reconstruction symmetry
Substrate        = Auto
@MATRIX_NOTATION
1     0
0     1
@END
Use_Cif_File = T
Cif_File_Path = SUBSTRATE
Miller_index = which
Slab_Vacuum_Thick = 15.0
Slab_Num_Layers = 8
Num_Relaxed_Layers = 2

Gen_Substrate=T
```

**`lat1.cif`** and **`lat2.cif`** are the user defined initial crystal files used for
cleave the surfaces. They are in CIF format and the symmetry information should be included.

**`input_mismatch.dat`**

```text
# This variable specifies the maximum area of searched superlattices.
MaximumArea = 200.0 

# This variable specifies the maximum lattice-mismatch value.
MaximumMismatchValue = 0.05 

# This variable specifies the maximum component of Miller index used for creating
# the facets based on the input crystal structures.
MaximumMillerIndex = 5 

# The flag specifies whether the input crystal structures are 2D layered materials.
# This parameter is set as "True" if the input crystal structures are 2D layered materials.
2DStructure = F

# This parameter is only used for the grain boundary system, in which two bulk phases
# are belonged to the same materials. The flag specifies whether the twin boundaries are
# preserved. This parameter is set as "True" if the twin boundary is needed to be preserved.
SameSubstrate = F

# If this parameter is set as "True" only the surface with the Miller indices listed in
# the "MillerIndex1List" will be generated. If this parameter is set as "False", all of
# surfaces with Miller index less than the specified maximum Miller index will be considered.
SpecifyingMillerIndex1 = F

# This parameter is a list of specified Miller indices used for generating the surfaces
# for the 1st material.
@MillerIndex1List
1 4 1 
@End 

SpecifyingMillerIndex2 = F

@MillerIndex2List
1 1 0 
@End
```

**`gen_slab_model.sh`** is a script used to call calypso.x program to cleave surface.
It can be downloaded from the website: <http://download.calypso.cn/>

Once all the input files are prepared, you may run the structure prediction via the
following command, or alternatively, put this execution command into a job submit script:

```bash
./mismatch-zur.x > mis.log
```

The result is recorded in the file **`mismatch-total.dat`**. It's ranked by the degree
of lattice mismatch (maismatch_value). The parameters "hkl" and "uv" are used to
construct the surface by other software, such as Material Studios.

```text
No. hkl1       uv1       hkl2        uv2      mismatch_value
1   0 0 1   3.00  0.00   0 0 1   -2.00   3.00      1
            0.00  3.00           -3.00  -2.00
2   1 4 1   3.00  3.00   1 1 0   -2.00   2.00      2
           -1.00  0.00            0.50  -0.50
```

### Interface structure prediction of SIGMA5(210) grain boundary of rutile TiO2

This subsection will introduce how to predict the interfacial structures using DFTB+
as the local structure relaxation code.

In this example, the slab models of bulk phases are needed to be given as input.
To perform interface structure prediction, one needs to create a directory and
prepare the following files:

| File:             | Description                                                          |
|-------------------|----------------------------------------------------------------------|
| calypso.x         | The executable file for running CALYPSO program                      |
| input.dat         | The input file of CALYPSO specifying the controllable key parameters |
| SUBSTRATE*        | The slab models of bulk materials                                    |
| dftb_in.hsd_PRE-* | Input parameter files for DFTB+                                      |
| *-*.skf           | Slater-Koster files for DFTB+                                        |
| submit.sh         | A script to run DFTB+.                                               |

**`calypso.x`** can be downloaded according to different operating systems.

**`input.dat`** contains all the parameters to run the interface structure predictions.

In this example, we show how to control the program to adopt user specified slab models
of bulk phases and use DFTB+ code to relax structures locally. Here is an example:

```text
LSURFACE = T
LINTERFACE = T
ICode = 8
Rand_Scheme = 3
System_type = INTERFACE
PopSize = 50
MaxStep = 30
InterfaceTranslation = b
Interface_thckness = 3.5
@SURFACE_ATOMS
Ti 1
O  4
@END
@COORDINATE_NUMBER
Ti Ti 0  2.5  2.5
O  O  0  1.8  2.3
Ti O  6  1.8  2.5
O  To 3  1.8  2.5
@END
Substrate   = SUBSTRATE1
Substrate2  = SUBSTRATE2
```

**SUBSTRATE\*** is the user defined slab models of bulk phases.
The interface will be generated between two substrates.
CIF and VASP formats can be recognized by CALYPSO.
Note that filenames are optional but must be identical with the set of filenames in the input.dat file.

> SUBSTRATE1

```text
data_TiO2_rutile\(2\1\0)
_audit_creation_date              2015-08-27
_audit_creation_method            'Materials Studio'
_symmetry_space_group_name_H-M    'P1'
_symmetry_Int_Tables_number       1
_symmetry_cell_setting            triclinic
loop_
_symmetry_equiv_pos_as_xyz
  x,y,z
_cell_length_a                    2.9590
_cell_length_b                    10.2725
_cell_length_c                    30.2725
_cell_angle_alpha                 90.0000
_cell_angle_beta                  90.0000
_cell_angle_gamma                 90.0000
loop_
_atom_site_type_symbol
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_U_iso_or_equiv
_atom_site_adp_type
_atom_site_occupancy
_selective 
   Ti    0.00000   0.00000  -0.00000   0.00000  Uiso   1.00 T
   Ti    0.00000   0.60000   0.06787   0.00000  Uiso   1.00 T
   Ti    0.00000   0.20000   0.13573   0.00000  Uiso   1.00 T
   Ti    0.00000   0.80000   0.20360   0.00000  Uiso   1.00 T
   Ti    0.00000   0.40000   0.27147   0.00000  Uiso   1.00 T
   Ti    0.00000  -0.00000   0.33933   0.00000  Uiso   1.00 T
   Ti    0.50000   0.30000   0.03393   0.00000  Uiso   1.00 T
   Ti    0.50000   0.90000   0.10180   0.00000  Uiso   1.00 T
   Ti    0.50000   0.50000   0.16967   0.00000  Uiso   1.00 T
   Ti    0.50000   0.10000   0.23753   0.00000  Uiso   1.00 T
   Ti    0.50000   0.70000   0.30540   0.00000  Uiso   1.00 T
   O     0.00000   0.93904   0.06206   0.00000  Uiso   1.00 T
   O     0.00000   0.53904   0.12992   0.00000  Uiso   1.00 T
   O     0.00000   0.13904   0.19779   0.00000  Uiso   1.00 T
   O     0.00000   0.73904   0.26566   0.00000  Uiso   1.00 T
   O     0.00000   0.33904   0.33352   0.00000  Uiso   1.00 T
   O     0.00000   0.26096   0.07368   0.00000  Uiso   1.00 T
   O     0.00000   0.86096   0.14154   0.00000  Uiso   1.00 T
   O     0.00000   0.46096   0.20941   0.00000  Uiso   1.00 T
   O     0.00000   0.06096   0.27728   0.00000  Uiso   1.00 T
   O     0.50000   0.11712   0.01325   0.00000  Uiso   1.00 T
   O     0.50000   0.71712   0.08111   0.00000  Uiso   1.00 T
   O     0.50000   0.31712   0.14898   0.00000  Uiso   1.00 T
   O     0.50000   0.91712   0.21685   0.00000  Uiso   1.00 T
   O     0.50000   0.51712   0.28472   0.00000  Uiso   1.00 T
   O     0.50000   0.48288   0.05462   0.00000  Uiso   1.00 T
   O     0.50000   0.08288   0.12249   0.00000  Uiso   1.00 T
   O     0.50000   0.68288   0.19035   0.00000  Uiso   1.00 T
   O     0.50000   0.28288   0.25822   0.00000  Uiso   1.00 T
   O     0.50000   0.88288   0.32609   0.00000  Uiso   1.00 T
```

> SUBSTRATE2

```text
data_TiO2_rutile\(2\1\0)
_audit_creation_date              2015-08-27
_audit_creation_method            'Materials Studio'
_symmetry_space_group_name_H-M    'P1'
_symmetry_Int_Tables_number       1
_symmetry_cell_setting            triclinic
loop_
_symmetry_equiv_pos_as_xyz
  x,y,z
_cell_length_a                    2.9590
_cell_length_b                    10.2725
_cell_length_c                    30.2725
_cell_angle_alpha                 90.0000
_cell_angle_beta                  90.0000
_cell_angle_gamma                 90.0000
loop_
_atom_site_label
_atom_site_fract_x
_atom_site_fract_y
_atom_site_fract_z
_atom_site_U_iso_or_equiv
_atom_site_adp_type
_atom_site_occupancy
_selective 
   Ti    0.00000   0.00000  -0.00000   0.00000  Uiso   1.00 T
   Ti    0.00000   0.60000   0.06787   0.00000  Uiso   1.00 T
   Ti    0.00000   0.20000   0.13573   0.00000  Uiso   1.00 T
   Ti    0.00000   0.80000   0.20360   0.00000  Uiso   1.00 T
   Ti    0.00000   0.40000   0.27147   0.00000  Uiso   1.00 T
   Ti    0.00000  -0.00000   0.33933   0.00000  Uiso   1.00 T
   Ti    0.50000   0.30000   0.03393   0.00000  Uiso   1.00 T
   Ti    0.50000   0.90000   0.10180   0.00000  Uiso   1.00 T
   Ti    0.50000   0.50000   0.16967   0.00000  Uiso   1.00 T
   Ti    0.50000   0.10000   0.23753   0.00000  Uiso   1.00 T
   Ti    0.50000   0.70000   0.30540   0.00000  Uiso   1.00 T
   O     0.00000   0.93904   0.06206   0.00000  Uiso   1.00 T
   O     0.00000   0.53904   0.12992   0.00000  Uiso   1.00 T
   O     0.00000   0.13904   0.19779   0.00000  Uiso   1.00 T
   O     0.00000   0.73904   0.26566   0.00000  Uiso   1.00 T
   O     0.00000   0.33904   0.33352   0.00000  Uiso   1.00 T
   O     0.00000   0.26096   0.07368   0.00000  Uiso   1.00 T
   O     0.00000   0.86096   0.14154   0.00000  Uiso   1.00 T
   O     0.00000   0.46096   0.20941   0.00000  Uiso   1.00 T
   O     0.00000   0.06096   0.27728   0.00000  Uiso   1.00 T
   O     0.50000   0.11712   0.01325   0.00000  Uiso   1.00 T
   O     0.50000   0.71712   0.08111   0.00000  Uiso   1.00 T
   O     0.50000   0.31712   0.14898   0.00000  Uiso   1.00 T
   O     0.50000   0.91712   0.21685   0.00000  Uiso   1.00 T
   O     0.50000   0.51712   0.28472   0.00000  Uiso   1.00 T
   O     0.50000   0.48288   0.05462   0.00000  Uiso   1.00 T
   O     0.50000   0.08288   0.12249   0.00000  Uiso   1.00 T
   O     0.50000   0.68288   0.19035   0.00000  Uiso   1.00 T
   O     0.50000   0.28288   0.25822   0.00000  Uiso   1.00 T
   O     0.50000   0.88288   0.32609   0.00000  Uiso   1.00 T
```

DFTB+ input files of hsd format are needed to relax structures:
**`dftb_in.hsd_PRE_1`**, **`dftb_in.hsd_PRE_2`**.

The structures will be relaxed by a set of relatively low precision control parameters in
*dftb_in.hsd_PRE_1* first; then the coarsely relaxed structures will be further relaxed
by a set of relatively high-precision parameters in *dftb_in.hsd_PRE_2*.

Control parameters line between "####" will be filled automatically via the program and
users shouldn’t change these values. Besides, users should provide Slater-Koster (SK)
files for DFTB+ calculation (Some SK files can be found in this link: <http://www.dftb.org/parameters/>).

**`submit.sh`** is the submission job file for perform the DFTB+ calculation.
Here is an example of submit.sh:

```bash
#!/bin/bash
export OMP_NUM_THREADS=4
/share/apps/dftb+ > dftb.log 2>&1
```

Once all the input files are ready, you may run the structure prediction via the following
command, or alternatively, put this execution command into a job submit script:

```bash
./calypso.x > caly.log 2>&1
```

The result analysis process of surface structure prediction is similar to the crystal
structure predictions. You may run the following commands:

```bash
cd results
cak.py --cif
```

You will see the interface formation enthalpy order of predicted structures in
**`Analysis_Output.dat`** file, and these newly predicted structure files with cif
format can be found in **`dir_0.1`** directory.

Please see [here](./_manuals.md#analysis-of-results) for more information about the analyses of CALYPSO results.

## Design of Superhard Materials

This section is to show the examples for design of superhard materials using CALYPSO code.
Here, VASP code is used for geometry optimization and enthalpy calculations.

The CALYPSO input file of **`input.dat`**, VASP input files of **`INCAR_*`** and
pseudopotential file of **`POTCAR`** are needed.

The following files should be present in the working directory:

| File:     | Description                                                      |
|-----------|------------------------------------------------------------------|
| calypso.x | The executable file for running CALYPSO program                  |
| input.dat | The input file of CALYPSO containing controllable key parameters |
| INCAR_*   | Input files for VASP                                             |
| POTCAR    | Pseudopotential for VASP                                         |
| submit.sh | Job submission file                                              |

**`calypso.x`** can be downloaded according to different operating systems.

Parameters in **input.dat** for the carbon system are shown:

```text
SystemName = Carbon
NumberOfSpecies = 1
NameOfAtoms = C
NumberOfAtoms = 1
NumberOfFormula = 4 4
Volume = 14.0
@DistanceOfIon
1.30
@End
Ialgo = 2
PsoRatio = 0.6
PopSize = 30
ICode = 1
NumberOfLocalOptim = 4
Command = sh submit.sh
MaxStep = 50
Hardness = T
```

For VASP, the number of **`INCAR_*`** (INCAR_1, INCAR_2, …) is in accordance with the
setting tag of *NumberOfLocalOptim*.

In this example, we use four INCAR files for structure relaxation. **INCAR_1** and
**INCAR_2** are used to perform very coarse structure relaxation keeping the volume fixed.
**INCAR_3** is used to perform full structure relaxation with medium precision,
and **INCAR_4** is used to perform very accurate calculations.

> INCAR_1

```text
SYSTEM = local optimization
PREC = LOW
EDIFF = 3e-2
IBRION = 2
ISIF = 2
NSW = 40
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.5
LWAVE = FALSE
LCHARG = FALSE
ISTART = 0
PSTRESS = 0.001
EDIFFG = -4e-2
```

> INCAR_2

```text
SYSTEM = local optimization
PREC = Normal
EDIFF = 2e-2
IBRION = 2
ISIF = 4
NSW = 40
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.2
LWAVE = FALSE
LCHARG = FALSE
PSTRESS = 0.001
EDIFFG = -1e-2
```

> INCAR_3

```text
SYSTEM = local optimization
PREC = Normal
EDIFF = 2e-4
IBRION = 1
ISIF = 3
NSW = 40
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.1
LWAVE = FALSE
LCHARG = FALSE
PSTRESS = 0.001
EDIFFG = 1e-3
```

> INCAR_4

```text
SYSTEM = local optimization
ENCUT = 600
EDIFF = 1e-5
IBRION = 2
ISIF = 3
NSW = 80
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.1
LWAVE = FALSE
LCHARG = FALSE
PSTRESS = 0.001
EDIFFG = 1e-4
```

:::{hint}
Multi-optimization strategy for structure relaxation is strongly suggested
:::

**`POTCAR`** should be provided.

:::{important}
**ATTENTION!!!** The order of elements in POTCAR must be identical to the element order
in the setting tag of **NameOfAtoms**.
:::

**`submit.sh`** is the submission job file for performing the VASP calculations.
Here is an example of submit.sh:

Once all the input files are ready, you can just type

```bash
./calypso.x > caly.log &
```

to execute the CALYPSO code in the sequential mode.
Or you can write this command into the *pbs* script and submit it.

CALYPSO will generate the **`results`** folder, which contains all outputs files of
CALYPSO. To analyze the results, just type following command:

```bash
cd results
cak.py --cif –hard
```

The index of the structures sorted by hardness in the descending order is presented in
**`Analysis_Output.dat`** file, and these newly predicted structure files with cif
format are shown in **`dir_0.1`** directory.

Please see [here](./_manuals.md#analysis-of-results) for more information about the analyses of CALYPSO results.

## Structure prediction of atom or molecule adsorption of 2D layer material

This section is to show the example for the structure prediction of hydrogenated graphene.
Here, DFTB+ code was used for geometry optimization and energy calculations.

The CALYPSO input file of **`input.dat`**, 2D substrate structure information file of
**`SUB.dat`**, DFTB+ input files of **`dftb_in_*.hsd`** and Slater-Koster (SK) files of
**`*.skf`** are needed.

| File:         | Description                                                      |
|---------------|------------------------------------------------------------------|
| calypso.x     | The executable file for running CALYPSO program                  |
| input.dat     | The input file of CALYPSO containing controllable key parameters |
| SUB.dat       | 2D substrate structure information                               |
| Dftb_in_*.hsd | Input files for DFTB+                                            |
| *.skf         | SK files for DFTB+                                               |
| submit.sh     | Job submission file                                              |

**`calypso.x`** can be downloaded according to different operating systems.

Parameters in **`input.dat`** for the hydrogenated graphene system are shown:

```text
SystemName = Hydrogenated-graphene
NumberOfSpecies = 2
NameOfAtoms = C H
Ialgo = 2
PsoRatio = 0.6
ICode = 8
NumberOfLocalOptim = 2
Command = sh submit.sh
PopSize = 30
MaxStep = 30

Adsoption = T
AdsoptionStyle = 2
NumberOfTypeAtom = 1
@Adatoms
H 2 2
@End
@SuperCell
2 0
0 2
@End
RangeOfZAxis = 1.4 1.2
```

**`SUB.dat`** contains the 2D substrate structure information. Here we take graphene as an example:

```text
graphine
1.0
  2.45940000    0.0000000    0.000000
  -1.2297000    2.1298750    0.000000
  0.00000000    0.0000000    15.00000
  C
  2
Direct
  0.66667  0.33333  0.50000
  0.33333  0.66667  0.50000
points
2
  0.66667  0.33333  0.50000
  0.33333  0.66667  0.50000
```

The structure information is given in the format of POSCAR.

If **AdsorptionStyle** is set to 2 in *input.dat*, the adsorption site is needed.

The line below the word **points** gives numbers of sites in the cell.
The next few lines give the direct coordinates of adsorption sites.

DFTB+ input files in hsd formated are needed to relax structures: **`dftb_in_1.hsd`**, **`dftb_in_2.hsd`**.
Besides, users should provide Slater-Koster (SK) files for DFTB+ calculation
(Some SK files can be found in this link: <http://www.dftb.org/parameters/>).

**`submit.sh`** is the submission job file for perform the DFTB+ calculation.
Here is an example of submit.sh:

```bash
#!/bin/bash
export OMP_NUM_THREADS=4
/share/apps/dftb+ > dftb.log 2>&1
```

Once all the input files are ready, you may run the structure prediction via the
following command, or alternatively, put this execution command into a job submit script.

```bash
./calypso.x > caly.log &
```

The result analysis process of surface structure prediction is similar to the crystal
structure predictions. You may run the following commands:

```bash
cd results
cak.py --cif 
```

and will see the surface formation enthalpy order of predicted structures in
**`Analysis_Output.dat`** file, and these newly predicted structure files with cif
format can be found in **`dir_0.1`** directory.

Please see [here](./_manuals.md#analysis-of-results) for more information about the analyses of CALYPSO results.

## Design of Optical Materials with Desirable Electronic Band Gap

This section is to show the examples for design of optical materials with desirable
electronic band gap using CALYPSO code.

We take the structure prediction of carbon (C) as an example. Here, VASP code was used
for geometry optimization and enthalpy calculations.

The CALYPSO input file of **`input.dat`** and VASP input files of **`INCAR_*`** and
pseudopotential file of **`POTCAR`** are needed.

The following files should be present in the working directory:

| Files     | Description                                                      |
|-----------|------------------------------------------------------------------|
| calypso.x | The executable file for running CALYPSO program                  |
| input.dat | The input file of CALYPSO containing controllable key parameters |
| INCAR_*   | Input files for VASP                                             |
| POTCAR    | Pseudopotential for VASP                                         |
| submit.sh | Job submission file                                              |

**`calypso.x`** can be downloaded according to different operating systems.

Parameters in **`input.dat`** are shown below:

```text
SystemName = C
NumberOfSpecies = 1
NameOfAtoms = C
NumberOfAtoms = 1
Band_edge = T
TarBandGap = 2.5
NumberOfFormula = 4 4
Volume = 15.0
@DistanceOfIon
1.0
@End
Ialog = 2
PsoRatio = 0.6
PopSize = 30
ICode = 1
NumberOfLocalOptim = 4
Command = sh submit.sh
MaxStep = 30
```

VASP, the number of **`INCAR_*`** (INCAR_1, INCAR_2, ...) should be larger than the
setting tag *NumberOfLocalOptim*.

In this example, we use four INCAR files for structure relaxation and one INCAR files
for calculating band gap.

**`INCAR_1`** and **`INCAR_2`** are used to perform very coarse structure relaxation
keeping the volume fixed, **`INCAR_3`** is used to perform full structure relaxation
with medium precision, **`INCAR_4`** is used to perform very accurate calculations,
and **`INCAR_META`** is used to perform very accurate band gap calculations.

> INCAR_1

```text
SYSTEM local optimization
PREC = LOW
EDIFF = 3e-2
IBRION = 2
ISIF = 2
NSW = 40
ISMEAR = 0 ; SIGMA = 0.5
POTIM = 0.5
LWAVE = FALSE
LCHARG = FALSE
ISTART = 0
PSTRESS = 0.001
EDIFFG = -4e-2
```

> INCAR_2

```text
SYSTEM local optimization
PREC = Normal
EDIFF = 2e-2
IBRION = 2
ISIF = 4
NSW = 40
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.2
LWAVE = FALSE
LCHARG = FALSE
PSTRESS = 0.001
EDIFFG = -4e-1
```

> INCAR_3

```text
SYSTEM local optimization
PREC = Normal
EDIFF = 2e-4
IBRION = 1
ISIF = 3
NSW = 40
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.1
LWAVE = FALSE
LCHARG = FALSE
PSTRESS = 0.001
EDIFFG = 2e-3
```

> INCAR_4

```text
SYSTEM local optimization
ENCUT = 400
EDIFF = 1e-5
IBRION = 2
ISIF = 3
NSW = 80
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.1
LWAVE = FALSE
LCHARG = FALSE
PSTRESS = 0.001
EDIFFG = 2e-3
```

> INCAR_META

```text
SYSTEM local optimization
PREC = Accurate
ENCUT = 400
EDIFF = 1e-6
IBRION = -1
ISMEAR = -5 ; SIGMA = 0.05
METAGGA = MBJ
LASPH = .TRUE.
LMINTAU = .TRUE.
NELM = 80
NEDOS = 800
```

:::{hint}
Multi-optimization strategy for structure relaxation is strongly suggested
:::

**`POTCAR`** should be provided.

Meta-GGA calculations require POTCAR files containing information on the kinetic energy
density of the core-electrons. To check the pseudopotential file (*POTCAR*), please type:

```bash
grep kinetic POTCAR
```

This should yield at least the following lines (for each element on the file):

```text
kinetic energy-density
mkinetic energy-density pseudized
```

and for PAW datasets with partial core corrections:

```text
kinetic energy density (partial)
```

:::{important}
**ATTENTION!!!** The order of elements in POTCAR must be identical to the element order
in the setting tag of **NameOfAtoms**.
:::

**`submit.sh`** is the job submission file for performing the VASP calculations.
Here is an example of *submit.sh* (VASP.4.* version is not support META-GGA):

```bash
#!/bin/bash
mpdboot
mpiexec -n 12 vasp_std > vasp.log 2>&1
```

Once all input files are ready, you can just type

```bash
./calypso.x > caly.log &
```

to execute the CALYPSO in the sequential mode.
Or you can write this command into the *pbs* script and submit it.

CALYPSO will generate the **`results`** folder, which contains all outputs files.
To analyze the results of CALYPSO, just type following command:

```bash
cd results
cak.py --cif
```

The index of the structures sorted by band gap in the ascending order is presented in
**`Analysis_Output.dat`** file, and these newly predicted structure files with cif
format are shown in **`dir_0.1`** directory.

Please see [here](./_manuals.md#analysis-of-results) for more information about the analyses of CALYPSO results.

## Crystal Structure Prediction with Fixed Cell Parameters or Atomic Positions

This section is to show the examples for the three-dimensional crystal structure
prediction with fixed cell parameters or partial atomic positions using CALYPSO code.
Here, VASP code is used for geometry optimization and enthalpy calculations.

The CALYPSO input file of **`input.dat`** and VASP input files of **`INCAR_*`** and
pseudopotential file of **`POTCAR`** are needed.

The following files should be presented in the working directory:

| File      | Description                                                        |
|:----------|:-------------------------------------------------------------------|
| calypso.x | The executable file for running CALYPSO program                    |
| input.dat | The input file of CALYPSO containing controllable key parameters   |
| cell.dat  | The input file contains fixed cell parameters and atomic positions |
| INCAR_*   | Input files for VASP                                               |
| POTCAR    | Pseudopotential for VASP                                           |
| submit.sh | submission job file                                                |

**`calypso.x`** can be downloaded according to different operating systems.

Parameters in **`input.dat`** are shown as below:

```text
SystemName = SiC
NumberOfSpecies = 2
NameOfAtoms =  C Si
NumberOfAtoms = 4 4
NumberOfFormula = 1 1
@DistanceOfIon
 1.2 1.4
 1.4 1.4
@End
Ialgo = 2
PsoRatio = 0.6
PopSize = 5
ICode= 1
NumberOfLbest=4
NumberOfLocalOptim= 3
Command = sh submit.sh
FixCell= T
FixAtom= T
```

**`cell.dat`** file contains the fixed information of cell parameters and partial atomic positions.

In this example, the atomic positions of C are fixed.
The first three lines indicate the lattice matrix.
The forth line is the number of atoms to be fixed followed with the fixed coordinates of atomic positions.

```text
4.4   0.0   0.0
0.0   4.4   0.0
0.0   0.0   4.4
4   0
0.0   0.0   0.0
0.5   0.5   0.0
0.5   0.0   0.5
0.0   0.5   0.5
```

In this example, three INCAR files are used for structure relaxation:

**INCAR_1** and **INCAR_2** files are used to perform very coarse structure relaxation with
the fixed volume, and **INCAR_3** file is used to perform full structure relaxation
(i.e., variable lattice parameters, variable volumes, and variable atomic coordinates)
with medium and accurate precision, respectively.

> INCAR_1

```text
SYSTEM = optimization
PREC = LOW
EDIFF = 3e-2
SYMPREC = 1e-3
IBRION = 2
ISIF = 2
NSW = 45
ISMEAR = 1 ; SIGMA = 0.2
POTIM = 0.05
PSTRESS = 0.01
EDIFFG = -4e-2
```

> INCAR_2

```text
SYSTEM = optimization
PREC = Normal
EDIFF = 2e-2
SYMPREC = 1e-3
IBRION = 2
ISIF = 2
NSW = 55
ISMEAR = 1 ; SIGMA = 0.2
POTIM = 0.1
PSTRESS = 0.01
EDIFFG = -4e-1
```

> INCAR_3

```text
SYSTEM = optimization
PREC = Accurate
ENCUT = 520
EDIFF = 1e-5
IBRION = 2
ISIF = 3
NSW = 60
ISMEAR = 1 ; SIGMA = 0.2
POTIM = 0.05
PSTRESS = 0.01
EDIFFG = 1e-3
```

:::{hint}
Multi-optimization strategy for structure relaxation is strongly suggested
:::

**`POTCAR`** should be provided.

:::{important}
**ATTENTION!!!** The order of elements in POTCAR must be identical to the element order
in the setting tag of **NameOfAtoms**.
:::

**`submit.sh`** is the job submission file for performing the VASP calculations.
Here is an example of *submit.sh*:

```bash
#!/bin/bash
mpdboot
mpiexec -n 12 vasp_std > vasp.log 2>&1
```

Once all input files are ready, you can just type

```bash
./calypso.x > caly.log &
```

to execute the CALYPSO in the sequential mode.
Or you can write this command into the *pbs* script and submit it.

CALYPSO will generate the **`results`** folder, which contains all outputs files.
To analyze the results of CALYPSO, just type following command:

```bash
cd results
cak.py --cif
```

The index of the structures sorted by enthalpies in the ascending order is presented in
**`Analysis_Output.dat`** file, and these newly predicted structure files with cif
format are shown in **`dir_0.1`** directory.

Please see [here](./_manuals.md#analysis-of-results) for more information about the analyses of CALYPSO results.

## Structural Prediction via X-ray Diffraction Data

This section is to show the example for the structural prediction of ZnO via X-ray
diffraction data using CALYPSO code. Here, VASP code was used for geometry optimization
and enthalpy calculations.

The CALYPSO input file of **`input.dat`** and VASP input files of **`INCAR_*`** and
pseudopotential file of **POTCAR** are needed.

The following files should be present in the working directory:

| **Files** | **Description**                                                  |
|:----------|:-----------------------------------------------------------------|
| calypso.x | The executable file for running CALYPSO program                  |
| input.dat | The input file of CALYPSO containing controllable key parameters |
| INCAR_*   | Input files for VASP                                             |
| POTCAR    | Pseudopotential file for VASP                                    |
| submit.sh | Job submission file                                              |
| XRD.data  | The experimental XRD data                                        |

**`calypso.x`** can be downloaded according to different operating systems.

Parameters in the **`input.dat`** are shown below:

```text
SystemName = ZnO
NumberOfSpecies = 2
NameOfAtoms = Zn O
NumberOfAtoms = 1 1
NumberOfFormula = 2 2
Volume = 25.0
@DistanceOfIon
1.0 1.0
1.0 1.0
@End
Ialog = 2
PsoRatio = 0.6
PopSize = 30
ICode = 1
NumberOfLocalOptim = 3
Command = sh submit.sh
MaxStep = 30
LXRD = T
WaveLength = 1.54056
StepOf2Theta = 0.02
RangeOf2Theta = 20.0 80.0
StandardPeakPosition = 35.8 36.8
```

**`XRD.dat`** file contains the information of the experimental XRD data.
The values of the first row and second row are $2\theta$ and intensities of XRD, respectively.

```text
20.00    38.3014
20.02    38.3014
20.04    38.3014
...
```

For VASP, the number of **`INCAR_*`** (INCAR_1, INCAR_2, ...) files should be in
accordance with the setting tag **`NumberOfLocalOptim`**.

In this example, three INCAR files are used for structure relaxation:

**INCAR_1** and **INCAR_2** files are used to perform very coarse structure relaxation with
the fixed volume, and **INCAR_3** file is used to perform full structure relaxation
(i.e., variable lattice parameters, variable volumes, and variable atomic coordinates)
with medium and accurate precision, respectively.

> INCAR_1

```text
SYSTEM = optimization
PREC = LOW
EDIFF = 1e-2
IBRION = 2
ISIF = 2
NSW = 45
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.05
PSTRESS = 0.001
EDIFFG = -4e-1
```

> INCAR_2

```text
SYSTEM = optimization
PREC = Normal
EDIFF = 2e-3
IBRION = 2
ISIF = 4
NSW = 55
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.1
PSTRESS = 0.001
EDIFFG = -4e-1
```

> INCAR_3

```text
SYSTEM = optimization
PREC = Accurate
ENCUT = 520
EDIFF = 1e-4
IBRION = 2
ISIF = 3
NSW = 200
ISMEAR = 0 ; SIGMA = 0.05
POTIM = 0.05
PSTRESS = 0.001
```

:::{hint}
Multi-optimization strategy for structure relaxation is strongly suggested
:::

**`POTCAR`** should be provided.

:::{important}
**ATTENTION!!!** The order of elements in POTCAR must be identical to the element order
in the setting tag of **NameOfAtoms**.
:::

**`submit.sh`** is the job submission file for performing the VASP calculations.
Here is an example of *submit.sh*:

```bash
#!/bin/bash
mpdboot
mpiexec -n 12 vasp_std > vasp.log 2>&1
```

Once all input files are ready, you can just type

```bash
./calypso.x > caly.log &
```

to execute the CALYPSO in the sequential mode.
Or you can write this command into the *pbs* script and submit it.

CALYPSO will generate the **`results`** folder, which contains all outputs files.
To analyze the results of CALYPSO, just type following command:

```bash
cd results
cak.py --cif
```

The index of the structures sorted by enthalpies in the ascending order is presented in
**`Analysis_Output.dat`** file, and these newly predicted structure files with cif
format are shown in **`dir_0.1`** directory.

Please see [here](./_manuals.md#analysis-of-results) for more information about the analyses of CALYPSO results.

## Prediction of Transition States in Solids

This section is to show the example for the prediction of transition state of diamond
to b-Sn of Si using CALYPSO code.
Here, VASP code was used for enthalpy calculations.

The CALYPSO input file of **`input.dat`** and VASP input files of **`INCAR_1`** and
pseudopotential file of **`POTCAR`** are needed.

The following files should be present in the working directory:

| **Files**     | **Description**                                                  |
|:--------------|:-----------------------------------------------------------------|
| calypso.x     | The executable file for running CALYPSO program                  |
| input.dat     | The input file of CALYPSO containing controllable key parameters |
| INCAR_1       | Input files for VASP                                             |
| POTCAR        | Pseudopotential file for VASP                                    |
| submit.sh     | Job submission file                                              |
| IF_struct.dat | The structures of initial and final states                       |

**`calypso.x`** can be downloaded according to different operating systems.

Parameters in **`input.dat`** are shown below:

```text
SystemName = Si
NumberOfSpeceis = 1
NameOfAtoms = Si
NumberOfAtoms = 8
NumberOfFormula = 1 1
Volume = 35.0
@DistanceOfIon
1.0
@End
Ialgo = 1
PsoRatio = 0.6
PopSize = 6
ICode = 1
Command = sh submit.sh
MaxStep = 30
LTranState = T
NumberOfImages = 3
```

**`IF_struct.dat`** file contains the structural information of initial and final states.

Here we take phase transition of diamond to b-Sn in Si as an example. The structural
information of initial state is followed by the structure of final state.

The format of each structure in *IF_struct.dat* file is the same with that used in VASP code:

- the first line is treated as a comment line
- the second line provides a universal scaling factor to scale all lattice vectors
  (the value is set to 1.0 in our module).
- the following three lines are three lattice vectors defining the unit cell of the
  system (first line corresponding to the first lattice vector, second to the
  second, and third to the third)
- the sixth line supplies the number of atoms per atomic species (one number for each
  atomic species), and the ordering must be consistent with the POTCAR
- the seventh line ("Direct") specifies the atomic position are provided in fractional coordinates
- the next lines give the three coordinates for each atom

```text
Si-initial state
  1.0
    5.46668 0.0     0.0
    0.0     5.46668 0.0
    0.0     0.0     5.46668
  8
Direct
  0.25    0.25    0.25
  0.75    0.75    0.25
  0.75    0.25    0.75
  0.25    0.75    0.75
  0.0     0.0     0.0
  0.0     0.5     0.5
  0.5     0.0     0.5
  0.5     0.5     0.0
Si-final state
  1.0
    4.68599 0.0     0.0
    0.0     4.69686 0.0
    0.0     0.0     5.16999
  8
Direct
  0.0     0.5     0.125
  0.5     0.5     0.25
  0.0     0.0     0.0
  0.5     0.0     0.875
  0.5     0.5     0.75
  0.0     0.0     0.5
  0.5     0.0     0.375
  0.0     0.5     0.625
```

In this example, VASP code is used for structure relaxation, one input file
**`INCAR_1`** is needed:

> INCAR_1

```text
SYSTEM = scf
PREC = Accurate
NSW = 1
IBRION = -1
EDIFF = 1e-3
ISMEAR = 1 ; SIGMA = 0.2
PSTRESS = 0.001
```

**`POTCAR`** should be provided.

:::{important}
**ATTENTION!!!** The order of elements in POTCAR must be identical to the element order
in the setting tag of **NameOfAtoms**.
:::

**`submit.sh`** is the job submission file for performing the VASP calculations.
Here is an example of *submit.sh*:

```bash
#!/bin/bash
mpdboot
mpiexec -n 12 vasp_std > vasp.log 2>&1
```

Once all input files are ready, you can just type

```bash
./calypso.x > caly.log &
```

to execute the CALYPSO in the sequential mode.
Or you can write this command into the *pbs* script and submit it.

CALYPSO will generate the **`results`** folder, which contains all outputs files.
To analyze the results of CALYPSO, just type following command:

```bash
cd results
cak.py --cif
```

The index of the structures sorted by enthalpies in the ascending order is presented in
**`Analysis_Output.dat`** file, and these newly predicted structure files with cif
format are shown in **`dir_0.1`** directory.

Please see [here](./_manuals.md#analysis-of-results) for more information about the analyses of CALYPSO results.

## Accelerating Structure Prediction by Machine Learning Potentials (MLP)

This section is to show the example for accelerating CALYPSO structure prediction by
Machine Learning Potentials (MLP).

The following files will be used in this part:

| **Files**      | **Description**                                                                                                            |
|:---------------|:---------------------------------------------------------------------------------------------------------------------------|
| calypso.x      | The executable file for running CALYPSO program                                                                            |
| input.dat      | The input file of CALYPSO containing controllable key parameters                                                           |
| get_vasp.py    | Python script that extracts structural information (structure, energy, atomic force and cell stress) from VASP OUTCAR file |
| config/test    | The training/testing data set file for fitting MLP                                                                         |
| neural.in      | The parameters of atom-centered symmetry function                                                                          |
| gap_parameters | The parameters of machine learning potential                                                                               |
| cgg2.py        | The Python script used for controlling all prediction process                                                              |

For accelerating CALYPSO structure prediction by MLP, you only need three steps:

1. Constructing training (and testing) data set
2. Fitting MLP
3. Accelerating CALYPSO by well-trained MLP

### Constructing training (and testing) data set

**`config`**
: Structural information used for training MLP

**`test`** (optional)
: Structural information used for testing the precision and transferability of MLP

For constructing the *config/test* file, you need to prepare a lot of **`OUTCAR`** files
named as **`OUTCAR_*`** (* means arbitrary string you want) in one directory:

```text
get_vasp.py OUTCAR_1 OUTCAR_2 ...
```

Then using this command to obtain the *config/test* file:

```bash
python get_vasp.py
```

### Fitting MLP

For fitting MLP, the following files should be present in the working directory:

```text
calypso.x config test input.dat neural.in
```

and the following parameters should be modified in **`input.dat`**.

MLP_IMODE : int, optional, default 0
: must be set to 2 for fitting MLP

NumberOfSpecies : int
: number of atomic species

NameOfAtoms: string
: element symbols

WeightOfAtoms : list[float]
: weight of each atomic species in calculating atom centered symmetry function (ACSF)

Rcut : float, optional, default 6.0
: defines the spherical region in calculating atomic neighboring list (unit: $\mathring{A}$)

SigmaE : float, optional, default 0.001
: relative weight of energy in fitting MLP

SigmaF : float, optional, default 0.01
: relative weight of atomic force in fitting MLP

SigmaS : float, optional, default 0.01
: relative weight of cell stress in fitting MLP

Ltrain : logical, optional, default True
: whether fitting MLP using config file

Ltest : logical, optional, default True
: whether testing MLP using test file

Lstress : logical, optional, default True
: whether include information of cell stress in fitting MLP

Isparse : int, optional, default 3
: sparse method in Gaussian process, currently 3 is supplied only

Sparsecut : float, optional, default 1.0
: threshold value of distance between two atomic feature vectors in sparse process

With our experience, there is no need to modify **`neural.in`** for different elementary or binary system.

Once all the input files are ready, run

```bash
./calypso.x
```

and drink a cup of tea.

After it finished successfully, you will get the parameter file of MLP **`gap_parameters`**
and the predicted results **`predicted.dat`** on test file using fitted MLP.

### Structure prediction assisted by MLP

If you have fitted the MLP which reached required accuracy, you could accelerate
structure prediction by this MLP.

The following files should be present in the working directory:

```text
input.dat gap_parameters cgg2.py
```

and the following parameters should be modified in input.dat:

:Split: logical, must be set to True, default False
:NumberOfParallel: int, number of structural optimization tasks which could be run in parallel.
  For convenience, *PopSize* should be divisible by *NumberOfParallel*, default 20
:CALYPSO_PATH: string, absolute path of calypso.x
:GAPP_PATH: string, absolute path of *gap_parameters*
:Pstress: float, external pressure in structural optimization (Unit: GPa)
:Ftol: float, break condition of energy (Unit: eV), default 0.0005
:Gtol: float, break condition of the gradient of energy (Unit: eV/$\mathring{A}$), default 0.005
:Maxcycle: int, maximum number of structural optimization tasks, default 200
:MaxTime: float, maximum time of structural optimization tasks (Unit: s), default 1000

Once all input files are ready, type the following command:

```bash
nohup python cgg2.py > caly.log &
```

The output files are similar to the normal CALYPSO structure prediction.

Please see [here](./_manuals.md#analysis-of-results) for more information about the analyses of CALYPSO results.
