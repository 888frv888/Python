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
