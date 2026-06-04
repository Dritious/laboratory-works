from base.graph import *
from algorithms.way_algorithms import ways_by_floyd_warshall

matrix_of_adjacency = [[0, 10, 18, 8, 0, 0],
                       [10, 0, 16, 9, 21, 0],
                       [0, 16, 0, 0, 0, 15],
                       [7, 9, 0, 0, 0, 12],
                       [0, 0, 0, 0, 0, 23],
                       [0, 0, 15, 0, 23, 0]
                       ]

graph = DirGraph(matrix=matrix_of_adjacency)

floyd = ways_by_floyd_warshall(graph=graph)
print(floyd)
