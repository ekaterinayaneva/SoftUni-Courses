import unittest

#from polymorphism_and_magic_methods_6.vehicles_1_TESTING import Car, Truck


class TestCar(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car(100, 3)

    def test_drive_not_enough_fuel(self):
        self.car.drive(40)

        self.assertEqual(self.car.fuel_quantity, 100)

    def test_drive_enough_fuel(self):
        self.car.drive(20)

        self.assertEqual(self.car.fuel_quantity, 22)

    def test_refuel_eq(self):
        self.car.refuel(50)

        self.assertEqual(self.car.fuel_quantity, 150)

    def test_refuel_not_eq(self):
        self.car.refuel(50)

        self.assertNotEqual(self.car.fuel_quantity, 140)


class TestTruck(unittest.TestCase):
    def setUp(self) -> None:
        self.truck = Truck(200, 5)

    def test_drive_not_enough_fuel(self):
        self.truck.drive(40)

        self.assertEqual(self.truck.fuel_quantity, 200)

    def test_drive_enough_fuel(self):
        self.truck.drive(20)

        self.assertEqual(self.truck.fuel_quantity, 68)

    def test_refuel_eq(self):
        self.truck.refuel(50)

        self.assertEqual(self.truck.fuel_quantity, 247.5)

    def test_refuel_not_eq(self):
        self.truck.refuel(50)

        self.assertNotEqual(self.truck.fuel_quantity, 140)



if __name__ == '__main__':
    unittest.main()