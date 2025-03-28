import database.DB_connect
import database.studente_DAO

class Iscrizioni_DAO:

    def getIscrizioniDAO(self):

        cnx = database.DB_connect.get_connection()
        cursor = cnx.cursor()
        query ="""SELECT *
                FROM iscrizione"""
        cursor.execute(query)
        result={}
        studente=None
        alunni=database.studente_DAO.StudenteDao().getStudentiDAO()

        for row in cursor:
            for alunno in alunni:
                if alunno.matricola==row[0]:
                    studente=alunno


            if result.__contains__(row[1]):
                lista=result[row[1]]
            else:
                lista=[]

            lista.append(studente)
            result[row[1]]=lista

        cursor.close()


        return result

    def iscrivi_Dao(self,studente,corso):
        cnx = database.DB_connect.get_connection()
        cursor = cnx.cursor()
        query="""INSERT INTO iscrizione
        (matricola,codins)
        VALUES (%s,%s)
        """
        cursor.execute(query,(studente,corso))

        cnx.commit()
        cursor.close()
        cnx.close()
