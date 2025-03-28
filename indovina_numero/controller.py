from view import View
from model import Model
import flet as ft


class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()


    def handleNuova(self,e):
        self._view.txtMrim.value= self.getMmax()
        self._view.btnProva.disabled=False
        self._view.txtTentativo.disabled=False
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(ft.Text("Indovina il numero",size=18))

        self._model.inizializza()
        self._view.update()

        pass

    def handleProva(self,e):
        tentativo = self._view.txtTentativo.value

        try:
            intTentativo=int(tentativo)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("devi mettere intero", size=18,color="red"))
            self._view.update()
            return

        mRim, result=self._model.indovina(intTentativo)

        self._view.txtMrim.value=mRim

        if mRim==0:
            self._view.btnProva.disabled=True
            self._view.txtTentativo.disabled=True

            self._view._lvOut.controls.append(ft.Text("Hai perso", size=18, color="red"))
            self._view._lvOut.controls.append(ft.Text(f"il segreto era: {self._model.segreto}", size=18, color="red"))
            self._view.txtTentativo.value=""
            self._view.update()
        else:
            if result==0:
                self._view._lvOut.controls.append(ft.Text("Hai vinto", size=18, color="green"))
                self._view._lvOut.controls.append(ft.Text(f"il segreto era: {self._model.segreto}", size=18))
                self._view.btnProva.disabled=True
                self._view.txtTentativo.value=""
                self._view.update()
                return
            elif result==-1:
                self._view._lvOut.controls.append(ft.Text(f"il segreto è più piccolo", size=18))
                self._view.txtTentativo.value=""
                self._view.update()
            elif result==1:
                self._view._lvOut.controls.append(ft.Text(f"il segreto è più grande", size=18))
                self._view.txtTentativo.value=""
                self._view.update()
        pass

    def getNmax(self):
        return self._model.NMax
    def getMmax(self):
        return self._model.Mmax
    def getMrim(self):
        return self._model.Mrim