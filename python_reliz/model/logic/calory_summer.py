from model.data.Meal import Meal


def count_calory(meal):
    if not isinstance(meal, Meal):
        return

    calories = 0
    for item in meal.get_products():
        calories += item.get_calories()

    return calories