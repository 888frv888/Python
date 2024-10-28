def get_multiplied_digits(number: int) -> int:
	"""
	!!!ВНИМАНИЕ РЕКУРСИЯ!!!
	Функция перемножает цифры числа. Нули отбрасываются.
	:param number: тип int. Число для расчета.
	:rtype: int
	:return: возвращает произведение
	"""
	str_number: str = str(number)		# аргумент в строку
	first: int = int(str_number[0])		# берём первый символ и преобразуем в цифру
	if not (len(str_number) > 1):		# если при этом длина строки НЕ БОЛЬШЕ 1 (равна 1), то есть последняя цифра
		return first		# вернуть эту цифру.
	else:		# в противном случае можем работать дальше
		return first * get_multiplied_digits(int(str_number[1:]))		# вернуть цифру, умноженную на функцию
###########################################################################
result: int = get_multiplied_digits(40203)
print(result)
