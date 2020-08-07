#Calculates the factoriel of a given number

print("Input number: ", end=" ")
n = int(input())
total = 1
if(n<0):
    total = 0
for x in range(1, n+1):
    total = x * total
print(total)
