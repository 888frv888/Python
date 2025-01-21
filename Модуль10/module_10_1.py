# target = """Цель: понять как работают потоки на практике, решив задачу
# Задача "Потоковая запись в файлы":
# Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество
# записываемых слов, file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий
# файл с прерыванием после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
# После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:
#     10, example1.txt
#     30, example2.txt
#     200, example3.txt
#     100, example4.txt
# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
#     10, example5.txt
#     30, example6.txt
#     200, example7.txt
#     100, example8.txt
# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков.
# Как это сделать рассказано в лекции к домашнему заданию.
# Пример результата выполнения программы:
# Алгоритм работы кода:
# # Импорты необходимых модулей и функций
# # Объявление функции write_words
# # Взятие текущего времени
# # Запуск функций с аргументами из задачи
# # Взятие текущего времени
# # Вывод разницы начала и конца работы функций
# # Взятие текущего времени
# # Создание и запуск потоков с аргументами из задачи
# # Взятие текущего времени
# # Вывод разницы начала и конца работы потоков
# Вывод на консоль:
# Завершилась запись в файл example1.txt
# Завершилась запись в файл example2.txt
# Завершилась запись в файл example3.txt
# Завершилась запись в файл example4.txt
# Работа потоков 0:00:34.003411 # Может быть другое время
# Завершилась запись в файл example5.txt
# Завершилась запись в файл example6.txt
# Завершилась запись в файл example8.txt
# Завершилась запись в файл example7.txt
# Работа потоков 0:00:20.071575 # Может быть другое время
# Записанные данные в файл должны выглядеть так:
# Примечания:
#     Не переживайте, если программа выполняется долго, учитывая кол-во слов, максимальное время
#     выполнения в потоках не должно превышать ~20 секунд, а в функциях ~34 секунды.
#     Cледует заметить, что запись в example8.txt завершилась раньше, чем в example7.txt, т.к. потоки
#     работали почти одновременно."""

import threading, time

arguments_func = {10: "example1.txt",
				  30: "example2.txt",
				  200: "example3.txt",
				  100: "example4.txt"
				  }
arguments_thread = {10: "example5.txt",
					30: "example6.txt",
					200: "example7.txt",
					100: "example8.txt"
					}


def time_it(func):
	def box(*args):
		starting_time = time.time()
		result = func(*args)
		stoping_time = time.time()
		print(f"Работа потоков {stoping_time - starting_time}")
		return result

	return box


def wite_words(words_count: int, file_name: str) -> None:
	with open(file_name, "a", encoding="utf-8") as file:
		for number in range(words_count):
			file.write(f"Какое-то слово № {number}\n")
			time.sleep(0.1)
	print(f"завершилась запись в файл {file_name}")


@time_it
def write_main(dict_of_templates: dict[int:str]) -> None:
	for number, name in dict_of_templates.items():
		wite_words(number, name)


@time_it
def write_thread(dict_of_templates: dict[int:str]) -> None:
	threads_list: list = []
	for number, name in dict_of_templates.items():
		thread = threading.Thread(target=wite_words, args=(number, name))
		threads_list.append(thread)
		thread.start()
	for thread in threads_list:
		thread.join()


if __name__ == '__main__':
	# wite_words(100, "example4.txt")
	# wite_words(200, "example3.txt")
	# wite_words(30, "example2.txt")
	# wite_words(10, "example1.txt")

	# stop_time = time.time()
	# print(f"Работа потоков {stop_time - start_time}")
	#
	# start_time = time.time()
	#
	# thread1 = threading.Thread(target=wite_words, args=(10, "example5.txt"))
	# thread1.start()
	#
	# thread2 = threading.Thread(target=wite_words, args=(30, "example6.txt"))
	# thread2.start()
	#
	# thread3 = threading.Thread(target=wite_words, args=(200, "example7.txt"))
	# thread3.start()
	#
	# thread4 = threading.Thread(target=wite_words, args=(100, "example8.txt"))
	# thread4.start()
	#
	# thread1.join()
	# thread2.join()
	# thread3.join()
	# thread4.join()
	# stop_time = time.time()
	# print(f"Работа потоков {stop_time - start_time}")
	write_main(arguments_func)
	write_thread(arguments_thread)
