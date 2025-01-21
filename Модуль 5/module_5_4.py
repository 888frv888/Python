# target = """Цель: понять разницу между атрибутами объекта и класса, дополнив уже существующий класс. Применить метод __new__.
# Дополнительно о работе метода __new__:
# Как мы уже знаем метод __new__ вызывается перед тем, как вызовется метод __init__.
# Разберёмся, как происходит передача данных между ними на следующем примере:
# class Example:
#   def __new__(cls, *args, **kwargs):
#   print(args)
#     print(kwargs)
#     return object.__new__(cls)
#
#   def __init__(self, first, second, third):
#   print(first)
#   print(second)
#     print(third)
#
# ex = Example('data', second=25, third=3.14)
#
# Работа __new__:
#     'data' передаётся (упаковывается) в *args, т.к. это позиционный аргумент. Он будет находиться под индексом 0 как единственный элемент кортежа.
#     second=25 и third=3.14 передаются (упаковываются) в **kwargs т.к. это именованные аргументы. Они будут находиться под ключами 'second' и 'third' со значением 25 и 3.14 соответственно в словаре.
# Передача данных из __new__ в __init__:
# После того как метод __new__ отработает до конца, произойдут следующие события с параметрами __init__:
#     В параметр first распакуется из args единственный аргумент 'data'.
#     В параметр second распакуется значение под ключом с тем же названием из словаря kwargs.
#     В параметр third распакуется значение под ключом с тем же названием из словаря kwargs.
#
# Задача "История строительства":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
#     Название объекта добавлялось в список cls.houses_history.
#     Название строения можно взять из args по индексу.
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.
# Пример результата выполнения программы:
# Пример выполнения программы:
# h1 = House('ЖК Эльбрус', 10)
# print(House.houses_history)
# h2 = House('ЖК Акация', 20)
# print(House.houses_history)
# h3 = House('ЖК Матрёшки', 20)
# print(House.houses_history)
# # Удаление объектов
# del h2
# del h3
# print(House.houses_history)
# Вывод на консоль:
# ['ЖК Эльбрус']
# ['ЖК Эльбрус', 'ЖК Акация']
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Акация снесён, но он останется в истории
# ЖК Матрёшки снесён, но он останется в истории
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Эльбрус снесён, но он останется в истории
# Примечания:
#     Более подробно о работе метода __new__ можно узнать здесь.
#     В методе __new__ можно обращаться к атрибутам текущего класса при помощи параметра cls."""

class House:
	"""Класс, описывающий некоторые здания"""

	houses_history: set = set()

	def __new__(cls, *args, **kwargs):
		"""Создаем новый объект класса"""
		cls.houses_history.add(args[0])
		return super().__new__(cls)

	def __init__(self, name: str, number_of_floors: int):
		"""Инициализируем созданный объект"""
		self.name: str = name
		self.number_of_floors: int = number_of_floors

	def __len__(self) -> int:
		"""Возвращаем этажность здания"""
		return self.number_of_floors

	def __str__(self) -> str:
		"""Возвращаем информацию по зданию"""
		return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

	def go_to(self, new_floor: int) -> None:
		"""Метод 'шагает' по этажам снизу вверх"""
		if not 1 <= new_floor <= self.number_of_floors:
			print("Такого этажа не существует")
		else:
			for floor in range(1, new_floor + 1):
				print(floor)

	def __del__(self):
		"""Выводит сообщение при ликвидации объекта"""
		print(f"{self.name} снесён, но он останется в истории")

	def __eq__(self, other: object | int) -> bool:  # Наш экземпляр равен другому объекту?
		"""Сравнение объекта"""
		if isinstance(other, House):
			# Сравнение с другим экземпляром House:
			return self.number_of_floors == other.number_of_floors
		elif isinstance(other, int):
			# Сравнение с целым числом:
			return self.number_of_floors == other
		else:
			# Если сравниваем с чем-то другим, то ошибка типа
			raise TypeError("Должно быть целое число для сравнения. Или объект класса House")

	def __lt__(self, other: object | int) -> bool:
		"""Сравнение объекта"""
		if isinstance(other, House):
			return self.number_of_floors < other.number_of_floors
		elif isinstance(other, int):
			return self.number_of_floors < other
		else:
			raise TypeError("Должно быть целое число для сравнения. Или объект класса House")

	def __le__(self, other: object | int) -> bool:
		"""Сравнение объекта"""
		if isinstance(other, House):
			return self.__lt__(other.number_of_floors) or self.__eq__(other.number_of_floors)

	def __add__(self, other: object | int) -> object:
		"""Метод складывет этажи здания с другим зданием) или с целым числом"""
		if isinstance(other, House):
			self.number_of_floors += other.number_of_floors
			return self
			#return self.__class__(self.name, self.number_of_floors + other.number_of_floors)
		elif isinstance(other, int):
			self.number_of_floors += other
			return self
			#return self.__class__(self.name, self.number_of_floors + other)
		else:
			raise TypeError("Должно быть целое число для сложения. Или объект класса House")

	def __iadd__(self, other: object | int) -> object:
		"""То же сложение"""
		self.__add__(other)
		return self

	def __radd__(self, other: object | int) -> object:
		"""То же сложение"""
		self.__add__(other)
		return self

	def __sub__(self, other: object | int) -> object:
		"""Вычитание этажей объектов"""
		if isinstance(other, House):
			# self.number_of_floors -= other.number_of_floors
			return self.__class__(self.name, self.number_of_floors - other.number_of_floors)
		elif isinstance(other, int):
			# self.number_of_floors -= other
			return self.__class__(self.name, self.number_of_floors - other)
		else:
			raise TypeError("Должно быть целое число для вычитания. Или объект класса House")


if __name__ == '__main__':
	h1 = House('ЖК Эльбрус', 10)
	h2 = House('ЖК Акация', 20)
	print(h1)
	print(h2)
	print(h1 == h2)  # __eq__
	h1 = h1 + 10  # __add__
	print(h1)
	print(h1 == h2)
	h1 += 10  # __iadd__
	print(h1)
	h2 = 10 + h2  # __radd__
	print(h2)
	print(h1 > h2)  # __gt__
	print(h1 >= h2)  # __ge__
	print(h1 < h2)  # __lt__
	print(h1 <= h2)  # __le__
	print(h1 != h2)  # __ne__
	h1 = House('ЖК Эльбрус', 10)
	print(House.houses_history)
	h2 = House('ЖК Акация', 20)
	print(House.houses_history)
	h3 = House('ЖК Матрёшки', 20)
	print(House.houses_history)
	# Удаление объектов
	del h2
	del h3
	print(House.houses_history)
