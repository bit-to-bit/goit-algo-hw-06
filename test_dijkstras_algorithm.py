"""Task 3 - Dijkstras algorithm test"""

import graph
from dijkstras_algorithm import dijkstra, draw_dijkstra_graph

START = "G7"

g = graph.build_graph()
dijkstra = dijkstra(g, START)
sorted_list = {k: v for k, v in sorted(dijkstra.items(), key=lambda item: item[1])}
result_suffix = f"Найкоротші відстані від вершини {START} = {sorted_list}"
draw_dijkstra_graph(g, sorted_list, result_suffix)
