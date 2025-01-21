target = """Цель: применить знания о рекурсии в решении задачи.
Задача 'Рекурсивное умножение цифр':
Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр 
этого числа.
Пункты задачи:
    Напишите функцию get_multiplied_digits и параметр number в ней.
    Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
    Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый символ 
    из str_number в числовом представлении(int).
    Возвращайте значение first * get_multiplied_digits(int(str_number[1:])). Таким образом вы умножите первую цифру
     числа на результат работы этой же функции с числом, но уже без первой цифры.
    4 пункт можно выполнить только тогда, когда длина str_number больше 1, т.к. в противном случае не получиться взять 
    срез str_number[1:].
    Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
Стек вызовов будет выглядеть следующим образом:
get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3
Пример результата выполнения программы:
Исходный код:
result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
Вывод на консоль:
24
24
Примечания:
    При преобразовании строки(str) в число(int) первые нули убираются. int('00123') -> 123.
    Если возникает ошибка, рекомендуется пошагово отладить программу "жучком". Чаще всего ошибка заключается в 
    бесконечной рекурсии или же в неверном обращении по индексу."""

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
