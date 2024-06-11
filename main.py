from rich.live import Live
from CustomLiveable import CustomLiveable
from Player import Player
from Enemy import Enemy
from Item import Item
from StatusEffect import StatusEffect
from Consumable import Consumable
from KeyboardInput import KeyboardInput

import json
from OpenAI import OpenAIclass
from Context import Context
from random import randint

class Main :
    def __init__(self):
        self.player = Player("Player", 0, 100, 10, 1)
        self.context = Context()
        self.openai = OpenAIclass()
        self.console = CustomLiveable(self.player)

        # Read the JSON file
        with open('prompt.json') as file:
            data = json.load(file)
        self.prompts = data['prompts']

        for prompt in self.prompts:
            if prompt['name'] == 'IntroductionRPG':
                IntroductionRPG = prompt
            if prompt['name'] == 'Who are you?':
                whoareu = prompt
            if prompt['name'] == 'Context_Valor':
                Context_Valor = prompt
            if prompt['name'] == 'fight':
                self.fight = prompt

        self.header_messages = [self.openai.system_message(whoareu['prompt']), self.openai.user_message(IntroductionRPG['prompt'])] # This message is sent to the AI to start the conversation, it defines the rules.

    def start(self):
        mode = "story"
        is_running = True
        while True:
            with Live(self.console, refresh_per_second=10) as live, KeyboardInput() as input:
                if mode != "fight":
                    if self.context.choosen_action:
                        messages = self.header_messages + [self.openai.system_message("Current context: " + self.context.environment.description), self.openai.user_message("Chosen action: " + self.context.choosen_action["description"])]
                    else:
                        messages = self.header_messages
                    if mode == "story" and self.context.choosen_action and self.context.choosen_action["command"] == "fight":
                        messages += [self.openai.system_message(self.fight['prompt'])]
                        mode = "fight"
                    if mode == "win":
                        messages += [self.openai.system_message("You won the fight against the enemy!")]
                        mode = "story"
                    if mode == "runaway":
                        messages += [self.openai.system_message("You ran away from the enemy!")]
                        mode = "story"
                    response = self.openai.return_completion(messages)
                    print(response)
                    self.context.set_context_from_json(json.loads(response), mode)
                    self.console.title = f"{mode.capitalize()} time! :fire:"
                    self.console.description = self.context.environment.description
                    self.console.actions = self.context.actions
                    self.console.enemy = self.context.enemy
                self.console.input = ''
                while True:
                    key = input.getkey()
                    if key == 'escape':
                        is_running = False
                        break
                    if key == 'return' and self.console.input != '':
                        break
                    self.console.key_pressed(key)
                if not is_running:
                    break
                if mode == "fight":
                    if self.console.input == '1':
                        player_damage = self.player.attack_target(self.console.enemy)
                        if not self.console.enemy.is_alive():
                            self.player.add_exp(self.console.enemy.xp)
                            self.player.add_gold(self.console.enemy.gold)
                            self.console.title = "Story time! :fire:"
                            self.console.description = f"You defeated the enemy! You gained {player_damage} experience points and {self.console.enemy.gold} gold!"
                            self.console.actions = self.context.actions
                            self.console.enemy = None
                            mode = "win"
                        else:
                            self.console.description = f"You attacked the enemy for {player_damage} damage!"
                            enemy_damage = self.console.enemy.attack_target(self.player)
                            if not self.player.is_alive():
                                self.console.title = "Game over! :fire:"
                                self.console.description = "You died! You lost the game!"
                                self.console.actions = []
                                self.console.input = ''
                                mode = "gameover"
                            else:
                                self.console.description += f"\n{self.console.enemy.name} attacked you for {enemy_damage} damage!"
                    elif self.console.input == '2':
                        self.console.description = "You defended yourself from the enemy and blocked its attack!"
                    elif self.console.input == '3':
                        if self.player.get_gold() >= 10:
                            self.player.restore_hp(10)
                            self.player.gold -= 10
                            self.console.description = "You healed yourself for 10 HP!"
                        else:
                            self.console.description = "You don't have enough gold to heal yourself! You lost your turn!"
                        enemy_damage = self.console.enemy.attack_target(self.player)
                        if not self.player.is_alive():
                            self.console.title = "Game over! :fire:"
                            self.console.description = "You died! You lost the game!"
                            self.console.actions = []
                            self.console.input = ''
                            mode = "gameover"
                        else:
                            self.console.description += f"\n{self.console.enemy.name} attacked you for {enemy_damage} damage!"
                    elif self.console.input == '4':
                        # run
                        if randint(0, 4) == 0:
                            self.console.title = "Story time! :fire:"
                            self.console.description = "You ran away from the enemy!"
                            self.console.enemy = None
                            self.console.actions = self.context.actions
                            mode = "runaway"
                        else:
                            enemy_damage = self.console.enemy.attack_target(self.player)
                            enemy_damage += self.console.enemy.attack_target(self.player)
                            if not self.player.is_alive():
                                self.console.title = "Game over! :fire:"
                                self.console.description = "You died! You lost the game!"
                                self.console.actions = []
                                self.console.input = ''
                                mode = "gameover"
                            else:
                                self.console.description = f"You tried to run away from the enemy, but the enemy catched and made you {enemy_damage} damage!"
                    self.console.input = ''
                else:
                    choosen_action = int(self.console.input) - 1
                    self.context.choose_action(choosen_action)
                    self.console.previous_action = self.context.choosen_action["description"]

if __name__ == "__main__":
    main = Main()
    main.start()
