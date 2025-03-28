import random

from database.DAO import DAO
from model import model

mod=model.Model()

def testGrafoRic():
    def getCucine2(citta,prezzo):
        lista = []
        cucine_R={}

        resDAO = DAO.getCucineDAO(citta, prezzo, 1, 5)
        for i in resDAO:
            b = str(i)
            # cucine = b.removeprefix("[").removesuffix("]").replace("'", "").replace(" ", "").split(",")
            cucine = b.removeprefix("[").removesuffix("]").replace("'", "").split(",")

            for c in cucine:
                c = c.strip()
                if c not in lista:
                    lista.append(c)
                    cucine_R[c] = False
        return cucine_R

    allcitta=mod.getAllCitta()
    allprezzi=mod.getAllPrezzi()
    mod.listaUtente=[]



    for c in allcitta:
        print(f"\n****{c}")
        for p in allprezzi:
            print(f"- {p}")

            s=""

            cucine_R = getCucine2(c,p)
            k=list(cucine_R.keys())

            for i in range(3):
                pos=random.choice(range(0,len(k)))
                el=k[pos]
                cucine_R[el]=True

            mod.cucine_R=cucine_R

            for a in cucine_R.keys():
                if cucine_R[a]:
                    s+=f" {a}"

            print("Cucine: "+s)
            mod.calcola(c,p,7,False,False)

    print("finito")

def testClassi():
    citta=DAO.getAllCittaDAO()

    for c in citta:
        res=DAO.testClassiDAO(c)
        print(f"\n{c}:")
        print(res)

rist=DAO.getAllRistorantiDAO("$","Rome")
for r in rist:
    s = str(r.Reviews)
    lRec = s.replace("[", "").replace("]", "").split("', '")
    dizRec = {}
    dizRec[lRec[2].replace("'", "").strip()] = lRec[0].replace("'", "").strip()
    dizRec[lRec[3].replace("'", "").strip()] = lRec[1].replace("'", "").strip()
    print(dizRec)