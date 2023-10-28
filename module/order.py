from datetime import datetime

from module.exceptions import InvalidItemId, MealTooBigError
from module.complex_data import calorie_counter, price_counter
class Order:
    counter = 0

    def __init__(self, items, date=None):
        Order.counter += 1
        self.order_id = f"order-{self.counter}"
        if date is None:
            date = datetime.date.today()
        else:
            self.date = datetime.datetime.strptime(date, "%d-%b-%Y")
        self.items = items
        self._calories = None
        self._price = None
        try:
            self.calories 
            
        except (InvalidItemId, MealTooBigError) as e:
            self.order_accepted = False
            self.order_refused_reason = e.message
            self._calories = 0
            self._price = 0
        else:
            self.order_accepted = True
            self.order_refused_reason = None
    
    @property
    def calories(self):
        if self._calories is None:
            self._calories = calorie_counter(self.items)
        return self._calories
    @property
    def price(self):
        if self._price is None:
             self._price = price_counter(self.items)
        return self._price

        