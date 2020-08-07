# Write a program which can filter even numbers in a
# list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

def is_even(num):
    if (num % 2 == 0):
        return True
    else:
        return False


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = filter(is_even, my_list)
for item in new_list:
    print(item, end=" ")

