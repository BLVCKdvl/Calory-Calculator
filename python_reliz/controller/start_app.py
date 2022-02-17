import random

from model.data.Meal import Meal, MEAL_NAMES
from model.data.Product import *
from model.logic.calory_summer import count_calory
from utils.console_input import user_input
from view.console import console_print


def main():
    amount_of_products = int(user_input("Enter the amount of products in meal: "))

    meal = Meal(MEAL_NAMES[random.randrange(len(MEAL_NAMES))])

    for _ in range(amount_of_products):
        meal.add(Product(PRODUCT_NAMES[random.randrange(len(PRODUCT_NAMES))],
                         random.randint(MIN_CALORY, MAX_CALORY)))

    console_print(f"{meal}\nAmount of calories {count_calory(meal)}")
