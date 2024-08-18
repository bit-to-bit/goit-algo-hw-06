'''Task 2 - DFS and BFS'''
import networkx as nx
import matplotlib.pyplot as plt


def get_dfs_path(graph, vertex, visited=None):
    if visited is None:
        visited = []
    visited.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            get_dfs_path(graph, neighbor, visited)


def get_bfs_path(graph, queue, visited=None):
    if visited is None:
        visited = []
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.append(vertex)
        queue.extend(set(graph[vertex]) - set(visited))
    get_bfs_path(graph, queue, visited)


def draw_graph_paths(g, nodes_order, suffix: None):

    pos = nx.spring_layout(g, seed=3113794652)  # positions for all nodes

    blue = f"#{70:02x}{70:02x}{200:02x}"

    lables = {x: f"{x}\n({i+1})" for i, x in enumerate(nodes_order)}

    nx.draw_networkx_labels(g, pos, labels=lables, font_size=8)

    nx.draw_networkx_nodes(g, pos, node_color=blue, node_size=500, alpha=0.5)

    nx.draw_networkx_edges(
        g,
        pos,
        width=8,
        alpha=0.3,
        edge_color=blue,
    )

    plt.title(f"Мапа метро Харкова\n{suffix}")
    plt.show()
