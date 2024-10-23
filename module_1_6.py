my_dict: dict = {'Don': 1974, 'Mike': 1975, 'Ivan': 1976, 'Boris': 1966}
print('Содержимое словаря: ', my_dict)
print('Значение по ключу "Don": ', my_dict['Don'])
print('Значение по ключу "Olga": ', my_dict.get('Olga', 'Такого ключа нет.'))
my_dict.update({'Vera': 2000, 'Sveta': 2005})
print('Добавляем две пары: ', my_dict)
print('Извлекаем "Don" и получаем его значение: ', my_dict.pop('Don'))
print('Содержимое словаря: ', my_dict, '\n'*2)
my_set: set ={57, 'Test', True, 42.24, 57, "Test"}
print('Содержимое исходного множества: ', my_set)
my_set.update({33, 85})
# print('Содержимое добавленного множества: ', my_set)
my_set.remove("Test")
print('Содержимое изменённого множества: ', my_set)
