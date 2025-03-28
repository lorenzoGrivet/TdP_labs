from model.model import Model

mymodel=Model()
mymodel.getTeamsOfYear(2015)
mymodel.buildGraph(2015)
mymodel.printGraphDetails()

v0=list(mymodel.grafo.nodes)[0]
vicini=mymodel.getSortedNeighbors(v0)

for v in vicini:
    print(v,v0)