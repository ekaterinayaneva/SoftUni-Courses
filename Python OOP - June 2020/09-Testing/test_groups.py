import unittest

from polymorphism_and_magic_methods_6.groups_TESTING import Person, Group


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person('Ekaterina', 'Yaneva')

    def test_add(self):
        person_2 = Person('Yordan', 'Ilchev')
        person_3 = self.person + person_2

        self.assertEqual(person_3.name, 'Ekaterina')
        self.assertEqual(person_3.surname, 'Ilchev')

    def test_str(self):
        self.assertEqual(self.person.name, 'Ekaterina')
        self.assertNotEqual(self.person.surname, 'Ilchev')


class TestGroup(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person('Ekaterina', 'Yaneva')
        person_2 = Person('Yordan', 'Ilchev')
        self.group = Group('group', [self.person, person_2])

    def test_add(self):
        person_3 = Person('test', 'test')
        group_2 = Group('group', [person_3])
        group_3 = self.group + group_2
        self.assertEqual(len(group_3), 3)

    def test_get_item(self):
        result = self.group[0]
        self.assertIn('Ekaterina', result)
        self.assertEqual(result, 'Person 0: Ekaterina Yaneva')

    def test_str(self):
        result = str(self.group)
        self.assertEqual(result, 'Group group with members Ekaterina Yaneva, Yordan Ilchev')


if __name__ == '__main__':
    unittest.main()
