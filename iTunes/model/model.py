import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}


    def getSetAlbum(self,a1,dTot):
        self.bestSet=None
        self.bestScore=0
        connessa=nx.node_connected_component(self._graph,a1)
        parziale= set([a1])
        connessa.remove(a1)

        self._ricorsione(parziale, connessa, dTot)

        return self.bestSet

    def _ricorsione(self,parziale, connessa, dTot):

        if self.durataTot(parziale) > dTot:
            return

        if len(parziale)>self.bestScore:
            self.bestSet=copy.deepcopy(parziale)
            self.bestScore=len(parziale)

        for c in connessa:
            parziale.append(c)
            rimanenti= copy.deepcopy(connessa)
            rimanenti.remove(c)
            self._ricorsione(parziale,rimanenti,dTot)
            parziale.remove(c)


    def durataTot(self,parziale):
        dTot=0
        for n in parziale:
            dTot+=n.totd
        return dTot

    def buildGraph(self, d):
        self._graph.clear()
        self._graph.add_nodes_from(DAO.getAlbums(toMillisec(d)))
        self._idMap = {a.AlbumId: a for a in list(self._graph.nodes)}
        # for a in list(self._graph.nodes):
        #     self._idMap[a.AlbumId] = a
        edges = DAO.getEdges(self._idMap)

        self._graph.add_edges_from(edges)

    def getConnessaDetails(self, v0):
        conn = nx.node_connected_component(self._graph, v0)
        durataTOT = 0
        for album in conn:
            durataTOT += toMinutes(album.totD)

        return len(conn), durataTOT
    def getGraphDeails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getNodes(self):
        return list(self._graph.nodes)

    def getGraphSize(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getNodeI(self,i):
        return self._idMap[i]

def toMillisec(d):
    return d*60*1000

def toMinutes(d):
    return d/1000/60