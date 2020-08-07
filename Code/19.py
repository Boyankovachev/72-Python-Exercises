# You are required to write a program to sort the (name, age, height) tuples by ascending
# order where name is string, age and height are numbers. The tuples are input by console.
# The sort criteria is: 1: Sort based on name; 2: Then sort based on age; 3: Then sort by score.
# The priority is that name > age > score. If the following tuples are given as input to the program:
# Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 Then, the output of the program should be: \
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
# from typing import List

def sort_tuples(sort_list):
    for j in range(0, 3):
        for k in range(0, len(sort_list) - 1):
            for i in range(0, len(sort_list) - 1):
                if sort_list[i][j] > sort_list[i + 1][j]:
                    temp = sort_list[i]
                    sort_list[i] = sort_list[i + 1]
                    sort_list[i + 1] = temp
    return sort_list


my_list = []
while True:
    user_input = input()
    if not user_input:
        break
    my_list.append(tuple(user_input.split(",")))

sort_tuples(my_list)
print(my_list)
