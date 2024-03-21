# A Genetic Algorithm for Efficiently Solving the Virtualized Radio Access Network Placement Problem

## Description
This repository aims to demonstrate the Genetic Algorithm implementation presented in our paper.

To run the experiments we also implemented a heuristic on the individuals first generation, creating a single individual synthetically. This individual is created based on the VNCs, where VNCs that centralize more VNFs are more likely to be chosen. This approach does not bias the search, since it causes the insertion of a single individual in population, at the beginning of the search, which may or may not be feasible. To run the experiments we used a bare metal machine with a Intel(R) Core(TM) i7-10700F CPU @ 2.90GHz 16 cores, 32GB of main memory and 1TB of SSD, using python version 3.10.6.
## Citation

@INPROCEEDINGS{Almeida:2023,
  author={Almeida, Gabriel M. and Camilo-Junior, Celso and Correa, Sand and Cardoso, Kleber},
  booktitle={ICC 2023 - IEEE International Conference on Communications}, 
  title={A Genetic Algorithm for Efficiently Solving the Virtualized Radio Access Network Placement Problem}, 
  year={2023},
  volume={},
  number={},
  pages={1874-1879},
  doi={10.1109/ICC45041.2023.10279334}}

