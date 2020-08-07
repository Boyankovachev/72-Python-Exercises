# Define a class named American which has a static method called printNationality.


class American(object):
    def __init__(self):
        self.nationality = "American"

    def printNationality(self):
        print(self.nationality)

anAmerican = American()
anAmerican.printNationality()
