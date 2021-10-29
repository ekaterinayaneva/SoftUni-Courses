#from inheritance_5.restaurant_5.project.food.main_dish import MainDish
from project.food.main_dish import MainDish


class Salmon(MainDish):
    SALMON_GRAMS = 22

    def __init__(self, name, price):
        MainDish.__init__(self, name, price, Salmon.SALMON_GRAMS)
