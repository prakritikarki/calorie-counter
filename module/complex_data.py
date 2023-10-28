
from module.exceptions import InvalidItemId

import json

with open("module/data/combos.json") as file:
	combos = json.load(file)["combos"]
	
combos_info = {
    combo["id"]:combo
    for combo in combos
}
print (combos_info)

with open("module/data/meals.json") as file:
	meals = json.load(file)["meals"]

meals_info = {
    meal["id"]:meal
    for meal in meals}

print(meals_info)

def calorie_counter(items):
    total = 0
    for item in items:
        if item in meals_info:
            total += meals_info[item]["calories"]
        elif item in combos_info:
            combo = combos_info[item]
            total += calorie_counter(combo["meals"])
        else:
            raise InvalidItemId(item)
    return total
item_list = ["combo-2", "meal-3", "meal-8","Tacos"]
total_calories = calorie_counter(item_list)
print(f'Total calories: {total_calories}')

def price_counter(items):
    total = 0
    for item in items:
        if item in meals_info:
            total += meals_info[item]["price"]
        elif item in combos_info:
            combo = combos_info[item]
            total += combo["price"]
        else:
            raise InvalidItemId(item)
    return total
item_list = ["combo-2", "meal-3", "meal-8"]
total_price = price_counter(item_list)
print(f'Total calories: {total_price}')