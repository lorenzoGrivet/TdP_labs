from database.DAO import DAO
from model.model import Model

# res= DAO.getAllObjects()
model=Model()
model.creaGrafo()

model.getConnessa(1234)

# conn=DAO.getAllConnessioni(model._idMap)
#
# print(len(res))
# print(len(conn))