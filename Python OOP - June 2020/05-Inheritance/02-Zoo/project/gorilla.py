#from inheritance_5.zoo_2.project.mammal import Mammal
from project.mammal import Mammal


class Gorilla(Mammal):
    def __init__(self, name):
        Mammal.__init__(self, name)

