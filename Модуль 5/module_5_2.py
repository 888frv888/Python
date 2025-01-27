# target = """Цель: понять как работают базовые магические методы на практике.
# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче.
# Необходимо дополнить класс House следующими специальными методами:
#     __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
#     __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
# Пример результата выполнения программы:
# Пример выполняемого кода:
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
# # __str__
# print(h1)
# print(h2)
# # __len__
# print(len(h1))
# print(len(h2))
# Вывод на консоль:
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# 10
# 20"""

class House:

	def __init__(self, name: str, number_of_floors: int):
		self.name = name
		self.number_of_floors = number_of_floors

	def __len__(self):
		return self.number_of_floors

	def __str__(self):
		return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

	def go_to(self, new_floor: int) -> None:
		if new_floor > self.number_of_floors or new_floor < 1:
			print("Такого этажа не существует")
		else:
			for floor in range(1, new_floor + 1):
				print(floor)

if __name__ == '__main__':
	h1 = House('ЖК Эльбрус', 10)
	h2 = House('ЖК Акация', 20)
	# h1.go_to(5)
	# h2.go_to(10)

	# __str__
	print(h1)
	print(h2)

	# __len__
	print(len(h1))
	print(len(h2))
