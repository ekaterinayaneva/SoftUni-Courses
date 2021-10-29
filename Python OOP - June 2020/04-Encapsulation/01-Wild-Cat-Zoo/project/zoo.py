class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__workers_capacity = workers_capacity
        self.__animal_capacity = animal_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
       try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
       except:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salary = sum([worker.salary for worker in self.workers])
        if self.__budget >= workers_salary:
            self.__budget -= workers_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_tend = sum([animal.get_needs() for animal in self.animals])
        if self.__budget >= animals_tend:
            self.__budget -= animals_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [l for l in self.animals if l.__class__.__name__ == 'Lion']
        tigers = [t for t in self.animals if t.__class__.__name__ == 'Tiger']
        cheetahs = [c for c in self.animals if c.__class__.__name__ == 'Cheetah']

        result = f"You have {len(self.animals)} animals \n"
        result += f"----- {len(lions)} Lions: \n"
        result += '\n'.join([l.__repr__() for l in lions]) + '\n'
        result += f"----- {len(tigers)} Tigers: \n"
        result += '\n'.join([t.__repr__() for t in tigers]) + '\n'
        result += f"----- {len(cheetahs)} Cheetahs: \n"
        result += '\n'.join([c.__repr__() for c in cheetahs]) + '\n'

        return result

    def workers_status(self):
        caretakers = [c for c in self.workers if c.__class__.__name__ == 'Caretaker']
        keepers = [k for k in self.workers if k.__class__.__name__ == 'Keeper']
        vets = [v for v in self.workers if v.__class__.__name__ == 'Vet']

        result = f"You have {len(self.workers)} workers" '\n'
        result += f"----- {len(keepers)} Keepers" '\n'
        result += '\n'.join([k.__repr__() for k in keepers]) + '\n'
        result += f"----- {len(caretakers)} Caretakers" '\n'
        result += '\n'.join([c.__repr__() for c in caretakers]) + '\n'
        result += f"----- {len(vets)} Vets" '\n'
        result += '\n'.join([v.__repr__() for v in vets]) + '\n'

        return result


#from encapsulation_4.wild_cat_zoo_1.project.caretaker import Caretaker
#from encapsulation_4.wild_cat_zoo_1.project.cheetah import Cheetah
#from encapsulation_4.wild_cat_zoo_1.project.keeper import Keeper
#from encapsulation_4.wild_cat_zoo_1.project.lion import Lion
#from encapsulation_4.wild_cat_zoo_1.project.vet import Vet
#from encapsulation_4.wild_cat_zoo_1.project.tiger import Tiger




