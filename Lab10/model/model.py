import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.stati= DAO.getStati()
        self.idMap={}
        for a in self.stati:
            self.idMap[a.CCode]=a

        self.grafo=nx.Graph()
        # for i in self.stati:
        #     self.grafo.add_node(i.CCode)
        # self.grafo.add_nodes_from()
        self.connesse=-1



    def calcolaConfini(self,anno):
        self.grafo.clear()

        self.e=DAO().getNodi(anno)
        self.grafo.add_nodes_from(self.e)
        confini=DAO().getConfiniAnno(anno)

        for a in confini:
            if not (self.grafo.has_edge(a.state1no,a.state2no) or self.grafo.has_edge(a.state2no,a.state1no)):
                self.grafo.add_edge(a.state1no,a.state2no)


        risultato=0
        for a in self.grafo.nodes:
            if nx.dfs_successors(self.grafo,a) == {}:
                risultato+=1

        print(risultato)
        comp_connesse= nx.connected_components(self.grafo)
        self.connesse=len(list(comp_connesse)) #-risultato


    def calcolaPercorso(self,partenza,anno):
        successori=nx.dfs_successors(self.grafo,int(partenza))

        return successori




    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)



