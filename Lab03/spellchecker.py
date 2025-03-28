import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multi = md.MultiDictionary()
        pass

    def handleSentence(self, txtIn, language):

        #ricerca contains
        start_time = time.time()

        testo = replaceChars(txtIn)
        lista_testo = testo.lower().split(" ")

        risultato_contains = self.multi.searchWord(lista_testo, language)
        end_time = time.time()
        tempo_contains=end_time-start_time

        start_time = time.time()
        risultato_linear=self.multi.searchWordLinear(lista_testo,language)
        end_time=time.time()
        tempo_linear=end_time-start_time

        start_time = time.time()
        risultato_dicotomic = self.multi.searchWordDicotomic(lista_testo, language)
        end_time = time.time()
        tempo_dicotomic = end_time - start_time

        finale=[(risultato_contains,tempo_contains),(risultato_linear,tempo_linear),(risultato_dicotomic,tempo_dicotomic)]

        return finale
        pass

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
    pass