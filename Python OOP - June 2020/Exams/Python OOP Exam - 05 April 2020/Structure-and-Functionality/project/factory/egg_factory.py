from project.factory.factory import Factory


class EggFactory(Factory):
    def __init__(self, name: str, capacity: int):
        Factory.__init__(self, name, capacity)


    def add_ingredient(self, ingredient_type: str, quantity: int):
        possible_ingredients = ["chicken egg", "quail egg"]
        if ingredient_type not in possible_ingredients:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")
        if not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        if ingredient_type in self.ingredients:
            self.ingredients[ingredient_type] += quantity
            return
        self.ingredients[ingredient_type] = quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients.keys():
            raise KeyError("No such product in the factory")
        if self.ingredients[ingredient_type] < quantity:
            raise ValueError("Ingredient quantity cannot be less than zero")
        self.ingredients[ingredient_type] -= quantity

    @property
    def products(self):
        return self.ingredients





# f = EggFactory('at', 1000)
#
# f.add_ingredient('chicken egg', 100)
# f.add_ingredient('quail egg', 100)
# f.add_ingredient('quail egg', 100)
#
# print(f.ingredients)
# print(f.proba)
