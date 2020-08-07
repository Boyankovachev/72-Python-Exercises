# Write a program to compute 1/2+2/3+3/4+...+n/n+1
# with a given n input by console (n>0).
# Example: If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 3.55
# In case of input data being supplied to the question,
# it should be assumed to be a console input.


def compute(n):
    total = 0.0
    for x in range(0, n+1):
        total = total + float(x/(x+1))
    return total


while True:
    print("Input a number: ", end="")
    num = int(input())
    if num > 0:
        break

print(compute(num))
