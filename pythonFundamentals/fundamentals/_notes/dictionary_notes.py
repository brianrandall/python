# #dictionaries

# from string import whitespace


# cup = {
#     'has_handle': True,
#     'color': 'white',
#     'shape': 'cylindrical', 
#     'liquidType': 'coffee'
# }

# #get something from dictionary
# print(cup['liquidType'])

# #add an item
# cup['isFull'] = False
# print(cup['isFull'])

# #replace a value (set a key value pair)
# print(cup['color'])
# cup['color'] = 'pink'
# print(cup['color'])

# #remove an item
# del cup['color']
# cup.pop('liquidType')
# cup.clear()

# print(cup)

momCup = {
    'name': 'mom cup',
    'has_handle': True,
    'color': 'white',
    'shape': 'cylindrical', 
    'liquidType': 'coffee'
}

dadCup = {
    'name': 'dad cup',
    'has_handle': False,
    'color': 'black',
    'shape': 'square', 
    'liquidType': 'beer'
}

listCups = []
listCups.append(momCup)
listCups.append(dadCup)

#print value of dictionary 1, value of "has_handle"
print(listCups[1]['has_handle'])


