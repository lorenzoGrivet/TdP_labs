import copy
import warnings

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):
        try:
            totDint = int(self._view._txtInDurata.value)
        except ValueError:
            warnings.warn_explicit(message="duration not integer",
                                   category=TypeError,
                                   filename="controller.py",
                                   lineno=15)
            return

        self._model.buildGraph(totDint)

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato."))
        nN, nE = self._model.getGraphSize()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {nN} nodi e {nE} archi."))


        nodes = self._model.getNodes()
        nodes.sort(key = lambda x: x.Title)
        # for n in nodes:
        #     self._view._ddAlbum.options.append(
        #         ft.dropdown.Option(
        #             data = n,
        #             text = n.Title,
        #             on_click = self.getSelectedAlbum
        #         )
        #     )
        listDD = map(lambda x: ft.dropdown.Option(data = x,
                                                  text = x.Title,
                                                  on_click = self.getSelectedAlbum), nodes)
        self._view._ddAlbum.options.extend(listDD)
        self._view.update_page()
    def getSelectedAlbum(self, e):
        print("getSelectedAlbum called")
        if e.control.data is None:
            self._choiceAlbum = None
        else:
            self._choiceAlbum = e.control.data
        print(self._choiceAlbum)

    def handleAnalisiComp(self, e):
        if self._choiceAlbum is None:
            warnings.warn("Album field not selected.")
            return
        sizeC, totDurata = self._model.getConnessaDetails(self._choiceAlbum)

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(
            f"La componente connessa che include {self._choiceAlbum} "
            f"ha dimensione {sizeC} e durata totale {totDurata}"))
        self._view.update_page()
    def handleGetSetAlbum(self, e):
        a1= self._choiceAlbum
        dTot= int(self._view._txtInSoglia.value)
        self._model.getSetAlbum(a1,dTot)
        pass