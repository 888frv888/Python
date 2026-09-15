# target = """Цель: Применить очереди в работе с потоками, используя класс Queue.
# Задача "Потоки гостей в кафе":
# Необходимо имитировать ситуацию с посещением гостями кафе.
# Создайте 3 класса: Table, Guest и Cafe.
# Класс Table:
#     Объекты этого класса должны создаваться следующим способом - Table(1)
#     Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
# Класс Guest:
#     Должен наследоваться от класса Thread (быть потоком).
#     Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
#     Обладать атрибутом name - имя гостя.
#     Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
# Класс Cafe:
#     Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
#     Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
#     Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
# Метод guest_arrival(self, *guests):
#     Должен принимать неограниченное кол-во гостей (объектов класса Guest).
#     Далее, если есть свободный стол, то сажать гостя за стол (назначать столу guest), запускать поток гостя
#     и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
#     Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить
#     сообщение "<имя гостя> в очереди".
# Метод discuss_guests(self):
# Этот метод имитирует процесс обслуживания гостей.
#     Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
#     Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive),
#     то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен".
#     Так же текущий стол освобождается (table.guest = None).
#     Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу
#     присваивается гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди>
#     вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
#     Далее запустить поток этого гостя (start)
# Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
#     Table - стол, хранит информацию о находящемся за ним гостем (Guest).
#     Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
#     Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей
#     (guest_arrival) и их обслуживания (discuss_guests).
# Пример результата выполнения программы:
# Выполняемый код:
# class Table:
# ...
# class Guest:
# ...
# class Cafe:
# ...
# # Создание столов
# tables = [Table(number) for number in range(1, 6)]
# # Имена гостей
# guests_names = [
# 'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
# 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
# ]
# # Создание гостей
# guests = [Guest(name) for name in guests_names]
# # Заполнение кафе столами
# cafe = Cafe(*tables)
# # Приём гостей
# cafe.guest_arrival(*guests)
# # Обслуживание гостей
# cafe.discuss_guests()
# Вывод на консоль (последовательность может меняться из-за случайного время пребывания гостя):
# Maria сел(-а) за стол номер 1
# Oleg сел(-а) за стол номер 2
# Vakhtang сел(-а) за стол номер 3
# Sergey сел(-а) за стол номер 4
# Darya сел(-а) за стол номер 5
# Arman в очереди
# Vitoria в очереди
# Nikita в очереди
# Galina в очереди
# Pavel в очереди
# Ilya в очереди
# Alexandra в очереди
# Oleg покушал(-а) и ушёл(ушла)
# Стол номер 2 свободен
# Arman вышел(-ла) из очереди и сел(-а) за стол номер 2
# .....
# Alexandra покушал(-а) и ушёл(ушла)
# Стол номер 4 свободен
# Pavel покушал(-а) и ушёл(ушла)
# Стол номер 3 свободен
# Примечания:
#     Для проверки значения на None используйте оператор is (table.guest is None).
#     Для добавления в очередь используйте метод put, для взятия - get.
#     Для проверки пустоты очереди используйте метод empty.
#     Для проверки выполнения потока в текущий момент используйте метод is_alive."""

###################### Старая версия ##########################################3
# import random
# import threading
# import time
# from queue import Queue
#
#
# class Guest(threading.Thread):
# 	def __init__(self, name: str):
# 		super().__init__()
# 		self.name = name
#
# 	def run(self) -> None:
# 		time.sleep(random.randint(3, 10))
#
#
# class Table:
# 	def __init__(self, table_number: int):
# 		self.number = table_number
# 		self.guest = None
#
#
# class Cafe:
# 	def __init__(self, *cafe_tables: Table):
# 		self.tables = cafe_tables
# 		self.queue = Queue()
# 		self.operating_tables = 0
#
# 	def guest_arrival(self, *guests_list: Guest):
# 		for guest in guests_list:
# 			for free_table in self.tables:
# 				if free_table.guest is None:
# 					free_table.guest = guest
# 					self.operating_tables += 1
# 					free_table.guest.start()
# 					print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
# 					break
# 				elif not free_table is self.tables[-1]:
# 					continue
# 				else:
# 					self.queue.put(guest)
# 					print(f"{guest.name} в очереди")
# 					break
#
# 	def discuss_guests(self):
# 		while not self.queue.empty() or self.operating_tables:
# 			for table in self.tables:
# 				if table.guest is None:
# 					continue
# 				if not table.guest.name is None and not table.guest.is_alive():
# 					print(f"{table.guest.name} покушал(-а) и ушел(-а)\nСтол номер {table.number} свободен")
# 					table.guest = None
# 					self.operating_tables -= 1
# 				if not self.queue.empty() and table.guest is None:
# 					table.guest = self.queue.get()
# 					print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
# 					table.guest.start()
# 					self.operating_tables += 1
##################################################################################################################
##################################### Новая версия ########################################
import random
import threading
import time
from queue import Queue


