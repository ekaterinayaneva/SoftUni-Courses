class CapacityMixin:
    def __init__(self):
        pass

    @staticmethod
    def get_capacity(capacity, amount):
        if amount > capacity:
            return "Capacity reached!"