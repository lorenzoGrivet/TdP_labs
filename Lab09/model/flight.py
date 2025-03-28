from dataclasses import dataclass

@dataclass
class Flight:
    id: int
    dep_airport: int
    arr_airport: int
    distance: int

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id==other.id


