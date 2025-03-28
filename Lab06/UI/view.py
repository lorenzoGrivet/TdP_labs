import flet as ft
from database.DAO import DAO
from model import model

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddAnno=None
        self.ddBrand=None
        self.ddRetailer=None
        self.btn_topVendite =None
        self.btn_analizzaVendite=None
        self.lv=None


    def load_interface(self):
        # title
        self._title = ft.Text("Analisi vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        self.ddAnno=ft.Dropdown(width=200,label="anno")
        self.ddBrand = ft.Dropdown(width=200,label="brand")
        self.ddRetailer = ft.Dropdown(width=500,label="retailer")

        self.fillDd("anno")
        self.fillDd("brand")
        self.fillDd("retailer")

        row1=ft.Row([self.ddAnno,self.ddBrand,self.ddRetailer],alignment=ft.MainAxisAlignment.CENTER)

        self.btn_topVendite=ft.ElevatedButton(text="Top vendite",width=200,on_click=self._controller.handleTop)
        self.btn_analizzaVendite = ft.ElevatedButton(text="Analizza vendite", width=200,on_click=self._controller.handleAnalizza)

        row2=ft.Row([self.btn_topVendite,self.btn_analizzaVendite],alignment=ft.MainAxisAlignment.CENTER)

        self.lv=ft.ListView(auto_scroll=True)

        self._page.add(row1,row2,self.lv)

        self.update_page()




    def fillDd(self,a):

        if a=="anno":
            self.ddAnno.options.append(ft.dropdown.Option("Nessun filtro"))
            for i in DAO().fillAnnoDao():
                self.ddAnno.options.append(ft.dropdown.Option(str(i)))

        if a=="brand":
            self.ddBrand.options.append(ft.dropdown.Option("Nessun filtro"))
            for i in DAO().fillBrandDao():
                self.ddBrand.options.append(ft.dropdown.Option(str(i)))

        if a=="retailer":
            self.ddRetailer.options.append(ft.dropdown.Option("Nessun filtro"))
            for i in self._controller._model.getRetailers().values():
                self.ddRetailer.options.append(ft.dropdown.Option(key=i.code,text=i.name))



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
