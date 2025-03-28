from database.corso_dao import CorsoDao


class Model:
    def get_corsi_periodo(self,pd):
        return CorsoDao.get_corsi_periodo(pd)

    def get_studenti_periodo(self,pd):
        matricole=CorsoDao.get_studenti_periodo(pd)
        return len(matricole)
        pass