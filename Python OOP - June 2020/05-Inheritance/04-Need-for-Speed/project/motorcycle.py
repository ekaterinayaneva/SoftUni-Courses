#from inheritance_5.need_for_speed_4.project.vehicle import Vehicle
from project.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, fuel, horse_power, fuel_consumption):
        Vehicle.__init__(self, fuel, horse_power, fuel_consumption)
        self.fuel_consumption = 1.25

    def drive(self, kilometers):
        needed_fuel = self.fuel_consumption * kilometers
        if self.fuel >= needed_fuel:
            self.fuel -= needed_fuel