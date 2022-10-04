#what is a function?

#a set of instructions
#we don't have to repeat text, just re call function
#DRY -> DO NOT REPEAT YOURSELF


from os import dup


momCup = {
    'name': 'mom cup',
    'has_handle': True,
    'color': 'white',
    'shape': 'cylindrical', 
    'liquidType': 'coffee'
}

#use def

def add(a, b):
    return a + b

def info(dict):
    for key in dict:
        print(f"key: {key} - value {dict[key]}")
    return dict

print(info(momCup))        

print(add(5, 6))

tuple = ('tyler', 'joe')
print(tuple)
