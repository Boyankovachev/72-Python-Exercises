# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the
# value of a. Suppose the following input is supplied to the program: 9
# Then, the output should be: 11106

def calculate_result(num):
    flag = num
    total = 0
    for x in range(0,4):
        total = total + int(num)
        num = num + flag

    return total

print("Type in a nuber: ", end="")
user_input = input()
print(calculate_result(user_input))