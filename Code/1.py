#All numbers divisible by 7 and not multiple of 5, between 2000 and 3200

l = []
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        l.append(num)
for item in l:
    print(str(item) + ', ', end=" ")
print()