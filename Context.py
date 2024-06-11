# RPG Game with chatGPT
# Class for environment and context
from Enemy import Enemy


class Environment: 
    def __init__(self, difficulty = 0 , description = '', objects_in_range = []):
        self.difficulty = difficulty
        self.description = description
        self.previous_description = ""
        self.objects_in_range = objects_in_range

class Context:
    def __init__(self):
        self.environment = Environment()
        self.actions = []
        self.choosen_action = None
        self.previous_action = None
        self.results_command = []
        self.enemy = None
        self.fight_actions = [                            
            {'title': 'attack', 'icon': ':crossed_swords:', 'description': 'Attack the enemy'},
            {'title': 'defend', 'icon': ':shield:', 'description': 'Block the next attack'},
            {'title': 'heal', 'icon': ':pill:', 'description': 'Heal yourself, but be careful, the enemy can attack you while you are healing!'},
            {'title': 'run', 'icon': ':running:', 'description': 'Try to run away from the enemy, but be careful, you can get hurt!'}
        ]


    def set_context_from_json(self, json, mode):
        self.environment.previous_description = self.environment.description
        self.environment.description = json['description']
        self.actions = []
        if mode == "story":
            for action in json['possible_actions']:
                self.add_action(action)
            self.enemy = None
        else:
            self.enemy = Enemy(json['enemy']['name'], int(json['enemy']['health']), int(json['enemy']['attack']), int(json['enemy']['defense']), int(json['enemy']['experience']), int(json['enemy']['gold']))
            self.actions = self.fight_actions

    def add_action(self, action):
        if len(action["icon"]) > 1:
            action["icon"] = action["icon"].strip()[0]
        if len(action["icon"].encode('utf-8')) < 3:
            action["icon"] = ""
        self.actions.append({'title': action["title"].strip(), 'description': action["description"].strip(), 'icon': action["icon"].strip(), 'command': action["command"].strip()})

    def choose_action(self, index):
        self.previous_action = self.choosen_action
        self.choosen_action = self.actions[index]