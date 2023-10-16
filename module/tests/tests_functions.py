from unittest import TestCase
from module.complex_data import calorie_counter, price_counter

class CaloriesCounterTestCase(TestCase):
    def test_count_meals_calories(self):
        result = calorie_counter(["meal-1","meal-2","meal-7"])
        self.assertEqual(result,1421, f"Expected 1421, got {result}")


    def test_count_combo_calories(self):
        result = calorie_counter(["combo-2","combo-3"])
        self.assertEqual(result,1155,f"Expected 1155, got {result}")

    def test_count_meals_and_combos_calories(self):
        result = calorie_counter(["meal-1","combo-3"])
        self.assertEqual(result,1055,f"Expected 1055,got {result}")
   
class PriceCounterTestCase(TestCase):
    def test_count_meals_price(self):
        result = price_counter(["meal-1","meal-2","meal-7"])
        self.assertEqual(result,14, f"Expected 14, got {result}")


    def test_count_combo_price(self):
        result = price_counter(["combo-2","combo-3"])
        self.assertEqual(result,20,f"Expected 20, got {result}")

    def test_count_meals_and_combos_prices(self):
        result = price_counter(["meal-1","combo-3"])
        self.assertEqual(result,15,f"Expected 15,got {result}")
   