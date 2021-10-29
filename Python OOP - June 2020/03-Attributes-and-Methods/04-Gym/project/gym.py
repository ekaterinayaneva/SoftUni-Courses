class Gym:
    def __init__(self):

        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer = [c for c in self.customers if c.id == subscription_id][0]
        trainer = [t for t in self.trainers if t.id == subscription_id][0]
        plan = [p for p in self.plans if p.id == subscription_id][0]
        equipment = [e for e in self.equipment if e.id == subscription_id][0]

        result = subscription.__repr__() + '\n' \
                 + customer.__repr__() + '\n' \
                 + trainer.__repr__() + '\n' \
                 + equipment.__repr__() + '\n' \
                 + plan.__repr__()

        return result


#from attributes_and_methods_3.gym_4.project.customer import Customer

#from attributes_and_methods_3.gym_4.project.equipment import Equipment

#from attributes_and_methods_3.gym_4.project.exercise_plan import ExercisePlan

#from attributes_and_methods_3.gym_4.project.gym import Gym

#from attributes_and_methods_3.gym_4.project.subscription import Subscription

#from attributes_and_methods_3.gym_4.project.trainer import Trainer

