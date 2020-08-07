# Define a class which has at least two methods: getString: to get a string
# from console input printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class Test:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        print("Input string: ", end="")
        self.input_string = input()

    def printString(self):
        self.input_string = self.input_string.upper()
        print(self.input_string)


test = Test()
test.getString()
test.printString()
