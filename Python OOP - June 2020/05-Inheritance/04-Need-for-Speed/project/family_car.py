#from inheritance_5.need_for_speed_4.project.car import Car
from project.car import Car


class FamilyCar(Car):
    def __init__(self, fuel, horse_power, fuel_consumption):
        Car.__init__(self, fuel, horse_power, fuel_consumption)
        self.fuel_consumption = 3

    def drive(self, kilometers):
        needed_fuel = self.fuel_consumption * kilometers
        if self.fuel >= needed_fuel:
            self.fuel -= needed_fuel