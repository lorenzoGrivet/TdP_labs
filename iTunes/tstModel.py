from model.model import Model

mymodel = Model()
mymodel.buildGraph(120*60*1000)
print(mymodel.getGraphDeails())
mymodel.getNodeI(261)
print()

