class InputOutputString:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input()

    def print_string(self):
        print(self.string.upper())

my_string = InputOutputString()
my_string.get_string()
my_string.print_string()
