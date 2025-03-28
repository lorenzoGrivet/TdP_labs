from database.DB_connect import DBConnect
from model.nerc import Nerc
from model.powerOutages import Event


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllNerc():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
        from nerc
        """

        cursor.execute(query)

        for row in cursor:
            result.append(Nerc(row["id"], row["value"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEvents(nerc):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                from poweroutages.poweroutages p 
                where p.nerc_id =%s
                order by p.date_event_began ASC
                """

        cursor.execute(query, (nerc,))

        for row in cursor:
            result.append(
                Event(row["id"], row["event_type_id"],
                      row["tag_id"], row["area_id"],
                      row["nerc_id"], row["responsible_id"],
                      row["customers_affected"], row["date_event_began"],
                      row["date_event_finished"], row["demand_loss"]))

        cursor.close()
        conn.close()
        return result