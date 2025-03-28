from operator import attrgetter
from database.DAO import DAO

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        anno=int(self._view._txtAnno.value)
        self._model.calcolaConfini(anno)

        self._view._txt_result.controls.append(ft.Text(f"Grafo creato"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodes()} nodi"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumEdges()} archi"))

        self._view._txt_result.controls.append(ft.Text(f"Componenti connesse: {(self._model.connesse)}"))


        # gradi= dict(self._model.grafo.degree())
        # ordinata=sorted(gradi,key=gradi.get,reverse=True)

        # for nodo in self._model.grafo.nodes:
        #     self._view._txt_result.controls.append(ft.Text(f"{self._model.idMap[nodo]}: {self._model.grafo.degree(nodo)} vicini"))

        diz_ordinato=dict(sorted(self._model.idMap.items() , key=lambda item: item[1].StateNme))

        for a in diz_ordinato:
            # print(self._model.idMap[a])

            if self._model.e.__contains__(self._model.idMap[a].CCode):

                self._view._txt_result.controls.append(ft.Text(f"{self._model.idMap[a]} -> {self._model.grafo.degree(a)}"))


        self._view.update_page()

    def handlePercorso(self,e):
        self._view._txt_result.controls.clear()
        partenza=self._view.txt_partenza.value
        anno=self._view._txtAnno.value
        risultato=self._model.calcolaPercorso(partenza,anno)

        for a in risultato:
            self._view._txt_result.controls.append(ft.Text(f"{self._model.idMap[a]} -> {self._model.grafo.degree(a)}"))

        self._view.update_page()

    def attiva_btn(self,e):
        self._view.txt_partenza.disabled=False
        self._view.btn_percorso.disabled=False
        self.fillDDPercorso()


    def fillDDPercorso(self):
        anno=self._view._txtAnno.value
        nodi=DAO().getNodi(anno)
        for a in nodi:

            self._view.txt_partenza.options.append(ft.dropdown.Option(key=a,text=self._model.idMap[a]))

