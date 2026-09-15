# """
# Цель: приобрести навык создания простейших Юнит-тестов
#
# Задача "Проверка на выносливость":
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.
#
# Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
# test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk
#  у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
# test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод
#  run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
# test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у
#  объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте
#  метод assertNotEqual, чтобы убедится в неравенстве результатов.
# Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.
#
# Пункты задачи:
#
# Скачайте исходный код для тестов.
# Создайте класс RunnerTest и соответствующие описанию методы.
# Запустите RunnerTest и убедитесь в правильности результатов.
# Пример результата выполнения программы:
#
# Вывод на консоль:
#
# Ran 3 tests in 0.001s OK
#
# Примечания:
#
# Попробуйте поменять значения в одном из тестов, результаты
# """

import unittest
import runner


class RunnerTest(unittest.TestCase):

	def test_walk(self):
		walker = runner.Runner("Test_1")
		for _ in range(10):
			walker.walk()
		self.assertEqual(walker.distance, 50)

	def test_run(self):
		runer = runner.Runner("Test_2")
		for _ in range(10):
			runer.run()
		self.assertEqual(runer.distance, 100)

	def test_challenge(self):
		challenger_1 = runner.Runner("Test_3_1")
		challenger_2 = runner.Runner("Test_3_2")
		for _ in range(10):
			challenger_1.run()
			challenger_2.walk()
		self.assertNotEqual(challenger_1.distance, challenger_2.distance, msg="Challenger 1 and Challenger 2 have the same distance")

if __name__ == '__main__':
	unittest.main()
