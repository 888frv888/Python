import random
import threading
import time


class Bank:
	def __init__(self):
		self.balance = 0
		self.lock = threading.Lock()

	def deposit(self):
		for i in range(100):
			step = random.randint(50, 500)
			self.balance += step
			if self.balance >= 500 and self.lock.locked():
				self.lock.release()
			print(f"Пополнение: {step}. Баланс: {self.balance}")
			time.sleep(0.001)

	def take(self):
		for i in range(100):
			step = random.randint(50, 500)
			print(f"Запрос на {step}")
			if self.balance >= step:
				self.balance -= step
				print(f"Снятие: {step}. Баланс: {self.balance}")
			else:
				print(f"Запрос отклонен, недостаточно средств")
				self.lock.acquire()
			time.sleep(0.001)


if __name__ == '__main__':
	bk = Bank()
	th1 = threading.Thread(target=Bank.deposit, args=(bk,))
	th2 = threading.Thread(target=Bank.take, args=(bk,))
	th1.start()
	th2.start()
	th1.join()
	th2.join()
	print(f"Итоговый баланс: {bk.balance}")
