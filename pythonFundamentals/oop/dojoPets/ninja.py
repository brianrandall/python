from petClass import Pet

class Ninja:
    def __init__ (self, firstName, lastName, pet, treats, petFood):
        self.firstName = firstName
        self.lastName =lastName
        self.pet = pet
        self.treats = treats
        self.petFood = petFood
    
    def walk(self):
        self.pet.play()
        return self
    def feed(self):

        self.pet.eat()

        return self
    def bathe(self):
        self.pet.noise()
        return self

brian = Ninja('brian', 'randall', 'dog', 'burritos', 'pizza')
brian.walk().feed().bathe()