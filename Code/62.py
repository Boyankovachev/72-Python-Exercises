# By using list comprehension, please write a program
# generate a 358 3D array whose each element is 0.


new_list = [[[]]]
for x in range(3):
    new_list.append([])
    for y in range(5):
        new_list[x].append([])
        for z in range(8):
            new_list[x][y].append(0)

print(new_list)
