
import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._allAirports = DAO.getAllAirports()
        self._idMap = {}
        for a in self._allAirports:
            self._idMap[a.ID] = a
        self._grafo = nx.Graph()

    def buildGraph(self, nMin):
        self._grafo.clear()
        self._nodi = DAO.getAllNodes(nMin)
        self._grafo.add_nodes_from(self._nodi)
        self._addEdgesV1()

    def _addEdgesV1(self):
        allConnessioni = DAO.getAllEdgesV1(self._idMap)
        for c in allConnessioni:
            v0 = c.V0
            v1 = c.V1
            peso = c.N
            if v0 in self._grafo and v1 in self._grafo:
                if self._grafo.has_edge(v0, v1):
                    self._grafo[v0][v1]["weight"] += peso
                else:
                    self._grafo.add_edge(v0, v1, weight = peso)
