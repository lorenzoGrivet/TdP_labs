from model.model import Model

mymodel = Model()
mymodel.buildGraph()
print()
print(f"Il grafo ha {mymodel.getNumModels()} nodi")
print(f"Il grafo ha {mymodel.getNumEdges()} archi")