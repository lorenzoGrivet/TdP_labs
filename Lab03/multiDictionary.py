import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dizio =d.Dictionary()
        #self.rich = rw.RichWord()
        pass

    def printDic(self, language):
        print(self.dizio.printAll())
        pass

    def searchWord(self, words, language):
        #lista_richwords=[]
        sbagliate=[]
        diz=self.dizio.loadDictionary(language)

        for parola in words:
            a = rw.RichWord(parola)

            if (diz.__contains__(parola)):
                a.corretta=True
            else:
                a.corretta=False
                sbagliate.append(a)

            #lista_richwords.append(a)
        return sbagliate
        pass
    def searchWordLinear(self,words,language):
        sbagliate=[]
        diz= self.dizio.loadDictionary(language)

        for parola in words:
            a=rw.RichWord(parola)

            for i in diz:
                if i==parola:
                    a.corretta=True
                    break
                else:
                    a.corretta=False

            if (a.corretta==False):
                sbagliate.append(a)

        return sbagliate
        pass

    def searchWordDicotomic(self,words,language):
        sbagliate = []
        diz = self.dizio.loadDictionary(language)

        for parola in words:
            a=rw.RichWord(parola)

            medio= diz[round(len(diz)/2)]

            if (parola==medio):
                a.corretta=True
                break

            if (parola<medio):
               for i in range(0,round(len(diz)/2)):

                   if diz[i]==parola:
                       a.corretta=True
                       break
                   else:
                       a.corretta=False

            if parola>medio:
                for i in range(round(len(diz)/2)+1,len(diz)):

                    if diz[i] == parola:
                        a.corretta = True
                        break
                    else:
                        a.corretta = False

            if a.corretta==False:
                sbagliate.append(a)

        return sbagliate
        pass






