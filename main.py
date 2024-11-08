# our Cat Entity
#Constructor creates an instance of a class
class Cat:
    def __init__(self,given_name,given_colour):
        self.name=given_name
        self.colour= given_colour
# An instance of a cat
# An instance is a specific occurence of a class

mimi= Cat("Mimi","Brown")
print(mimi.name)