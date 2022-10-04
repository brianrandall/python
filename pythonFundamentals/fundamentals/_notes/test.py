from typing import Concatenate

firstName = "brian"
lastName = "randall"
age = 32


print("hi my name is %s %s and i am %d years old" % (firstName, lastName, age))

print("hi my name is {} {} and i am {} years old" .format(firstName, lastName, age))

print(f"hi my name is {firstName} {lastName} and i am {age} years old")

# //Concatenate string + number
print(firstName + str(age))

