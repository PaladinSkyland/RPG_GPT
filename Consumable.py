class Consumable:
    def __init__(self, name, description, price, exp=0, hp=0, attack=0, defense=0, status=None, clear_status=False):
        self.name = name
        self.description = description
        price = price
        self.exp = exp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.status = status
        self.clear_status = clear_status

    def use(self, player):
        player.add_exp(self.exp)
        player.add_hp(self.hp)
        player.add_attack(self.attack)
        player.add_defense(self.defense)
        if self.status:
            player.add_status(self.status)
        if self.clear_status:
            player.clear_status()