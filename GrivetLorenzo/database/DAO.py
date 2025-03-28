from database import DB_connect
from model.ristorante import Ristorante


class DAO:

    def __init__(self):
        pass

    @staticmethod
    def getAllRistorantiDAOTest(prezzo, citta):
        #non prende cucine particolari

        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        res = []

        if prezzo == "Qualsiasi":
            query = """select t1.*
                        from (
                        select *
                        from ristoranti.ta_restaurants_curated trc
                        where (Price_Range = '$' or Price_Range = '$$ - $$$' or Price_Range='$$$$')
                        and City = %s
                        and not isnull(trc.Number_of_Reviews)
                        and not (Cuisine_Style like "%Vegan Options%" or Cuisine_Style like "%Vegetarian Friendly%" or Cuisine_Style like "%Gluten Free Options%")
                        ) t1"""
            cursor.execute(query, (citta,))
        else:
            query = """select t1.*
                        from (
                        select *
                        from ristoranti.ta_restaurants_curated trc
                        where Price_Range = %s
                        and City = %s
                        and not isnull(trc.Number_of_Reviews)
                        and not (Cuisine_Style like "%Vegan Options%" or Cuisine_Style like "%Vegetarian Friendly%" or Cuisine_Style like "%Gluten Free Options%")
                        ) t1,
                        (
                        select tr.City, avg(tr.Rating*tr.Number_of_Reviews) as media
                        from ta_restaurants_curated tr
                        where not isnull(tr.Number_of_Reviews)
                        group by tr.City 
                        ) t2
                        where t1.City = t2.City
                        and t1.Rating*t1.Number_of_Reviews > t2.media"""

            cursor.execute(query, (prezzo, citta,))

        for a in cursor:
            res.append(Ristorante(**a))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllRistorantiDAORestrizioni(prezzo, citta, veg, cel, hal):
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        res = []

        query_base = """select t1.*
                        from (
                        select *
                        from ristoranti.ta_restaurants_curated trc
                        where City = %s
                        and not isnull(trc.Number_of_Reviews)"""

        if prezzo != "Qualsiasi":
            query_base+= " and Price_Range = %s"
        else:
            query_base +=" and Price_Range != %s"

        if veg:
            query_base+='\nand (Cuisine_Style like "%Vegan Options%" or Cuisine_Style like "%Vegetarian Friendly%")'
        if cel:
            query_base+='\nand Cuisine_Style like "%Gluten Free Options%"'
        if hal:
            query_base+='\nand Cuisine_Style like "%Halal%"'

        query_base +=""") t1,
                        (
                        select tr.City, avg(tr.Rating*tr.Number_of_Reviews) as media
                        from ta_restaurants_curated tr
                        where not isnull(tr.Number_of_Reviews)
                        group by tr.City 
                        ) t2
                        where t1.City = t2.City
                        and t1.Rating*t1.Number_of_Reviews > t2.media"""

        cursor.execute(query_base, (citta, prezzo))

        for a in cursor:
            res.append(Ristorante(**a))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllRistorantiDAO(prezzo,citta):
        cnx=DB_connect.DBConnect.get_connection()
        cursor= cnx.cursor(dictionary=True)

        res=[]

        if prezzo == "Qualsiasi":
            query = """select t1.*
                        from (
                        select *
                        from ristoranti.ta_restaurants_curated trc
                        where (Price_Range = '$' or Price_Range = '$$ - $$$' or Price_Range='$$$$')
                        and City = %s
                        and not isnull(trc.Number_of_Reviews)
                        ) t1,
                        (
                        select tr.City, avg(tr.Rating*tr.Number_of_Reviews) as media
                        from ta_restaurants_curated tr
                        where not isnull(tr.Number_of_Reviews)
                        group by tr.City 
                        ) t2
                        where t1.City = t2.City
                        and t1.Rating*t1.Number_of_Reviews > t2.media"""
            cursor.execute(query,(citta,))

        else:
            query = """select t1.*
                        from (
                        select *
                        from ristoranti.ta_restaurants_curated trc
                        where Price_Range = %s
                        and City = %s
                        and not isnull(trc.Number_of_Reviews)
                        ) t1,
                        (
                        select tr.City, avg(tr.Rating*tr.Number_of_Reviews) as media
                        from ta_restaurants_curated tr
                        where not isnull(tr.Number_of_Reviews)
                        group by tr.City 
                        ) t2
                        where t1.City = t2.City
                        and t1.Rating*t1.Number_of_Reviews > t2.media"""

            cursor.execute(query,(prezzo,citta,))

        for a in cursor:
            res.append(Ristorante(**a))

        cursor.close()
        cnx.close()
        return res


    @staticmethod
    def getAllCittaDAO():
        cnx=DB_connect.DBConnect.get_connection()
        cursor= cnx.cursor(dictionary=False)

        res=[]
        query="""select distinct t.City
                from ristoranti.ta_restaurants_curated t
                order by t.City"""

        cursor.execute(query)

        for a in cursor:
            res.append(a[0])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllPrezziDAO():
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=False)

        res = []
        query = """select distinct t.Price_Range
                    from ristoranti.ta_restaurants_curated t
                    where t.Price_Range <> ""
                    order by t.Price_Range"""

        cursor.execute(query)

        for a in cursor:
            res.append(a[0])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getMinMaxRatingDAO(citta,prezzo):
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=False)

        res = []
        if (prezzo is not None) and prezzo!="Qualsiasi":
            query = """select min(t.Rating),max(t.Rating)
                        from ta_restaurants_curated t
                        where t.City =%s
                        and t.Price_Range = %s
                        and t.Rating >0
                        and not isnull(t.Number_of_Reviews)"""
            cursor.execute(query, (citta,prezzo))

        else:
            query="""select min(t.Rating),max(t.Rating)
                        from ta_restaurants_curated t
                        where t.City =%s
                        and (Price_Range = '$' or Price_Range = '$$ - $$$' or Price_Range='$$$$')
                        and t.Rating >0
                        and not isnull(t.Number_of_Reviews)"""

            cursor.execute(query, (citta,))

        for a in cursor:
            res.append(a)
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCucineDAO(citta,prezzo,min,max):
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=False)

        res = []

        if prezzo is None or prezzo=="Qualsiasi":
            query= """select Cuisine_Style 
                    from ta_restaurants_curated t
                    where City =%s
                    and (Price_Range = '$' or Price_Range = '$$ - $$$' or Price_Range='$$$$')
                    and Rating >=%s
                    and Rating <=%s
                    and not isnull(t.Number_of_Reviews)
                    and not (Cuisine_Style like "%Vegan Options%" or Cuisine_Style like "%Vegetarian Friendly%" or Cuisine_Style like "%Gluten Free Options%" or Cuisine_Style like "%Halal%")
                    """
            cursor.execute(query, (citta, min, max))

        else:
            query = """select Cuisine_Style 
                    from ta_restaurants_curated t
                    where City =%s
                    and Price_Range = %s
                    and Rating >=%s
                    and Rating <=%s
                    and not isnull(t.Number_of_Reviews)
                    and not (Cuisine_Style like "%Vegan Options%" or Cuisine_Style like "%Vegetarian Friendly%" or Cuisine_Style like "%Gluten Free Options%" or Cuisine_Style like "%Halal%")
                    """

            cursor.execute(query, (citta,prezzo,min,max))

        for a in cursor:
            res.append(a[0])
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def esisteRistoranteDAO(citta, prezzo, min, max):
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=False)

        res = []

        if prezzo is None or prezzo=="Qualsiasi":
            prezzo = "no"
            query = """select * 
                        from ta_restaurants_curated t
                        where City =%s
                        and (Price_Range = '$' or Price_Range = '$$ - $$$' or Price_Range='$$$$')
                        and Rating >=%s
                        and Rating <=%s
                        and not isnull(t.Number_of_Reviews)
                        """
            cursor.execute(query, (citta, min, max))
        else:
            query = """select * 
                        from ta_restaurants_curated t
                        where City =%s
                        and Price_Range = %s
                        and Rating >=%s
                        and Rating <=%s
                        and not isnull(t.Number_of_Reviews)
                        """

            cursor.execute(query, (citta, prezzo, min, max))

        for a in cursor:
            res.append(a[0])
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getTopDieciDAO(citta, prezzo,min,max,cucina):
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        res = []
        if (cucina is None or cucina=="Qualsiasi") and (prezzo is None or prezzo=="Qualsiasi"):
            #cucina non scelta prezzo non scelto
            query="""select *
                    from ta_restaurants_curated t
                    where t.City =%s
                    and (Price_Range = '$' or Price_Range = '$$ - $$$' or Price_Range='$$$$')
                    and t.Rating >=%s
                    and t.Rating <=%s
                    and not isnull(t.Number_of_Reviews)
                    order by Rating desc, ranking asc
                    limit 10
                    """
            cursor.execute(query, (citta, min, max))
            pass

        elif (cucina is None or cucina=="Qualsiasi") and not (prezzo is None or prezzo=="Qualsiasi"):
            #cucina non scelta prezzo scelto
            query="""select *
                    from ta_restaurants_curated t
                    where t.City =%s
                    and t.Price_Range = %s
                    and t.Rating >=%s
                    and t.Rating <=%s
                    and not isnull(t.Number_of_Reviews)
                    order by Rating desc, ranking asc
                    limit 10
                    """
            cursor.execute(query, (citta, prezzo, min, max))
            pass

        elif not (cucina is None or cucina=="Qualsiasi") and (prezzo is None or prezzo=="Qualsiasi"):
            #cucina scelta prezzo non scelto
            query = """select *
                    from ta_restaurants_curated t
                    where t.City =%s
                    and (Price_Range = '$' or Price_Range = '$$ - $$$' or Price_Range='$$$$')
                    and t.Rating >=%s
                    and t.Rating <=%s
                    and t.Cuisine_Style like %s
                    and not isnull(t.Number_of_Reviews)
                    order by Rating desc, ranking asc
                    limit 10
                    """
            cursor.execute(query, (citta,min,max,f"%{cucina}%"))
            pass

        else:
            #cucina scelta prezzo scelto
            query = """select *
                    from ta_restaurants_curated t
                    where t.City =%s
                    and t.Price_Range = %s
                    and t.Rating >=%s
                    and t.Rating <=%s
                    and t.Cuisine_Style like %s
                    and not isnull(t.Number_of_Reviews)
                    order by Rating desc, ranking asc
                    limit 10
                    """
            cursor.execute(query, (citta, prezzo,min,max,f"%{cucina}%"))
            pass

        for a in cursor:
            res.append(Ristorante(**a))
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def testClassiDAO(c):
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=False)

        res = []
        query = """select *
from (
select count(*) c1
from ristoranti.ta_restaurants_curated t
where t.City =%s
and not isnull(t.Number_of_Reviews) 
and t.Number_of_Reviews <5
) t1,
(
select count(*) c2
from ristoranti.ta_restaurants_curated t
where t.City =%s
and not isnull(t.Number_of_Reviews) 
and t.Number_of_Reviews <30
and t.Number_of_Reviews >=5
) t2,
(
select count(*) c3
from ristoranti.ta_restaurants_curated t
where t.City =%s
and not isnull(t.Number_of_Reviews) 
and t.Number_of_Reviews <100
and t.Number_of_Reviews >=30
) t3,
(
select count(*) c4
from ristoranti.ta_restaurants_curated t
where t.City =%s
and not isnull(t.Number_of_Reviews) 
and t.Number_of_Reviews <500
and t.Number_of_Reviews >=100
) t4,
(
select count(*) c5
from ristoranti.ta_restaurants_curated t
where t.City =%s
and not isnull(t.Number_of_Reviews) 
and t.Number_of_Reviews >=500
) t5
"""

        cursor.execute(query,(c,c,c,c,c,))

        for a in cursor:
            res.append(a)

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def testRecensioni(citta,prezzo):
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        res = []

        query = """select *
                from ta_restaurants_curated t
                where City =%s
                and Price_Range = %s
                and not isnull(t.Number_of_Reviews)
                """

        cursor.execute(query, (citta,prezzo))

        for a in cursor:
            res.append(Ristorante(**a))
        cursor.close()
        cnx.close()
        return res