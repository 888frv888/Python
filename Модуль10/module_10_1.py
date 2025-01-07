import threading, time


def wite_words(word_count: int, file_name: str) -> None:
	with open(file_name, "a", encoding="utf-8") as file:
		for number in range(word_count):
			file.write(f"Какое-то слово № {number}\n")
			time.sleep(0.1)
	print(f"завершилась запись в файл {file_name}")


if __name__ == '__main__':
	start_time = time.time()

	wite_words(10, "example1.txt")
	wite_words(30, "example2.txt")
	wite_words(200, "example3.txt")
	wite_words(100, "example4.txt")

	stop_time = time.time()
	print(f"Работа потоков {stop_time - start_time}")

	start_time = time.time()

	thread1 = threading.Thread(target=wite_words, args=(10, "example5.txt"))
	thread1.start()

	thread2 = threading.Thread(target=wite_words, args=(30, "example6.txt"))
	thread2.start()

	thread3 = threading.Thread(target=wite_words, args=(200, "example7.txt"))
	thread3.start()

	thread4 = threading.Thread(target=wite_words, args=(100, "example8.txt"))
	thread4.start()

	thread1.join()
	thread2.join()
	thread3.join()
	thread4.join()
	stop_time = time.time()
	print(f"Работа потоков {stop_time - start_time}")
