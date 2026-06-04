from graph import *

def mst_by_prim(graph: Graph):
    vertices = graph.list_of_vertices()
    first_vertex = vertices[0]

    visited_vertices = set([first_vertex])
    mst = []
    total_weight = 0

    while len(visited_vertices)<len(vertices):
        next_edge = None #fromat: (vertex_1,vertex_2,weight)
        for vertex_1 in visited_vertices:
            for vertex_2, weight in graph.vertices[vertex_1]:
                if vertex_2 not in visited_vertices:
                    if next_edge is None or weight < next_edge[2]:
                        next_edge = (vertex_1, vertex_2, weight)
        
        mst.append(next_edge)
        vertex_1, vertex_2 , weight = next_edge
        visited_vertices.add(vertex_2)
        total_weight+= weight

    return mst, total_weight

def mst_by_kruskal(graph: Graph):
    vertex_root = {v:v for v in graph.list_of_vertices()} #define paren-child relationship of verices in spaning tree
    vertex_rank = {v:0 for v in graph.list_of_vertices()} #define roots relationship in spaning tree
    
    def find_root(vertex):
        if vertex_root[vertex]!= vertex:
            return find_root(vertex_root[vertex]) #if vertex root update     
        else:
            return vertex
        
    def merge_vertices(vertex_1, vertex_2):
        root_1 = find_root(vertex_1)
        root_2 = find_root(vertex_2)

        if root_1 == root_2:
            return False #same roots makes loop
        
        if vertex_rank[root_1] < vertex_rank[root_2]:
            vertex_root[root_1] = root_2
        
        elif vertex_rank[root_2] < vertex_rank[root_1]:
            vertex_root[root_2] = root_1
        
        else:
            vertex_root[root_2] = root_1
            vertex_rank[root_1]+=1
        
        return True
    
    mst = []
    total_weight = 0
    edges = graph.edges_by_weihgt()

    for vertex_1, vertex_2, weight in edges:
        if merge_vertices(vertex_1, vertex_2):
            mst.append((vertex_1,vertex_2,weight))
            total_weight+=weight
    
    return mst, total_weight