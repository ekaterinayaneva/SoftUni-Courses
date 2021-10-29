from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:
    def __init__(self, name: str, chocolate_factory: ChocolateFactory, egg_factory: EggFactory, paint_factory: PaintFactory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = {}

    def add_chocolate_ingredient(self, type: str, quantity: int):
        self.chocolate_factory.add_ingredient(type, quantity)

    def add_egg_ingredient(self, type: str, quantity: int):
        self.egg_factory.add_ingredient(type, quantity)

    def add_paint_ingredient(self, type: str, quantity: int):
        self.paint_factory.add_ingredient(type, quantity)

    def make_chocolate(self, recipe: str):
        self.chocolate_factory.make_chocolate(recipe)
        if self.chocolate_factory.products[recipe] <= 0:
            pass
        else:
            self.chocolate_factory.products[recipe] -= 1
        if recipe in self.storage.keys():
            self.storage[recipe] += 1
            return

        self.storage[recipe] = 1


    def paint_egg(self, color: str, egg_type: str):
        egg_colors = [e for e in self.paint_factory.ingredients]
        egg_types = [e for e in self.egg_factory.ingredients]
        if color not in egg_colors or egg_type not in egg_types:
            raise ValueError("Invalid commands")

        if color not in self.storage:
            self.storage[color] = {}
            self.storage[color][egg_type] = 0

        self.storage[color][egg_type] += 1
        self.egg_factory.remove_ingredient(egg_type, 1)
        self.paint_factory.remove_ingredient(color, 1)


    def __repr__(self):
        result = ''
        for s in self.name:
            result += f'Shop name: {s.name}\n'
            for k, v in self.storage.items():
                result += 'Shop Storage:\n'
                result += f'{k}: {v}\n'

        return result



#f = EasterShop('at')

# f.add_egg_ingredient('chicken egg', 8) akaziev lipov           monov lekovit
# f.add_paint_ingredient('blue', 5)
#
# f.paint_egg('blue', 'chicken egg')
# #f.paint_egg('blue', 'chicken egg')
# print(f.storage)


# chokfab = ChocolateFactory('al', 200)
# chokfab.add_ingredient('milk chocolate', 100)
# f.add_chocolate_ingredient('milk chocolate', 100)
# chokfab.add_recipe('Pai', {'milk chocolate': 6})
# chokfab.add_recipe('Pai', {'milk chocolate': 6})
# chokfab.make_chocolate('Pai')
# #
# f.make_chocolate('Pai')
# #
# print(f.storage)
# print(chokfab.ingredients)
#
#
# f.add_ingredient('white chocolate', 100)
# f.add_ingredient('dark chocolate', 100)
# f.add_ingredient('milk chocolate', 100)
#
# f.remove_ingredient('dark chocolate', 7)
# f.remove_ingredient('chocolate', 2)
# f.add_ingredient('chocolate', 3)
#
# print(f.name)
# print(f.ingredients)
# print(len(f.ingredients))
# print(f.can_add(5))
# print(f.proba)