class Enemy:
    def __init__(self, name, health, attack, defense, xp, gold):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.xp = xp
        self.gold = gold
        self.statuseffect = {}

    def take_damage(self, damage):
        self.health -= damage

    def attack_target(self, target):
        damage = max(0, self.attack - target.get_defense())
        target.take_damage(damage)
        return damage
    
    def is_alive(self):
        return self.health > 0

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
