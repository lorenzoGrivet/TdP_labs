import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff

        self._page = page
        self._page.title = "TdP Lab 09"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._btnAnalizza = None
        self._txtIn = None
        self._txt_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("Flights Manager", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with  controls
        self._txtIn = ft.TextField(label="Distanza Minima")
        self._btnAnalizza = ft.ElevatedButton(text="Analizza Aeroporti", on_click=self._controller.handleAnalizza)
        row1 = ft.Row([self._txtIn, self._btnAnalizza],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)


        # List View where the reply is printed
        self._txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._txt_result.controls.append(ft.Text("Add your output text here!"))
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

    def update_page(self):
        self._page.update()
