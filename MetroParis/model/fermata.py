from dataclasses import dataclass

@dataclass
class Fermata:
    _id_fermata: int
    _nome: str
    _coordX: int
    _coordY: int

    @property
    def id_fermata(self):
        return self._id_fermata

    @property
    def nome(self):
        return self._nome

    @property
    def coordX(self):
        return self._coordX

    @property
    def coordY(self):
        return self._coordY

    def __hash__(self):
        return self._id_fermata

    def __str__(self):
        return f"{self._nome}"
