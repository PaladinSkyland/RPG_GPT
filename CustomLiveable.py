class CustomLiveable:
    def __init__(self):
        self.data = ""

    def __rich__(self):
        return self.data
