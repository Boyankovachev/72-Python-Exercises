# By using list comprehension, please write a program to print the list
# after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

old_list = [12,24,35,70,88,120,155]
new_list = []

for item in old_list:
    if old_list.index(item) % 2 != 0:
        new_list.append(item)

print(new_list)