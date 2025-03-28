from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo=nx.DiGraph()
        self._idMap={}
        for f in self._fermate:
            self._idMap[f.id_fermata]=f

    def buildGraph(self):
        self._grafo.add_nodes_from(self._fermate)

        # for u in self._fermate:
        #     for v in self._fermate:
        #         res=DAO.getEdge(u,v)
        #
        #         if len(res)>0:
        #             self._grafo.add_edge(u,v)
        #             print(f"Added edge between {u} and {v}")

        #modo 2
        # for u in self._fermate:
        #     vicini = DAO.getEdgesVicini(u)
        #
        #     for v in vicini:
        #         v_nodo=self._idMap[v.id_stazA]
        #         self._grafo.add_edge(u,v_nodo)
        #         print(f"Added edge between {u} and {v_nodo}")

        #modo3
        allConnessioni=DAO.allConnessioni()
        for c in allConnessioni:
            u_nodo=self._idMap[c.id_stazP]
            v_nodo = self._idMap[c.id_stazA]
            self._grafo.add_edge(u_nodo,v_nodo)

        pass

    def creaGrafoPesato(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._fermate)
        self.addEdgePesati()


    def getArchiPesoMaggiore(self):
        if len(self._grafo.edges)==0:
            print("Non ci sono archi")
            return
        else:
            edges= self._grafo.edges

            result=[]

            for u,v in edges:
                peso = (self._grafo[u][v]["weigth"])
                if peso>1:
                    result.append((u,v,peso))


            return result



    def addEdgePesati(self):
        self._grafo.clear_edges()
        allConnessioni=DAO.allConnessioni()

        for c in allConnessioni:
            if self._grafo.has_edge(self._idMap[c.id_stazP],self._idMap[c.id_stazA]):
                self._grafo[self._idMap[c.id_stazP]][self._idMap[c.id_stazA]]["weigth"]+=1
            else:
                self._grafo.add_edge(self._idMap[c.id_stazP], self._idMap[c.id_stazA],weigth=1)

    def getEdgesWeigth(self,v1,v2):
        return self._grafo[v1][v2]

    def addEdgeModel3(self):
        pass

    def getBFSNodes(self,source):
        edges= nx.bfs_edges(self._grafo,source)
        visited=[]

        for u,v in edges:
            visited.append(v)

        return visited

    def getDFSNodes(self,source):
        edges= nx.dfs_edges(self._grafo,source)
        visited=[]

        for u,v in edges:
            visited.append(v)

        return visited



    @property
    def fermate(self):
        return self._fermate

    def getNumModels(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)