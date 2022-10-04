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

class Pet:
    def __init__ (self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f'{self.name} has had a food. health has increased to {self.health} and energy has increased to {self.energy}. maybe he will want to play now? doubt it.. ')
    def play(self):
        self.health += 10
        print(f'{self.name} does not want to play anymore. he is tired. health increased to {self.health}')  
    def noise(self):
        print(f'we have given {self.name} a bath.. finally. he was not happy about it')
        print('"AAWWAGGGGGWHHHGFFGHH.... i liked being stinky........."')

petDog = Pet('larry', 'dog', 'sleeping')
brian = Ninja('brian', 'randall', petDog, 'burritos', 'pizza')

brian.walk().feed().bathe()