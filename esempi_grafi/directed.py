import networkx as nx

dg = nx.DiGraph()
dg.add_weighted_edges_from([(1,4,0.5), (3,1,0.75)])

print([s for s in dg.successors(1)])
print([p for p in dg.predecessors(1)])

mg = nx.MultiGraph()

mg.add_weighted_edges_from([(1,2,.5), (1,2,.75),
(2,3,.5)])

print(mg[1][2])
