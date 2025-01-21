target = """Дополнительное практическое задание по модулю: "Подробнее о функциях."
Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
Задание "Раз, два, три, четыре, пять .... Это не всё?":
Наши студенты, без исключения, - очень умные ребята. Настолько умные, что иногда по утру сами путаются в том, 
что намудрили вчера вечером.
Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). Тем не менее, даже 
после сна, его код остался рабочим и выглядел следующим образом:
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел 
и длин всех строк?"
Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) 
по-разному.
Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения 
для таких структур он не нашёл.
Помогите сокурснику осуществить его задумку.
Что должно быть подсчитано:
    Все числа (не важно, являются они ключами или значениям или ещё чем-то).
    Все строки (не важно, являются они ключами или значениям или ещё чем-то)
Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99
Входные данные (применение функции):
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
Выходные данные (консоль):
99
Примечания (рекомендации):
    Весь подсчёт должен выполняться одним вызовом функции.
    Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
    Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
    Для определения типа данного используйте функцию isinstance."""

def calculate_structure_sum(*args: int | str | list | tuple | dict | set ) -> int:
	"""
	!!!ВНИМАНИЕ РЕКУРСИЯ!!!
	Функция принимает параметром аргумент, в виде хаотичной структуры данных,
	суммирует все целые числа, строковые элементы измеряет и добавляет к сумме
	:param args: хаотичная структура данных (писки, кортежи, множества, словари в разных комбинациях
	:rtype: int
	:return: сумма целых чисел и длин строк
	"""
	counter: int = 0
	for element in args:
		if isinstance(element, int):
			counter += element
		elif isinstance(element, str):
			counter += len(element)
		elif isinstance(element, list | tuple | set):
			counter += calculate_structure_sum(*element)
		elif isinstance(element, dict):
			counter += calculate_structure_sum(*element.items())
	return counter


data_structure = [
	[1, 2, 3],
	{'a': 4, 'b': 5},
	(6, {'cube': 7, 'drum': 8}),
	"Hello",
	((), [{(2, 'Urban', ('Urban2', 35))}])
]

def main():
	result: int = calculate_structure_sum(data_structure)
	print(result)

if __name__ == '__main__':
	main()
