import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleCreaGrafo(self, e):
        if self._view._ddAnno.value is None:
            pass

        self._model.buildGraph(self._view._ddAnno.value)

        self._view._txt_result.controls.clear()

        self._view._txt_result.controls.append(ft.Text(f"Grafo creato"))
        n,a=self._model.printGraphDetails()
        self._view._txt_result.controls.append(ft.Text(f"Grafo creato con {n} nodi e {a} archi"))

        self._view.update_page()

        pass

    def handleDettagli(self, e):
        vicini=self._model.getSortedNeighbors(self.selectedTeam)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"vicini di: {self.selectedTeam}"))
        for v in vicini:
            self._view._txt_result.controls.append(ft.Text(f"{v[1]} - {v[0]}"))
        self._view.update_page()

        pass

    def handlePercorso(self, e):
        pass

    def handleDDYearSelection(self,e):
        teams=self._model.getTeamsOfYear(self._view._ddAnno.value)
        self._view._txtOutSquadre.clean()
        self._view._txtOutSquadre.controls.append(ft.Text(f"Ho trovato {len(teams)} squadre che hanno giocato nel {self._view._ddAnno.value}"))

        for i in teams:
            self._view._txtOutSquadre.controls.append(ft.Text(f"{i.teamCode}"))
            self._view._ddSquadra.options.append(ft.dropdown.Option(data=i,text=i.teamCode,on_click=self.readDDTeams))

        self._view.update_page()

    def readDDTeams(self,e):
        if e.control.data is None:
            self.selectedTeam=None
        else:
            self.selectedTeam=e.control.data
        print(f"{self.selectedTeam}")

    def fillDDYear(self):
        years=self._model.getYears()
        yearsDD=map(lambda x: ft.dropdown.Option(x),years)
        self._view._ddAnno.options=yearsDD
        self._view.update_page()