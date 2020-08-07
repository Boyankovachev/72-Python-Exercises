# Please write a program which accepts a string from console and print the
# characters that have even indexes.
# Example: If the following string is given as input to the program:
# H1e2l3l4o5w6o7r8l9d
# Then, the output of the program should be:
# Helloworld

print("Input a string: ", end="")
user_input = input()
new_string = ""
for x in range(len(user_input)):
    if(x%2!=0):
        new_string = new_string + user_input[x]

print(new_string)