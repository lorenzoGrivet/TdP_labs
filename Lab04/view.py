import flet as ft
#import controller as c


class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here

        #row 1

        #DA FARE CONTROLLO ON_CHANGE
        self.lingua = ft.Dropdown(label="Lingua",width=150,on_change=self.controlla_lingua)
        self.imposta_parametri("lingua")

        row1=ft.Row([self.lingua])

        self.tipo = ft.Dropdown(label="Tipo", width=150,on_change=self.controlla_tipo)
        self.imposta_parametri("tipo")
        self.testo = ft.TextField(label="Testo",width=500)
        self.btn= ft.ElevatedButton(text="Traduci",on_click=self.__controller.handleSentence)

        row2=ft.Row([self.tipo,self.testo,self.btn])

        self.page.add(row1,row2)

        self.page.update()

    def imposta_parametri(self,a):
        if a=="lingua":
            for i in ["Italian","English","Spanish"]:
                self.lingua.options.append(ft.dropdown.Option(i))
        elif a=="tipo":
            for i in ["Default","Linear","Dicotomic"]:
                self.tipo.options.append(ft.dropdown.Option(i))
        self.update()




    def controlla_lingua(self,e):
        if not (self.lingua.value== "Italian" or self.lingua.value== "English" or self.lingua.value == "Spanish"):
            self.page.add(ft.Text("inserisci lingua"))
            print("*******************************************")


    def controlla_tipo(self,e):
        if not (self.tipo.value == "Default" or self.tipo.value == "Linear" or self.tipo.value == "Dicotomic"):
            self.page.add(ft.Text("inserisci tipo"))
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
