from base.graph import *
from algorithms.way_algorithms import way_by_bellman_ford

matrix_of_adjacency = [[0, 124, 57, 0, 69],
                       [0, 0, 5, 45, 89],
                       [45, 47, 0, 25, 0],
                       [0, 35, 0, 0, 25],
                       [58, 12, 78, 89, 0]]

graph = DirGraph(matrix=matrix_of_adjacency)

bellman_ford = way_by_bellman_ford(graph=graph, start_vertex=5)
print(bellman_ford)
