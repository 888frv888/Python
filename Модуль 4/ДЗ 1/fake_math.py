def divide(first: int = 1, second: int = 1) -> float:
	"""
	Функция возвращает частное от деления по школьным правилам (на ноль делить нельзя).
	:param first: Делимое. Предпочтителен тип int.
	:param second: Делитель. Предпочтителен тип int. В случае присвоения нуля возвращает str 'Ошибка'
	:return: float. Возвращаемое частное.
	"""
	if second == 0:
		return 'Ошибка'
	else:
		return first / second

def main():
	pass

if __name__ == '__main__':
	main()