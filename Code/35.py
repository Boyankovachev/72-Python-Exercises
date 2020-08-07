# Write a program which can map() to make a list whose
# elements are square of numbers between 1 and 20 (both included).

my_list = []
for x in range(1,21):
    my_list.append(x)

new_list = map(lambda num: num * num, my_list)
for item in new_list:
    print(item, end=" ")
