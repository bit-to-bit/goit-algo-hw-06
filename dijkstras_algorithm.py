"""Task 3 - Dijkstras algorithm"""

import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight["weight"]

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


def draw_dijkstra_graph(g, shortest_paths, suffix: None):

    pos = nx.spring_layout(g, seed=3113794652)  # positions for all nodes

    blue = f"#{70:02x}{70:02x}{200:02x}"

    lables = {k: f"{k}\n<{v}>" for k, v in shortest_paths.items()}

    nx.draw_networkx_labels(g, pos, labels=lables, font_size=8)

    nx.draw_networkx_nodes(g, pos, node_color=blue, node_size=500, alpha=0.5)

    nx.draw_networkx_edges(
        g,
        pos,
        width=8,
        alpha=0.3,
        edge_color=blue,
    )
    labels = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

    plt.title(f"Мапа метро Харкова\n{suffix}", wrap=True)
    # plt.text(4, 1, suffix, ha="left", rotation=15, wrap=True)
    plt.text(
        5, 10, "suffix", fontsize=18, style="oblique", ha="center", va="top", wrap=True
    )

    plt.show()
