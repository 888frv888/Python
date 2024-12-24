import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))


def get_advanced_writer(file_name: str):
	def write_everything(*data_set):
		# string = str(data_set).lstrip("(").rstrip(")") + "\n"		#
		# string = " ".join(map(str, data_set)) + "\n"				# попытки правильно собрать строку
		string = str(data_set).strip("()") + "\n"  					#
		print(string)
		try:
			with open(file_name, "a", encoding="utf-8") as file:
				file.write(string)
		except FileExistsError:
			print("Нет такого файла")
		except Exception:
			print("!!!SOME THING WRONG!!!")

	return write_everything


class MysticBall:
	def __init__(self, *args):
		self.words = []
		self._build_words_from_args(*args)

	def _build_words_from_args(self, *args):
		self.words = [str(string) for string in args]

	def __call__(self):
		return random.choice(self.words)


if __name__ == '__main__':
	print(result)
	write = get_advanced_writer('example.txt')
	write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
	first_ball = MysticBall('Да', 'Нет', 'Наверное')
	print(first_ball())
	print(first_ball())
	print(first_ball())
