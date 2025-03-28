import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "TdP 2024 - Lab 10"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        self._txt_result = None


    def load_interface(self):
        # title
        self._title = ft.Text("Country Borders", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with controls
        self._txtAnno = ft.TextField(label="Anno",on_change= self._controller.attiva_btn)
        self._btnCalcola = ft.ElevatedButton(text="Calcola Confini", on_click=self._controller.handleCalcola)
        row1 = ft.Row([self._txtAnno, self._btnCalcola], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        # List View where the reply is printed
        self._txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)


        self.btn_percorso=ft.ElevatedButton(text="Calcola Percorso", on_click=self._controller.handlePercorso,disabled=True)
        self.txt_partenza=ft.Dropdown(disabled=True)
        row2=ft.Row([self.txt_partenza,self.btn_percorso], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)
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
