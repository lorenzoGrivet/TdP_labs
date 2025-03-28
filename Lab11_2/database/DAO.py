from database.DB_connect import DBConnect
from model.products import Product
from model.sales import Sale


class DAO():
    def __init__(self):
        pass

    def getAnni(self):
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor()
        query="""select distinct  year (gds.`Date` ) as year
                from go_sales.go_daily_sales gds 
                order by year asc """
        cursor.execute(query)
        risultato=[]
        for row in cursor:
            risultato.append(row[0])
        cursor.close()
        cnx.close()
        return risultato

    def getColori(self):
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor()
        query="""select distinct  gp.Product_color as color
                from go_sales.go_products gp 
                order by color ASC """
        cursor.execute(query)
        risultato=[]
        for row in cursor:
            risultato.append(row[0])
        cursor.close()
        cnx.close()
        return risultato

    def getAllProducts(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
         from go_sales.go_products"""
        cursor.execute(query)
        risultato = []
        for row in cursor:
            risultato.append(Product(**row))
        cursor.close()
        cnx.close()
        return risultato

    def getProdottiColore(self,colore):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *
                from go_sales.go_products gp 
                where gp.Product_color = %s """
        cursor.execute(query,(colore,))
        risultato = []
        for row in cursor:
            risultato.append(Product(**row))
        cursor.close()
        cnx.close()
        return risultato

    def getVendite(self,colore,anno):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select gds.Retailer_code ,gds.Product_number ,gds.Order_method_code ,gds.`Date` ,gds.Quantity ,gds.Unit_price ,gds.Unit_sale_price 
                from go_sales.go_products gp , go_sales.go_daily_sales gds 
                where gp.Product_number =gds.Product_number and gp.Product_color = %s and year (gds.`Date`)=%s"""
        cursor.execute(query, (colore,anno))
        risultato = []
        for row in cursor:
            risultato.append(Sale(**row))
        cursor.close()
        cnx.close()
        return risultato


