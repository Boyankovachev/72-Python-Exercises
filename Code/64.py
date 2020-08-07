# By using list comprehension, please write a program to
# print the list after removing the value 24 in [12,24,35,24,88,120,155].


old_list = [12, 24, 35, 70, 88, 120, 155]
new_list = []
for i in range(len(old_list)):
    if old_list[i] != 24:
        new_list.append(old_list[i])

print(new_list)