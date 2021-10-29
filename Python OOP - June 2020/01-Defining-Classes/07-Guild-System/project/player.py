class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills_dict = {}
        self.guild = "Unaffiliated"

    
    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills_dict:
            return "Skill already added"

        self.skills_dict[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"


    def player_info(self):
        result = f"Name: {self.name}  \n  Guild: {self.guild}  \n {self.hp}  \n {self.mp} \n "
        for key, value in self.skills_dict.items():
            result += f"=== {key} - {value}  \n"

        return result
