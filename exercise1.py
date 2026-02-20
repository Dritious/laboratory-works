from graph import UndirGraph
from mst_algorithms import *

matrix_of_adjacency = [[0,4,13,7,0,0],
                       [4,0,4,4,4,0],
                       [13,4,0,0,27,0],
                       [7,4,0,0,6,0],
                       [0,4,27,6,0,10],
                       [0,0,0,0,10,0]]

graph = UndirGraph(matrix_of_adjacency)

prim = mst_by_prim(graph)
print(prim)

kruskal = mst_by_kruskal(graph)
print(kruskal)