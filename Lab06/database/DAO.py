from database.DB_connect import DBConnect
from model import product,retailer,daily_sale


class DAO():
    def __init__(self):
        pass



    def getProductsDao(self):
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor()

        risultato={}
        query="""select * from go_sales.go_products"""

        cursor.execute(query)

        for i in cursor:
            p = product.Product(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])

            risultato[i[0]]=p

        cursor.close()
        cnx.close()

        return risultato

    def getRetailerDao(self):
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor()

        risultato={}
        query="""select * from go_sales.go_retailers"""

        cursor.execute(query)

        for i in cursor:
            r = retailer.Retailer(i[0],i[1],i[2],i[3])

            risultato[i[0]]=r

        cursor.close()
        cnx.close()
        return risultato


    def fillAnnoDao(self):
        cnx=DBConnect.get_connection()
        cursor = cnx.cursor()

        query="""select distinct year (`Date`) 
                from go_sales.go_daily_sales """

        cursor.execute(query)
        risultato=[]

        for i in cursor:
            risultato.append(i[0])

        cursor.close()
        cnx.close()
        return risultato

    def fillBrandDao(self):
        cnx=DBConnect.get_connection()
        cursor = cnx.cursor()

        query="""select distinct Product_brand
                from go_sales.go_products """

        cursor.execute(query)
        risultato=[]

        for i in cursor:
            risultato.append(i[0])

        cursor.close()
        cnx.close()
        return risultato

    def getTop5(self,anno,brand,retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        if anno=="Nessun filtro":
            anno=None
        if brand=="Nessun filtro":
            brand=None
        if retailer=="Nessun filtro":
            retailer=None

        query = """
        select *
from go_daily_sales gds 
inner join go_products gp on gds.Product_number = gp.Product_number 
where year (gds.`Date`) = coalesce (%s,year (gds.`Date`)) and gp.Product_brand = coalesce (%s,gp.Product_brand) and gds.Retailer_code =coalesce (%s,gds.Retailer_code)
order by (Quantity *Unit_sale_price ) desc 
limit 5
"""

        cursor.execute(query,(anno,brand,retailer,))
        risultato = []

        for i in cursor:
            risultato.append(daily_sale.DailySale(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

        cursor.close()
        cnx.close()
        return risultato

    def analizzaDao(self, anno, brand, retailer):

        cnx=DBConnect.get_connection()
        cursor=cnx.cursor()

        if anno=="Nessun filtro":
            anno=None
        if brand=="Nessun filtro":
            brand=None
        if retailer=="Nessun filtro":
            retailer=None

        lista=[]

        query="""select *
        from go_daily_sales gds 
        inner join go_products gp on gds.Product_number = gp.Product_number 
        where year (gds.`Date`)= coalesce(%s,year (gds.`Date`)) and gp.Product_brand = coalesce(%s, gp.Product_brand) and gds.Retailer_code = coalesce(%s,gds.Retailer_code) """

        cursor.execute(query,(anno,brand,retailer,))

        for i in cursor:
            lista.append(daily_sale.DailySale(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

        cursor.close()
        cnx.close()
        return lista


