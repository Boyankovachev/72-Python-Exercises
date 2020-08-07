# Define a custom exception class which takes a string message as attribute.

class MyException(Exception):
    def __init__(self, str):
        self.msg = str


error = MyException("something is wrong")
raise error
