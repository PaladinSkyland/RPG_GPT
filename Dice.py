# RPG Game with chatGPT
# Class for dice
import random

class Dice_roller:
    def __init__(self):
        pass

    def roll_dice(self, sides):
        return random.randint(1, sides)

    def roll(self, string):
        # Split the string into a list of strings
        # Each string should be in the format 'NdM'
        # Where N is the number of dice to roll
        # And M is the number of sides on the dice
        dice = string.split('d')
        # Convert the strings to integers
        num_dice = int(dice[0])
        num_sides = int(dice[1])
        # Roll the dice
        rolls = [self.roll_dice(num_sides) for _ in range(num_dice)]
        # Return the rolls
        return rolls
    
    def roll_sum(self, string):
        return sum(self.roll(string))