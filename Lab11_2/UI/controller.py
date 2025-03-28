import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        anni= self._model.anni
        colori=self._model.colori
        for a in anni:
            self._view._ddyear.options.append(ft.dropdown.Option(a))
        for a in colori:
            self._view._ddcolor.options.append(ft.dropdown.Option(a))

        pass


    def handle_graph(self, e):
        self._view.txtOut.clean()
        self._view._ddnode.options.clear()
        anno=int(self._view._ddyear.value)
        colore=self._view._ddcolor.value
        self._model.creaGrafo(anno,colore)

        self._view.txtOut.controls.append(ft.Text(f"Numero nodi: {self._model.getNodes()} --- Numero archi: {self._model.getEdges()}"))
        self._view.txtOut.controls.append(ft.Text(f"Primi tre archi per peso:"))

        res=self._model.maggiori()
        for a in res:
            self._view.txtOut.controls.append(ft.Text(f"Nodo1: {a[0].Product_number}, Nodo2: {a[1].Product_number}---> Peso: {a[2]["peso"]}"))

        rip=self._model.ripetuti()
        self._view.txtOut.controls.append(ft.Text(rip))

        self.fillDDProduct()

        self._view.update_page()
        for i in self._model.grafo.edges(data=True):
            print(f"{i[0].Product_number},{i[1].Product_number},{i[2]["peso"]}")

        pass



    def fillDDProduct(self):
        colore=self._view._ddcolor.value
        prodotti= self._model.prodottiColore(colore)

        for a in prodotti:
            self._view._ddnode.options.append(ft.dropdown.Option(a.Product_number))



    def handle_search(self, e):
        self._view.txtOut2.clean()
        partenza=self._view._ddnode.value
        self._model.calcolaPercorso(self._model.idMap[int(partenza)])

        self._view.txtOut2.controls.append(ft.Text(f"Numero archi con il percorso più lungo: {len(self._model.sol_best)-1}"))
        self._view.update_page()

        pass
