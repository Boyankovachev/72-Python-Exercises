# Please write a program which prints all permutations of [1,2,3]


my_list = [1,2,3]
for x in range(3):
    for y in range(3):
        for z in range(3):
            print(str(my_list[x]) + str(my_list[y]) + str(my_list[z]))
