import flet as ft
from UI import view
from model import model

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._pd=None


    def get_corsi_periodo(self,e):
        if self._pd is None:
            self._view.create_alert("Selezionare periodo didattico")
            return

        corsi = self._model.get_corsi_periodo(self._pd)
        self._view.lst_result.controls.clear()

        for corso in corsi:
            self._view.lst_result.controls.append(ft.Text(corso))
        self._view.update_page()

    def get_studenti_periodo(self,e):
        if self._pd is None:
            self._view.create_alert("Selezionare periodo didattico")
            return
        numero_studenti=self._model.get_studenti_periodo(self._pd)
        self._view.lst_result.controls.append(ft.Text(f"Ci sono {numero_studenti} iscritti"))
        self._view.update_page()
        pass

    def get_studenti_corso(self,e):

        pass

    def get_dettaglio_corso(self,e):
        pass

    def leggi_tendina(self,e):
        self._pd=self._view.dd_periodo.value
        #print(e.control.value)
        print(self._pd)