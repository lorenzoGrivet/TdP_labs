from database import DAO

class Model:
    def __init__(self):
        self.products= DAO.DAO().getProductsDao()
        self.retailers = DAO.DAO().getRetailerDao()



    def analizza(self,anno,brand,retailer):
        lista=DAO.DAO().analizzaDao(anno,brand,retailer)
        totale=0.0
        n_vendite=len(lista)
        distinct_ret=[]
        distinct_prod=[]
        n_ret=None
        n_prod=None

        for i in lista:
            totale=totale+ (float(i.quantity)*float(i.sale_price))

            if not distinct_ret.__contains__(i.ret_code):
                distinct_ret.append(i.ret_code)

            if not distinct_prod.__contains__(i.prod_number):
                distinct_prod.append(i.prod_number)

        n_ret=len(distinct_ret)
        n_prod=len(distinct_prod)

        return (totale,n_vendite,n_ret,n_prod)




    def getProducts(self):
        return self.products

    def getRetailers(self):
        return self.retailers