import types
import unittest

from project.factory.paint_factory import PaintFactory
#from project.factory.factory import Factory


class TestPaintFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory('Painting', 2000)

    def test_setted_param(self):
        self.assertEqual(self.factory.name, 'Painting')
        self.assertEqual(self.factory.capacity, 2000)
        self.assertEqual(self.factory.__class__.__name__, 'PaintFactory')

    def test_add_ingredient_not_possible(self):
        with self.assertRaises(TypeError) as ex:
            self.factory.add_ingredient('purple', 5)
        self.assertEqual(str(ex.exception), "Ingredient of type purple not allowed in PaintFactory")

    def test_add_ingredient_can_add_raise(self):
#        self.factory.add_ingredient('red', 5)
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient('red', 2005)
#            self.factory.can_add(3000)
        self.assertEqual(str(ex.exception), "Not enough space in factory")

    def test_add_ingredient_can_add(self):
        self.factory.add_ingredient('red', 5)
        self.assertTrue(self.factory.can_add(100), 1895)

    def test_add_ingredient_self_ingredient(self):
        self.factory.add_ingredient('red', 5)
        self.factory.add_ingredient('blue', 10)
        self.assertEqual(len(self.factory.ingredients), 2)
        self.assertEqual(self.factory.ingredients, {'blue': 10, 'red': 5})

        self.assertEqual(self.factory.ingredients['red'], 5)
        self.assertIn('red', self.factory.ingredients)

    def test_remove_ingredient(self):
        self.factory.add_ingredient('red', 5)
        self.factory.add_ingredient('blue', 10)
        self.assertEqual(len(self.factory.ingredients), 2)
        self.factory.remove_ingredient('blue', 10)
        self.assertEqual(len(self.factory.ingredients), 2)
        self.assertEqual(self.factory.ingredients, {'blue': 0, 'red': 5})

        self.assertEqual(self.factory.ingredients['red'], 5)

    def test_remove_ingredient_not_possible_ingredient(self):
        self.factory.add_ingredient('red', 5)
        self.factory.add_ingredient('blue', 10)
        with self.assertRaises(KeyError) as ex:
            self.factory.remove_ingredient('green', 3)
        self.assertNotEqual(str(ex.exception), 'No such product in the factory')

    def test_remove_ingredient_not_possible_qantity(self):
        self.factory.add_ingredient('red', 5)
        self.factory.add_ingredient('blue', 10)
        with self.assertRaises(ValueError) as ex:
            self.factory.remove_ingredient('red', 8)
        self.assertEqual(str(ex.exception), 'Ingredient quantity cannot be less than zero')

    def test_validate_property(self):
        self.assertFalse((isinstance(self.factory.products, types.FunctionType)))


if __name__ == "__main__":
    unittest.main()

