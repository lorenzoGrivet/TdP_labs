from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllNazioni():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=False)

        query="""select distinct Country 
                from go_sales.go_retailers gr 
                """
        cursor.execute(query)

        risultato=[]
        for a in cursor:
            risultato.append(a[0])

        cursor.close()
        cnx.close()
        return risultato

    @staticmethod
    def getAllAnni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=False)

        query = """select distinct year( `Date` )
                    from go_sales.go_daily_sales gds 
                        """
        cursor.execute(query)

        risultato = []
        for a in cursor:
            risultato.append(a[0])

        cursor.close()
        cnx.close()
        return risultato

    @staticmethod
    def getRetailers(anno,nazione):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select *
                        from go_sales.go_retailers gr
                        where gr.Country =%s"""

        cursor.execute(query, (nazione,))

        risultato = []

        for a in cursor:
            risultato.append(Retailer(**a))

        cursor.close()
        cnx.close()
        return risultato

    @staticmethod
    def getArchi(anno,codice,nazione):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=False)

        query = """select gds.Retailer_code ,count(distinct(gds.Product_number)) as conteggio
                from go_sales.go_daily_sales gds , go_sales.go_daily_sales gds2, go_sales.go_retailers gr
                where year(gds2.`Date`) = %s
                    and year(gds.`Date`) = %s
                    and gds2.Retailer_code = %s
                    and gds.Retailer_code!= %s 
                    and gds2.Product_number = gds.Product_number 
                    and gr.Retailer_code  = gds.Retailer_code
                    and gr.Country = %s
                group by gds.Retailer_code"""

        cursor.execute(query, (anno,anno,codice,codice,nazione,))

        risultato = []

        for a in cursor:
            risultato.append(a)
            # print(a)



        cursor.close()
        cnx.close()
        return risultato
    
