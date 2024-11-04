def print_params(a = 1, b = 'строка', c = True):
	print(a, b, c)

values_list = [5, True, 'String']
values_dict = {'a':'Bilbo', 'b':125, 'c':'Beggins'}
values_list_2 = [54.32, 'Строка']

print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*values_list)
# print_params(*values_dict)							 # распаковка словаря по ключам
print_params(**values_dict)								# распаковка словаря по значениям
print_params(*values_list_2, 42)
