import flet as ft

from model.nerc import Nerc


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._idMap = {}
        self.fillIDMap()

    def handleWorstCase(self, e):
        max_anni=self._view._txtYears.value
        max_ore=self._view._txtHours.value
        nerc=self._view._ddNerc.value


        risultato=self._model.worstCase(int(nerc),max_anni,max_ore)

        self._view._txtOut.clean()
        self._view._txtOut.controls.append(ft.Text(f"Clienti affetti: {self._model.max_persone}"))
        self._view._txtOut.controls.append(ft.Text(f"Somma: risultato[2]"))
        for a in risultato[0]:
            self._view._txtOut.controls.append(ft.Text(f"{a.__str__()}"))

        self._view.update_page()


        pass

    def fillDD(self):
        nercList = self._model.listNerc

        for n in nercList:
            self._view._ddNerc.options.append(ft.dropdown.Option(key=n._id,text=n))
        self._view.update_page()

    def fillIDMap(self):
        values = self._model.listNerc
        for v in values:
            self._idMap[v.value] = v
