import copy
import itertools
import math
import time

import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.aumentareCucine = False
        self.grafo = nx.Graph()
        self.listaUtente=[]
        self.cucine_R={}
        self.solBest=[]
        self.maxPunteggio=-1
        self.maxDaCercare=-1

    #parte iniziale**********************
    def getAllCitta(self):
        return DAO.getAllCittaDAO()
    def getAllPrezzi(self):
        return DAO.getAllPrezziDAO()
    def getMinMaxRating(self,citta,prezzo):
        return (DAO.getMinMaxRatingDAO(citta,prezzo))

    def getCucine(self,citta,prezzo,min,max):
        lista=[]
        self.cucine_R.clear()

        resDAO = DAO.getCucineDAO(citta, prezzo, min, max)
        for i in resDAO:
            b = str(i)
            # cucine = b.removeprefix("[").removesuffix("]").replace("'", "").replace(" ", "").split(",")
            cucine = b.removeprefix("[").removesuffix("]").replace("'", "").split(",")

            for c in cucine:
                c = c.strip()
                if c not in lista:
                    lista.append(c)
                    self.cucine_R[c]=False
        return lista

    def esisteRistorante(self,citta, prezzo, min,max):
        res= DAO.esisteRistoranteDAO(citta,prezzo,min,max)
        if len(res)==0:
            return False
        else:
            return True

#*********************************


    def getTopDieci(self,citta,prezzo,min,max,cucina):
        res=DAO.getTopDieciDAO(citta,prezzo,min,max,cucina)
        return res

