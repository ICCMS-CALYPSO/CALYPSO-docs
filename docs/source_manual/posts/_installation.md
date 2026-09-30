# Installation

CALYPSO requires python>=3.11. It is strongly suggested to create a python virtual environment before installing.

```bash
conda create -n calypso python=3.11
conda activate calypso
```

## Installation from precompiled packages (wheel)

Download the compatible package according to your system. Mind these markers:

    OS: x86_64
    Python interpreter: cp311|cp312(CPython)
    Precompiling fortran compiler: gfortran|ifort|ifx
    GLIBC version: glibcXXX or manylinuxXXX

An example of the wheel package:

`calypso-<version>+gfortran11_4_0-cp311-cp311-manylinux_2_35_x86_64.whl`

### Minimal installation

We are trying to minimize the dependencies but the following third-party packages are still needed:

```
paramiko
monty
numpy<2
scipy
spglib
sqlalchemy>=2.0.25
```

If your machine has internet access, execute

```bash
pip install calypso-xxx.whl
```

will automatically download dependencies.

If internet access is not available, please refer to [offline installation](#offline-installation).

### [Optional] Pytorch Installation

CALYPSO integrated some machine learning models which requires pytorch and other requirements. The models are:

1. **`[TBD]`** a structure synthetic possibility prediction model.
2. **`CrystalFlow`** a flow-based generative model for crystalline materials.
3. **`Cond-CDVAE`** a crystal structure generation model by given formula and pressure.

If you intend to use them, the following additional requirements are required:

**`torch2.0.2+cpu`**
```
# requirements-torch20cpu.txt
-f https://download.pytorch.org/whl/torch_stable.html
-f https://data.pyg.org/whl/torch-2.0.0+cpu.html
ase>=3.22.1
pymatgen>=2023.3.23
numpy<2
hydra-core>=1.3.2
joblib>=1.1.1
networkx>=2.8.4
scikit-learn>=1.2.1
omegaconf>=2.3.0
tqdm>=4.65.0
p_tqdm
aviary @ https://github.com/CompRhys/aviary/archive/refs/tags/v1.0.0.zip

torch==2.0.1+cpu
lightning>=2.3,<2.4 ; python_version>="3.8" and python_version<="3.11"
torch_geometric>=2.3.0
pyg_lib
torch_scatter
torch_sparse
torch_cluster
torch_spline_conv
```

**`torch2.0.1+cu118`**
```
# requirements-torch20cu118.txt
-f https://download.pytorch.org/whl/torch_stable.html
-f https://data.pyg.org/whl/torch-2.0.0+cu118.html
ase>=3.22.1
pymatgen>=2023.3.23
numpy<2
hydra-core>=1.3.2
joblib>=1.1.1
networkx>=2.8.4
scikit-learn>=1.2.1
omegaconf>=2.3.0
tqdm>=4.65.0
p_tqdm
aviary @ https://github.com/CompRhys/aviary/archive/refs/tags/v1.0.0.zip

torch==2.0.1+cu118
lightning>=2.3,<2.4 ; python_version>="3.8" and python_version<="3.11"
torch_geometric>=2.3.0
pyg_lib
torch_scatter
torch_sparse
torch_cluster
torch_spline_conv
```

**`torch2.1.2+cu121`**
```
# requirements-torch21cu121.txt
-f https://download.pytorch.org/whl/torch_stable.html
-f https://data.pyg.org/whl/torch-2.1.0+cu121.html
ase>=3.22.1
pymatgen>=2023.3.23
numpy<2
hydra-core>=1.3.2
joblib>=1.1.1
networkx>=2.8.4
scikit-learn>=1.2.1
omegaconf>=2.3.0
tqdm>=4.65.0
p_tqdm
aviary @ https://github.com/CompRhys/aviary/archive/refs/tags/v1.0.0.zip

torch==2.1.2+cu121
lightning>=2.4,<2.5 ; python_version>="3.9" and python_version<="3.12"
torch_geometric>=2.3.0
pyg_lib
torch_scatter
torch_sparse
torch_cluster
torch_spline_conv
```

Choose one above according to your device and write to file `dep.txt`, then

```bash
pip install -r dep.txt
```

> If you'd like to reinstall the dependencies, uninstall the old ones first:
> ```bash
> pip uninstall torch lightning torch_geometric pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv
> ```

You may refer to [lightning compatibility matrix](https://lightning.ai/docs/pytorch/stable/versioning.html#compatibility-matrix) for more compatibility information.


### Offline Installation

download the requirements (from machine with the same platform and python version of target offline machine) and copy to target offline machine

assume you already have `calypso-xxx.whl`

```bash
mkdir deps
pip download calypso-xxx.whl -d deps
cp calypso-xxx.whl deps
zip -qr deps.zip deps
```

install the dependencies on target offline machine

```bash
unzip -q deps.zip
pip install deps/*.whl
```

## Test Installation

To verify your installation, one can simply run the commands:

```bash
> calypso.x --help
usage: calypso.x [-h] [--config CONFIG] [-v] [--seed SEED]

options:
  -h, --help       show this help message and exit
  --config CONFIG
  -v               verbose info
  --seed SEED      random seed
```

Other examples are provided in the "path-to-package/Examples" directory.
This directory contains basic input.dat and shell scripts for running CALYPSO.
It is advisable to create independent directory for each job, making a clean and neat environment.
