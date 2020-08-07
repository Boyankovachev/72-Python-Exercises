# Please write a program using generator to print the even numbers
# between 0 and n in comma separated form while n is input by console.
# Example: If the following n is given as input to the program:
# 10
# Then, the output of the program should be:
# 0,2,4,6,8,10


def gen(n):
    i = 0
    while i < n + 1:
        if i % 2 == 0:
            yield i
        i += 1


while True:
    print("Input a number: ", end="")
    num = int(input())
    if num > 0:
        break
s = []
for item in gen(num):
    s.append(str(item))

print(",".join(s))

