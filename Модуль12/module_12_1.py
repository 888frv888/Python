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
