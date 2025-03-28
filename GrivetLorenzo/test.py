import random
import time

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

    file=open("tempi/tempiRicorsione.txt", "a")
    file.write("\n\nNUOVO TEST********************************\n")

    for c in allcitta:
        print(f"\n****{c}")
        file.write(c+":\n")

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
            t1=time.time()
            a,b=mod.calcola(c,p,5,False,False,False)
            t2=time.time()

            file.write(f"{t2-t1} - {len(b)}\n")
    file.close()
    print("finito")

def testClassi():
    #test per suddivisione classi
    citta=DAO.getAllCittaDAO()

    for c in citta:
        res=DAO.testClassiDAO(c)
        print(f"\n{c}:")
        print(res)

# rist=DAO.getAllRistorantiDAO("$","Rome")
# for r in rist:
#     s = str(r.Reviews)
#     lRec = s.replace("[", "").replace("]", "").split("', '")
#     dizRec = {}
#     dizRec[lRec[2].replace("'", "").strip()] = lRec[0].replace("'", "").strip()
#     dizRec[lRec[3].replace("'", "").strip()] = lRec[1].replace("'", "").strip()
#     print(dizRec)


def testMigliori(i):
    #tempo per trovare i 10 migliori sql-python

    file=open("tempi/tempi.txt", "w")
    file2=open("tempi/tempiPython.txt", "w")
    citta=DAO.getAllCittaDAO()
    prezzi=DAO.getAllPrezziDAO()

    for c in citta:
        for p in prezzi:

            t1=time.time()
            d=mod.getTopDieci(c,p,1,5,"Qualsiasi")
            t2=time.time()

            t3=time.time()
            rist= DAO.getAllRistorantiDAOTest(p,c)
            ristOrd=sorted(rist,key=lambda x:(-x.Rating,x.Ranking))
            if len(ristOrd)<10:
                pass
            else:
                ristOrd=ristOrd[:10]
            t4=time.time()

            file.write(f"{i} {t2-t1}\n")
            file2.write(f"{i} {t4-t3}\n")
            print(i)
            i+=1

#for i in range(0,3):
#     testGrafoRic()

def creaDizionari():
    #divido i tempiricorsione in dizionari per ogni fascai di prezzo
    file=open("tempi/tempiRicorsione.txt", "r")
    lis = file.readlines()
    diz={}
    citta=None
    i=-1
    n=1

    for a in lis:
        a=a.strip("\n").strip()
        if a=="" or "*" in a:
            pass
        else:
            if "a" in a or "e" in a or "i" in a or "o" in a or "u" in a:
                i=1
                a=a.replace(":","")
                citta=a
            else:
                # print(n)
                # n+=1

                b=a.split(" - ")
                a=b[0]

                if (citta,i) in diz.keys():
                    tempi = diz[(citta,i)]
                    tempi.append(a)
                    diz[citta,i]=tempi
                    i+=1
                else:
                    diz[(citta,i)]=[a]
                    i+=1

    file.close()

    dizPrimo={}
    dizSecondo={}
    dizTerzo={}

    for k in diz.keys():
        if k[1]==1:
            dizPrimo[k[0]]=diz[k]
        elif k[1]==2:
            dizSecondo[k[0]]=diz[k]
        elif k[1]==3:
            dizTerzo[k[0]]=diz[k]
        else:
            print("no")
    return dizPrimo,dizSecondo,dizTerzo

def testMain():
    #testMain
    dP,dS,dT= creaDizionari()

    dizionari=[dP,dS,dT]

    for d in dizionari:

        for a in d.keys():
            lis=d[a]

            somma=0
            for i in lis:
                somma+= float(i)

            avg=somma/len(lis)
            print(lis,avg)
            d[a]=avg


    nomiFile=["tempiPrimo.txt","tempiSecondo.txt","tempiTerzo.txt"]

    for n in nomiFile:
        file=open(n,"w")

        if n == "tempiPrimo.txt":
            dizionario=dP
        elif n=="tempiSecondo.txt":
            dizionario=dS
        else:
            dizionario=dT

        for a in dP.keys():
            file.write(f"{a[:3]} {dizionario[a]}\n")
        file.close()

def testRecensioni(n,nulle):
    citta=DAO.getAllCittaDAO()
    prezzi=DAO.getAllPrezziDAO()
    for c in citta:
        for p in prezzi:

            allR= DAO.testRecensioni(c,p)
            for r in allR:
                n += 1
                b,r2=mod.getRecensioni(r)
                if b:
                    print(r2.dizRec)
                else:
                    print("********************************************************************************************************\n***************************************************************************\n***********************************************************************\n**********************************************************************\n**************************************************************************\n*********************************************************\n***************************")
                    nulle+=1

    return n,nulle
