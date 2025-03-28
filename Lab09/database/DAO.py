from database.DB_connect import DBConnect
from model.airport import Airport
from model.flight import Flight


class DAO():
    def __init__(self):
        pass

    def getAllFlight(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()

        query= "select id,origin_airport_id, destination_airport_id,distance from flights f"

        cursor.execute(query)

        result=[]
        for a in cursor:
            result.append(Flight(a[0],a[1],a[2],a[3]))
        cursor.close()
        cnx.close()

        return result

    def getAllAirport(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()

        query = "select id,airport from airports a"

        cursor.execute(query)

        result = []
        for a in cursor:
            result.append(Airport(a[0], a[1]))
        cursor.close()
        cnx.close()

        return result
