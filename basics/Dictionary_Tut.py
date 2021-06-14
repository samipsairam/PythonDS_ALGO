# Dictionary is another data structure which in other language is called as 'HashTable' or 'Map' or 'Object' in another language
# Dictionary or dict is a data type or data structure itself
# Have KV pairs
# Dictionary is unordered Key-Value pairs, Unlike List they are not ordered hence cannot be get by index
dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}

print(dictionary['a'])
print(dictionary['a'][1])

# list of dict
my_list = [
    {
        'a': [1, 2, 3],
        'b': 'Hello',
        'c': True
    },
    {
        'a': [4, 5, 6],
        'b': 'World',
        'c': False
    }
]
print(my_list[0]['a'][2])

'''
LIST vs DICT use:
orderd => list, unorderd => dict 
more_information => dict
'''

# Dictionary Keys
# Keys shouldn't be Immutable
# Keys should be unique else it would override the old assignement
dict1 = {
    123: [1, 2, 3],
    True: 'Hello',
    'grey': True             # keys should be immutable so gives 'Unhashable TypeError'
}
print(dict1)

user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'height': 5.2
}
print(user.get('age'))    # give None if no age key exists
print(user.get('name','DEMOIN'))   # adds default value if name key doesnot exists
print(user.get('height',0.0))

# user2 = dict(name = 'JohnHon')

# finding item in dict
print('basket' in user)
print('size' in user)
print('greet' in user.keys())
print('hello' in user.values())
print(user.items())

user2 = user.copy()
print(user2)
user.clear()
print(user)
print(user2)

print(user2.pop('greet'))
print(user2)

user2.update({'age':55})
print(user2)