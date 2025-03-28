from dataclasses import dataclass

@dataclass
class Airport:
    id: int
    nome: str


    def __eq__(self, other):
        return self.id==self.id

    def __hash__(self):
        return hash(self.id)