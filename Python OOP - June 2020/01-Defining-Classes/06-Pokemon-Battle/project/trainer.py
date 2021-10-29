from defining_classes_1.pokemon_battle_6.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []


    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return f"This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"


    def release_pokemon(self, pokemon_name: str):
       # if pokemon_name in self.pokemon:
        self.pokemon.remove(pokemon_name)
        return f"You have released {pokemon_name}"

   #     return "Pokemon is not caught"


    def trainer_data(self):
        result = f"Pokemon Trainer {self.name} \nPokemon count {len(self.pokemon)} \n"
        for pokemon in self.pokemon:
            result += f"- {pokemon.pokemon_details()} \n"
        return result


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.trainer_data())


print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())

