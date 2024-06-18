# RPG Game with chatGPT
# Class for player

class Player:
    def __init__(self, name='Player', exp=0, hp=100, attack=1, defense=1):
        self.name = name
        self.exp = exp
        self.base_hp = hp
        self.hp_loss = 0
        self.base_attack = attack
        self.base_defense = defense
        self.gold = 0

    def get_stats(self):
        return f"Name: {self.name}\nLevel: {self.get_level()}\nExp: {self.exp}\nHP: {self.hp}\nAttack: {self.attack}\nDefense: {self.defense}\nGold: {self.gold}\n"

    def get_gold(self):
        return self.gold

    def get_exp(self):
        return self.exp

    def get_level(self):
        return 1 + self.exp // 100

    def get_max_hp(self):
        return self.base_hp + 10 * (self.get_level() - 1)

    def get_attack(self):
        return self.base_attack + (self.get_level() - 1)

    def get_defense(self):
        return self.base_defense + (self.get_level() - 1)
    
    def add_gold(self, gold):
        self.gold += gold

    def add_exp(self, exp):
        self.exp += exp

    def restore_hp(self, hp):
        if self.hp_loss > hp:
            self.hp_loss -= hp
        else:
            self.hp_loss = 0
    
    def take_damage(self, damage):
        self.hp_loss += damage

    def is_alive(self):
        return self.hp_loss < self.get_max_hp()

    def attack_target(self, target):
        damage = max(0, self.get_attack() - target.defense)
        target.take_damage(damage)
        return damage

    def defeat(self, ennemy):
        self.add_exp(ennemy.xp)
        self.add_gold(ennemy.gold)
