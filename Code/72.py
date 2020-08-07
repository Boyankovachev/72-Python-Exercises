# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits
# in a farm. How many rabbits and how many chickens do we have?

heads = 35
legs = 94
chickens = 0
rabbits = 0
flag = False
while not flag:
    for x in range(35):
        if(flag == True):
            break
        rabbits = x
        for y in range(35 - x):
            chickens = y
            if rabbits*4 + chickens*2 == legs:
                flag = True
                break

print(rabbits, chickens)
