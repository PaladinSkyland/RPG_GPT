# RPG Game with chatGPT
# Class for environment and context

class Environment: 
    def __init__(self, location = 'Environment', difficulty = 0 , description = '', objects_in_range = []):
        self.locationname = location
        self.difficulty = difficulty
        self.description = description
        self.objects_in_range = objects_in_range


class Context:
    def __init__(self, player = None, environment = None):
        self.player = player
        self.environment = environment

    def get_player(self):
        return self.player

    def get_environment(self):
        return self.environment

    def set_player(self, player):
        self.player = player

    def set_environment(self, environment):
        self.environment = environment