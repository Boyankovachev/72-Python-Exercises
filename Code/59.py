# Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

my_list = [5, 6, 77, 45, 22, 12, 24]
for item in my_list:
    if item % 2 == 0:
        my_list.remove(item)
print(my_list)
