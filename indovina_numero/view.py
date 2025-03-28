import flet as ft


class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)

        self.txtNmax= ft.TextField(label="numero massimo",value=self._controller.getNmax(),disabled=True)
        self.txtMmax= ft.TextField(label="tentativi massimi",value=self._controller.getMmax(),disabled=True)
        self.txtMrim= ft.TextField(label="tentativi rimanenti",value=self._controller.getMrim(),disabled=True)
        self.txtTentativo= ft.TextField(label="tentativo",disabled=True)
        row1= ft.Row([self.txtNmax,self.txtMmax,self.txtMrim],alignment=ft.MainAxisAlignment.CENTER)


        self.btnNuova=ft.ElevatedButton(text="Nuova partita",on_click=self._controller.handleNuova)
        self.btnProva =ft.ElevatedButton(text="Prova",on_click=self._controller.handleProva,disabled=True)

        row2=ft.Row([self.btnNuova,self.txtTentativo,self.btnProva],alignment=ft.MainAxisAlignment.CENTER)

        self._lvOut= ft.ListView()


        self._page.add(self._titolo,row1,row2,self._lvOut)

    def setController(self, controller):
        self._controller = controller

    def update(self):
        self._page.update()
