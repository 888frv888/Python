# import re

def calculate_structure_sum(*args) -> int:
	"""
		Функция принимает параметром аргумент, в виде хаотичной структуры данных,
		суммирует все целые числа, строковые элементы измеряет и добавляет к сумме
		:param args: хаотичная структура данных (писки, кортежи, множества, словари в разных комбинациях
		:rtype: int
		:return: сумма целых чисел и длин строк
	"""
	string: str = str(*args)
	words: str = ''
	counter: int = 0
	for i in range(len(string)-1):
		if string[i].isalpha() or string[i].isdigit():
			words += string[i]
		else:
			words += ' '
	words_list = words.split()
	for element in words_list:
		if element.isnumeric(): counter += int(element)
		else: counter += len(element)
	return counter


data_structure = [

	[1, 2, 3],

	{'a': 4, 'b': 5},

	(6, {'cube': 7, 'drum': 8}),

	"Hello",

	((), [{(2, 'Urban', ('Urban2', 35))}])

]


if __name__ == '__main__':
	result = calculate_structure_sum(data_structure)
	print(result)
