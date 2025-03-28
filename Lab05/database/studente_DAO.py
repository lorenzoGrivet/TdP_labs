# Add whatever it is needed to interface with the DB Table studente


import database.DB_connect
from database.DB_connect import get_connection
from model.studente import Studente
import mysql.connector


class StudenteDao:

    def getStudentiDAO(self):
        cnx = database.DB_connect.get_connection()

        cursor = cnx.cursor()
        query =""" SELECT *
                FROM studente"""
        cursor.execute(query)
        result = []

        for row in cursor:
            result.append(Studente(row[0],row[1],row[2],row[3]))

        cursor.close()

        return result

if __name__=="__main__":
    a= StudenteDao()
    lista=a.getStudentiDAO()
    for e in lista:
        print(e)
