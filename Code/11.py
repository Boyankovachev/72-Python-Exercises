# Write a program which accepts a sequence of comma separated 4 digit binary numbers
# as its input and then check whether they are divisible by 5 or not. The numbers
# that are divisible by 5 are to be printed in a comma separated sequence. Example:
# 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.

print("Input the thing stated up there too lazy to ready dfq")
user_input = input()
input_list = user_input.split(",")
sorted_list = []
for item in input_list:
    if int(item)%5 == 0:
        sorted_list.append(item)
print(sorted_list)