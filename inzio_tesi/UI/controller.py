import copy
import webbrowser

import flet as ft
class Controller:
    def __init__(self, view, model):
        self.halal = None
        self.vegetariano = None
        self.celiaco = None
        self.view=view
        self.model=model

        #scelteselezionate
        self.selectedCitta=None
        self.selectedPrezzo=None
        self.selectedCucina=None
        self.selectedRistorante=None
        self.selectedDaLista=None
        self.minRating=None
        self.maxRating=None
        self.minOk=False
        self.maxOk=False
        self.link=None

    def fillDDIniziali(self):
        citta = self.model.getAllCitta()
        cittaDD = list(map(lambda x: ft.dropdown.Option(key=x,data=x,on_click=self.getSelectedCitta),citta))
        self.view.ddCitta.options=cittaDD

        prezzi = self.model.getAllPrezzi()
        prezzi.append("Qualsiasi")
        prezziDD = list(map(lambda x: ft.dropdown.Option(key=x,data=x,on_click=self.getSelectedPrezzo),prezzi))
        self.view.ddPrezzo.options=prezziDD
        self.view.ddPrezzo_R.options=prezziDD #anche il dd della seconda tab
        self.view.update_page()
        pass

    def fillRating(self,citta,prezzo):
        valori =self.model.getMinMaxRating(citta,prezzo)
        self.view.minRating.value=valori[0][0]
        self.view.maxRating.value=valori[0][1]
        self.minRating=valori[0][0]
        self.maxRating=valori[0][1]
        self.minOk=True
        self.maxOk=True
        self.view.update_page()
        self.fillDDCucine(self.minRating,self.maxRating)
        pass

    def fillDDCucine(self,min,max):
        self.view.ddCucina.options.clear()
        #gestire int e str
        try:
            intMin=float(min)
            intMax=float(max)
        except ValueError:
            self.view.create_alert("Inserire valori numerici come rating")
            return

        self.minOk=True
        self.maxOk=True

        cucine=self.model.getCucine(self.selectedCitta,self.selectedPrezzo,intMin,intMax)
        cucine.sort()
        cucine.insert(0,"Qualsiasi")

        cucineDD=list(map(lambda x: ft.dropdown.Option(key=x,data=x,on_click=self.getSelectedCucina),cucine))
        self.view.ddCucina.options=cucineDD

        self.view.update_page()

        #checkbox tab 2
        col=[]
        for a in cucine:
            if a!="Qualsiasi":
                col.append(ft.Checkbox(label=a,data=False,on_change=self.handlecheckCucina))
        col.insert(0,ft.Text("Preferenze di cucina:\n",weight="bold",color="blue"))
        self.view.cont_cucine_R.controls=col
        self.view.update_page()
        pass


    def fillDDLista(self,risto,bool):
        if bool:
            #aggiungo
            self.view.ddLista.options.append(ft.dropdown.Option(key=risto,data=risto,on_click=self.getSelectedDaLista))
        if not bool:
            #rimuovo
            for a in self.view.ddLista.options:
                if a.key.Name == risto.Name:
                    self.view.ddLista.options.remove(a)

            pass

        #aggiorno gia la pagina dopo

    def handleTopDieci(self,e):
        self.view.lstResult.controls.clear()
        self.view.lstRistorante.controls.clear()
        self.view.lstRistorante.controls.append(ft.Text("Dettagli:",weight="bold",color="blue"))
        self.view.ddRistorante.options.clear()
        self.view.lstResult.controls.append(ft.Text("Migliori dieci ristoranti:",weight="bold",color="blue"))

        if self.selectedCitta is None:
            self.view.create_alert("Scegli la città")
            return

        if self.minOk==True and self.maxOk==True and self.minRating>self.maxRating:
            self.view.create_alert("Hai inserito un rating minimo maggiore del massimo")
            return

        if self.minOk==False and self.view.minRating.value!="" and not (type(self.view.minRating.value).__name__=="int" or type(self.view.minRating.value).__name__=="float"):
            self.view.create_alert("Valore minimo rating non numerico")
            return
        if self.minOk==True and (self.view.minRating.value!="") and self.minRating<0:
            self.view.create_alert("Valore minimo rating deve essere positivo")
            return
        if self.minOk==False and (self.view.minRating.value==""):
            self.view.minRating.value=1
            self.minRating=1
        if self.minOk==True and self.minRating>5:
            self.view.create_alert("Il valore minimo del rating deve essere minore di 5")
            return

        if self.maxOk==False and self.view.maxRating.value!="" and not (type(self.view.maxRating.value).__name__=="int" or type(self.view.maxRating.value).__name__=="float"):
            self.view.create_alert("Valore massimo rating non numerico")
            return
        if self.maxOk==True and (self.view.minRating.value!="") and self.maxRating<0:
            self.view.create_alert("Valore massimo rating deve essere positivo")
            return
        if self.maxOk==False and (self.view.maxRating.value==""):
            self.view.maxRating.value=5
            self.maxRating=5
        if self.maxOk==True and self.maxRating>5:
            self.view.create_alert("Il valore massimo del rating deve essere minore di 5")
            return

        if not self.model.esisteRistorante(self.selectedCitta,self.selectedPrezzo,self.minRating,self.maxRating):
            self.view.create_alert("Non esistono ristoranti per il range che hai scelto")
            return

        if self.selectedPrezzo is None:
            self.selectedPrezzo = "Qualsiasi"
            self.view.ddPrezzo.value = "Qualsiasi"

        if self.selectedCucina is None:
            self.view.ddCucina.value="Qualsiasi"
            self.selectedCucina="Qualsiasi"
        self.view.update_page()

        #se arrivo qua vuol dire che va tutto bene
        print("min:",self.minRating)
        print("max:",self.maxRating)
        print("Prezzo:",self.selectedPrezzo)

        res=self.model.getTopDieci(self.selectedCitta,self.selectedPrezzo,self.minRating,self.maxRating,self.selectedCucina)

        i=0
        for a in res:
            i+=1
            row=ft.Row(controls=[ft.Text(f"{i}. ",weight="bold"),ft.Text(a)])
            self.view.lstResult.controls.append(row)
            self.view.ddRistorante.options.append(ft.dropdown.Option(key=a,data=a,on_click=self.getSelectedRistorante))
        self.view.update_page()
        pass



    def handleAggiungi(self,e):
        self.view.lstLista.controls.clear()
        self.view.lstLista.controls.append(ft.Text("Lista:", weight="bold", color="blue"))
        lista,b=self.model.aggiungiRistorante(self.selectedRistorante)

        if lista==False and b=="piena":
            self.view.create_alert("La lista è già piena")
            return
        if lista==False and b=="doppia":
            self.view.create_alert("Hai già inserito questo ristorante")
            return
        if lista==False and b=="null":
            self.view.create_alert("Non hai selezionato alcun ristorante")
            return

        #ok
        self.fillDDLista(self.selectedRistorante,True)

        for r in lista:
            self.view.lstLista.controls.append(ft.Text(f"- {r}"))
        self.view.update_page()

        pass

    def handleRimuovi(self,e):

        if self.selectedDaLista is None:
            self.view.create_alert("Non hai selezionato alcun ristorante")
            return

        lista,b=self.model.rimuoviRistorante(self.selectedDaLista)

        if lista==False and b==False:
            self.view.create_alert("Il ristorante non è in lista")
            return

        if lista==False and b==True:
            self.view.create_alert("La lista è vuota")
            return

        self.view.lstLista.controls.clear()
        self.view.lstLista.controls.append(ft.Text("Lista:", weight="bold", color="blue"))

        #ok
        self.fillDDLista(self.selectedDaLista,False)

        for r in lista:
            self.view.lstLista.controls.append(ft.Text(f"- {r}"))
        self.view.update_page()

        pass

    def handleSvuota(self,e):
        self.model.svuotaLista()

        self.view.lstLista.controls.clear()
        self.view.lstLista.controls.append(ft.Text("Lista:", weight="bold", color="blue"))

        self.view.ddLista.options.clear()
        self.view.update_page()
        pass



    def handleCalcola(self,e):

        self.view.lstRicorsione.clean()
        self.view.update_page()
        try:
            intGiorni= int(self.view.nGiorni_R.value)
        except ValueError:
            self.view.create_alert("Il numero dei giorni deve essere un numero intero")
            return

        if self.view.ddPrezzo_R.value=="" or self.view.ddPrezzo_R.value is None:
            if self.selectedPrezzo is None:
                self.selectedPrezzo="Qualsiasi"

            self.view.ddPrezzo_R.value=self.selectedPrezzo

        self.view.update_page()



        bool,res= self.model.calcola(self.selectedCitta,self.selectedPrezzo,intGiorni,self.vegetariano,self.celiaco,self.halal)

        if not bool and res ==0:
            self.view.create_alert("I ristoranti in lista sono più dei giorni")
            return
        elif not bool and res==-1:
            self.view.create_alert("Seleziona almeno una preferenza di cucina")
            return
        elif not bool and res==1:
            self.view.create_alert("Hai aggiunto troppe prefererenze di cucina")
            return
        elif not bool and res==2:
            self.view.create_alert("Hai aggiunto troppe preferenze di cucina")
            return
        else:
            self.view.lstRicorsione.clean()
            self.view.lstRicorsione.controls.append(ft.Text("Itinerario:",weight="bold",color="blue"))

            stampa=self.stampa(res)
            for a in stampa:
                self.view.lstRicorsione.controls.append(a)

            if len(res)<intGiorni:
                self.view.lstRicorsione.controls.append(ft.Row(height=6))
                self.view.lstRicorsione.controls.append(ft.Text("Non sono stati trovati abbastanza ristoranti con i vincoli inseriti, prova ad aggiungere delle preferenze"))
                self.model.aumentareCucine=True
                pass
            else:
                self.model.aumentareCucine=False

        self.view.update_page()
        pass




