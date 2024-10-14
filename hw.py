import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Завдання 1: Створення графа
def create_graph():
    G = nx.Graph()

    # Додавання вершин (станцій або зупинок)
    stations = ["A", "B", "C", "D", "E"]
    G.add_nodes_from(stations)

    # Додавання ребер (шляхів між станціями)
    G.add_edges_from([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E")])

    # Візуалізація графа
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
    plt.title("Транспортна мережа")
    plt.show()

    # Аналіз характеристик графа
    print(f"Кількість вершин: {G.number_of_nodes()}")
    print(f"Кількість ребер: {G.number_of_edges()}")
    print(f"Список сусідів для кожної вершини:")
    for station in stations:
        print(f"{station}: {list(G.neighbors(station))}")

    return G, stations

# Завдання 2: Власна реалізація DFS та BFS
# DFS (глибина)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

# BFS (ширина)
def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend([neighbor for neighbor in graph[node] if neighbor not in visited])

    return visited

# Завдання 3: Власна реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node is not None:
        visited.add(current_node)
        destinations = graph[current_node].items()
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node, weight in destinations:
            weight = weight + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            break
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    return shortest_paths

# Основна функція для запуску всіх завдань
if __name__ == "__main__":
    # Завдання 1: Створення графа
    graph_nx, stations = create_graph()

    # Перетворення графа networkX у звичайний словник
    graph_dict = {
        "A": {"B": 1, "C": 1},
        "B": {"A": 1, "D": 1},
        "C": {"A": 1, "D": 1, "E": 1},
        "D": {"B": 1, "C": 1},
        "E": {"C": 1}
    }

    # Завдання 2: Пошукові алгоритми (DFS та BFS)
    dfs_result = dfs(graph_dict, "A")
    print(f"Шлях DFS від A: {dfs_result}")

    bfs_result = bfs(graph_dict, "A")
    print(f"Шлях BFS від A: {bfs_result}")

    # Завдання 3: Алгоритм Дейкстри
    # Додавання ваг
    weighted_graph = {
        "A": {"B": 5, "C": 10},
        "B": {"A": 5, "D": 2},
        "C": {"A": 10, "D": 1, "E": 7},
        "D": {"B": 2, "C": 1},
        "E": {"C": 7}
    }

    dijkstra_result = dijkstra(weighted_graph, "A")
    print("Найкоротші шляхи за алгоритмом Дейкстри від A:")
    for destination, (prev_node, weight) in dijkstra_result.items():
        print(f"До {destination}: вага = {weight}, попередня вершина = {prev_node}")
