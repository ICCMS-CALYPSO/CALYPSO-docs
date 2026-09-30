# CALYPSO as a library

Now one can use calypso in a pythonic way.

## Generator structures with python interface

```python
import numpy as np
from calypso.generators.crystal_generator import FortranBulk 

amounts_of_element = [4, 4, 12]
volume = 40
element_wise_min_distance = np.ones((3, 3))
sg_number = 216
bulk = FortranBulk(
    group_number=sg_number,
    volume=volume,
    element_numbers=[57, 26, 8],
    amounts_of_bbs=amounts_of_element,
    bbwise_min_distance=element_wise_min_distance,
)
(
    lattice_matrix,
    frac_coords,
    element_numbers,
) = bulk()
```

## Using BCM module to calculate the fingerprint
```python
from calypso.descriptors.BondCharMatrix import Descriptor as BCMDescriptor
from calypso.data import CalyData


calydata_1 = CalyData(
    symbols=[1, 3, 1, 3],
    lattice=[[1.5, 0, 0], [1.5, 2, 0], [0, 0, 3]],
    cartpos=[[0, 0, 0], [0.5, 0.5, 0], [0, 0, 0.6], [0, 0.6, 0]],
    )
bcm_1 = get_BondCharMatrix(calydata_1)

calydata_2 = CalyData(
    symbols=[1, 3, 1, 3],
    lattice=[[1.5, 0, 0], [1.5, 2, 0], [0, 0, 3]],
    cartpos=[[0, 0, 0], [0.5, 0.5, 0], [0, 0, 0.6], [0, 0.6, 0]],
    )
bcm_2 = get_BondCharMatrix(calydata_2)

des = Descriptor(simthreshold=0.1)
dist_list, sim_list = des.equal(calydata_1, calydata_2)
```

## IO module

```python
from calypso.io.vasp import Poscar

calydata = Poscar.from_file("POSCAR")
calydata = Poscar.from_str(poscar_str)

poscar = Poscar(calydata)
poscar.write_file("file_name.vasp")


from calypso.io.vasp import Outcar

outcar = Outcar.from_file("OUTCAR")
last_frame = outcar.get_calydata(index=-1)
first_frame = outcar.get_calydata(index=0)
all_frame = outcar.get_calydata(index=":")
slice_frames = outcar.get_calydata(index=slice(1, 3, 4))

from calypso.io.extxyz import Extxyz
xyzs = Extxyz.from_file("example.xyz")
last_frame = xyzs.get_calydata(index=-1)
first_frame = xyzs.get_calydata(index=0)
all_frame = xyzs.get_calydata(index=":")
slice_frames = xyzs.get_calydata(index=slice(1, 3, 4))
```

## Dispatcher module

```python
from dataclasses import asdict
from pathlib import Path
from threading import Thread

from calypso.dispatchers.orchestrator.jobs import Job
from calypso.dispatchers.orchestrator.machine import Machine, MachineData
from calypso.dispatchers.orchestrator.orchestrator import Orchestrator

machine_data = MachineData(
    name="test_machine",
    executor="Local",
    scheduler="Shell",
    numb_node=1,
    numb_cpu_per_node=1,
    machine_capacity=1,
    group_size=1,
    remote_root=str(self.test_dir),
    envs="",
    source="",
    module="",
    queue="",
)
machines = [Machine(machine_data)]

# Initialize Orchestrator
with Orchestrator(
    machinelist=[asdict(machine_data)],
    timeinternal=1,
    maxjobnumb=20,
    pickup=False,
) as orchestrator:
    job = Job(
        name="job1-same-local-remote",
        command="touch job1_output.txt",
        local_root=str(test_dir),
        local_work_dir="work_dir",
        remote_root=str(test_dir),
        remote_work_dir="work_dir",
        upload_files=["file1.txt"],
        upload_share_files=[f"{file3_txt.absolute()}"],
        download_files=["job1_output.txt"],
    )
    orchestrator.orchestrate(job, wait=True)
    # Check if jobs are in the collection and queue
    # self.assertEqual(len(orchestrator.job_collection), 1)
```

## Convexhull

```python
from calypso.tools.convexhull import Entry, Entries, PhaseDiagram
from calypso.formula import Formula

entries = [
    Entry("H2", 0),
    Entry("O2", 0),
    Entry("H2O", -3.0),
    Entry("H2O2", -4.0),
]

entries = Entries(
    [
        Entry("H2", 1.3, label="x1"),
        Entry(Formula("CaO"), 2.3, label="x2"),
    ]
)

entries = Entries.from_file("ref_ene_file.txt")

phasediagram = PhaseDiagram(entries)

phase_dim = phasediagram.phase_dim
element_dim = phasediagram.element_dim
form_energy = phasediagram.get_formation_energy(Entry("H2O", 0))
energy_above_hull = phasediagram.get_energy_above_hull(Entry("H2O", 0))
```

## Evolution structure with PSO

```python
from calypso.io.vasp import Outcar
from calypso.evolution.pso import PBest, Gbest
from calypso.evolution.pso.crystal_pso import Evolution
from calypso.descriptors.BondCharMatrix import Descriptor

popsize = 10
nbest = 3
simthreshold = 0.1

descriptor = Descriptor(simthreshold=simthreshold)
pbest=PBest(popsize=popsize),
gbest=GBest(nbest=nbest, descriptor=descriptor),

evolutioner = Evolution(
                  pbest=pbest,
                  gbest=gbest,
                  descriptor=descriptor,
                  fitness_name="ENTHALPY",
                  ialgo="LPSO",
                  distanceofion={"La": 0.5, "H": 0.5},
                )

ini_calydata_list = [Poscar.from_file(f"POSCAR_{i}").calydata for i in range(1, 11)]
opt_calydata_list = [Outcar.from_file(f"OUTCAR_{i}").get_calydata(-1) for i in range(1, 11)]
for idx, opt_calydata in enumerate(opt_calydata_list):
    opt_calydata.caly_idx = idx
    pbest.update_pbest(opt_calydata)
    gbest.update_gbest(opt_calydata)
calydata_list = list(zip(ini_calydata_list, opt_calydata_list))

refer_entries = (
    Entries.from_file(REF_ENE_FILE)
    if REF_ENE_FILE.exists()
    else None
)
determined_calydata_list = evolutioner.determine_group(
    calydata_list=calydata_list,
    refer_entries=refer_entries,
    reverse=False,
)

evolution_calydata_list = []
for ini_calydata, opt_calydata in determined_calydata_list:
    pbest_calydata = pbest.get_pbest(calydata=opt_calydata)
    gbest_calydata = gbest.get_best(calydata=opt_calydata)
    calydata = evolutioner.generate(
      ini_calydata=ini_calydata,
      opt_calydata=opt_calydata,
      pbest_calydata=pbest_calydata,
      gbest_calydata=gbest_calydata,
    )
    evolution_calydata_list.append(calydata)
```
