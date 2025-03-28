import datetime
from dataclasses import dataclass


@dataclass
class Sale:
    Retailer_code: int
    Product_number: int
    Order_method_code: int
    Date: datetime.date
    Quantity: int
    Unit_price:float
    Unit_sale_price:float

