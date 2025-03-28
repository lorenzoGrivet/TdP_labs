import copy

from database.DAO import DAO
from model import powerOutages


class Model:
    def __init__(self):
        self._solBest = []
        self.max_persone=-1
        self._listNerc = None
        self._listEvents = None
        self.loadNerc()



    def worstCase(self, nerc, maxY, maxH):
        # TO FILL
        parziale=[]
        self.loadEvents(nerc)
        self.ricorsione(parziale,maxY,maxH,self._listEvents,0)
        print(f"{self.print_parziale(self._solBest)}:  {self.max_persone}")

        somma=0.0
        for a in self._solBest:
            somma+= ((a._date_event_finished-a._date_event_began).total_seconds())/3600


        return self._solBest, self.max_persone,somma



        pass
    def ricorsione(self, parziale, maxY, maxH, rimanenti,livello):

        # TO FILL

        maxY=int(maxY)
        maxH=int(maxH)

        # print(f"entro in {livello}")

        #terminale
        if len(rimanenti)==0:

            #CONTEGGIO CLIENTI
            conto = self.calcola_persone(parziale)

            if conto > self.max_persone:
                self.max_persone=conto
                self._solBest=copy.deepcopy(parziale)

                # a=""
                # for i in parziale:
                #     a+= str(i._id)+" - "
                # print(a+"-----CONTO: "+str(conto))

            return

        else:

            for elem in (rimanenti) :

                print(str(elem._id)+"elemento ciclo")

                if self.va_bene(parziale,elem,maxH,maxY):
                    parziale.append(elem)


                    nuovi_rimanenti= copy.deepcopy(rimanenti)
                    nuovi_rimanenti.remove(elem)

                    rimanenti.remove(elem)

                    # print(f"parziale prima di entrare in {livello+1}: {self.print_parziale(parziale)}")
                    self.ricorsione(parziale, maxY, maxH, nuovi_rimanenti,livello+1)
                    # print(f"parziale dopo di uscire da {livello + 1}: {self.print_parziale(parziale)}")

                    # print(f"esco******  da {livello}")
                    parziale.pop()
                else:
                    rimanenti.remove(elem)
                    self.ricorsione(parziale, maxY, maxH, rimanenti,livello+1)



    def calcola_persone(self,parziale):
        conto=0
        for i in range(len(parziale)):
            conto+= parziale[i]._customers_affected
        return conto



    def loadEvents(self, nerc):
        a=DAO.getAllEvents(nerc)
        self._listEvents = a
        i=0

    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()


    def print_parziale(self,parziale):
        s=""
        for a in parziale:
           s+= str(a._id)+" "

        return s

    @property
    def listNerc(self):
        return self._listNerc

    def va_bene(self,parziale,elem,maxH,maxY):
        if parziale==[]:
            return True

        somma = ((elem._date_event_finished-elem._date_event_began).total_seconds())/3600
        anno_min=0
        for i in range(len(parziale)):
            somma += ((parziale[i]._date_event_finished - parziale[i]._date_event_began).total_seconds())/3600

            if parziale[i]._id == elem._id:
                return False

            d=((parziale[i]._date_event_began).year)
            if  d<anno_min or anno_min==0:
                anno_min=parziale[i]._date_event_began.year



        if ( (elem._date_event_finished.year - parziale[0]._date_event_began.year) <= maxY  and somma <= maxH):
            return True
        else:
            return False



