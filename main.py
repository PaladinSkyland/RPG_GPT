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

class Main :
    def __init__(self):
        self.player = Player("yoyo53")
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

        self.header_messages = [self.openai.system_message(whoareu['prompt']), self.openai.user_message(IntroductionRPG['prompt'])] # This message is sent to the AI to start the conversation, it defines the rules.
    
    def start(self):
        is_running = True
        while True:
            with Live(self.console, refresh_per_second=10) as live, KeyboardInput() as input:
                if self.context.choosen_action:
                    messages = self.header_messages + [self.openai.system_message(self.context.environment.description), self.openai.user_message(self.context.choosen_action["title"])]
                else:
                    messages = self.header_messages
                response = self.openai.return_completion(messages)
                print(response)
                self.context.set_context_from_json(json.loads(response))
                if len(self.context.actions) == 0:
                    continue
                self.console.title = "Story time! :fire:"
                self.console.description = self.context.environment.description
                self.console.actions = self.context.actions
                self.console.input = ''
                while True:
                    key = input.getkey()
                    if key == 'escape':
                        is_running = False
                        break
                    if key == 'return':
                        break
                    self.console.key_pressed(key)
                if not is_running:
                    break
                choosen_action = int(self.console.input) - 1
                self.context.choose_action(choosen_action)
                self.console.previous_action = self.context.choosen_action["description"]

if __name__ == "__main__":
    main = Main()
    main.start()
