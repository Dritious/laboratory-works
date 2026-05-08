from base.graph import *
from typing import Any, Dict, List, Tuple


INF = float('inf')


def way_by_dijkstra(graph: Graph, start_vertex, end_vertex):
    vertices = graph.vertices

    min_distant = {v: INF if v !=
                   start_vertex else 0 for v in vertices}

    unvisited_vertices = set(v for v in vertices)

    while unvisited_vertices:

        current_vertex = min(unvisited_vertices, key=lambda v: min_distant[v])
        unvisited_vertices.remove(current_vertex)

        if current_vertex == end_vertex:
            return min_distant[end_vertex]

        for (vertex_2, weight) in vertices[current_vertex]:
            if vertex_2 in unvisited_vertices:
                min_distant[vertex_2] = min(
                    min_distant[vertex_2], min_distant[current_vertex]+weight)

    return INF


def way_by_bellman_ford(graph: Graph, start_vertex) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]], bool]:
    # Инициализация
    vertices = graph.vertices
    distances = {v: INF for v in vertices}
    predecessors = {v: None for v in vertices}
    distances[start_vertex] = 0

    edges = graph.list_of_edges()

    # Релаксация ребер |V| - 1 раз
    for _ in range(len(vertices) - 1):
        updated = False
        for u, v, weight in edges:
            if distances[u] != INF and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u
                updated = True
        if not updated:
            break  # Ранний выход если нет обновлений

    # Проверка на отрицательные циклы
    has_negative_cycle = False
    for u, v, weight in edges:
        if distances[u] != INF and distances[u] + weight < distances[v]:
            has_negative_cycle = True
            break

    return distances, predecessors, has_negative_cycle


def ways_by_floyd_warshall(graph: Graph):

    vertices = graph.list_of_vertices()
    n = len(vertices)

    # Создаем отображение вершина -> индекс для работы с матрицами
    vertex_to_idx = {v: i for i, v in enumerate(vertices)}
    idx_to_vertex = {i: v for i, v in enumerate(vertices)}

    # Инициализация матриц
    distances = [[INF] * n for _ in range(n)]
    next_vertex = [[None] * n for _ in range(n)]

    # Расстояние до самой себя = 0
    for i in range(n):
        distances[i][i] = 0
        next_vertex[i][i] = idx_to_vertex[i]

    # Заполняем матрицы на основе ребер графа
    for u, v, weight in graph.list_of_edges():
        i = vertex_to_idx[u]
        j = vertex_to_idx[v]
        distances[i][j] = weight
        next_vertex[i][j] = v

    # Основной алгоритм Флойда-Уоршелла
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][k] != INF and distances[k][j] != INF:
                    if distances[i][k] + distances[k][j] < distances[i][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]
                        next_vertex[i][j] = next_vertex[i][k]

    # Проверка на отрицательные циклы
    has_negative_cycle = False
    for i in range(n):
        if distances[i][i] < 0:
            has_negative_cycle = True
            break

    # Преобразуем матрицы обратно к словарям с именами вершин
    result_distances = {}
    result_next = {}

    for i in range(n):
        u = idx_to_vertex[i]
        result_distances[u] = {}
        result_next[u] = {}
        for j in range(n):
            v = idx_to_vertex[j]
            result_distances[u][v] = distances[i][j]
            result_next[u][v] = next_vertex[i][j]

    return result_distances, result_next, has_negative_cycle
