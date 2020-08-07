# Write a program which can map() to make a list whose
# elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

def square(num):
    return num*num

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = map(square, my_list)
for item in new_list:
    print(item, end=" ")
