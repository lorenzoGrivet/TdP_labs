import mysql.connector
from database import DB_connect
from model.corso import Corso


class CorsoDao:

    @staticmethod
    def get_corsi_periodo(pd):
        cnx=DB_connect.DBConnect().get_connection()
        result=[]

        if cnx is None:
            print("errore connessione")
            return
        else:
            cursor=cnx.cursor()
            query = """SELECT * 
                    FROM iscritticorsi.corso c  
                    WHERE c.pd = %s"""

            cursor.execute(query,(pd,))

            for row in cursor:
                #result.append(Corso(row["codins"],row["crediti"],row["nome"],row["pd"]))
                result.append(Corso(row[0], row[1], row[2], row[3]))

            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def get_studenti_periodo(pd):
        cnx=DB_connect.DBConnect().get_connection()
        result=[]

        if cnx is None:
            print("errore connessione")
            return
        else:
            cursor=cnx.cursor()
            query = """select matricola
from iscritticorsi.iscrizione i, iscritticorsi.corso c 
where i.codins  = c.codins and c.pd =%s"""

            cursor.execute(query,(pd,))

            for row in cursor:
                result.append(row)

            cursor.close()
            cnx.close()
            return result


    def get_all_corsi(self):
        cnx = DB_connect.DBConnect().get_connection()
        result = []

        if cnx is None:
            print("errore connessione")
            return
        else:
            cursor = cnx.cursor()
            query = """SELECT * 
                       FROM iscritticorsi.corso c"""

            cursor.execute(query)