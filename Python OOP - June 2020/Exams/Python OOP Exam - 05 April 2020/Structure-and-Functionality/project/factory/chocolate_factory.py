from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name: str, capacity: int):
        Factory.__init__(self, name, capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient_type: str, quantity: int):
        possible_ingredients = ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]

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

    def add_recipe(self, recipe_name: str, recipe: dict):
       # self.recipes[recipe_name] = recipe     samo tova ili
        if recipe_name in self.recipes.keys():
            for k, v in recipe.items():
                if k not in self.recipes[recipe_name]:
                    self.recipes[recipe_name][k] = v
                    return
                self.recipes[recipe_name][k] += v
                return
        for k, v in recipe.items():
            self.recipes[recipe_name] = {}
            self.recipes[recipe_name][k] = v

    def make_chocolate(self, recipe_name: str):
        if recipe_name not in self.recipes:
            raise TypeError("No such recipe")

        if recipe_name not in self.products:
            self.products[recipe_name] = 0

        self.products[recipe_name] += 1

        for ingr in self.recipes[recipe_name]:
            self.ingredients[ingr] -= self.recipes[recipe_name][ingr]

        #for k, v in self.recipes[recipe_name].items():
         #   self.proba[k] = v
            #self.ingredients[k] -= v


#
# f = ChocolateFactory('at', 1000)
# f.add_ingredient('white chocolate', 100)
# f.add_ingredient('dark chocolate', 100)
# f.add_ingredient('milk chocolate', 100)
# #f.add_recipe('Pai', {'white chocolate': 5, 'milk chocolate': 6, 'dark chocolate': 7})
# f.add_recipe('Pai', {'milk chocolate': 6})
# f.add_recipe('Pai', {'white chocolate': 10})
# f.add_recipe('Pai', {'dark chocolate': 20})
# f.add_recipe('Pai', {'dark chocolate': 20})
# print(f.recipes)
#
# f.make_chocolate('Pai')
# f.make_chocolate('Pai')
# print(f.products)
# print(f.ingredients)


# f.add_ingredient('white chocolate', 100)
# f.add_ingredient('dark chocolate', 100)
# f.add_ingredient('milk chocolate', 100)
# #
# f.remove_ingredient('dark chocolate', 7)
# f.remove_ingredient('chocolate', 2)
# f.add_ingredient('chocolate', 3)
#
# print(f.name)
# print(f.ingredients)
# print(len(f.ingredients))
# print(f.can_add(2000))
# print(f.proba)

