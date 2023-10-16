#using complex data
meals = [
    {
        "id": "meal-1",
        "name": "hamburger",
        "calories": 600,
        "price": 5
    },
    {
        "id": "meal-2",
        "name": "cheese burger",
        "calories": 750,
        "price": 7
	},
    {
        "id": "meal-3",
        "name": "veggie burger",
        "calories": 400,
        "price": 6
	},
    {
        "id": "meal-4",
        "name": "vegan burger",
        "calories": 350,
        "price": 6
	},
    {
        "id": "meal-5",
        "name": "sweet potatoes",
        "calories": 230,
        "price": 3
	},
    {
        "id": "meal-6",
        "name": "salad",
        "calories": 15,
        "price": 4
	},
    {
        "id": "meal-7",
        "name": "iced tea",
        "calories": 70,
        "price": 2
	},
    {
        "id": "meal-8",
        "name": "lemonade",
        "calories": 90,
        "price": 2
	}
]

combos = [
    {
        "id": "combo-1",
        "name": "cheesy combo",
        "meals": ["meal-2", "meal-5", "meal-8"],
        "price": 11,
    },
    {
        "id": "combo-2",
        "name": "veggie combo",
        "meals": ["meal-3", "meal-5", "meal-7"],
        "price": 10,
    },
    {
        "id": "combo-3",
        "name": "vegan combo",
        "meals": ["meal-4", "meal-6", "meal-8"],
        "price": 10,
    }
]

from module.exceptions import InvalidItemId
meals_info = {
    meal["id"]:meal
    for meal in meals
}
combos_info = {
    combo["id"]:combo
    for combo in combos
}
# def calorie_counter(items):
#     total = 0
#     for item in items:
#         if item in meals_info:
#             total += meals_info[item]["calories"]
#         elif item in combos_info:
#             combo = combos_info[item]
#             total += calorie_counter(combo["meals"])
#         else:
#             print(f'{item} not found in the menu')
#     return total
# item_list = ["combo-2", "meal-3", "meal-8"]
# total_calories = calorie_counter(item_list)
# print(f'Total calories: {total_calories}')

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