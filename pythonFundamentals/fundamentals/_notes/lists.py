groceryList = ['apples', 'eggs', 'coffee', 'meat']
#how do we interact with a list?
#name_of_list[idex of value]

#to get an item
print(groceryList[2])
#add to a list
groceryList.append("noodles")
print(groceryList)

#remove last item from a list
groceryList.pop()
print(groceryList)

#remove specific item from list
item = groceryList.pop(2)
print(groceryList)
print(item)

#last item in list
print(groceryList[-1])

#change values
groceryList[1] = "potatoes"
print(groceryList)



#etc - more on learn platform
