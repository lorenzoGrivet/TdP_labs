# Add whatever it is needed to interface with the DB Table corso
import database.DB_connect
from database.DB_connect import get_connection

from model.corso import Corso
import mysql.connector


class CorsoDao:

    def getCorsiDAO(self):
        cnx = database.DB_connect.get_connection()

        cursor = cnx.cursor()
        query =""" SELECT *
                FROM corso"""
        cursor.execute(query)
        result = []

        for row in cursor:
            result.append(Corso(row[0],row[1],row[2],row[3]))

        cursor.close()

        return result

if __name__=="__main__":
    a= CorsoDao()
    lista=a.getCorsiDAO()
    for e in lista:
        print(e)
