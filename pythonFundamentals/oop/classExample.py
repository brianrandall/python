#define class name
class shoe1:
#attributes
    def __init__(self):
        self.brand = 'adidas'
        self.type = 'tennis shoe'
        self.price = '$45.99'
        self.in_stock = True
#methods
    #update shoe brand name
    def rebrand (self, newBrand):
        self.brand = newBrand
    #sold out - changes stock status to "false"
    def soldOut(self):
        self.in_stock = False
    #on sale - decreases price by a percentage
    def onSale(self, percent):
        self.price = self.price * (1 - percent)

shoeAdidas = shoe1()
print(shoeAdidas.price)

class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    	# we assign them accordingly
        self.brand = brand
        self.type = shoe_type
    	self.price = price
    	# the status is set to True by default
        self.in_stock = True
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.type)	# output: Low-top Trainers
print(dress_shoe.type)	# output: Ballet Flats

#calling methods
class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
    # adding the greeting method
    def greeting(self):
    	print(f"Hello, my name is {self.name}")

adrien = User("Adrien", "adion@codingdojo.com")
cool_person = User("Sadie", "sflick@codingdojo.com")
    
adrien.greeting()
# prints Hello, my name is Adrien
    
cool_person.greeting()
# prints Hello, my name is Sadie