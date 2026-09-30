# About CALYPSO Program

## Program Features

- Predictions of the energetically stable/metastable structures at given chemical
  compositions and external conditions (e.g., pressure) for 0D nanoparticles or
  clusters, 2D layers and its atom adsorption, 2D surface reconstructions, and 3D crystals.
- Functionality-driven design of novel functional materials, e.g., superhard materials,
  electrides, and optical materials with desirable hardness values, electron localization
  functions, and energy band gap, respectively.
- Options for the structural evolutions using global or local PSO techniques.
- Structure predictions with automatic variation of chemical compositions.
- Incorporation of various structure constraints, e.g., fixed rigid molecules, fixed
  cell parameters, fixed space group or fixed atomic positions.
- X-ray diffraction data assisted structural prediction.
- Prediction of transition states in solids.
- CALYPSO is currently interfaced with VASP, CASTEP, Quantum Espresso, GULP, SIESTA,
  FPLO, Gaussian, CP2K, LAMMPS, and ABACUS codes for local geometrical optimization and
  total-energy calculations.
  Its interface with other codes can also be implemented by users’ request.
- It is written in Fortran 90 and memory is allocated dynamically.

## Major Techniques

The success of CALYPSO method is on account of its efficient integration of several major structure dealing techniques.

1. Structural evolution through PSO algorithm. PSO is best known for its ability to overcome large barriers of energy landscapes by making use of the smart structure self-learning within swarm intelligence algorithm. Both global and local PSO algorithms have been implemented. The global PSO has the advantage of fast convergence, while local PSO is good at avoiding structure premature ready for dealing with complex systems.
2. Symmetry constraints on generation of random structures to ensure the creation of physically feasible structure, reduce searching space, and enhance the structural diversity during evolution.
3. Two structural characterization techniques for eliminating similar structures, and partitioning energy surfaces for local PSO structure searches.
   1. bond characterization matrix technique
   2. atom-centered symmetrical function technique
4. Introduction of random structures per generation with controllable percentage to enhance structural diversity during evolution.
5. Interface to a number of local structural optimization codes varying from highly accurate DFT methods to fast semi-empirical approaches that can deal with large systems. Local structural optimization is the most time-consuming part of CALYPSO structure prediction. This is a must process since it enables the reduction of noise of energy surfaces and the generation of physically justified structures.

**CALYPSO routinely provides:**

- [Crystal structure prediction](./_examples.md#crystal-structure-prediction)
- [2-dimensional layer structure prediction](./_examples.md#two-dimensional-structure-prediction)
- [Clusters or nanoparticles structure prediction](./_examples.md#cluster-structure-prediction)
- [Molecular crystal structure prediction](./_examples.md#molecular-structure-prediction)
- [Surface reconstruction structure prediction](./_examples.md#surface-structure-prediction)
- [Inverse structural design of superhard materials](./_examples.md#design-of-superhard-materials)
- [Structural design of 2D material with atoms adsorption](./_examples.md#structure-prediction-of-atom-or-molecule-adsorption-of-2d-layer-material)
- [Inverse structural design of optical materials](./_examples.md#design-of-optical-materials-with-desirable-electronic-band-gap)
- [X-ray diffraction data assisted structural prediction](./_examples.md#structural-prediction-via-x-ray-diffraction-data)
- [Prediction of transition states in solids](./_examples.md#prediction-of-transition-states-in-solids)

For more details on the methodologies and formalisms of CALYPSO,
please read the references cited below.

## References

- **CALYPSO Software:**

[Yanchao Wang, Jian Lv, Li Zhu, and Yanming Ma\*, *CALYPSO: A Method for Crystal Structure Prediction*, **Comput. Phys. Commun.** 183, 2063 (2012)](http://www.sciencedirect.com/science/article/pii/S0010465512001762)

- **Crystal Structure Prediction:**

[Yanchao Wang, Jian Lv, Li Zhu and Yanming Ma\*, *Crystal structure prediction via particle-swarm optimization,* **Phys. Rev. B** 82, 094116 (2010)](http://prb.aps.org/abstract/PRB/v82/i9/e094116)

- **Cluster Structure Prediction:**

[Jian Lv, Yanchao Wang, Li Zhu, and Yanming Ma\*, *Particle-swarm structure prediction on clusters*, **J. Chem. Phys.** 137, 084104 (2012)](http://jcp.aip.org/resource/1/jcpsa6/v137/i8/p084104_s1)

- **Two-Dimensional Layer Structure Prediction:**

1. [Xinyu Luo, Jihui Yang, Hanyu Liu, Xiaojun Wu, Yanchao Wang, Yanming Ma, Su-Huai Wei, Xingao Gong, and Hongjun Xiang, *Predicting Two-Dimensional Boron-Carbon Compounds by the global optimization method.* **J. Am. Chem. Soc.** 133, 16285(2011)](http://pubs.acs.org/doi/abs/10.1021/ja2072753)

2. [Yanchao Wang, Maosheng Miao, Jian Lv, Li Zhu, Ketao Yin, Hanyu Liu, and Yanming Ma\*, *An effective Structure Prediction Method for Layered Materials Based on 2D Particle Swarm Optimization Algorithm*, **J. Chem. Phys.** 137, 224108 (2012)](http://jcp.aip.org/resource/1/jcpsa6/v137/i22/p224108_s1)

- **Inverse Design of Superhard Materials:**

[Xinxin Zhang, Yanchao Wang, Jian Lv, Chunye Zhu, Qian Li, Miao Zhang, Quan Li and Yanming Ma\*, *First-Principles Structural Design of Superhard Materials*, **J. Chem. Phys.** 138, 114101 (2013)](http://jcp.aip.org/resource/1/jcpsa6/v138/i11/p114101_s1)

- **Surface Reconstruction Structure Prediction:**

[Shaohua Lu, Yanchao Wang, Hanyu Liu, Maosheng Miao and Yanming Ma\*, *Self-assembled ultrathin nanotubes on diamond (100) surface*, **Nat. Commun.** 5, 3666 (2014)](http://www.nature.com/ncomms/2014/140416/ncomms4666/full/ncomms4666.html)

- **Structural design of 2D material with atoms adsorption:**

[Bo Gao, Xuecheng Shao, Jian Lv, Yanchao Wang\* and Yanming Ma\*, *Structure Prediction of Atoms Adsorbed on Two-Dimensional Layer Materials: Method and Applications,* **J. Phys. Chem. C** 119, 20111 (2015)](https://pubs.acs.org/doi/10.1021/acs.jpcc.5b05035)

## Bug Report

The CALYPSO package has been thoroughly tested for numerous systems by the CALYPSO team and
other users, and has been progressively improved by adding new features and eliminating bugs.

We would greatly appreciate comments, suggestions and criticisms by the users of CALYPSO.

For bug report, the users can contact the authors and send a copy of both
input and output by E-mail to the Ma group <calypso@calypso.cn>.
