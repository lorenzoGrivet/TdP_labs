import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):
        self._model.crea_grafico(self._view._txtIn.value)

        self._view._txt_result.clean()

        self._view._txt_result.controls.append(ft.Text(f"Numero nodi: {len(self._model.grafo.nodes)}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero archi: {len(self._model.grafo.edges)}"))

        for i in self._model.grafo.edges:
            dist=self._model.grafo.edges[i]["distanza"]

            self._view._txt_result.controls.append(ft.Text(f"La distanza tra {i[0]} e {i[1]} è {dist}"))

        self._view.update_page()

