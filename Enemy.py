class Enemy:
    def __init__(self, name, health, attack, defense, xp, gold):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.xp = xp
        self.gold = gold

    def take_damage(self, damage):
        self.health -= damage

    def attack_target(self, target):
        damage = max(0, self.attack - target.get_defense())
        target.take_damage(damage)
        return damage
    
    def is_alive(self):
        return self.health > 0
