def my_max(spisok: list) -> int:
	maximum = spisok[0]
	for element in spisok:
		if element > maximum: maximum = element
	return maximum

def even_counter(spisok: list[int]) -> int:
	counter: int = 0
	for element in spisok:
		if element % 2 == 0: counter += 1
	return counter

def my_unique_finder(spisok: list) -> list:
	unique_list: list = []
	for element in spisok:
		if element not in unique_list: unique_list.append(element)
	return unique_list

if __name__ == '__main__':
	test_list: list = [1, 345, 6424, 1, 345]
	print('Тестовый список: ', test_list)
	print('Максимальное число в списке: ', my_max(test_list))
	print('Количество четных чисел в списке: ', even_counter(test_list))
	print('Уникальные элементы в списке: ', my_unique_finder(test_list))