# Introduction

CALYPSO is a swarm-intelligence based structure prediction method and its same-name computer software.
The approach requires only chemical compositions of given compounds to predict stable or
metastable structures at certain external conditions (e.g., pressure).
The method can also be used to inversely design multi-functional materials (e.g.,
superhard materials, electrides, optical materials, etc.).
The CALYPSO package is protected by the Copyright Protection Center of China with the
Registration No. 2010SR028200 and Classification No. 61000-7500.

## Meaning of CALYPSO

CALYPSO is a short name of "**C**rystal structure **A**na**LY**sis by **P**article
**S**warm **O**ptimization".
It was originally designed to predict 3-dimensional (3D) "crystal structures".
Now, CALYPSO has a more generalized meaning of "structure" prediction, able to deal
with structures ranging from 0D to 1D, 2D, and 3D.

"CALYPSO" (with all capitalized letters) is the only name in the field of structure prediction.
But the word "Calypso" has diverse meanings.
Calypso is the name of one of the Nereids (sea nymphs) in Greek mythology.
Calypso also refers to companies, music, places, etc.
Have a look at [Wikipedia](http://en.wikipedia.org/wiki/Calypso).

CALYPSO structure prediction software takes the advantage of structure evolution via PSO
algorithm, one of swarm intelligence schemes.
However, many other efficient structure-dealing techniques (e.g., symmetry constraints,
bond characterization matrix, introduction of random structures per generation, etc.)
were also implemented in CALYPSO.
We found that all these techniques implemented are equivalently important for the
structure searching efficiency.
It is therefore more appropriate to name the developed structure prediction method as a
"CALYPSO" method.

## Why PSO?

As an unbiased global optimization method, PSO is inspired by the choreography of a
bird flock and can be viewed as a distributed behavior algorithm that performs
multidimensional search (see, e.g., Kennedy & Eberhart 1995 [^PSO_1995]).
PSO is metaheuristic as it makes few or no assumptions about the solutions and can
search very large spaces of candidate solutions (dubbed as particles) by moving them in
the search-space based on efficient algorithms over the particle's position and velocity.

We quote from website of <http://www.swarmintelligence.org>.

PSO has been successfully applied in many research and application areas.
It is demonstrated that PSO can get better results in a faster, cheaper way compared
with other methods.

Another reason that PSO is attractive is that there are few parameters to adjust.
One version, with slight variations, works well in a wide variety of applications.
PSO has been used for approaches across a wide range of applications, as well as for
specific applications focused on a specific requirement.

## History of PSO on Structure Prediction

Although PSO algorithm has been employed to various optimization problems, the
application of PSO in structure prediction started only recently.
It was attempted for isolated systems (small clusters and molecules) by
Call, Zubarev & Boldyrev in 2007 [^Call_2007].
However, this effort did not lead to any practical application.

The CALYPSO team independently initialized the idea of applying PSO algorithm into
structure prediction in 2006 (Ma and Wang) before Call *et al.*'s work and made the
first application of PSO algorithm into structure prediction of extended systems
(e.g., 3D crystals by Wang, Lv, Zhu & Ma in 2010 [^crystal_2010],
2D layers by Luo *et al.,* in 2011 [^2d_layer_2011]
and Wang et al., in 2012 [^crystal_2012],
2D surface reconstruction by Lu et al., in 2014 [^2d_surface_2014],
2D atoms adsorbed on layer materials by Gao et al., in 2015 [^2dadsorbed_2015]).
Structure searching efficiencies of isolated systems have been substantially improved
by the CALYPSO team (Lv, Wang, Zhu & Ma in 2012 [^cluster_2012]), where the success of
this application has been backed up with the introduction of various efficient
techniques (e.g., bond characterization matrix for fingerprinting structures, symmetry
constraints on structure generation, etc.).

[^PSO_1995]: [Kennedy, J. and Eberhart, R., *Particle Swarm Optimization*, **Proceedings of the IEEE International Conference on Neural Networks**, 4, 1942-1948 (1995)](https://www.semanticscholar.org/paper/Particle-swarm-optimization-Poli-Kennedy/b7919bcfa38aa97514187501a23c983e8eb5482b)

[^Call_2007]: [Seth T. Call, Dmitry Yu. Zubarev, Alexander I. Boldyrev\*, *Global minimum structure searches via particle swarm optimization*, **J. Comput. Chem.**, 28, 1177 (2007)](https://doi.org/10.1002/jcc.20621)

[^crystal_2010]: [Yanchao Wang, Jian Lv, Li Zhu and Yanming Ma\*, *Crystal structure prediction via particle-swarm optimization,* **Phys. Rev. B** 82, 094116 (2010)](http://prb.aps.org/abstract/PRB/v82/i9/e094116)

[^2d_layer_2011]: [Xinyu Luo, Jihui Yang, Hanyu Liu, Xiaojun Wu, Yanchao Wang, Yanming Ma, Su-Huai Wei, Xingao Gong, and Hongjun Xiang, *Predicting Two-Dimensional Boron-Carbon Compounds by the global optimization method.* **J. Am. Chem. Soc.** 133, 16285(2011)](http://pubs.acs.org/doi/abs/10.1021/ja2072753)

[^crystal_2012]: [Yanchao Wang, Jian Lv, Li Zhu, and Yanming Ma\*, *CALYPSO: A Method for Crystal Structure Prediction*, **Comput. Phys. Commun.** 183, 2063 (2012)](http://www.sciencedirect.com/science/article/pii/S0010465512001762)

[^2d_surface_2014]: [Shaohua Lu, Yanchao Wang, Hanyu Liu, Maosheng Miao and Yanming Ma\*, *Self-assembled ultrathin nanotubes on diamond (100) surface*, **Nat. Commun.** 5, 3666 (2014)](http://www.nature.com/ncomms/2014/140416/ncomms4666/full/ncomms4666.html)

[^2dadsorbed_2015]: [Bo Gao, Xuecheng Shao, Jian Lv, Yanchao Wang\* and Yanming Ma\*, *Structure Prediction of Atoms Adsorbed on Two-Dimensional Layer Materials: Method and Applications,* **J. Phys. Chem. C** 119, 20111 (2015)](https://pubs.acs.org/doi/10.1021/acs.jpcc.5b05035)

[^cluster_2012]: [Jian Lv, Yanchao Wang, Li Zhu, and Yanming Ma\*, *Particle-swarm structure prediction on clusters*, **J. Chem. Phys.** 137, 084104 (2012)](http://jcp.aip.org/resource/1/jcpsa6/v137/i8/p084104_s1)
