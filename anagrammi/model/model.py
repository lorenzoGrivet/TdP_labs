import copy
#from functools import lru_cache
import model


class Model:
    def __init__(self):
        self._anagrammi=set()
        self._anagrammi_list=[]


    def calcola_anagrammi(self,parola):
        self._anagrammi=set()
        self.ricorsione("",parola)
        self._anagrammi_list=[]
        self.ricorsione_list([],parola)

   # @lru_cache(maxsize=NotImplemented)
    def ricorsione(self,parziale,lettere_rimanenti):
        #caso terminale non ci sono lettere rimanenti
        if len(lettere_rimanenti)==0:
            self._anagrammi.add(parziale)
            return
        else:
            #caso non terminale: aggiungere una lettera alla volta e andare avanti in  ricorsionw
            for i in range(len(lettere_rimanenti)):
                parziale+=lettere_rimanenti[i]
                nuove_lettere_rimanenti= lettere_rimanenti[:i]+lettere_rimanenti[i+1:]
                self.ricorsione(parziale,nuove_lettere_rimanenti)
                parziale=parziale[:-1]

    def ricorsione_list(self,parziale,lettere_rimanenti):
        #caso terminale non ci sono lettere rimanenti
        if len(lettere_rimanenti)==0:
            self._anagrammi_list.append(copy.deepcopy(parziale))
            return
        else:
            #caso non terminale: aggiungere una lettera alla volta e andare avanti in  ricorsionw
            for i in range(len(lettere_rimanenti)):
                parziale.append(lettere_rimanenti[i])
                nuove_lettere_rimanenti= lettere_rimanenti[:i]+lettere_rimanenti[i+1:]
                self.ricorsione_list(parziale,nuove_lettere_rimanenti)
                parziale.pop()



if __name__=="__main__":
    word="faro"

    mod=Model()
    (mod.calcola_anagrammi(word))
    print(mod._anagrammi)
    #print(mod._anagrammi_list)