def calculate_structure_sum(*args: int | str | list | tuple | dict | set ) -> int:
	"""
	!!!ВНИМАНИЕ РЕКУРСИЯ!!!
	Функция принимает параметром аргумент, в виде хаотичной структуры данных,
	суммирует все целые числа, строковые элементы измеряет и добавляет к сумме
	:param args: хаотичная структура данных (писки, кортежи, множества, словари в разных комбинациях
	:rtype: int
	:return: сумма целых чисел и длин строк
	"""
	counter: int = 0
	for element in args:
		if isinstance(element, int):
			counter += element
		elif isinstance(element, str):
			counter += len(element)
		elif isinstance(element, list | tuple | set):
			counter += calculate_structure_sum(*element)
		elif isinstance(element, dict):
			counter += calculate_structure_sum(*element.items())
	return counter


data_structure = [

	[1, 2, 3],

	{'a': 4, 'b': 5},

	(6, {'cube': 7, 'drum': 8}),

	"Hello",

	((), [{(2, 'Urban', ('Urban2', 35))}])

]

def main():
	result: int = calculate_structure_sum(data_structure)
	print(result)

if __name__ == '__main__':
	main()