import multiprocessing
import time
from os import getcwd


def read_info(file_name):
	all_data = []
	with open(file_name, "r", encoding="utf-8") as file:
		for string in file:
			all_data.append(int(string))
		# while True:
		# 	string = file.readline()
		# 	if not string:
		# 		break
		# 	all_data.append(int(string))


if __name__ == "__main__":
	#file_name_list = [file_name for file_name in os.listdir(os.getcwd()) if file_name.startswith("file")]
	file_name_list = [f'./file {number}.txt' for number in range(1, 5)]
	start = time.perf_counter()
	_ = [*map(read_info, file_name_list)]
	print(f"{time.perf_counter() - start} (линейный)")

	print("#" * 50)
	time.sleep(3)
	print("#" * 50)

	start = time.perf_counter()
	with multiprocessing.Pool() as pool:
		pool.map(read_info, file_name_list)
	print(f"{time.perf_counter() - start} (многопроцессный)")
