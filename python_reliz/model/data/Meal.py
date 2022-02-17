from model.data.Product import Product

MEAL_NAMES = ["soup", "pizza", "fish and chips"]


class Meal:
    def __init__(self, name=""):
        self.name = name
        self.__products = []

    def get_products(self):
        return self.__products

    def add(self, product):
        if self.__check_if_product(product):
            self.__products.append(product)

    def remove(self, product):
        if product in self.__products:
            self.__products.remove(product)

    @staticmethod
    def __check_if_product(product):
        return isinstance(product, Product)

    def __str__(self):
        info = f"Meal \'{self.name}\':\n"

        for item in self.__products:
            info += " *" + str(item) + "\n"

        return info