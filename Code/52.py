# Please write a program which accepts basic mathematic expression
# from console and print the evaluation result.
# Example: If the following string is given as input to the program:
# 35+3
# Then, the output of the program should be:
# 38


class InputError(Exception):
    def __init__(self, msg):
        self.msg = msg


print("Enter mathematic equation: ", end="")
user_input = input()
if user_input.count("+") > 0:
    list_input = user_input.split("+")
    result = float(list_input[0]) + float(list_input[1])
elif user_input.count("-") > 0:
    list_input = user_input.split("-")
    result = float(list_input[0]) - float(list_input[1])
elif user_input.count("*") > 0:
    list_input = user_input.split("*")
    result = float(list_input[0]) * float(list_input[1])
elif user_input.count("/") > 0:
    list_input = user_input.split("/")
    result = float(list_input[0]) / float(list_input[1])
else:
    raise InputError("Wrong Input")

print(result)