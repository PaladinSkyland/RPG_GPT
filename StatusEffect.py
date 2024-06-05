class StatusEffect:
    def __init__(self, name, description, duration, negative, attack=0, defense=0, hp=0):
        self.name = name
        self.description = description
        self.duration = duration
        self.negative = negative
        self.attack = attack
        self.defense = defense
        self.hp = hp


    def apply_effect(self, target):
        self.effect(target)

    def __str__(self):
        return self.name