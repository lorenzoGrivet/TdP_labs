import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "TdP Flights Manager 2024"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._txt_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("TdP Flights Manager 2024", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW with  controls
        # text field for the name
        self._txtInNumC = ft.TextField(label="Num compagnie min",
                                       width=150)
        self._btnAnalizza = ft.ElevatedButton(text="Analizza Aeroporti",
                                              on_click=self._controller.handelAnalizza,
                                              width=150)
        row1 = ft.Row([
            ft.Container(self._txtInNumC, width=200),
            ft.Container(self._btnAnalizza, width=200)],
            alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row1)

        self._ddAeroportoP = ft.Dropdown(label="Partenza",
                                         width=290,
                                         disabled=True)
        self._btnConnessi = ft.ElevatedButton(text="Aeroporti Connessi",
                                              on_click=self._controller.handleConnessi,
                                              width=150,
                                              disabled=True)
        row2 = ft.Row([
            ft.Container(self._ddAeroportoP, width=200),
            ft.Container(self._btnConnessi, width=200)],
            alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self._ddAeroportoA = ft.Dropdown(label="Arrivo", width=290,
                                                     disabled=True)
        self._btnPercorso = ft.ElevatedButton(text="Test Connessione",
                                              on_click=self._controller.handleTestConnessione,
                                              width=150,
                                              disabled=True)
        row3 = ft.Row([
            ft.Container(self._ddAeroportoA, width=200),
            ft.Container(self._btnPercorso, width=200)],
            alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)


        self._txtInNumTratte = ft.TextField(label="Num Tratte Max", width=200,
                                                     disabled=True)
        self._btnCercaItinerario = ft.ElevatedButton(text="Cerca Itinerario",
                                                     on_click=self._controller.handleCercaItinerario,
                                                     width=200,
                                                     disabled=True)
        row3 = ft.Row([self._txtInNumTratte, self._btnCercaItinerario],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self._txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self._txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
