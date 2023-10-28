# calorie-counter in python version 3.11.5
 

 "This file contains the solution that provides code to calculate the price and calories of food items ordered."

 Installation
 
 Clone the repository
git clone https://github.com/prakritikarki/calorie-counter.git

cd calorie-counter

##Create and activate a virtual environment

python -m venv .venv

.venv\Scripts\activate

Install dependencies(inside virtual environment):

python -m pip install -r requirements.txt

Files

Most of the codes are in the module folder.
combos.json and meals.json are the json files within the data folder.
complex_data .py holds the solution to calorie and price counter of the food items.
exceptions.py file has the code that indicates meal toobig error i.e. if the total calories is highe than 2000, it leaves error message and the InvalidItemId function to represent if any item ordered is not in the menu.

Order class

if the total calories count of the order is greater than 2000 calories, the order will be refused and if an order contains an unknown item id, again the order will also be refused

#Data analysis

#Run tests
python -m unittest

 
