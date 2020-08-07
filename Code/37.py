# Define a class named American and its subclass NewYorker.


class American:
    def __init__(self, name):
        self.name = name


class NewYorker(American):
    def __init__(self, name, hood):
        super().__init__(name)
        self.hood = hood

    def print_name_and_hood(self):
        print(self.name, self.hood)


Mike = NewYorker("Mike", "Jersey")
Mike.print_name_and_hood()
