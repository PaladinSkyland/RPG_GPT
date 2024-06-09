import json
from OpenAI import OpenAIclass
from Player import Player
from Context import Context

class Main :
    def __init__(self):
        self.player = Player()
        self.context = Context()
        self.openai = OpenAIclass()

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
        # Start the conversation
        response = self.openai.return_completion(self.header_messages)
        print(response)
        self.context.set_context_from_json(json.loads(response))
        print(self.context.environment.description)
        print("Possible Actions : ")
        for index, action in enumerate(self.context.actions):
            print(index + 1, "for", action["title"])
        choosen_action = int(input("Choose an action : ")) - 1
        self.context.choose_action(choosen_action)
        while True:
            print(self.context.choosen_action)
            messages = self.header_messages + [self.openai.user_message(self.context.choosen_action["title"]), self.openai.system_message(self.context.choosen_action["description"])]
            print(messages)
            response = self.openai.return_completion(messages)
            self.context.set_context_from_json(json.loads(response))
            print(self.context.environment.description)
            print("Possible Actions : ")
            for index, action in enumerate(self.context.actions):
                print(index + 1, "for", action[0])
            choosen_action = int(input("Choose an action : ")) - 1
            self.context.choose_action(choosen_action)
        
        
        



# Start the game
main = Main()
main.start()
