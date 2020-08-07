# Please write a binary search function which searches an item
# in a sorted list. The function should return the
# index of element to be searched in the list.

def search_element(li, item):
    for x in li:
        if x == item:
            return li.index(x)


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(search_element(my_list, 5))
