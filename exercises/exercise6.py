from base.graph import *
from algorithms.salesman import roberts_flores_hamiltonian
matrix_of_adjacency = [[0, 78, 8, 58, 69],
                       [8, 0, 47, 4, 74],
                       [3, 38, 0, 45, 53],
                       [58, 1, 78, 0, 47],
                       [43, 15, 25, 69, 0]
                       ]

graph = DirGraph(matrix=matrix_of_adjacency)

salesman = roberts_flores_hamiltonian(graph=graph)
print(salesman)