# import re

def calculate_structure_sum(*args) -> int:
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
