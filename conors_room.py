class ConorRoom:
    def __init__(self, key):
        self.key = key
        self.riddle_correct = False

    def check_out(self):
        print("Hello traveler!")

    def entrance(self):
        print("welcome to the beach \n the ocean is a powerful and mysterious creature")

    def play(self):
        # This is the first function called.
        self.key += 1
        print(self.key)
