

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 
    'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# #part 1
# #1
x[1][0] = 15
# print(x)
# #2
students[0]['last_name'] = 'Bryant'
print(students)
# #3
sports_directory['soccer'][0] = 'Andres'
print(sports_directory) 
# #4
z[0]['y'] = 30
print(z)

#part 2

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for dict in students:
        name = []
        for key in dict:
            name.append(f"{key} - {dict[key]}")
        print(f"{name[0]}, {name[1]}")
iterateDictionary(students)

#part 3
def iterateDictionary2(key_name, some_list):
    for dict in some_list:
        if key_name in dict:
            print(dict[key_name])
        else:
            print("not a thing")
            break
iterateDictionary2('first_name', students)

#part 4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(f"\n{len(some_dict[key])} {(key).upper()}")
        for val in some_dict[key]:
            print(val)
printInfo(dojo)