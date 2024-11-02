def calculate_structure_sum(*args) -> int:
	counter: int = 0
	for element in args:
		if isinstance(element, int):
			counter += element
		elif isinstance(element, str):
			counter += len(element)
		elif isinstance(element, list):
			counter += calculate_structure_sum(*element)
		elif isinstance(element, tuple):
			counter += calculate_structure_sum(*element)
		elif isinstance(element, dict):
			counter += calculate_structure_sum(tuple(element.items()))
		elif isinstance(element, set):
			counter += calculate_structure_sum(tuple(element))
	return counter


data_structure = [

	[1, 2, 3],

	{'a': 4, 'b': 5},

	(6, {'cube': 7, 'drum': 8}),

	"Hello",

	((), [{(2, 'Urban', ('Urban2', 35))}])

]


if __name__ == '__main__':
	result: int = calculate_structure_sum(data_structure)
	print(result)
