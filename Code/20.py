# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

class MyClass:
    @staticmethod
    def function(n):
        my_list = []
        for x in range(0, n):
            if x % 7 == 0:
                my_list.append(x)
        return my_list


class_instance = MyClass()
print(class_instance.function(100))
