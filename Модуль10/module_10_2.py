import threading, time


class Knight(threading.Thread):
	def __init__(self, name, power):
		super().__init__()
		self.name = name
		self.power = power


	def run(self):
		print(f"{self.name}, на нас напали!")
		enemies, timer = 100, 0
		while enemies:
			timer += 1
			enemies -= self.power
			print(f"{self.name} сражается {timer} день (дня)..., осталось {enemies} воинов.")
			time.sleep(1)
		print(f"{self.name} одержал победу спустя {timer} дней(дня)!")

if __name__ == '__main__':
	first_knight = Knight("Sir Lancelot", 10)
	second_knight = Knight("Sir Galahad", 20)
	first_knight.start()
	second_knight.start()
