# Write a program which accepts a sequence of words separated by whitespace
# as input to print the words composed of digits only.
# Example: If the following words is given as input to the program:
# 2 cats and 3 dogs.
# Then, the output of the program should be:
# ['2', '3']
# In case of input data being supplied to the question, it should be assumed to be a console input.

print("Input a sentence: ", end="")
user_input = input()
input_list = user_input.split(" ")
result_list = []
for item in input_list:
    flag = True
    for char in item:
        if char <= '0' or char >= '9':
            flag = False
    if flag:
        result_list.append(item)

print(result_list)
