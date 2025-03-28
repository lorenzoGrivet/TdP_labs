import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.DAO=DAO()
        self.anni=self.DAO.getAnni()
        self.colori=self.DAO.getColori()
        self.livello=0
        self.livelloMax=0




        prodotti=self.DAO.getAllProducts()
        self.idMap={}
        for a in prodotti:
            self.idMap[a.Product_number]=a
        self.grafo=nx.Graph()


        self.sol_best=[]
        self.partenza=None

        pass


    def creaGrafo(self,anno, colore):
        self.grafo.clear()

        nodi=self.DAO.getProdottiColore(colore)
        self.grafo.add_nodes_from(nodi)

        vendite= self.DAO.getVendite(colore,anno)

        for a in vendite:

            for b in vendite:
                if a.Product_number!=b.Product_number and a.Retailer_code==b.Retailer_code and a.Date==b.Date:


                    if self.grafo.has_edge(self.idMap[a.Product_number] ,self.idMap[b.Product_number]):
                        # if self.grafo[ self.idMap[a.Product_number] ][ self.idMap[b.Product_number] ]["lista"]==[]:
                        #
                        #     self.grafo[ self.idMap[a.Product_number] ][ self.idMap[b.Product_number] ]["peso"]+=1
                        #     self.grafo[self.idMap[a.Product_number]][self.idMap[b.Product_number]]["lista"] = [a.Date]
                        #
                        # else:
                        l=self.grafo[self.idMap[a.Product_number]][self.idMap[b.Product_number]]["lista"]

                        if not l.__contains__(a.Date):
                            self.grafo[self.idMap[a.Product_number]][self.idMap[b.Product_number]]["peso"] += 1
                            l.append(a.Date)
                            self.grafo[self.idMap[a.Product_number]][self.idMap[b.Product_number]]["lista"]=l


                    #####################################
                    else:
                        self.grafo.add_edge(self.idMap[a.Product_number] ,self.idMap[b.Product_number],peso=1)
                        self.grafo[self.idMap[a.Product_number]][self.idMap[b.Product_number]]["lista"] = [a.Date]


    def maggiori(self):
        grafo2= copy.deepcopy(self.grafo)

        self.grafo_ordinato= sorted(grafo2.edges(data=True) , key=lambda x: x[2]["peso"],reverse=True)
        return self.grafo_ordinato[:3]

    def ripetuti(self):
        listaN=[]
        for a in self.grafo_ordinato[:3]:
            listaN.append(a[0])
            listaN.append(a[1])

        res=[]
        for a in listaN:
            p=copy.deepcopy(listaN)
            p.remove(a)
            if p.__contains__(a):
                if not res.__contains__(a.Product_number):
                    res.append(a.Product_number)
        return res


    def prodottiColore(self,colore):
        prodotti=self.DAO.getProdottiColore(colore)
        return prodotti


    def calcolaPercorso(self,partenza):
        self.sol_best=[]

        parziale=[partenza]
        # grafoR=copy.deepcopy(self.grafo)
        self.ricorsione(parziale,partenza)
        print("**************")

        return len(self.sol_best)
    def ricorsione(self,parziale,partenza):
        self.livello += 1
        if self.livello>self.livelloMax:
            self.livelloMax=self.livello
            print(f"Livello: {self.livelloMax}")


        if self.controllaTerminale(parziale,partenza):
            # print("entro in terminale")


            #condizioni terminali
            if len(parziale)>len(self.sol_best):
                self.sol_best=copy.deepcopy(parziale)

                # print("Trovata sol ottima:")
                s=""
                for a in self.sol_best:
                   s+=str(a.Product_number) + " - "
                print(f"{len(self.sol_best)}:  {s}")

            else:
                # print("terminale verificata, non ottima")
                pass

            return
        else:
            succ=list(self.grafo.neighbors(partenza))

            for a in succ:
                if self.controlla(parziale,partenza,a):
                    parziale.append(a)
                    self.ricorsione(parziale,a)
                    self.livello+= -1
                    # print(f"Livello: {self.livello}")
                    parziale.pop()

        # if self.controllaTerminale(parziale,partenza):
        #     if len(parziale)>len(self.sol_best):
        #         self.sol_best=parziale
        #
        #     return
        # else:
        #     succ=list(self.grafo.neighbors(partenza))
        #
        #     for a in succ:
        #         if self.controlla(parziale,partenza,a):
        #             parziale.append(a)
        #             self.ricorsione(parziale,a)
        #             parziale.pop()


    def controllaTerminale(self,parziale, partenza):
        a=True
        if len(parziale)>1:
            max = self.grafo[parziale[-2]][parziale[-1]]["peso"]
        else:
            max=0

        succ= list(self.grafo.neighbors(partenza))
        for i in succ:

            arcoEsistente = False
            for d in range(len(parziale) - 1):
                if (partenza==parziale[d] and i ==parziale[d+1]) or (i==parziale[d] and partenza ==parziale[d+1]):
                # if self.grafo.get_edge_data(partenza, i) == self.grafo.get_edge_data(parziale[d], parziale[d + 1]):
                    arcoEsistente = True

            if self.grafo[partenza][i]["peso"] >= max and not arcoEsistente:
                a=False

        return a


    def controlla(self,parziale,part,esame):
        a=False
        max=0
        if len(parziale)>1:
            max=self.grafo[parziale[-2]][parziale[-1]]["peso"]

        arcoEsistente=False
        for i in range(len(parziale)-1):
            if (part==parziale[i] and esame== parziale[i+1]) or (esame==parziale[i] and part== parziale[i+1]):
            # if self.grafo.get_edge_data(part,esame)==self.grafo.get_edge_data(parziale[i],parziale[i+1]):
                arcoEsistente=True

        if self.grafo[part][esame]["peso"]>=max and not arcoEsistente:
            a=True
        e=0
        return a


    def getNodes(self):
        return len(self.grafo.nodes)

    def getEdges(self):
        return len(self.grafo.edges)