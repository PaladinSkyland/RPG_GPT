class Consumable:
    def __init__(self, name, description, price, hp=0, attack=0, defense=0):
        self.name = name
        self.description = description
        self.price = price
        self.hp = hp
        self.attack = attack
        self.defense = defense
