import flet as ft

from model.model import Model
from UI.view import View
from UI.controller import Controller


def main(page: ft.Page):
    myModel= Model()
    myView= View(page)
    myController= Controller(myView,myModel)
    myView.set_controller(myController)
    myView.loadInterface()

    pass


ft.app(target=main)