class Guest(threading.Thread):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def run(self) -> None:
        time.sleep(random.randint(3, 10))


class Table:
    def __init__(self, table_number: int) -> None:
        self.number = table_number
        self.guest: Guest | None = None


class Cafe:
    def __init__(self, *cafe_tables: Table) -> None:
        # self.tables = cafe_tables
        # self.queue = Queue()
        # self.operating_tables = 0

        # Все столы храним как список — чтобы перебирать и проверять is_alive
        self.all_tables: list[Table] = list(cafe_tables)

        # Очередь свободных столов (пул ресурсов)
        self.free_tables_queue: Queue[Table] = Queue()
        for t in self.all_tables:
            self.free_tables_queue.put(t)

        # Очередь гостей (поток задач)
        self.guest_queue: Queue[Guest] = Queue()

    def guest_arrival(self, *guests_list: Guest) -> None:
        for guest in guests_list:
            # --- старая логика посадки ---
            # for free_table in self.tables:
            #     if free_table.guest is None:
            #         free_table.guest = guest
            #         self.operating_tables += 1
            #         free_table.guest.start()
            #         print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            #         break
            #     elif not free_table is self.tables[-1]:
            #         continue
            #     else:
            #         self.queue.put(guest)
            #         print(f"{guest.name} в очереди")
            #         break

            # --- новая логика посадки ---
            if not self.free_tables_queue.empty():
                current_table = self.free_tables_queue.get()
                current_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {current_table.number}")
            else:
                self.guest_queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self) -> None:
        # --- старое условие цикла ---
        # while not self.queue.empty() or self.operating_tables:

        # --- новое условие цикла ---
        while not self.guest_queue.empty() or any(
            t.guest is not None for t in self.all_tables
        ):
            # Освобождаем столы от гостей, которые доели
            for current_table in self.all_tables:
                if current_table.guest is None:
                    continue

                # --- старая проверка ---
                # if not table.guest.name is None and not table.guest.is_alive():

                # --- новая проверка ---
                if not current_table.guest.is_alive():
                    print(
                        f"{current_table.guest.name} покушал(-а) и ушёл(-а)\n"
                        f"Стол номер {current_table.number} свободен"
                    )
                    current_table.guest = None
                    # Возвращаем стол в пул свободных
                    self.free_tables_queue.put(current_table)

            # Если есть свободные столы и гости в очереди — сажаем
            # --- старая логика (внутри for table in self.tables) ---
            # if not self.queue.empty() and table.guest is None:
            #     table.guest = self.queue.get()
            #     print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            #     table.guest.start()
            #     self.operating_tables += 1

            # --- новая логика (отдельно от перебора столов) ---
            if not self.guest_queue.empty() and not self.free_tables_queue.empty():
                current_table = self.free_tables_queue.get()
                current_table.guest = self.guest_queue.get()
                current_table.guest.start()
                print(
                    f"{current_table.guest.name} вышел(-ла) из очереди "
                    f"и сел(-а) за стол номер {current_table.number}"
                )

            time.sleep(1)  # пауза против busy-waiting


if __name__ == '__main__':
    # Создание столов
    # tables = (Table(number) for number in range(1, 6))  # генератор
    tables = [Table(number) for number in range(1, 6)]     # список

    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang',
        'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina',
        'Pavel', 'Ilya', 'Alexandra'
    ]

    # Создание гостей
    # guests = (Guest(name=name) for name in guests_names)  # генератор
    guests = [Guest(name) for name in guests_names]          # список

    # Заполнение кафе столами
    cafe = Cafe(*tables)

    # Приём гостей
    cafe.guest_arrival(*guests)

    # Обслуживание гостей
    cafe.discuss_guests()
    print("Все гости разошлись")
