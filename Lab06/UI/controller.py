import flet as ft
from database import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleTop(self,e):
        self._view.lv.clean()

        lista= DAO.DAO().getTop5(self._view.ddAnno.value,self._view.ddBrand.value,self._view.ddRetailer.value)

        for a in lista:
            self._view.lv.controls.append(ft.Text(a))
            self._view.update_page()
        self._view.update_page()


    def handleAnalizza(self,e):
        self._view.lv.clean()
        lista = self._model.analizza(self._view.ddAnno.value, self._view.ddBrand.value, self._view.ddRetailer.value)

        self._view.lv.controls.append(ft.Text(f"Statistiche vendite:"))
        self._view.lv.controls.append(ft.Text(f"Ricavi totali: {lista[0]}"))
        self._view.lv.controls.append(ft.Text(f"Numero vendite: {lista[1]}"))
        self._view.lv.controls.append(ft.Text(f"Numero retailers coinvolti: {lista[2]}"))
        self._view.lv.controls.append(ft.Text(f"Numero prodotti coinvolti: {lista[3]}"))

        self._view.update_page()



