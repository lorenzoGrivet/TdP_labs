from dictionary import Dictionary


class Translator:

    def __init__(self):
        pass

    def printMenu(self):
        print("1. Aggiungi nuova parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Exit")
        pass

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        diz={}
        file = open(dict,"r")
        for a in file:
            lista= a.split(" ")
            diz[lista[0].lower().strip()]=lista[1].lower().strip()

        file.close()
        d=Dictionary(dizionario=diz)
        return d
        pass

    def handleAdd(self, entry,dizionario):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        lista=entry.split()
        dizionario.addWord(lista[0],lista[1])
        return dizionario
        pass

    def handleTranslate(self, query,dizionario):
        # query is a string <parola_aliena>
        traduzione=dizionario.translate(query)
        return traduzione
        pass

    def handleWildCard(self,query,dizionario):
        # query is a string with a ? --> <par?la_aliena>
        #dacercare= query.replace("?",".")
        traduzione=dizionario.translateWordWildCard(query)
        return traduzione
        pass