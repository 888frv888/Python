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
