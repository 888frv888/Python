# target = """Задание: Декораторы в Python
# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
# Задание:
# Напишите 2 функции:
#     Функция, которая складывает 3 числа (sum_three)
#     Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции
#     будет простым числом и "Составное" в противном случае.
# Пример:
# result = sum_three(2, 3, 6)
# print(result)
# Результат консоли:
# Простое
# 11
# Примечания:
#     Не забудьте написать внутреннюю функцию wrapper в is_prime
#     Функция is_prime должна возвращать wrapper
#     @is_prime - декоратор для функции sum_three"""

def is_prime(func):
	def wrapper(*args):
		func_result = func(*args)
		is_prime_number = True
		for i in range(2, func_result):
			if func_result % i == 0:
				is_prime_number = False
				break
		if is_prime_number:
			print("Простое")
		else:
			print("Составное")
		return func_result

	return wrapper


@is_prime
def sum_three(a: int, b: int, c: int) -> int:
	"""
	Function summ tree numbers a, b and c
	:param a:
	:param b:
	:param c:
	:return: int
	"""
	return sum((a, b, c))


if __name__ == '__main__':
	result = sum_three(2, 3, 6)
	print(result)
