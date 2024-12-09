from math import pi


class Figure:
	sides_count: int = 0
	valid_sides = 0
	default_side = 1

	def __init__(self, *args):
		self.__color = args[0]
		self.__sides = [self.default_side] * self.sides_count
		self.set_sides(*args[1:])
		self.filled: bool = False

	def get_color(self):
		return list(self.__color)

	def __len__(self):
		return sum(self.__sides)

	def __is_valid_color(self, red: int, green: int, blue: int):
		for element in (red, green, blue):
			if not 0 <= element <= 255 and isinstance(element, int):
				return False
		return True

	def set_color(self, red: int, green: int, blue: int):
		if self.__is_valid_color(red, green, blue):
			self.__color = [red, green, blue]

	def __is_valid_sides(self, *sides):
		if not len(sides) == self.valid_sides:
			return False
		for element in sides:
			if not isinstance(element, int) and element > 0:
				return False
		return True

	def get_sides(self):
		return self.__sides

	# def build_sides(self):
	#     for count in range(self.sides_count):
	#         self.__sides.append(self.default_side)

	def set_sides(self, *new_sides):
		if self.__is_valid_sides(*new_sides):
			self.__sides = list(new_sides)
	# else:
	# 	self.build_sides()


class Circle(Figure):
	sides_count = 1
	valid_sides = 1

	def __init__(self, *args):
		super().__init__(*args)
		self.__radius = 0

	def get_square(self):
		return pow(self.__sides, 2) / (4 * pi)


class Triangle(Figure):
	sides_count = 3
	valid_sides = 3

	def get_square(self):
		p = sum(self.__sides) / 2
		s = pow((p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2])), 0.5)
		return s


class Cube(Figure):
	sides_count = 12
	valid_sides = 1

	def __init__(self, *args):
		super().__init__(*args)
		self.__sides = [] * self.sides_count

	# def _Figure__is_valid_sides(self, *sides):
	# 	if not len(sides) == self.valid_sides:
	# 		return False
	# 	for element in sides:
	# 		if not isinstance(element, int) and element > 0:
	# 			return False
	# 	return True

	def set_sides(self, *new_sides):
		new_sides_list = list(new_sides)
		if len(new_sides_list) == self.valid_sides:
			for side in self.__sides:
				side = int(new_sides)

	def get_volume(self):
		cube_side = self.get_sides()
		print(*cube_side)
		return pow(cube_side[0], 3)


if __name__ == '__main__':
	circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
	cube1 = Cube((222, 35, 130), 6)

	# Проверка на изменение цветов:
	circle1.set_color(55, 66, 77)  # Изменится
	print(circle1.get_color())
	cube1.set_color(300, 70, 15)  # Не изменится
	print(cube1.get_color())
	# Проверка на изменение сторон:
	cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
	print(cube1.get_sides())
	circle1.set_sides(15)  # Изменится
	print(circle1.get_sides())
	# Проверка периметра (круга), это и есть длина:
	print(len(circle1))
	# Проверка объёма (куба):
	print(cube1.get_volume())
