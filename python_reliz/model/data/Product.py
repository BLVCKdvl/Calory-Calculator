PRODUCT_NAMES = ["banana", "yogurt", "soup", "tomato", "banana"]

MIN_CALORY = 1

MAX_CALORY = 250


class Product:
    def __init__(self, name="", calories=MIN_CALORY):
        self.name = name
        self.__calories = MIN_CALORY
        self.set_calories(calories)

    def get_calories(self):
        return self.__calories

    def set_calories(self, mass):
        if isinstance(mass, int):
            self.__calories = mass

    def __str__(self):
        return f"{self.name} with {self.__calories} calories"
