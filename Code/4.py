# Write a program which accepts a sequence of comma-separated numbers from console
# and generate a list and a tuple which contains every number. Suppose the following input is
# supplied to the program: 34,67,55,33,12,98 Then, the output should be:
# ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98)


print("Input a sequence of numbers, seprated by comma. Example: 12,43,64,23")
user_input = input()
my_list = user_input.split(',')
my_tuple = tuple(user_input.split(','))
print(my_list, my_tuple)
