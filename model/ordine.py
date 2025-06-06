from dataclasses import dataclass
from datetime import datetime as dtime


@dataclass
class Ordine:
    order_id: int
    customer_id: int
    order_status: int
    order_date: int
    required_date: dtime
    shipped_date: dtime
    store_id: int
    staff_id: int

    def __hash__(self):
        return hash(self.order_id)

    def __eq__(self, other):
        return self.order_id == other.order_id

    def __str__(self):
        return f"Ordine - {self.order_id}"



