from inheritance_5.mix_it_6.project.capacity_mixin import CapacityMixin
from inheritance_5.mix_it_6.project.vehicle.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, available_seats, fuel_tank, fuel_consumption, fuel):
        Vehicle.__init__(self, available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self._fuel = fuel

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, value):
        if self._fuel > self.fuel_tank:
            self._fuel = self.fuel_tank

    def drive(self, distance):
        needed_fuel = self.fuel_consumption * distance
        if self._fuel >= needed_fuel:
            self._fuel -= needed_fuel
            return " We've enjoyed the travel!"

    def refuel(self, liters):
        if self._fuel + liters <= self.fuel_tank:
            self._fuel += liters
            return self._fuel
        else:
            self._fuel = self.fuel_tank
            CapacityMixin.get_capacity(self.fuel_tank, self._fuel + liters)