#*********************************

    def aggiungiRistorante(self,risto):
        if risto is None:
            return False, "null"
        if len(self.listaUtente)==10:
            return False, "piena" #errore, già piena
        if risto in self.listaUtente:
            return False,"doppia" #errore, non è piena (quindi c'è già)

        self.listaUtente.append(risto)
        return self.listaUtente,True
        pass

    def rimuoviRistorante(self,risto):
        if self.listaUtente ==[]:
            return False,True
        if risto not in self.listaUtente:
            return False,False

        self.listaUtente.remove(risto)
        return self.listaUtente,True

    def svuotaLista(self):
        self.listaUtente.clear()
        return


    #********************

    def checkCucina(self,nome,valore):
        if nome not in self.cucine_R.keys():
            pass
        else:
            self.cucine_R[nome]=valore
        return nome,self.cucine_R[nome]

    #**************ricorsione***************

    def calcola(self,citta,prezzo,giorni,veg,cel,hal):
        restrizioni=["Vegan Options","Vegetarian Friendly","Gluten Free Options"]

        cucine = [nome for (nome, valore) in self.cucine_R.items() if valore] #queste sono le tipologie che l'utente ha selezionato

        if giorni<= len(self.listaUtente): #se i giorni sono di meno dei ristoranti non va bene
            return False,0
        elif len(cucine)==0:#se non ho selezionato cucine
          return False,-1
        elif not self.aumentareCucine and len(cucine)>math.ceil(giorni/2): #se ne ho piu della meta dei giorni no
            return False,1
        elif self.aumentareCucine and len(cucine)>7: #se ne ho piu dei giorni no (non ho trovato abbastanza ristoranti  )
            return False,2


        if veg or cel or hal:
            allRistoranti=DAO.getAllRistorantiDAORestrizioni(prezzo,citta,veg,cel,hal) #scelgo i ristoranti dal database
        else:
            allRistoranti= DAO.getAllRistorantiDAO(prezzo,citta)   #********ATTENZIONE************************************

        ristorantiOK=[]

        for r in allRistoranti: #allristoranti sono tutti della citta e quel prezzo
            a=False
            i=0

            while not a: #aggiungo i ristoranti se hanno una cucina tra quelle selezionate
                if i==len(cucine):#stop
                    a=True

                elif cucine[i] in r.Cuisine_Style:

                    #assegno ristorante a "classe" di recensioni, mi serve per il punteggio
                    r=self.assegnaClasse(r)

                    #uso questo ciclo per trasformare str in set per confronto che faccio dopo
                    s=r.Cuisine_Style.removeprefix("[").removesuffix("]").replace("'", "").strip().split(",")
                    r.setCucine=set()

                    for d in s:
                        d=d.strip()
                        # non voglio considerare le restrizioni come tipo di cucina (i ristoranti che ho sono già filtrati dalla query)
                        if d not in restrizioni:
                            r.setCucine.add(d) #il set sono tutte le cucine che NON sono restrizioni


                    #prendo recensioni
                    # s=str(r.Reviews)
                    # lRec=s.replace("[","").replace("]","").split("', '")
                    # diz_Rec={}
                    # diz_Rec[lRec[2].replace("'","").strip()]=lRec[0].replace("'", "").strip()
                    # diz_Rec[lRec[3].replace("'","").strip()]=lRec[1].replace("'", "").strip()
                    #
                    # r.dizRec=diz_Rec


                    #aggiungo
                    ristorantiOK.append(r)
                    a=True
                else:
                    i+=1

        self.creaGrafo(ristorantiOK)

        self.maxDaCercare=giorni-len(self.listaUtente)

        ta=time.time()
        self.solBest=[]
        self.maxPunteggio=0
        a=False
        if len(self.listaUtente)==0:
            a=True
        ricorsioneFatta=False
        d=len(self.listaUtente)-1

        if len(self.listaUtente)>0:
            while not a:
                if d<0:
                    a=True
                elif self.listaUtente[d] in self.grafo.nodes:
                    self.ricorsione(copy.deepcopy(self.listaUtente),self.listaUtente[d],giorni)
                    ricorsioneFatta=True
                    a=True
                else:
                    a=False
                    d-=1

        if a==True and ricorsioneFatta==False:

            conn = list(nx.connected_components(self.grafo))
            e=0
            for partenza in conn:
                partenza=list(partenza)
                partenzaOrdinata = list(sorted(partenza,key=lambda x:(x.Rating),reverse=True))
                e+=1
                print(e)
                giorni=giorni-len(self.listaUtente)
                self.ricorsione([partenzaOrdinata[0]],partenzaOrdinata[0],giorni)

            self.solBest=self.listaUtente+self.solBest


        tb=time.time()
        print(f"Tempo ricorsione: {tb-ta}")
        print(f"Soluzione: {len(self.solBest)}")
        for a in self.solBest:
            print(f"{a}, {a.Cuisine_Style}")
        print("***Fine***\n")
        return True,self.solBest


    def creaGrafo(self,nodi):
        self.grafo=nx.Graph()
        self.grafo.add_nodes_from(nodi)

        archi=[]
        t1=time.time()
        for i in range(len(nodi)):
            for j in range(i+1,len(nodi)):
                a=nodi[i]
                b=nodi[j]

                c=len(a.setCucine.intersection(b.setCucine))

                d=len(a.setCucine-b.setCucine)
                e=len(b.setCucine-a.setCucine)

                if d>math.ceil(len(a.setCucine)/2) or e>math.ceil(len(b.setCucine)/2): #aggiungo arco solo se un risto ha piu metà cucine diverse dall'altro o viceversa
                    daAggiungere=True
                else:
                    daAggiungere=False

                if daAggiungere: #**************************ATTENZIONE cambiare anche con restrizioni
                    archi.append((a,b))

        t2=time.time()
        print(f"Tempo: {t2-t1}")
        self.grafo.add_edges_from(archi)
        print(len(self.grafo.nodes),len(self.grafo.edges))
        pass


    def ricorsione(self, parziale, ultimo,giorni):
        # print("*")
        ammissibili = self.getAmmissibili(parziale,ultimo,giorni)

        if self.isTerminale(parziale,ammissibili):
            # print(parziale)
            c=self.calcolaPuntaggio(parziale)

            if c> self.maxPunteggio:
                print(c)
                self.solBest=copy.deepcopy(parziale)
                self.maxPunteggio=c
                return
        else:
            for a in ammissibili:
                parziale.append(a)
                self.ricorsione(parziale,a,giorni)
                parziale.pop()

        pass

    def getAmmissibili(self, parziale, ultimo,giorni):
        amm=[]
        if len(parziale)==giorni:
            return amm
        else:
            vic= list(self.grafo.neighbors(ultimo))
            for a in vic:
                if a not in parziale:
                    if ultimo.Ranking < a.Ranking: #************attenzione**********
                        amm.append(a)
            return amm
        pass

    def isTerminale(self, parziale,ammissibili):
        if len(ammissibili)==0:
            return True

        return False
        pass

    def calcolaPuntaggio(self, parziale):
        somma=0
        for i in parziale:
            somma+=i.Rating
        return somma
        pass

    def assegnaClasse(self, r):

        if r.Number_of_Reviews < 5:
            r.classe=0
        elif r.Number_of_Reviews >=5 and r.Number_of_Reviews<30:
            r.classe=1
        elif r.Number_of_Reviews>=30 and r.Number_of_Reviews<100:
            r.classe=2
        elif r.Number_of_Reviews>=100 and r.Number_of_Reviews<500:
            r.classe=3
        elif r.Number_of_Reviews>=500:
            r.classe=4
        else:
            pass

        #calcolo il rating tenendo anche conto di recensioni.
        deltaRating = r.Rating - 3
        correzione = deltaRating * r.classe * 0.1  # moltiplico la classe di recensioni a cui risto appartiene(da 0 a 4) per la
        # differenza del rating rispetto alla media. correggo per 0,1.
        # così piu recensioni positive un risto ha iu aumenta il suo rating, se invece ne ha poche positive aumenta di meno
        r.Rating = r.Rating + correzione
        return r
        pass


