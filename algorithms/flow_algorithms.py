from collections import deque
import math
from base.graph import DirGraph


def bfs_max_edge_path(graph: DirGraph, source, sink):
    queue = deque([source])
    parents = {source: None}

    while queue:
        v = queue.popleft()

        # сортируем рёбра по убыванию веса
        edges = sorted(graph.vertices[v], key=lambda x: -x[1])

        for to, weight in edges:
            if weight > 0 and to not in parents:
                parents[to] = v
                if to == sink:
                    # восстанавливаем путь
                    path = []
                    cur = sink
                    while parents[cur] is not None:
                        prev = parents[cur]
                        path.append((prev, cur))
                        cur = prev
                    path.reverse()
                    return path
                queue.append(to)

    return None


def ford_fulkerson(graph: DirGraph, source, sink):
    max_flow = 0

    while True:
        path = bfs_max_edge_path(graph, source, sink)
        if not path:
            break

        flow = math.inf
        for u, v in path:
            for to, w in graph.vertices[u]:
                if to == v:
                    flow = min(flow, w)

        # уменьшаем пропускную способность
        for u, v in path:
            for i, (to, w) in enumerate(graph.vertices[u]):
                if to == v:
                    graph.vertices[u][i] = (to, w - flow)

        max_flow += flow

    return max_flow