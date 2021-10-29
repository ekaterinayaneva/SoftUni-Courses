class PizzaDelivery:
    ordered = False

    def __init__(self, name, price, ingredients: {}):
        self.name = name
        self.price = price
        self.ingredients = ingredients


    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):

        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"

        if ingredient in self.ingredients.keys():
            self.ingredients[ingredient] += quantity
            self.price += quantity * ingredient_price
        else:
            self.ingredients[ingredient] = quantity
            self.price += ingredient_price * quantity


    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):

        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"


        if ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

      #  elif ingredient in self.ingredients.keys() and self.ingredients[ingredient] != quantity:
        elif self.ingredients[ingredient] - quantity < 0:
            return f"Please check again the desired quantity of {ingredient}!"
        else:
            self.ingredients[ingredient] -= quantity
            self.price -= ingredient_price * quantity


    def get_dict_pairs(self):
        dict_pairs = []
        for key, value in self.ingredients.items():
            dict_pairs.append(f'{key}: {value}')
        return dict_pairs


    def pizza_ordered(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join(self.get_dict_pairs())} and the price will be {self.price}lv."


Margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})

Margarita.add_extra('mozzarella', 1, 0.5)
Margarita.add_extra('cheese', 1, 1)

Margarita.remove_ingredient('cheese', 1, 1)
print(Margarita.remove_ingredient('bacon', 1, 2.5))
print(Margarita.remove_ingredient('tomatoes', 2, 0.5))
Margarita.remove_ingredient('cheese', 2, 1)

print(Margarita.pizza_ordered())
print(Margarita.add_extra('cheese', 1, 1))






