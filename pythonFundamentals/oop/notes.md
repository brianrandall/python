# OOP
'object oriented programming'

what is an object?
- house
- car
- shoe
- computer
- etc... 


## class
- a class is like a `blueprint`

what is a blueprint? -> specifications on what a structure will be like

## constructor
`the crew that comes in and builds the house, leaving you with the final product`

### def \_\__init__() -> method
dunder init = double underscore initialize

aka "magic method"


what is a `method` ?
- a function inside of a class

## attributes
`the details about what make up a class ("object")`

```py
class house:
    def __init__(self):
        self.numFloors = 2
        self.numBathrooms = 2.5
        self.isFrontDoorOpen = False
```

## method
`functions inside of a class, things that the class can do, behaiviors for class`
<br><br><br><br>

## example
```py
class Person:
    def __innit__(self, height, hairColor, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.height = height
        self.hairColor = hairColor
        self.age
p1 = Person(firstName='brian', lastName='randall', height='5ft7', hairColor='brown', 
age='32')
# pascal case (each word, first letter uppercase)
class Laptop:
    creator = 'brian'
    def __init__(self, brand, screenSize, color, gpu, hdSize, ram, hasWebcam):
        self.brand = brand
        self.screenSize = screenSize
        self.color = color
        self.gpu = gpu
        self.hdSize = hdSize
        self.ram = ram
        self.hasWebcam = hasWebcam
        self.isOn = False
        self.timesTurnedOn = 0
        #(default value is False, doesn't need anything to be passed to it)
    
    #methods are the functions that can be taken upon a class
    #function to "turn on" laptop
    def turnOn(self):
        if self.timesTurnedOn == 0
            print("Welcome, this is the first time I am running")
        self.timesTurnedOn += 1
        self.isOn = True
        #currently returning "none" -- needs to return "self
        #in order to be able to chain
        return self

    def turnOff(self):
        self.isOn = False
        return self

    def info(self):
        print(f"brand: {self.brand}")
        print(f"screenSize: {self.screenSize}")
        print(f"color: {self.color}")
        print(f"gpu: {self.gpu}")
        print(f"hdSize: {self.hdSize}")
        print(f"ram: {self.ram}")
        print(f"has webcam: {self.hasWebcam}")
        print(f"on?: {self.isOn}")
        print(f"times turned on: {self.timesTurnedOn}")
    #class method example
    @classmethod
    def change_creator(cls, who):
        cls.creator = who
        return cls
    


laptop1 = Laptop('Dell', 15, 'black', '3080ti', '1tb', '16gb', True )
laptop2 = Laptop('ASUS', 14, 'black', '1650ti', '512gb', '8gb', False )

print(laptop1.gpu)
laptop1(info)
#etc

#chaining example
laptop1.turnOn().turnOff()

#do class method stuff
Laptop.change_creator('dave')

```        

## chaining
`connecting multiple methods together on a single line`

how?
- make sure we are always returning "self" on every normal method.
- every method in a class should "return self"

## class methods
- the focus is the entire class
- normal methods focus on specific instances of class (self)
- in this case, class is "laptop"
