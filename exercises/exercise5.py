from base.graph import *
from algorithms.salesman import travelling_salesman_branch_and_bound
matrix_of_adjacency = [[0, 78, 8, 58, 69],
                       [8, 0, 47, 4, 74],
                       [3, 38, 0, 45, 53],
                       [58, 1, 78, 0, 47],
                       [43, 15, 25, 69, 0]
                       ]

graph = DirGraph(matrix=matrix_of_adjacency)

salesman = travelling_salesman_branch_and_bound(graph=graph)
print(salesman)
