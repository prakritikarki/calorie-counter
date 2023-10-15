

calories = {
   'Hamburger': 600,
   'Cheese Burger': 750,
   'Veggie Burger': 400,
   'Vegan Burger': 350,
   'Sweet Potatoes': 230,
   'Salad': 15,
   'Iced Tea': 70,
   'Lemonade': 90,
}

combos = {
    "Cheesy Combo" : ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo" : ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo" : ["Vegan Burger", "Salad", "Lemonade"],
}
#creatin a calorie counter function,handling combos and handling errors
def calorie_counter(*items):
    total=0
    for item in items:
        if item in calories:
         total += calories[item]
        else:
            try:
               combo_items = combos[item]
               for combo_item in combo_items:
                total += calories[combo_item]
            except KeyError:
               print(f"{item} not found in the menu")

    return total

#using recursive function
def calorie_counter(items):
    total = 0
    for item in items:  
        if item in calories:
            total += calories[item]
        elif item in combos:
            total += calorie_counter(combos[item])
        else:
            print(f"{item} not found in the menu")
    return total


menu_items = ["Cheesy Combo", "Hamburger", "Lemonade"]
total_calories = calorie_counter(menu_items)
print(f"Total calories: {total_calories}")


#using recursive function
from module.exceptions import MealTooBigError
def calorie_counter(items):
    total = 0
    for item in items:  
        if item in calories:
            total += calories[item]
        elif item in combos:
            total += calorie_counter(combos[item])
        else:
            print(f"{item} not found in the menu")
    if total > 2000:
        raise MealTooBigError(total)
    return total


menu_items = ["Cheesy Combo", "Veggie Combo","Vegan Combo", "Lemonade"]
try:
    total_calories = calorie_counter(menu_items)
    print(f"Total calories: {total_calories}")
except MealTooBigError as e:
    print(f"Error:{e}")




