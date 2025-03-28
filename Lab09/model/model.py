from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.voli=DAO().getAllFlight()
        self.aeroporti=DAO().getAllAirport()

        self.grafo=None




    def calcola_distanza(self):

        diz={}

        for v in self.voli:
            if diz.__contains__((v.dep_airport, v.arr_airport)):
                diz[(v.dep_airport,v.arr_airport)][0] += v.distance
                diz[(v.dep_airport, v.arr_airport)][1] += 1
            elif diz.__contains__((v.arr_airport,v.dep_airport)):
                diz[( v.arr_airport,v.dep_airport)][0] += v.distance
                diz[(v.arr_airport, v.dep_airport)][1] +=1
            else:
                diz[(v.dep_airport, v.arr_airport)] = [v.distance,1]

        return diz


    def crea_grafico(self,min):
        self.grafo = nx.Graph()
        for i in self.aeroporti:
            self.grafo.add_node(i.id)

        diz= self.calcola_distanza()

        for a in diz.keys():
            somma=diz[a][0]
            n=diz[a][1]
            media=somma/n

            if media>=int(min):
                self.grafo.add_edge(a[0],a[1],distanza=media)




