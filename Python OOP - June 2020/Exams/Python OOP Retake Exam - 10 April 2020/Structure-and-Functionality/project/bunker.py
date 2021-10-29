class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_supplies = [f_s for f_s in self.supplies if f_s.__class__.__name__ == 'FoodSupply']
        if len(food_supplies) == 0:
            raise IndexError("There are no food supplies left!")
        return food_supplies

    @property
    def water(self):
        water_supplies = [w_s for w_s in self.supplies if w_s.__class__.__name__ == 'WaterSupply']
        if len(water_supplies) == 0:
            raise IndexError("There are no water supplies left!")
        return water_supplies

    @property
    def painkillers(self):
        painkillers_med = [p for p in self.medicine if p.__class__.__name__ == 'Painkiller']
        if len(painkillers_med) == 0:
            raise IndexError("There are no painkillers left!")
        return painkillers_med

    @property
    def salves(self):
        salves_med = [s for s in self.medicine if s.__class__.name__ == 'Salve']
        if len(salves_med) == 0:
            raise IndexError("There are no salves left!")
        return salves_med

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type: str):
        if not survivor.needs_healing:
            return

        if medicine_type == 'Painkiller':
            med = self.painkillers[-1]
        else:
            med = self.salves[-1]

        del self.medicine[-1]
        med.apply(survivor)
        return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type: str):
        if not survivor.needs_sustenance:
            return

        if sustenance_type == 'FoodSupply':
            supp = self.food[-1]
        else: # sustenance_type == 'WaterSupply':
            supp = self.water[-1]

        del self.supplies[-1]
        supp.apply(survivor)
        return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2

        for s in self.survivors:
            self.sustain(s, 'FoodSupply')
            self.sustain(s, 'WaterSupply')
