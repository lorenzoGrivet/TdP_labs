from dataclasses import dataclass

@dataclass
class Studente:
    matricola: int
    cognome: str
    nome: str
    CDS: str

    def __str__(self):
        return f"{self.matricola}, {self.cognome}, {self.nome}, {self.CDS}"

    def __eq__(self, other):
        return self.matricola==other.matricola

    def __hash__(self):
        return hash(self.matricola)