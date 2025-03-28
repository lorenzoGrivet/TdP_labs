from database.DB_connect import DBConnect
from model.airport import Airport
from model.connessioni import Connessione


class DAO():

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * from airports a order by a.AIRPORT asc"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(Nmin):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select tmp.ID, tmp.IATA_CODE, count(*) as N
                        from (
                        SELECT a.ID , a.IATA_CODE , f.AIRLINE_ID, count(*) as n
                        FROM airports a , flights f 
                        WHERE a.ID = f.ORIGIN_AIRPORT_ID or a.ID = f.DESTINATION_AIRPORT_ID 
                        group by a.ID , a.IATA_CODE , f.AIRLINE_ID
                        ) as tmp
                        group by tmp.ID, tmp.IATA_CODE
                        having N >= %s"""

        cursor.execute(query, (Nmin,))

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdgesV1(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, count(*)
                    from flights f
                    group by f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID
                    order by f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID"""

        cursor.execute(query)

        for row in cursor:
            result.append(Connessione(idMap[row["ORIGIN_AIRPORT_ID"]], idMap[row["DESTINATION_AIRPORT_ID"]], row["count(*)"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdgesV2(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, count(*)
                       from flights f
                       group by f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID
                       order by f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID"""

        cursor.execute(query)

        for row in cursor:
            result.append(
                Connessione(idMap[row["ORIGIN_AIRPORT_ID"]], idMap[row["DESTINATION_AIRPORT_ID"]], row["count(*)"]))

        cursor.close()
        conn.close()
        return result