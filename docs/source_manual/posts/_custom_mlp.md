# User-provided MLP optimization scripts

Use `ICode = "MLP"` and `MLPType = "custom"` to run a potential that is not
implemented by CALYPSO. Supply a complete optimization script through the
existing `CustomizableScript` interface. No calculator factory or backend code
needs to be written by the user.

## Configuration

The following entries belong in `[CALYPSO.OPT]` in a TOML input file:

```toml
MLPType = "custom"
CustomizableScript = "/absolute/path/my_mlp_run.py"
RunCustomizableScriptCMD = "/path/to/mlp_env/bin/python my_mlp_run.py > opt.log 2>&1"
ShareFiles = ["/absolute/path/my_model.pt"]
```

`CustomizableScript` must be an existing file with an absolute source path.
`RunCustomizableScriptCMD` must invoke its basename, as the script is copied to
and executed inside each task's working directory. The specified interpreter
must be available on the execution machine and contain the user's model
packages and script dependencies. `$CALYPSO_MLP_CMD` may also be used when it is
configured in the machine environment.

Custom mode prepares the normal initial structure and bookkeeping files, but
**does not generate or upload** `calypso_run_mlp.py`, `calypso_check_mlp.py`, or
the default run-flow script. The executor copies the supplied script separately.
A user script may therefore also be named `calypso_run_mlp.py` without being
overwritten by generated code. Input and result filenames such as
`caly_ini.xyz`, `POSCAR`, and `caly_opt.pkl` are reserved.

`MLPKwargs`, `OptAlgo`, `OptStep`, `Fmax`, `Pstress`, `MLPKeepSym`, `UCFMask`, and
`TrajFile` are **not injected into the user script**. Set the model parameters,
optimizer, pressure, symmetry handling, and trajectory filename in your script.
In particular, record the pressure actually used in `pullay_stress` in the result.
This mode currently applies to the MLP calculator, not the MLP+VASP calculator.

## Model and support files

Put each required model file or auxiliary file in `ShareFiles` using an absolute
source path. Files must exist and have distinct basenames when they refer to
different sources. Their basenames must not conflict with the custom script,
reserved input/output files, or declared `UploadFiles`.

The MLP calculator stages these files in the shared task directory. It compares
file sizes and SHA256 hashes, reuses identical copies, and publishes changed
copies through an atomic replacement. Local execution creates symlinks in each
task directory. SSH execution uploads shared files to the remote shared
directory and creates task symlinks. Load files by basename in the script:

```python
calc = MyCalculator(model="my_model.pt")
```

Keep the original model files unchanged during preparation and execution.
Directory paths are not supported in `ShareFiles` for custom mode. For a model
stored as a directory, arrange for that directory to be accessible on every
execution machine and load it explicitly from the user script. Installed or
pretrained models requiring no staged file can leave `ShareFiles` empty.

Additional task inputs can use the existing `UploadFiles` mechanism. Additional
results can be added to `DownloadFiles`.

## Script input and output contract

Start from an existing generated `calypso_run_mlp.py` for the intended structure
kind. Replace its model import and calculator initialization, and retain the
structure handling and output format. The crystal, cluster, layer, and
surface/interface scripts have different optimization and constraint handling;
the example below is a **crystal** example.

The default inputs uploaded for custom mode are:

- `caly_ini.xyz`: initial structure in extended XYZ format.
- `POSCAR`: the same initial structure in VASP format.

The script must produce all three default result files:

- `traj.traj`: ASE trajectory.
- `caly_opt.xyz`: optimized structure in extended XYZ format.
- `caly_opt.pkl`: pickled dictionary read by `MLPCalculator.after_calculation`.

Keep these names even if you also write other output formats. The dictionary
uses the same fields as the generated MLP script:

| Field | Meaning and units |
| --- | --- |
| `symbols` | List of element symbols, one per atom. |
| `lattice` | 3 x 3 cell matrix, in angstrom. |
| `cartpos` | N x 3 Cartesian positions, in angstrom. |
| `force` | N x 3 forces, in eV/angstrom. |
| `volume` | Cell volume, in angstrom cubed. |
| `energy` | Total energy of the structure, in eV. |
| `stress` | Stress in GPa, normally ASE Voigt order: xx, yy, zz, yz, xz, xy. |
| `enthalpy` | Total enthalpy of the structure, in eV. |
| `pullay_stress` | Applied external pressure, in GPa; the existing key spelling is retained. |
| `opt_setting` | Optimization metadata, including `mlp_opt_state`, `optimizer`, `fmax`, `converge`, and `time_consuming`. |

When using ASE, calculator stress is normally in eV/angstrom cubed. Preserve the
conversion to GPa used by the generated script before writing `stress`.
The total energy must not be replaced with energy per atom. CALYPSO reads the
result through its existing result reader and restores its tags and PSO
bookkeeping from the files prepared on the controlling machine.

## Runnable example

See `example/crystal-mlp/local_shell_toml_custom/` in the repository. It includes:

- `input.toml` and `machine-1.json` for a small local crystal search.
- `my_mlp_run.py`, a complete script based on the generated crystal MLP script.
- `lj_model.json`, Lennard-Jones parameters loaded through `ShareFiles`.

This is an interface demonstration using ASE's Lennard-Jones calculator, not a
trained machine-learning potential. It needs ASE and NumPy in the worker
interpreter. Replace the initialization block with your own potential when
adapting it.

Copy the example to a working directory, update the two absolute source paths
in `input.toml`, and set `RunCustomizableScriptCMD` to the desired interpreter.
Then run from that directory:

```bash
calypso.x -c input.toml
```

The included Python script fixes its own optimization settings near the final
`run_opt` call; its cell mask is set inside the function. Change those settings
in the script when adapting the example.
