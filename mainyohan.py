from rich.live import Live
from CustomLiveable import CustomLiveable
from Player import Player
from Enemy import Enemy
from Item import Item
from StatusEffect import StatusEffect
from Consumable import Consumable
from KeyboardInput import KeyboardInput

player = Player('yoyo53')
goblin = Enemy('Goblin', 30, 3, 2, 30, 15)

# create an instance of the custom liveable class
console = CustomLiveable(player=player)
console.actions = [
    {'title': 'attack', 'icon': ':crossed_swords:'},
    {'title': 'defend', 'icon': ':shield:'},
    {'title': 'use item', 'icon': ':pill:'},
    {'title': 'run', 'icon': ':running:'}
]
console.title = "Battle time! :fire:"
console.description = "You are in a battle with a goblin. What will you do?"
console.enemy = goblin

with Live(console, refresh_per_second=10) as live, KeyboardInput() as input:
    while True:
        key = input.getkey()
        if key == 'escape':
            break
        console.key_pressed(key)