#selezione delle scelte
    def getSelectedCitta(self,e):
        print("entrato")
        if e.control.data is None:
            pass
        else:
            self.selectedCitta=e.control.data
            self.handleSvuota(1) #se cambio citta allora svuoto la lista
            self.view.ddRistorante.options.clear()
            self.view.lstRistorante.controls=[ft.Text("Dettagli:",weight="bold",color="blue")]
            self.view.lstResult.controls=[ft.Text("Migliori dieci ristoranti:",weight="bold",color="blue")]
            self.view.lstRicorsione.controls=[ft.Text("Itinerario:",weight="bold",color="blue")]

            self.view.txtCitta_R.value=self.selectedCitta

            self.view.update_page()

            if self.selectedPrezzo is not None:
                self.fillRating(self.selectedCitta, self.selectedPrezzo)
            else:
                self.fillRating(self.selectedCitta,"Qualsiasi")
        pass



    def getSelectedPrezzo(self,e):
        print("entrato")

        if e.control.data is None:
            pass
        else:
            self.selectedPrezzo=e.control.data

            self.view.ddPrezzo_R.value=self.selectedPrezzo

            if self.selectedCitta is not None:
                self.fillRating(self.selectedCitta, self.selectedPrezzo)
        pass



    def getSelectedCucina(self,e):
        if e.control.data is None:
            pass
        else:
            self.selectedCucina=e.control.data
        pass



