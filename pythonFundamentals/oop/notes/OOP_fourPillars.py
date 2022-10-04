class Chair:
    def __init__ (self, material, fabric_type, num_of_legs, color, size):
        self.material = material
        self.fabric_type = fabric_type
        self.num_of_legs = num_of_legs
        self.color = color
        self.size = size
        self.in_use = False

    def info(self):
        print()
        print(f'material: {self.material}')
        print(f'num_of_legs: {self.num_of_legs}')
        print(f'color: {self.color}')
        print(f'size: {self.size}')
        print()
        return self

    def toggle_in_use(self):
        if self.in_use:
            self.in_use = False
        else:
            self.in_use = True
        return self

class OfficeChair(Chair):
    def __init__(self, material='plastic', fabric_type='leather', num_of_legs='5', color='black', size='med'):
        super().__init__(material, fabric_type, num_of_legs, color, size)

    def toggle_reclining(self):
        if self.is_reclining:
            self.is_reclining = False
        else:
            self.is_reclining = True
        return self
    def info(self):
        super().info()
        print(f'is_reclining: {self.is_reclining}')

class GamingChair(OfficeChair):
    def __init__(self, material='metal', fabric_type='leather', num_of_legs='5', color='black', size='large'):
        super.__init__(material, fabric_type, num_of_legs, color, size)

chair1 = Chair(material='metal', fabric_type='leather', num_of_legs=2, color='brown', size='exxxtra large')

oc = OfficeChair()
oc.toggle_in_use()
oc.info()

gc = GamingChair()
gc.info()