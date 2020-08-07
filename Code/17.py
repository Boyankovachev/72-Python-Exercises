# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following: D 100 W 200
# D means deposit while W means withdrawal. Suppose the following input is supplied to the program:
# D 300 D 300 W 200 D 100 Then, the output should be: 500

class NotEnoughFundsException(Exception):
    pass

print("Input a bank account transactions history. Example: D 500 D 500 W 200 W 600 D 500")
user_input = input()
input_list = user_input.split(" ")
total = 0
for x in range(0, len(input_list)):
    if input_list[x] == "D":
        total = total + int(input_list[x+1])
    if input_list[x] == "W":
        if int(total < int(input_list[x+1])):
            raise NotEnoughFundsException
        total = total - int(input_list[x+1])
print(total)