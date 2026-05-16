from base.graph import DirGraph
from algorithms.way_algorithms import ways_by_floyd_warshall

INF = float('inf')


def get_path(u, v, next_vertex):
    if next_vertex[u][v] is None:
        return None
    path = [u]
    while u != v:
        u = next_vertex[u][v]
        if u is None:
            return None
        path.append(u)
    return path


def run_algorithm(graph):
    res_dist, res_next, _ = ways_by_floyd_warshall(graph)
    for start_node in graph.list_of_vertices():
        for end_node in graph.list_of_vertices():
            if start_node != end_node:
                d = res_dist[start_node][end_node]
                if d == INF:
                    print(f"{start_node} -> {end_node}: -1")
                else:
                    path = get_path(start_node, end_node, res_next)
                    print(f"Стоимость {d}, Путь: {' '.join(map(str, path))}")


def load_from_file():
    graph = DirGraph()

    with open("input.txt", "r") as file:
        line1 = file.readline().split()
        if not line1:
            return None

        n, m = map(int, line1)

        for i in range(1, n + 1):
            graph.add_vertex(i)

        for i in range(m):
            v1, v2, w = map(int, file.readline().split())
            graph.add_edge(v1, v2, w)

    return graph


def load_from_input():

    graph = DirGraph()

    n = int(input("Введите количество вершин: "))
    m = int(input("Введите количество рёбер: "))

    for i in range(1, n + 1):
        graph.add_vertex(i)

    print("Введите рёбра (v1 v2 weight):")
    for _ in range(m):
        v1, v2, w = map(int, input().split())
        graph.add_edge(v1, v2, w)

    return graph


def main():
    while True:
        print("Меню:")
        print("1 - Загрузить из файла")
        print("2 - Ввести вручную")
        print("0 - Выход")

        choice = input("Выбор: ")

        if choice == "1":
            graph = load_from_file()
            if graph:
                run_algorithm(graph)

        elif choice == "2":
            graph = load_from_input()
            run_algorithm(graph)

        elif choice == "0":
            print("Выход...")
            break

        else:
            print("Неверный ввод!")


if __name__ == "__main__":
    main()
