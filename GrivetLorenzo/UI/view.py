import flet as ft

class View(ft.UserControl):

    def __init__(self,page=ft.Page):
        super().__init__()
        self.cont_cucine_R = None
        self.txtCitta_R = None
        self.lstLista = None
        self.btnSvuota = None
        self.btnRimuovi = None
        self.ddLista = None
        self.btnAggiungi = None
        self.lstRistorante = None
        self.ddRistorante = None
        self.lstResult = None
        self.btnTopDieci = None
        self.ddCucina = None
        self.maxRating = None
        self.minRating = None
        self.ddPrezzo = None
        self.ddCitta = None

        self.page=page
        self.controller=None
        self.tabs= None
        self.tab1=None
        self.tab2=None

    def loadInterface(self):
        self.page.theme_mode=ft.ThemeMode.LIGHT

        self.tabs=ft.Tabs()

        self.tab1=ft.Tab(text="Tab 1",content=self.createContent1())
        self.tab2=ft.Tab(text="Tab 2",content=self.createContent2())

        self.tabs.tabs.append(self.tab1)
        self.tabs.tabs.append(self.tab2)

        self.page.add(self.tabs)

        self.tab1.icon=ft.icons.FLATWARE
        self.tab2.icon =ft.icons.MAP

        self.controller.fillDDIniziali()
        self.page.update()
        pass

    def createContent1(self):
        content=None

        #titolo
        pad=ft.Container(height=4)
        rowTitolo = ft.Row(controls=[ft.Text("Ricerca Ristoranti", color="blue", size=24,weight="bold")])

        ###########PARTE 1

        self.ddCitta = ft.Dropdown(label="Scegli una città",width=220)
        self.ddPrezzo = ft.Dropdown(label="Scegli fascia di prezzo",width=220)
        self.minRating = ft.TextField(label="Minimo",on_change=self.controller.getSelectedMinRating,width=100)
        self.maxRating = ft.TextField(label="Massimo",on_change=self.controller.getSelectedMaxRating,width=100)
        self.ddCucina = ft.Dropdown(label="Scegli la tipologia di cucina",width=250)
        self.btnTopDieci = ft.ElevatedButton(text="Trova migliori",on_click=self.controller.handleTopDieci)

        row1_1 = ft.Row(controls=[ft.Container(self.ddCitta), ft.Container(self.ddPrezzo)],spacing=20)
        row2 = ft.Row(controls=[ft.Container(ft.Text("Rating da:")),ft.Container(self.minRating),ft.Container(ft.Text("a:")),ft.Container(self.maxRating)],spacing=20)
        row3 = ft.Row(controls=[ft.Container(ft.Text("Tipologia cucina:")),ft.Container(self.ddCucina),ft.Container(self.btnTopDieci)],spacing=20)

        col1=ft.Column(controls=[row1_1,pad,row2,pad,row3],alignment=ft.MainAxisAlignment.START,width=600,spacing=30)

        #listview risultato
        self.lstResult = ft.ListView(controls=[ft.Text("Migliori dieci ristoranti:",weight="bold",color="blue")],height=300,spacing=6,divider_thickness=1)
        col2=ft.Column(controls=[ft.Container(self.lstResult)],horizontal_alignment=ft.CrossAxisAlignment.END,width=700)

        colLinea=ft.Container(height=300,width=1,bgcolor=ft.colors.BLUE)

        rowParte1 = ft.Row(controls=[col1,col2],vertical_alignment=ft.CrossAxisAlignment.START)

        #linea per dividere le due sezioni
        rowLinea= ft.Row(controls=[ft.Container(expand=True, height=1,bgcolor=ft.colors.BLUE )])


        ###########PARTE 2

        #pima colonna
        self.ddRistorante = ft.Dropdown(label="Scegli un ristorante",width=300)
        self.btnAggiungi = ft.ElevatedButton(text="Aggiungi",on_click=self.controller.handleAggiungi)
        self.btnNaviga = ft.ElevatedButton(text="Pagina Web",on_click=self.controller.open_link)
        self.lstRistorante = ft.ListView(controls=[ft.Text("Dettagli:",weight="bold",color="blue")],width=500,expand=False,auto_scroll=True,spacing=6)

        row1 = ft.Row(controls=[ft.Container(self.ddRistorante),ft.Container(self.btnAggiungi),ft.Container(self.btnNaviga)])
        col1 = ft.Column(controls=[row1,ft.Container(self.lstRistorante,width=500)],width=700,spacing=30)

        #seconda colonna
        self.ddLista = ft.Dropdown(label="Seleziona dalla lista",on_change=self.controller.getSelectedDaLista)
        self.btnRimuovi = ft.ElevatedButton(text="Rimuovi",on_click=self.controller.handleRimuovi)
        self.btnSvuota = ft.ElevatedButton(text="Svuota",on_click=self.controller.handleSvuota)
        self.lstLista = ft.ListView(controls=[ft.Text("Lista:",color="blue",weight="bold")],spacing=6)

        row1_2 = ft.Row(controls=[ft.Container(self.ddLista),ft.Container(self.btnRimuovi),ft.Container(self.btnSvuota)])
        col2 = ft.Column(controls=[row1_2,self.lstLista],width=700,spacing=30)

        rowParte2 = ft.Row(controls=[col1,col2],vertical_alignment=ft.CrossAxisAlignment.START)

        #unisco tutto
        content=ft.Column(controls=[pad,rowTitolo,pad,rowParte1,rowLinea,pad,rowParte2])

        return content

    def createContent2(self):
        pad=ft.Container(height=4)
        titolo_R = ft.Text("Itinerario", color="blue",weight="bold", size=24)

        self.txtCitta_R = ft.TextField(read_only=True,label="Città")
        self.ddPrezzo_R = ft.Dropdown(label="Prezzo")
        row1_R = ft.Row(controls=[ft.Container(self.txtCitta_R),ft.Container(self.ddPrezzo_R)])

        self.nGiorni_R=ft.TextField()
        row2_R=ft.Row(controls=[ft.Container(ft.Text("Numero giorni:")),ft.Container(self.nGiorni_R)])

        self.vegetariano = ft.Switch(label="Vegetariano",on_change=self.controller.getVegetariano)
        self.celiaco= ft.Switch(label="Celiaco",on_change=self.controller.getCeliaco)
        self.halal = ft.Switch(label="Halal",on_change=self.controller.getHalal)
        self.scelteAlimentari = ft.Row(controls=[ft.Container(self.vegetariano),ft.Container(self.celiaco),ft.Container(self.halal)])

        self.cont_cucine_R = ft.ListView(controls=[ft.Text("Preferenze di cucina:",weight="bold",color="blue")],auto_scroll=False)
        row3_R=ft.Row(controls=[ft.Container(self.cont_cucine_R,height=300,width=700)])

        self.btnCalcola_R=ft.ElevatedButton(text="Calcola",on_click=self.controller.handleCalcola)
        row4_R = ft.Row(controls=[ft.Container(self.btnCalcola_R)])

        col1_R = ft.Column(controls=[row1_R,row2_R,self.scelteAlimentari,row3_R,row4_R], horizontal_alignment=ft.CrossAxisAlignment.START, width=700,spacing=30)

        self.lstRicorsione= ft.ListView(controls=[ft.Text("Itinerario:",weight="bold",color="blue")],spacing=6)
        col2_R=ft.Column(controls=[self.lstRicorsione],width=700,spacing=30)

        rowTot=ft.Row(controls=[col1_R,col2_R],vertical_alignment=ft.CrossAxisAlignment.START)

        content=ft.Column(controls=[pad,titolo_R,pad,rowTot])
        return content


    def set_controller(self, controller):
        self.controller = controller

    def update_page(self):
        self.page.update()
        pass

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()
