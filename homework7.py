my_dict = {'Artem': 1989, 'Anna': 1987, 'Anton': 1998}
print(my_dict)
print(my_dict['Artem'])
print(my_dict.get('Vasya'))
my_dict.update({'Sahsa': 1990, 'Max': 2004})
print(my_dict)
del my_dict['Max']
print(my_dict)

my_set ={'Artem', 3.14, True, 'Apple', 2, 3, 3.14, 'Artem', True}
print(my_set)
my_set.add(5)
my_set.discard(2)
print(my_set)
