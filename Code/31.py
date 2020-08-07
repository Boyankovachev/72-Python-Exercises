# Define a function that can accept an integer number as input and print the
# "It is an even number" if the number is even, otherwise print "It is an odd number


def even_or_odd(num):
    if (num % 2 == 0):
        print("Integer is even")
    elif num % 2 != 0:
        print("Integer is odd")


print("Enter and integer")
num = int(input())
even_or_odd(num)
