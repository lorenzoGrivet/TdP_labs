import networkx as nx

g = nx.Graph()
g.add_edge(1, 2)  # default edge data=1
g.add_edge(2, 3, weight=0.9)  # specify edge data

elist = [(1, 2, 1), (2, 3, 1), (1, 4, 1), (4, 2, 1),
         ('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 7.3)]
g.add_weighted_edges_from(elist)
g.add_edge(2, 5, arbitraryAttr="foo")

print(g[2])
print("---------")
print(g['a']['b'])
print("---------")
print('e' in g)
print("---------")
for n in g:
    print(n)
print("---------")
for nbr in g[2]:
    print(nbr)
print("---------")
print(g[2][5]['arbitraryAttr'])
