#variable declaration
num1 = 42
num2 = 2.3 
#boolean
boolean = True
#strings
string = 'Hello World'

#lists
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#tuples
fruit = ('blueberry', 'strawberry', 'banana')

#log statement
print(type(fruit))
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])

#conditionals

#if statement
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: #length check
    print("It's a short word!")
#else if
elif len(string) > 15:
    print("It's a long word!")
#else 
else:
    print("Just right!")
#for loop

#range 0 - < 5
for x in range(5):
    print(x)
    #range 2 - < 5
for x in range(2,5):
    print(x)
    #start, #stop #increment by 3
for x in range(2,10,3):
    print(x)
x = 0
#while loop
while(x < 5):
    print(x)
    x += 1

#list

#initialize
pizza_toppings.pop()
#access value(1)
pizza_toppings.pop(1)

#dictionaries
print(person)
person.pop('eye_color') #add value
print(person)

#dictionaries

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

#define function
def print_hello_ten_times():
    for num in range(10):
        print('Hello')
#call function
print_hello_ten_times()

def print_hello_x_times(x): #argument
    for num in range(x): #parameter
        print('Hello') #return

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)