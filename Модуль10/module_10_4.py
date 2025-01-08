import random
import threading
import time
from queue import Queue


class Guest(threading.Thread):
	def __init_(self, name):
		super().__init__()
		self.name = name

	def run(self) -> None:
		time.sleep(random.randint(3, 10))


class Table:
	def __init__(self, table_number: int):
		self.number = table_number
		self.guest = None


class Cafe:
	def __init__(self, *cafe_tables):
		self.tables = cafe_tables
		self.queue = Queue()
		self.operating_tables = 0

	def guest_arrival(self, *guests_list):
		for guest in guests_list:
			for free_table in self.tables:
				if free_table.guest is None:
					free_table.guest = guest
					self.operating_tables += 1
					free_table.guest.start()
					print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
					break
				elif not free_table is self.tables[-1]:
					continue
				else:
					self.queue.put(guest)
					print(f"{guest.name} в очереди")
					break

	def discuss_guests(self):
		while not self.queue.empty() or self.operating_tables:
			for table in self.tables:
				if table.guest is None:
					continue
				if not table.guest.name is None and not table.guest.is_alive():
					print(f"{table.guest.name} покушал(-а) и ушел(-а)\nСтол номер {table.number} свободен")
					table.guest = None
					self.operating_tables -= 1
				if not self.queue.empty() and table.guest is None:
					table.guest = self.queue.get()
					print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
					table.guest.start()
					self.operating_tables += 1
if __name__ == '__main__':
	# Создание столов
	tables = (Table(number) for number in range(1, 6))
	# Имена гостей
	guests_names = ('Maria', 'Oleg', 'Vakhtang',
					'Sergey', 'Darya', 'Arman',
					'Vitoria', 'Nikita', 'Galina',
					'Pavel', 'Ilya', 'Alexandra')
	# Создание гостей
	guests = (Guest(name=name) for name in guests_names)
	# Заполнение кафе столами
	cafe = Cafe(*tables)
	# Приём гостей
	cafe.guest_arrival(*guests)
	# Обслуживание гостей
	cafe.discuss_guests()
	print(f"Все гости разошлись")