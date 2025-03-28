import itertools
import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self.allTeams=[]
        self.grafo=nx.Graph()
        self.idMap={}
        pass

    def getSortedNeighbors(self,v0):
        vicini = self.grafo.neighbors(v0)

        viciniTuples=[]
        for v in vicini:
            viciniTuples.append((v,self.grafo[v0][v]["weight"]))

        viciniTuples.sort(key=lambda x:x[1])
        return viciniTuples

    def getYears(self):
        return DAO.getAllYears()

    def buildGraph(self,year):
        self.grafo.clear()
        if len(self.allTeams)==0:
            print("attenzione non ci sono squadre")
            return

        self.grafo.add_nodes_from(self.allTeams)

        myedges= list(itertools.combinations(self.allTeams,2))
        self.grafo.add_edges_from(myedges)

        # for t1 in self.grafo.nodes:
        #     for t2 in self.grafo.nodes:
        #         if t1!=t2:
        #             self.grafo.add_edge(t1,t2)

        salariesOfTeam=DAO().getSalaryOfTeams(year,self.idMap)
        for a in self.grafo.edges:
            self.grafo[a[0]][a[1]]["weight"]=salariesOfTeam[a[0]]+salariesOfTeam[a[1]]


    def printGraphDetails(self):
        print(f"Grafo creato con {len(self.grafo.nodes)} nodi e {len(self.grafo.edges)} archi")
        return len(self.grafo.nodes),len(self.grafo.edges)

    def getTeamsOfYear(self,anno):
        self.allTeams=DAO.getTeamsOfYear(anno)

        self.idMap={t.ID: t for t in self.allTeams}
        return self.allTeams
