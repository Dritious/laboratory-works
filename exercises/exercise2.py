from base.graph import *
from algorithms.way_algorithms import way_by_dijkstra

matrix_of_adjacency_1 = [[0, 55, 19, 77, 0],
                         [0, 0, 4, 0, 33],
                         [65, 66, 0, 45, 38],
                         [5, 0, 42, 0, 0],
                         [44, 22, 0, 23, 0]]

graph_1 = DirGraph(matrix=matrix_of_adjacency_1)

dijkstra_1 = way_by_dijkstra(graph_1, 4, 2)
print(dijkstra_1)

matrix_of_adjacency_2 = [[0, 64, 18, 42, 0, 14],
                         [0, 0, 4, 85, 32, 83],
                         [31, 0, 0, 0, 68, 0],
                         [0, 20, 79, 0, 51, 33],
                         [109, 0, 0, 359, 0, 29],
                         [903, 110, 100, 22, 0, 0]]

graph_2 = DirGraph(matrix=matrix_of_adjacency_2)

dijkstra_2 = way_by_dijkstra(graph_2, 6, 5)
print(dijkstra_2)
