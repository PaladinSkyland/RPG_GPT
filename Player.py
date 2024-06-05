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
        self.inventory = {}
        self.items = {}
        self.statuseffect = {}

    def get_stats(self):
        return f"Name: {self.name}\nLevel: {self.get_level()}\nExp: {self.exp}\nHP: {self.hp}\nAttack: {self.attack}\nDefense: {self.defense}\nGold: {self.gold}\n"

    def get_inventory(self):
        return self.inventory

    def get_items(self):
        return self.items

    def get_gold(self):
        return self.gold

    def get_exp(self):
        return self.exp

    def get_level(self):
        return self.xp // 100

    def get_max_hp(self):
        return self.base_hp * self.get_level() + sum([item.hp for item in self.items.values()])

    def get_attack(self):
        return self.base_attack * self.get_level() + sum([item.attack for item in self.items.values()]) + sum([status.attack for status in self.statuseffect.values()])

    def get_defense(self):
        return self.base_defense * self.get_level() + sum([item.defense for item in self.items.values()]) + sum([status.defense for status in self.statuseffect.values()])

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
        target.take_damage(self.attack)

    def defeat(self, ennemy):
        self.add_exp(ennemy.xp)
        self.add_gold(ennemy.gold)

    def clear_status(self):
        for status in self.statuseffect.values():
            if status.negative:
                self.remove_status(status)

    def add_status(self, status):
        if status.name not in self.statuseffect:
            self.statuseffect[status.name] = status
    
    def remove_status(self, status):
        if status.name in self.statuseffect:
            del self.statuseffect[status.name]

    def add_to_inventory(self, consumable):
        if consumable.name in self.inventory:
            self.inventory[consumable.name]['quantity'] += 1
        else:
            self.inventory[consumable.name] = {'item': consumable, 'quantity': 1}

    def remove_from_inventory(self, consumable):
        if consumable.name in self.inventory:
            self.inventory[consumable.name]['quantity'] -= 1
            if self.inventory[consumable.name]['quantity'] == 0:
                del self.inventory[consumable.name]
    
    def use_consumable(self, consumable):
        if consumable.name in self.inventory:
            consumable.use(self)
            self.remove_item(consumable)

    def equip_item(self, item):
        if not item.name in self.items:
            self.items[item.name] = item
    
    def unequip_item(self, item):
        if item.name in self.items:
            del self.items[item.name]