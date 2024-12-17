def apply_all_func(int_list: list[int | float], *functions) -> dict:
	"""Функция обрабатывает список чисел различными функциями"""
	result = dict()
	for func in functions:
		result[func.__name__] = func(int_list)
	return result


if __name__ == '__main__':
	print(apply_all_func([6, 20, 15, 9], max, min))
	print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
