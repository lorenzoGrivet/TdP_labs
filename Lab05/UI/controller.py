import flet as ft

from model import model, studente, corso


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def cercaIscritti(self,e):
        corso= self._view.txt_corso.value
        risultato=[]
        b=False

        for a in model.Model().getIscrizioni().keys():
            if a==corso:
                b=True
                risultato=model.Model().getIscrizioni()[a]

                self._view.stampaVideo("iscritti",risultato)

        if b==False:
            self._view.create_alert("Corso vuoto!!")


    def cercaStudente(self,e):
        matricola = self._view.txt_matricola
        s= studente.Studente
        b=False

        for a in model.Model().getStudenti():
            if str(a.matricola)==str(matricola.value):
                s=a
                b=True

        if b==True:
            self._view.stampaVideo("studente",s)
        else:
            self._view.create_alert("Studente inesistente!!")


    def cercaCorsi(self,e):
        s=None
        risultato=[]
        diz_esami=model.Model().getIscrizioni()
        lista_corsi=model.Model().getCorsi()

        for i in model.Model().getStudenti():
            if str(i.matricola)==self._view.txt_matricola.value:
                s=i

        if s is None:
            self._view.create_alert("Studente inesistente!!")
        else:

            for cTemp in diz_esami.keys():

                for alunno in diz_esami[cTemp]:
                    if str(alunno.matricola)==str(s.matricola):
                        #aggiungere corso a lista risultato
                        for c in lista_corsi:
                            if str(c.codins) == str(cTemp):
                                risultato.append(c)

            if len(risultato)==0:
                self._view.create_alert("Studente non iscritto ad alcun corso!!")
            else:
                self._view.stampaVideo("corsi",risultato)



    def iscrivi(self,e):
        s= None
        c=None
        lista_studenti=model.Model().getStudenti()
        lista_corsi=model.Model().getCorsi()
        diz_corsi=model.Model().getIscrizioni()
        a=False

        for i in lista_studenti:
            if str(i.matricola) == self._view.txt_matricola.value:
                s = i

        if s is None:
            self._view.create_alert("Studente inesistente!!")
        else:

            for i in lista_corsi:
                if str(i.codins) == self._view.txt_corso.value:
                    c = i

            for alunno in diz_corsi[c.codins]:
                if str(alunno.matricola)== str(s.matricola):
                    self._view.create_alert("Studente gia iscritto!!")
                    a=True

            if a==False:
                self._model.aggiungiStudente(s,c)

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()
