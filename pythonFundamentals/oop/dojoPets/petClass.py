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
        return self
    def play(self):
        self.health += 10
        print(f'{self.name} does not want to play anymore. he is tired. health increased to {self.health}')  
        return self
    def noise(self):
        print(f'we have given {self.name} a bath.. finally. he was not happy about it')
        print('"AAWWAGGGGGWHHHGFFGHH.... i liked being stinky........."')
        return self


