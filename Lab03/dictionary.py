class Dictionary:
    def __init__(self):
        self._dict=[]
        pass

    def loadDictionary(self,path):
        diz = self.dict
        nome=""

        if path=="italian":
           nome="resources/Italian.txt"
        elif path=="english":
            nome = "resources/English.txt"
        elif path == "spanish":
            nome = "resources/Spanish.txt"

        file = open(nome, "r",encoding="utf-8")

        for a in file:
            a=a.strip("\n")
            a=a.strip("\t")
            a=a.strip()
            a=a.rstrip()
            a=a.replace('\n','')
            diz.append(a.lower())

        file.close()
        return diz
        pass

    def printAll(self):
        for a in self.dict:
            print(a)
        pass


    @property
    def dict(self):
        return self._dict
