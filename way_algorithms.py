from graph import *

def way_by_dijkstra(graph: Graph, start_vertex, end_vertex):
    vertices = graph.vertices

    min_distant = {v:float('inf') if v!=start_vertex else 0 for v in vertices}

    unvisited_vertices = set(v for v in vertices)

    while unvisited_vertices:

        current_vertex = min(unvisited_vertices, key = lambda v: min_distant[v])
        unvisited_vertices.remove(current_vertex)

        if current_vertex == end_vertex:
              return min_distant[end_vertex]
        
        for (vertex_2, weight) in vertices[current_vertex]:
                    if vertex_2 in unvisited_vertices:
                       min_distant[vertex_2] = min(min_distant[vertex_2],min_distant[current_vertex]+weight)
        
    return float('inf')      
        

                            


