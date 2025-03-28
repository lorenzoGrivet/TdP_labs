import warnings

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.selectedTeam = None

    def handleCreaGrafo(self, e):
        if self._view._ddAnno.value is None:
            self._view._txt_result.controls.append(ft.Text(f"Seleziona un anno"))
            return
        self._model.buildGraph(self._view._ddAnno.value)
        self._view._txt_result.clean()
        n,a = self._model.getGraphDetails()
        self._view._txt_result.controls.append(ft.Text(f"Il grafo è fatto di {n} nodi e {a} archi"))
        self._view.update_page()



    def handleDettagli(self, e):
        v0 = self.selectedTeam
        vicini = self._model.getSortedNeighbors(self.selectedTeam)
        self._view._txt_result.clean()
        self._view._txt_result.controls.append(ft.Text(f"Stampo i vicini di {self.selectedTeam}"))
        for v in vicini:
            self._view._txt_result.controls.append(ft.Text(f"{v[1]} - {v[0]}"))
        self._view.update_page()

    def handlePercorso(self, e):
        if self.selectedTeam is None:
            warnings.warn("Squadra non selezionata")
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text(f"Squadra non selezionata"))
            self._view.update_page()

    def fillDDYear(self):
        years = self._model.getYears()
        yearsDD = list(map(lambda x: ft.dropdown.Option(x), years))
        self._view._ddAnno.options = yearsDD
        self._view.update_page()

    def readDDTeams(self, e):
        if e.control.data is None:
            self.selectedTeam = None
        else:
            self.selectedTeam = e.control.data
        #print(self.selectedTeam)
    def handleYearDDSelection(self, e):
        self.allTeams = self._model.getTeamsOfYear(self._view._ddAnno.value)
        self._view._txtOutSquadre.clean()
        self._view._ddSquadra.options = []
        self._view._txtOutSquadre.controls.append(ft.Text(f"Ho trovato {len(self.allTeams)} squadre che hanno giocato nell'anno {self._view._ddAnno.value}"))
        for t in self.allTeams:
            self._view._txtOutSquadre.controls.append(ft.Text(f"{t.teamCode}"))
            self._view._ddSquadra.options.append(ft.dropdown.Option(data = t,
                                                                     text = t.teamCode,
                                                                     on_click=self.readDDTeams))
        self._view.update_page()