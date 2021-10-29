class MovieWorld:
    dvds_capacity = 15
    customers_capacity = 10

    def __init__(self, name: str):
        self.name = name

        self.customers = []
        self.dvds = []


    @staticmethod
    def dvd_capacity():
        return MovieWorld.dvds_capacity

    @staticmethod
    def customer_capacity():
        return MovieWorld.customers_capacity

    def add_customer(self, customer):
        if len(self.customers) <= MovieWorld.customers_capacity:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) <= MovieWorld.dvds_capacity:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [d for d in self.dvds if d.id == dvd_id][0]

        if dvd.is_rented:
            return "DVD is already rented"
        elif dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        else:
            customer.rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [d for d in self.dvds if d.id == dvd_id][0]

        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for c in range(len(self.customers)):
            result = f"{self.customers[c].__repr__()}" + '\n'

        for d in range(len(self.dvds)):
            result += f"{self.dvds[d].__repr__()}" + '\n'

        return result

