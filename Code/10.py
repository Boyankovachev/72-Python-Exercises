# Write a program that accepts a sequence of whitespace separated words
# as input and prints the words after removing all duplicate words and
# sorting them alphanumerically. Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again Then, the output should be:
# again and hello makes perfect practice world

print("Input white separated words:")
user_input = input()
input_list = user_input.split(" ")
for item in input_list:
    if input_list.count(item) > 1:
        input_list.remove(item)
input_list.sort()
ready_string = ""
for item in input_list:
    ready_string = ready_string.__add__(item + " ")
print(ready_string)