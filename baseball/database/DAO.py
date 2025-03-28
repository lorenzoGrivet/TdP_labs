from database.DB_connect import DBConnect
from model.team import Team


class DAO():
    def __init__(self):

        pass

    @staticmethod
    def getAllYears():

        cnx= DBConnect.get_connection()

        cursor= cnx.cursor(dictionary=True)
        risultato=[]

        query="""select distinct (t.`year`)
                from lahmansbaseballdb.teams t 
                where `year` >= 1980
                order by `year` desc """

        cursor.execute(query, ())

        for row in cursor:
            risultato.append(row["year"])

        cursor.close()
        cnx.close()
        return risultato


    @staticmethod
    def getTeamsOfYear(anno):
        cnx = DBConnect.get_connection()

        cursor = cnx.cursor(dictionary=True)
        risultato = []

        query = """select *
            from lahmansbaseballdb.teams t 
            where `year` =%s"""

        cursor.execute(query, (anno,))

        for row in cursor:
            risultato.append(Team(**row))

        cursor.close()
        cnx.close()
        return risultato

    def getSalaryOfTeams(self,year,idMap):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select t.ID as ID, sum( s.salary ) as totSalary
        from lahmansbaseballdb.salaries s , lahmansbaseballdb.teams t , lahmansbaseballdb.appearances a 
        where s.`year` = t.`year` and t.`year` = a.`year` and a.`year` = %s and t.ID = a.teamID and s.playerID = a.playerID 
        group by t.teamCode"""
        cursor.execute(query,(year,))

        risultato = {}
        for a in cursor:
            # risultato.append( (idMap[a["ID"]], a["totSalary"]) )
            risultato[idMap[a["ID"]]]= a["totSalary"]


        cursor.close()
        cnx.close()
        return risultato
