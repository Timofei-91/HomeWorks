my_dict = {'Тимофей': 1991, 'Никита': 1993, 'Вероника': 1997}
print(my_dict)
print(my_dict['Тимофей'],'Года рождения')
print(my_dict.get('Евгений', 'Такого имени нет'))
my_dict.update({'Ярик': 2004, 'Андрей': 1964})
print(my_dict)
my_dict.pop('Никита')
print(my_dict)
my_set = {1,2,3,4,1,3,3, "String", (12,3,52), True, 2.23}
print(my_set)
my_set.add(82)
my_set.add('Str')
print(my_set)

