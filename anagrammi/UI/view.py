import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Esercizio su ricorsione"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_word = None
        self.btn_anagrams = None
        self.btn_reset = None
        self.lst_correct = None
        self.lst_wrong = None

    def load_interface(self):
        # title
        self._title = ft.Text("Anagrammi", color="blue", size=24)
        self._page.controls.append(self._title)

        ##############################
        # ROW with some controls
        ##############################
        # text field for the name
        self.txt_word = ft.TextField(
            label="parola",
            width=400,
            hint_text="Inserire la parola da anagrammare"
        )

        # button for anagrams
        self.btn_anagrams = ft.ElevatedButton(text="Anagrammi", on_click=self._controller.calcola_anagrammi)
        self.btn_reset = ft.ElevatedButton(text="Reset", on_click=self._controller.reset)
        row1 = ft.Row([self.txt_word, self.btn_anagrams, self.btn_reset],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        #######################################
        # Result areas placed in different tabs
        #######################################
        # List View where the reply is printed
        self.lst_correct = ft.ListView(expand=1,
                                       spacing=10,
                                       padding=20,
                                       auto_scroll=True,
                                       controls=[ft.Text("----")])
        self.lst_wrong = ft.ListView(expand=1,
                                     spacing=10,
                                     padding=20,
                                     auto_scroll=True,
                                     controls=[ft.Text("----")])

        tabs_results = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="Anagrammi corretti",
                    content=ft.Container(
                        content=self.lst_correct,
                        alignment=ft.alignment.center
                    ),
                ),
                ft.Tab(
                    text="Anagrammi errati",
                    content=ft.Container(
                        content=self.lst_wrong,
                        alignment=ft.alignment.center
                    ),
                ),
            ],
            expand=1,
        )
        self._page.controls.append(tabs_results)
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
