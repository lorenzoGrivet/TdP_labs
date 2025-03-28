from dataclasses import dataclass

@dataclass
class Confine:
    dyad: int
    state1no: int
    state1ab: str
    state2no: int
    state2ab: str
    year: int
    conttype: int
    version: float

    def __hash__(self):
        return hash(str(self.state1no+self.state2no))

    def __str__(self):
        return f"{self.state1no} - {self.state2no}"