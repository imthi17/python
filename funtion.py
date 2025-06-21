# Class definition
class Pet:
    # Constructor method (encapsulation of data)
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

    # Method (behavior)
    def speak(self):
        if self.animal_type.lower() == "dog":
            return f"{self.name} says: Woof!"
        elif self.animal_type.lower() == "cat":
            return f"{self.name} says: Meow!"
        else:
            return f"{self.name} makes a sound!"

# Function that uses the class
def main():
    # Creating (instantiating) objects
    pet1 = Pet("Buddy", "Dog")
    pet2 = Pet("Whiskers", "Cat")
    pet3 = Pet("Luna", "Parrot")

    # Calling methods
    print(pet1.speak())
    print(pet2.speak())
    print(pet3.speak())

# Run the function
main()



