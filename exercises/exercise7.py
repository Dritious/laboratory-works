from algorithms.flow_algorithms import ford_fulkerson
from base.graph import DirGraph

matrix = [[0,32,95,75,57,0,0,0],
          [0,0,5,0,23,0,0,16],
          [0,0,0,18,0,6,0,0],
          [0,0,0,0,24,9,0,0],
          [0,0,0,0,0,0,20,94],
          [0,0,0,0,11,0,7,0],
          [0,0,0,0,0,0,0,81],
          [0,0,0,0,0,0,0,0]]

graph = DirGraph(matrix)

print(ford_fulkerson(graph,1,8))