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
			# self.number_of_floors += other.number_of_floors
			return self.__class__(self.name, self.number_of_floors + other.number_of_floors)
		elif isinstance(other, int):
			# self.number_of_floors += other
			return self.__class__(self.name, self.number_of_floors + other)
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
