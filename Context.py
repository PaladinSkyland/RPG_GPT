# RPG Game with chatGPT
# Class for environment and context

class Environment: 
    def __init__(self, difficulty = 0 , description = '', objects_in_range = []):
        self.difficulty = difficulty
        self.description = description
        self.objects_in_range = objects_in_range

class Context:
    def __init__(self):
        self.environment = Environment()
        self.actions = []
        self.choosen_action = None
        self.results_command = []

    def set_context_from_json(self, json):
        self.environment.description = json['for_player']['Description']
        for index, action in enumerate(json['for_player']['Possible Actions']):
            self.add_action(action, json['for_game_master']['Possible Actions Description'][index])

    def add_action(self, title, description):
        self.actions.append((title, description))

    def choose_action(self, index):
        self.choosen_action = self.actions[index]