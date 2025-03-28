#from database.corso_DAO import CorsoDao
#from database.iscrizioni_DAO import Iscrizioni_DAO
#from database.studente_DAO import StudenteDao


import database.studente_DAO
import database.iscrizioni_DAO
import database.corso_DAO
from UI import view
import flet as ft


class Model:
    def __init__(self):
        self.corsi = database.corso_DAO.CorsoDao().getCorsiDAO()
        self.studenti = database.studente_DAO.StudenteDao().getStudentiDAO()
        self.iscrizioni=database.iscrizioni_DAO.Iscrizioni_DAO().getIscrizioniDAO()
        self.view=view
        pass


    def aggiungiStudente(self,studente, corso):
        matricola=studente.matricola
        codice=corso.codins

        database.iscrizioni_DAO.Iscrizioni_DAO().iscrivi_Dao(matricola,codice)




    def getStudenti(self):
        return self.studenti


    def getCorsi(self):
        return self.corsi


    def getIscrizioni(self):
        return self.iscrizioni