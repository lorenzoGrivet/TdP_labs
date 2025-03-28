import networkx as nx
import math
import flet as ft

g = nx.Graph()
g.add_edge(1, 2)  # default edge data=1
g.add_edge(2, 3, weight=0.9)  # specify edge data

g.add_edge('y', 'x', function=math.cos)
g.add_node(math.cos)  # any hashable can be a node

elist = [(1, 2), (2, 3), (1, 4), (4, 2)]
g.add_edges_from(elist)
elist = [('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 7.3)]
g.add_weighted_edges_from(elist)
g.add_node(ft.Text("Pippo"))

print(g.nodes())
print(g.edges())
print(g.get_edge_data('a','b'))
print(g.get_edge_data('y','x'))