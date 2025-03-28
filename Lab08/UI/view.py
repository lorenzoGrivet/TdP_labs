import flet as ft
import os


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff

        self._txtOut = None
        self._page = page
        self._page.title = "TdP 2024 - Insurance Unit"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        page.window_width = 1000  # window's width is 200 px
        page.window_height = 1000
        page.window_center()
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None
        self._btnWorstCase = None
        self._txtHours = None
        self._logo = None
        self._txtYears = None
        self._ddNerc = None

    def load_interface(self):
        # title
        self._title = ft.Text("TdP 2024 - Insurance Unit", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW with controls
        img_path = os.path.join(os.getcwd(), 'UI/NERC-map.png')
        self._logo = ft.Image(src=img_path,
                              width=500,
                              height=500,
                              )

        self._ddNerc = ft.Dropdown(label="Select NERC")



        self._txtYears = ft.TextField(label="Insert max years")
        self._txtHours = ft.TextField(label="Insert max hours")
        self._btnWorstCase = ft.ElevatedButton(text="Worst-Case analysis", on_click=self._controller.handleWorstCase)

        row1 = ft.Row([
            ft.Column([self._logo]),
            ft.Column([self._ddNerc, self._txtYears, self._txtHours, self._btnWorstCase], spacing=60)
        ],alignment=ft.MainAxisAlignment.CENTER, spacing=30)
        self._page.add(row1)

        self._controller.fillDD()

        #TextOutput
        self._txtOut = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)

        self._page.add(self._txtOut)

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
