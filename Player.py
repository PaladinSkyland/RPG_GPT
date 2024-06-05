# RPG Game with chatGPT
# Class for player

class Player:
    def __init__(self, name = 'Player', level = 0 , exp= 0, hp = 100, attack = 1, defense = 1, gold = 0, items = [], equipped = [], statuseffect = [], alive = True):
        self.name = name
        self.level = level
        self.exp = exp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.gold = gold
        self.items = items
        self.equipped = equipped
        self.statuseffect = statuseffect
        self.alive = alive

    # Getters
    def get_stats(self):
        return f"Name: {self.name}\nLevel: {self.level}\nExp: {self.exp}\nHP: {self.hp}\nAttack: {self.attack}\nDefense: {self.defense}\nGold: {self.gold}\n"

    def get_items(self):
        return self.items

    def get_equipped(self):
        return self.equipped

    def get_gold(self):
        return self.gold

    def get_exp(self):
        return self.exp

    def get_level(self):
        return self.level

    def get_hp(self):
        return self.hp

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    # Setters
    def set_gold(self, gold):
        self.gold = gold

    def set_exp(self, exp):
        self.exp = exp

    def set_level(self, level):
        self.level = level

    def set_hp(self, hp):
        self.hp = hp

    def set_attack(self, attack):
        self.attack = attack

    def set_defense(self, defense):
        self.defense = defense

    def set_items(self, items):
        self.items = items

    def set_equipped(self, equipped):
        self.equipped = equipped


    # Adders
    def add_gold(self, gold):
        self.gold += gold

    def add_exp(self, exp):
        self.exp += exp

    def add_hp(self, hp):
        self.hp += hp

    def add_attack(self, attack):
        self.attack += attack

    def add_defense(self, defense):
        self.defense += defense

    # item management
    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def remove_item(self, item):
        if item in self.items:
            self.items[item] -= 1
            if self.items[item] == 0:
                del self.items[item]