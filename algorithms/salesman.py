from typing import Any, Dict, List, Tuple
import copy


def travelling_salesman_branch_and_bound(graph):
    matrix = copy.deepcopy(graph.matrix)
    vertices = graph.list_of_vertices()
    n = len(vertices)

    # Словари для отображения вершин на индексы и обратно
    vertex_to_idx = {v: i for i, v in enumerate(vertices)}
    idx_to_vertex = {i: v for i, v in enumerate(vertices)}

    best_cost = float('inf')
    best_path = None

    def reduce_matrix(mat):
        cost = 0

        # Редукция строк
        for i in range(n):
            row_min = min(mat[i])
            if row_min != float('inf') and row_min > 0:
                cost += row_min
                for j in range(n):
                    if mat[i][j] != float('inf'):
                        mat[i][j] -= row_min

        # Редукция столбцов
        for j in range(n):
            col_min = float('inf')
            for i in range(n):
                col_min = min(col_min, mat[i][j])
            if col_min != float('inf') and col_min > 0:
                cost += col_min
                for i in range(n):
                    if mat[i][j] != float('inf'):
                        mat[i][j] -= col_min

        return mat, cost

    def calculate_penalty(mat, i, j):
        # Второй минимум в строке
        row_vals = [mat[i][k]
                    for k in range(n) if k != j and mat[i][k] != float('inf')]
        row_second_min = min(row_vals) if row_vals else 0

        # Второй минимум в столбце
        col_vals = [mat[k][j]
                    for k in range(n) if k != i and mat[k][j] != float('inf')]
        col_second_min = min(col_vals) if col_vals else 0

        return row_second_min + col_second_min

    def select_best_edge(mat, current_idx):
        max_penalty = -1
        best_j = -1

        for j in range(n):
            if mat[current_idx][j] != float('inf'):
                penalty = calculate_penalty(mat, current_idx, j)
                if penalty > max_penalty:
                    max_penalty = penalty
                    best_j = j

        return best_j

    def branch_and_bound(mat, path, current_idx, current_cost, visited):
        nonlocal best_cost, best_path

        # Если посетили все вершины
        if len(path) == n:
            # Добавляем возврат к начальной вершине
            return_cost = mat[current_idx][path[0]]
            if return_cost != float('inf'):
                total_cost = current_cost + return_cost
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_path = path + [path[0]]
            return

        # Выбираем следующую вершину с максимальным штрафом
        next_idx = select_best_edge(mat, current_idx)
        if next_idx == -1:
            return

        edge_cost = mat[current_idx][next_idx]

        # Ветвь 1: включаем ребро (current_idx, next_idx)
        mat_include = copy.deepcopy(mat)

        # Обнуляем строку current_idx и столбец next_idx
        for i in range(n):
            mat_include[current_idx][i] = float('inf')
            mat_include[i][next_idx] = float('inf')

        # Запрещаем обратное ребро
        mat_include[next_idx][current_idx] = float('inf')

        # Редуцируем матрицу
        mat_include, reduction_cost = reduce_matrix(mat_include)

        new_cost = current_cost + edge_cost + reduction_cost

        if new_cost < best_cost:
            branch_and_bound(
                mat_include, path + [next_idx], next_idx, new_cost, visited | {next_idx})

        # Ветвь 2: исключаем ребро (current_idx, next_idx)
        mat_exclude = copy.deepcopy(mat)
        mat_exclude[current_idx][next_idx] = float('inf')
        mat_exclude, reduction_cost = reduce_matrix(mat_exclude)

        new_cost = current_cost + reduction_cost

        if new_cost < best_cost:
            branch_and_bound(mat_exclude, path, current_idx, new_cost, visited)

    # Начальная редукция
    initial_matrix = copy.deepcopy(matrix)
    reduced_matrix, initial_cost = reduce_matrix(initial_matrix)

    # Начинаем с вершины 0
    start_idx = 0
    start_vertex = idx_to_vertex[start_idx]

    branch_and_bound(reduced_matrix, [start_idx],
                     start_idx, initial_cost, {start_idx})

    # Преобразуем индексы обратно в вершины
    if best_path:
        vertex_path = [idx_to_vertex[idx] for idx in best_path]
        return vertex_path, best_cost
    else:
        return [], float('inf')

def roberts_flores_hamiltonian(graph, start: Any = None):
    
    vertices = graph.list_of_vertices()
    if not vertices:
        return []

    if start is None:
        start = vertices[0]


    # Список смежности без весов
    adjacency: Dict[Any, List[Any]] = {}
    for v in vertices:
        seen = set()
        neighs = []
        for to_v, _w in graph.vertices.get(v, []):
            if to_v not in seen:
                seen.add(to_v)
                neighs.append(to_v)
        adjacency[v] = neighs

    n = len(vertices)
    path = [start]
    used = {start}
    result = []

    def dfs(v: Any):
        if len(path) == n:
            if start in adjacency.get(v, []):
                result.append({
                    "kind": "cycle",
                    "path": path.copy(),
                })
            else:
                result.append({
                    "kind": "path",
                    "path": path.copy(),
                })
            return

        for nxt in adjacency.get(v, []):
            if nxt in used:
                continue

            used.add(nxt)
            path.append(nxt)

            dfs(nxt)

            path.pop()
            used.remove(nxt)

    dfs(start)
    return result
