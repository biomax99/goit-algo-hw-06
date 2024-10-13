import networkx as nx
import matplotlib.pyplot as plt

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

    return G

# Завдання 2: Реалізація пошукових алгоритмів DFS та BFS
def search_algorithms(G):
    # Пошук в глибину (DFS)
    dfs_path = list(nx.dfs_edges(G, source="A"))
    print(f"Шлях DFS від A: {dfs_path}")

    # Пошук в ширину (BFS)
    bfs_path = list(nx.bfs_edges(G, source="A"))
    print(f"Шлях BFS від A: {bfs_path}")

# Завдання 3: Алгоритм Дейкстри
def dijkstra_algorithm(G):
    # Додавання ваг для кожного ребра
    weighted_edges = [("A", "B", 5), ("A", "C", 10), ("B", "D", 2), ("C", "D", 1), ("C", "E", 7)]
    G.add_weighted_edges_from(weighted_edges)

    # Пошук найкоротшого шляху за алгоритмом Дейкстри
    shortest_path = nx.dijkstra_path(G, source="A", target="E")
    shortest_path_length = nx.dijkstra_path_length(G, source="A", target="E")

    print(f"Найкоротший шлях за Дейкстрою від A до E: {shortest_path}")
    print(f"Довжина найкоротшого шляху: {shortest_path_length}")

# Основна функція для запуску всіх завдань
if __name__ == "__main__":
    # Завдання 1: Створення графа
    graph = create_graph()

    # Завдання 2: Пошукові алгоритми (DFS та BFS)
    search_algorithms(graph)

    # Завдання 3: Алгоритм Дейкстри
    dijkstra_algorithm(graph)
