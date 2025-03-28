import flet as ft
from controller import Controller
from view import View


def main(page: ft.Page):
    v = View(page)
    c = Controller(v)
    v.setController(c)
    v.caricaInterfaccia()


ft.app(target=main)
