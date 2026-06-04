from collections import deque
from typing import Any, Dict, List, Tuple, Optional


def wave_algorithm(graph, start, finish=None):

    distance: Dict[Any, int] = {start: 0}
    parent: Dict[Any, Optional[Any]] = {start: None}
    queue = deque([start])

    while queue:
        current = queue.popleft()

        if finish is not None and current == finish:
            break

        for neighbor, weight in graph.vertices[current]:
            if neighbor not in distance:
                distance[neighbor] = distance[current] + 1
                parent[neighbor] = current
                queue.append(neighbor)

    path = None
    if finish is not None and finish in distance:
        path = []
        v = finish
        while v is not None:
            path.append(v)
            v = parent[v]
        path.reverse()

    return distance, parent, path