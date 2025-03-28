import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view


    def handleSentence(self,e):

        txtIn=self._view.testo.value
        language=self._view.lingua.value
        modality=self._view.tipo.value

        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                #return paroleErrate, t2 - t1


            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                #return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                #return paroleErrate, t2 - t1
            case _:
                return None

        row1 = ft.Row([ft.Text(f"Testo: {self._view.testo.value}")])
        row2 = ft.Row([ft.Text(f"Parole Errate: {paroleErrate}")], alignment=ft.MainAxisAlignment.START)
        row3 = ft.Row([ft.Text(f"Tempo: {t2 - t1}")])

        lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        lv.controls.append(row1)
        lv.controls.append(row2)
        lv.controls.append(row3)
        self._view.page.add(lv)
        self._view.testo.value=""

        self._view.page.update()





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
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text