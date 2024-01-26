
class FavoriteAnimal:
    def __init__(self, arm_length, leg_length, number_of_eyes, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.number_of_eyes = number_of_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print(f"Arm Length: {self.arm_length} units")
        print(f"Leg Length: {self.leg_length} units")
        print(f"Number of Eyes: {self.number_of_eyes}")
        print("Has Tail" if self.has_tail else "Does Not Have Tail")
        print("Is Furry" if self.is_furry else "Is Not Furry")

# Example of creating an instance of FavoriteAnimal
# For example, let's assume my favorite animal is a cat
my_favorite_animal = FavoriteAnimal(arm_length=0.3, leg_length=0.4, number_of_eyes=2, has_tail=True, is_furry=True)

# Describing the physical characteristics of the favorite animal
my_favorite_animal.describe()
