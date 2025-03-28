import copy
import itertools

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.allTeams = []
        self.grafo = nx.Graph()
        self.idMapTeams = {}

    def getScore(self, listOfNodes):
        score = 0
        if len(listOfNodes) == 1:
            return score
        for i in range(len(listOfNodes)-1):
            score += self.grafo[listOfNodes[i]][listOfNodes[i+1]]["weight"]

        return score




    def buildGraph(self, year):
        self.grafo.clear()
        if len(self.allTeams) == 0:
            print("Lista squadre vuota")
            return
        self.grafo.add_nodes_from(self.allTeams)


        myedges = list(itertools.combinations(self.allTeams, 2))

        self.grafo.add_edges_from(myedges)

        salariesOfTeams = DAO.getSalaryOfTeams(year, self.idMapTeams)
        for e in self.grafo.edges:
            self.grafo[e[0]][e[1]]["weight"] = salariesOfTeams[e[0]] + salariesOfTeams[e[1]]

        #print(myedges)

        # for t1 in self.grafo.nodes:
        #     for t2 in self.grafo.nodes:
        #         if t1 != t2:
        #             self.grafo.add_edge(t1, t2)



    def getPercorso(self, v0):
        self.bestPath = []
        self.bestObjVal = 0

        parziale = [v0]

        # for v in self.grafo.neighbors(v0):
        #     parziale.append(v)
        #     self.ricorsione(parziale)
        #     parziale.pop()

        self.ricorsioneV2(parziale)
        return self.bestPath

    def ricorsione(self, parziale):
        if self.getScore(parziale) > self.bestObjVal:
            self.bestPath = copy.deepcopy(parziale)
            self.bestObjVal = self.getScore(parziale)

        for v in self.grafo.neighbors(parziale[-1]):
            edgeW = self.grafo[parziale[-1]][v]["weight"]
            if v not in parziale and self.grafo[parziale[-2]][parziale[-1]]["weight"]>edgeW:
                parziale.append(v)
                self.ricorsione(parziale)
                parziale.pop()

    def ricorsioneV2(self, parziale):
        # verifico se sol attuale è migliore del best
        if self.getScore(parziale) > self.bestObjVal:
            self._bestPath = copy.deepcopy(parziale)
            self._bestObjVal = self.getScore(parziale)

        # verifico se posso aggiungere un altro elemeneto
        listaVicini = []
        for v in self.grafo.neighbors(parziale[-1]):
            edgeV = self.grafo[parziale[-1]][v]["weight"]
            listaVicini.append((v, edgeV))

        listaVicini.sort(key=lambda x: x[1], reverse=True)

        for v1 in listaVicini:
            if (v1[0] not in parziale and
                    self.grafo[parziale[-2][0]][parziale[-1][0]]["weight"] >
                    v1[1]):
                parziale.append(v1[0])
                self.ricorsioneV2(parziale)
                parziale.pop()
                return
        # aggiungo e faccio ricorsione




    def getYears(self):
        return DAO.getAllYears()

    def getTeamsOfYear(self, year):
        self.allTeams = DAO.getTeamsOfYear(year)
        self.idMapTeams = {t.ID: t for t in self.allTeams}




        return self.allTeams

    def getSortedNeighbors(self, v0):
        vicini = self.grafo.neighbors(v0)
        viciniTuples = []
        for v in vicini:
            viciniTuples.append((v, self.grafo[v0][v]["weight"]))

        viciniTuples.sort(key=lambda x: x[1])
        return viciniTuples


    def printGraphDetails(self):
        print(f"Grafo creato con {len(self.grafo.nodes)} nodi e {len(self.grafo.edges)} archi")


    def getGraphDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)