from math import inf

def divide(first: int = 1, second: int = 1) -> float:
	"""
	Функция возвращает частное от деления по правилам высшей
	математики (при делении на ноль в ответе получаем бесконечность).
	:param first: Делимое. Предпочтителен тип int.
	:param second: Делитель. Предпочтителен тип int.
	:return: float. Возвращаемое частное.
	"""
	if second == 0:
		return inf
	else:
		return first / second

def main():
	pass

if __name__ == '__main__':
	main()