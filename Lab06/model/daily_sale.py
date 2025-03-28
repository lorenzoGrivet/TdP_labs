import datetime
from dataclasses import dataclass

@dataclass
class DailySale:
    ret_code: str
    prod_number: int
    method: int
    date: datetime.date
    quantity: int
    price: float
    sale_price: float


    def __str__(self):
        return f"Data: {self.date}, Ricavo: {self.sale_price*self.quantity}, Retailer: {self.ret_code}, Product: {self.prod_number}"