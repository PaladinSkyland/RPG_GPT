class Enemy:
    def __init__(self, name, health, attack, defense, xp, gold):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.xp = xp
        self.gold = gold

    def take_damage(self, damage):
        self.health -= damage

    def attack_target(self, target):
        target.take_damage(self.attack)
    
    def is_alive(self):
        return self.health > 0
