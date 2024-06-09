from rich.live import Live
from CustomLiveable import CustomLiveable
from Player import Player
from Enemy import Enemy
from Item import Item
from StatusEffect import StatusEffect
from Consumable import Consumable
from KeyboardInput import KeybordInput

# create an instance of the custom liveable class
console = CustomLiveable()

with Live(console, refresh_per_second=10) as live, KeybordInput() as input:
    while True:
        key = input.getkey()
        if key == 'escape':
            break
        console.key_pressed(key)