#rating riempono il ddCucina
    def getSelectedMinRating(self,e):
        print("fatto")
        if e.data is None:
            pass
        else:
            self.minRating=e.data

            try:
                intMin=float(self.minRating)
                self.minOk=True
                self.minRating = intMin

                if self.maxOk:
                    self.fillDDCucine(self.minRating,self.maxRating)

            except:
                self.minOk=False
                self.view.ddCucina.options.clear()
                self.view.update_page()
                print("pulito")
                return
        pass


    def getSelectedMaxRating(self,e):
        print("fatto")
        if e.data is None:
            pass
        else:
            self.maxRating=e.data

            try:
                intMax=float(self.maxRating)
                self.maxOk=True
                self.maxRating = intMax

                if self.minOk:
                    self.fillDDCucine(self.minRating,self.maxRating)

            except:
                self.maxOk=False
                self.view.ddCucina.options.clear()
                self.view.update_page()
                print("pulito")
                return
        pass


    def getSelectedRistorante(self,e):
        if e.control.data is None:
            pass
        else:
            self.selectedRistorante=e.control.data
            self.view.lstRistorante.clean()
            self.view.lstRistorante.controls.append(ft.Text("Dettagli:", weight="bold", color="blue"))


            self.view.lstRistorante.controls.append(ft.Row(controls=[ft.Text(f"Nome",weight="bold"),ft.Text(self.selectedRistorante.Name,width=500)],vertical_alignment=ft.CrossAxisAlignment.START))
            self.view.lstRistorante.controls.append(ft.Row(controls=[ft.Text(f"Tipologie di cucina:",weight="bold"),ft.Text(self.selectedRistorante.Cuisine_Style.removeprefix("[").removesuffix("]").replace("'", ""),width=500)],vertical_alignment=ft.CrossAxisAlignment.START))
            self.view.lstRistorante.controls.append(ft.Row(controls=[ft.Text(f"Rating:",weight="bold"),ft.Text(self.selectedRistorante.Rating,width=500)],vertical_alignment=ft.CrossAxisAlignment.START))
            self.view.lstRistorante.controls.append(ft.Row(controls=[ft.Text(f"Range di prezzo:",weight="bold"),ft.Text(self.selectedRistorante.Price_Range,width=500)],vertical_alignment=ft.CrossAxisAlignment.START))


            if self.selectedRistorante.Number_of_Reviews==None or self.selectedRistorante.Number_of_Reviews=="":
                n=0
            else:
                n=self.selectedRistorante.Number_of_Reviews

            self.view.lstRistorante.controls.append(ft.Row(controls=[ft.Text(f"Numero di recensioni:",weight="bold"),ft.Text(int(n),width=500)],vertical_alignment=ft.CrossAxisAlignment.START))

            # self.view.lstRistorante.controls.append(ft.Row(controls=[ft.Text(f"Link:",weight="bold"),ft.Text(f"www.tripadvisor.com{self.selectedRistorante.URL_TA}",width=500)],vertical_alignment=ft.CrossAxisAlignment.START))
            self.link="https://www.tripadvisor.com"+self.selectedRistorante.URL_TA

            self.view.update_page()
        pass



    def getSelectedDaLista(self,e):
        if e.control.data is None:
            pass
        else:
            self.selectedDaLista=e.control.data


    def open_link(self,e):
        if self.link is None:
            pass
        else:
            webbrowser.open(self.link)
        pass


    def handlecheckCucina(self,e):
        a,b=self.model.checkCucina(e.control.label,e.control.value)
        print(a,b)
        pass
    
    
    def getVegetariano(self,e):
        if e.control.value is None:
            pass
        else:
            self.vegetariano= e.control.value
        pass
    
    def getCeliaco(self,e):
        if e.control.value is None:
            pass
        else:
            self.celiaco = e.control.value
        pass

    def getHalal(self,e):
        if e.control.value is None:
            pass
        else:
            self.halal = e.control.value
        pass


    def stampa(self,l):
        i=0
        a=[]
        for r in l:
            i+=1
            exp= ft.ExpansionTile(title=ft.Row(controls=[ft.Text(f"{i}. ",weight="bold"),ft.Text(r)]),
                                  controls_padding=ft.Padding(0,2,0,2),
                                  text_color=ft.colors.BLUE,
                                  on_change=self.espansione)

            exp.controls.append(ft.Row(controls=[
                    ft.Text(f"Tipologie di cucina:",weight="bold"),
                    ft.Text(r.Cuisine_Style.removeprefix("[").removesuffix("]").replace("'", ""))
                ]
            ))
            exp.controls.append(ft.Row(controls=[ft.Text(f"Rating: ",weight="bold"),ft.Text(r.Rating)]))
            a.append(exp)
        return a

    def espansione(self,e): #non funziona

        for a in self.view.lstRicorsione.controls:
            if a != e.control:
                a.expand=False
                a.update()
            else:
                a.expand=True
                a.update()
        self.view.update_page()
        pass