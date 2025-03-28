from dataclasses import dataclass

@dataclass
class Product:
    number: int
    line: str
    type: str
    prod_name: str
    brand: str
    color: str
    unit_cost: str
    unit_price: str


    def __eq__(self, other):
        return self.number== other.number

    def __hash__(self):
        return hash(self.number)


