

class player:
    def __init__(self, name, current_hp, max_hp, current_weapon, inventar):
        self.name = name
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.current_weapon = current_weapon
        self.inventar = inventar

    def add_hp(self, value):
        self.current_hp = self.current_hp + value
        if self.current_hp >= self.max_hp:
            self.current_hp = self.max_hp

    def lose_hp(self, value):
        self.current_hp = self.current_hp - value
        if self.current_hp <= 0:
            print("You are Dead!")

    def calculate_dmg(self):
        return

    def change_weapon(self, new_weapon):
        self.current_weapon = new_weapon
        print(new_weapon)
