from dataclasses import dataclass

from model.airport import Airport


@dataclass
class Connessione:
    V0 : Airport
    V1 : Airport
    N : int