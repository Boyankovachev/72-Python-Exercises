# Define a class, which have a class parameter and have a same instance parameter.

class Person:
    def __init__(self, name="Ivan40"):
        self.name = name


ivan = Person()
martin = Person("Martin")
print(ivan.name, martin.name)
