from abc import ABC, abstractmethod


class Factory(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    @abstractmethod
    def add_ingredient(self, ingredient_type: str, quantity: int):
        pass

    @abstractmethod
    def remove_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def can_add(self, value: int):
        result = self.capacity - (sum(self.ingredients.values()) + value)
        if result >= 0:
            return True #result
        return False
        #raise ValueError('Not enough space in factory')


