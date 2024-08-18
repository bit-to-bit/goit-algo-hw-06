"""Task 2 - DFS and BFS test"""

from collections import deque
import graph
import path

g = graph.build_graph()

dfs_lables = []
path.get_dfs_path(g, "G7", dfs_lables)
path.draw_graph_paths(g, dfs_lables, f"DFS = {dfs_lables}")

bfs_lables = []
path.get_bfs_path(g, deque(["G7"]), bfs_lables)
path.draw_graph_paths(g, bfs_lables, f"BFS = {bfs_lables}")
