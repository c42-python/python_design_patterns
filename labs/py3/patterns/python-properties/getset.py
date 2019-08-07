class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return self.first + " " + self.last

    @full_name.setter
    def full_name(self, value):
        first, last = value.split(" ")
        self.first = first
        self.last = last

guy = Person("Joe", "Smith")
print(guy.full_name)
guy.full_name = "Sam Jones"
print(guy.last + ", " + guy.first)