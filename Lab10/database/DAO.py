from database.DB_connect import DBConnect
from model.confine import Confine
from model.state import Stato


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getStati():

        cnx= DBConnect.get_connection()

        cursor= cnx.cursor(dictionary=True)
        risultato=[]

        query="""select * from country c"""

        cursor.execute(query, ())

        for row in cursor:
            risultato.append(Stato(**row))

        cursor.close()
        cnx.close()
        return risultato


    def getNodi(self,anno):

        cnx = DBConnect.get_connection()

        cursor = cnx.cursor(dictionary=False)
        risultato = []

        query = """select distinct state1no 
                    from contiguity c 
                    where `year` <%s"""

        cursor.execute(query, (anno,))

        for row in cursor:
            risultato.append(row[0])

        cursor.close()
        cnx.close()
        return risultato

    def getConfiniAnno(self,anno):

        cnx = DBConnect.get_connection()

        cursor = cnx.cursor()
        risultato = []

        query = """select * 
                    from contiguity c 
                    where c.`year` <= %s
                    and c.conttype=1
                    """

        cursor.execute(query,(anno,))

        for row in cursor:
            risultato.append(Confine(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

        cursor.close()
        cnx.close()
        return risultato