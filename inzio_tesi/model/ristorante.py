from dataclasses import dataclass


@dataclass
class Ristorante:
    riga: int
    Name: str
    City: str
    Cuisine_Style: str
    Ranking: float
    Rating: float
    Price_Range: str
    Number_of_Reviews: float
    Reviews: str
    URL_TA: str
    ID_TA: str

    def __hash__(self):
        return hash(self.ID_TA)

    def __str__(self):
        return f"{self.Name}"