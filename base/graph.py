from typing import Any, Dict, List, Tuple
from abc import ABC, abstractmethod


class Graph(ABC):
    def __init__(self, matrix=None):
        '''key - vartex name, value - array of adjacent vertices to current and weight of edge between it as tuples.'''
        self.vertices: Dict[Any, List[Tuple]] = {}
        self.matrix = matrix
        if matrix:
            _create_graph_by_matrix(self, matrix)

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def list_of_vertices(self):
        return list(self.vertices.keys())

    @abstractmethod
    def add_edge(self, vertex_1, vertex_2, weight): pass

    @abstractmethod
    def list_of_edges(self): pass


class DirGraph(Graph):
    def add_edge(self, vertex_1, vertex_2, weight):
        self.add_vertex(vertex_1)
        self.add_vertex(vertex_2)
        self.vertices[vertex_1].append((vertex_2, weight))

    def list_of_edges(self):
        edges = []
        for vertex_1 in self.vertices:
            for (vertex_2, weight) in self.vertices[vertex_1]:
                edges.append((vertex_1, vertex_2, weight))
        return edges

    def edges_by_weihgt(self):
        return sorted(self.list_of_edges(), key=lambda e: e[2])


class UndirGraph(Graph):
    def add_edge(self, vertex_1, vertex_2, weight):
        self.add_vertex(vertex_1)
        self.add_vertex(vertex_2)
        self.vertices[vertex_1].append((vertex_2, weight))
        self.vertices[vertex_2].append((vertex_1, weight))

    def list_of_edges(self):
        previous_edges = set()
        edges = []
        for vertex_1 in self.vertices:
            for (vertex_2, weight) in self.vertices[vertex_1]:
                if (vertex_2, vertex_1, weight) not in edges:
                    previous_edges.add((vertex_1, vertex_2, weight))
                    edges.append((vertex_1, vertex_2, weight))
        return edges

    def edges_by_weihgt(self):
        return sorted(self.list_of_edges(), key=lambda e: e[2])


def _create_graph_by_matrix(g: Graph, matrix):
    n = len(matrix)

    for i in range(n):
        g.add_vertex(i+1)

    for i in range(n):
        for j in range(n):
            weight = matrix[i][j]

            if weight != 0:
                g.add_edge(i+1, j+1, weight)

    return g
