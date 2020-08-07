# Use a list comprehension to square each odd number in a list. The list is input
# by a sequence of comma-separated numbers. Suppose the following input is supplied
# to the program: 1,2,3,4,5,6,7,8,9 Then, the output should be: 1,3,5,7,9


print("Input a comma separeted sequence of number: ", end="")
user_input = input()
result = [str(int(x) * int(x)) for x in user_input.split(",") if (int(x) % 2 != 0)]
print(",".join(result))