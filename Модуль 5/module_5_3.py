class House:

	def __init__(self, name: str, number_of_floors: int):
		self.name = name
		self.number_of_floors = number_of_floors

	def __len__(self):
		return self.number_of_floors

	def __str__(self):
		return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

	def go_to(self, new_floor: int) -> None:
#		if new_floor > self.number_of_floors or new_floor < 1:
		if not 1 <= new_floor <= self.number_of_floors:
			print("Такого этажа не существует")
		else:
			for floor in range(1, new_floor + 1):
				print(floor)

	def __eq__(self, other):			# Наш экземпляр равен другому объекту?
		if isinstance(other, House):
			# Сравнение с другим экземпляром House:
			return self.number_of_floors == other.number_of_floors
		elif isinstance(other, int):
			# Сравнение с целым числом:
			return self.number_of_floors == other
		else:
			# Если сравниваем с чем-то другим, то ошибка типа
			raise TypeError("Должно быть целое число для сравнения. Или объект класса House")

	def __ne__(self, other):
		return not self.__eq__(other)

	def __lt__(self, other):
		if isinstance(other, House):
			return self.number_of_floors < other.number_of_floors
		elif isinstance(other, int):
			return self.number_of_floors < other
		else:
			raise TypeError("Должно быть целое число для сравнения. Или объект класса House")

	def __ge__(self, other):
		return not self.__lt__(other)

	def __gt__(self, other):
		if isinstance(other, House):
			return self.number_of_floors > other.number_of_floors
		elif isinstance(other, int):
			return self.number_of_floors > other
		else:
			raise TypeError("Должно быть целое число для сравнения. Или объект класса House")

	def __le__(self, other):
		return not self.__gt__(other)

	def __add__(self, other):
		if isinstance(other, House):
			self.number_of_floors += other.number_of_floors
			return self
		elif isinstance(other, int):
			self.number_of_floors += other
			return self
		else:
			raise TypeError("Должно быть целое число для сложения. Или объект класса House")

	def __iadd__(self, other):
		self.__add__(other)
		return self


	def __radd__(self, other):
		self.__add__(other)
		return self

	def __sub__(self, other):
		if isinstance(other, House):
			self.number_of_floors -= other.number_of_floors
			return self
		elif isinstance(other, int):
			self.number_of_floors -= other
			return self
		else:
			raise TypeError("Должно быть целое число для сложения. Или объект класса House")

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
