from dataclasses import dataclass

@dataclass
class Connessione:
    _id_connessione: int
    _id_linea: int
    _id_stazP: int
    _id_stazA: int


    @property
    def id_connessione(self):
        return self._id_connessione

    @property
    def id_linea(self):
        return self._id_linea

    @property
    def id_stazP(self):
        return self._id_stazP

    @property
    def id_stazA(self):
        return self._id_stazA

    def __hash__(self):
        return hash(self._id_connessione)

    def __str__(self):
        return f"Connessione: {self._id_stazP} -> {self._id_stazA}"