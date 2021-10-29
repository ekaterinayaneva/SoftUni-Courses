import unittest
from project.survivor import Survivor

class TestSurvivor(unittest.TestCase):
    def test_set_attr(self):
        self.survivor = Survivor('Ekaterina', 32)
        self.assertEqual(self.survivor.name, 'Ekaterina')
        self.assertEqual(self.survivor.age, 32)
        self.assertEqual(self.survivor.health, 100)
        self.assertEqual(self.survivor.needs, 100)
        self.assertEqual(self.survivor.needs_healing, False)
        self.assertEqual(self.survivor.needs_sustenance, False)

    def test_name_raise_ex(self):
        with self.assertRaises(ValueError) as ex:
            Survivor('', 15)
        self.assertEqual(str(ex.exception), "Name not valid!")

    def test_age_raise_ex(self):
        with self.assertRaises(ValueError) as ex:
            Survivor('Eka', -3)
        self.assertEqual(str(ex.exception), "Age not valid!")

    def test_health_raise_ex(self):
        survivor = Survivor('Ekaterina', 32)
        with self.assertRaises(ValueError) as ex:
            survivor.health = -2
        self.assertEqual(str(ex.exception), "Health not valid!")

    def test_needs_raise_ex(self):
        survivor = Survivor('Ekaterina', 32)
        with self.assertRaises(ValueError) as ex:
            survivor.needs = -2
        self.assertEqual(str(ex.exception), "Needs not valid!")

    def test_needs_sustenance_raise(self):
        survivor = Survivor('Eka', 15)
        survivor.needs -= 35
        self.assertEqual(survivor.needs_sustenance, True)

    def test_needs_healing_raise(self):
        survivor = Survivor('Eka', 15)
        survivor.health -= 50
        self.assertEqual(survivor.needs_healing, True)








