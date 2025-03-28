import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()
G.add_weighted_edges_from([(0, 1, 5), (1, 2, 2),
                           (2, 3, -3), (1, 3, 10),
                           (3, 2, 8)])

fw = nx.floyd_warshall(G, weight="weight")
for a, b in fw.items():
    print(a)
    print(dict(b))

results = {a: dict(b) for a, b in fw.items()}
print(results)

pos=nx.planar_layout(G) # pos = nx.nx_agraph.graphviz_layout(G)
nx.draw_networkx(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

plt.savefig("plot")
plt.show()