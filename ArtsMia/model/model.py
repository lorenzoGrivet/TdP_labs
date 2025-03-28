import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._artObjectList=DAO.getAllObjects()
        self._grafo=nx.Graph()
        self._grafo.add_nodes_from(self._artObjectList)
        self._idMap={}
        for v in self._artObjectList:
            self._idMap[v.object_id]=v



    def getConnessa(self,v0in):
        v0=self._idMap[v0in]

        #1: successori
        successori = nx.dfs_successors(self._grafo,v0)
        allSucc=[]


        for v in successori.values():

            allSucc.extend((v))



        print(f"Metodo 1: {len(allSucc)}")

        #2: predecessori
        predecessori= nx.dfs_predecessors(self._grafo,v0)
        print(f"MEtodo 2: {len(predecessori.values())}")

        #3: conto nodi albero di visita
        tree=nx.dfs_tree(self._grafo,v0)
        print((f"Metodo 3: {len(tree.nodes)}"))

        #4
        connComp= nx.node_connected_component(self._grafo,v0)
        print(f"Metodo 4: {len(connComp)}")

        return len(connComp)


    def creaGrafo(self):
        self.addEdges()


    def addEdges(self):
        self._grafo.clear_edges()

        #ciclo sui nodi se grafo è piccolo
        # for u in self._artObjectList:
        #     for v in self._artObjectList:
        #         peso = DAO.getPeso(u,v)
        #         self._grafo.add_edge(u,v,weigth=peso)

        #oppure faccio query
        allEdges=DAO.getAllConnessioni(self._idMap)

        for e in allEdges:
            self._grafo.add_edge(e.v1,e.v2,weigth=e.peso)



    def checkExistence(self,idOggetto):
        return idOggetto in self._idMap

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)