# print('Hi, PyCharm')
# x = 43
# y = 32
# print(x * y)
# print("End line")
def my_sqr(n, *args, txt='Сумма квадратов'):
	s: int = 0
	for i in args:
		s += i ** n
	print(txt + ':', s)

my_sqr(1, 1,2,3,4,5,6, txt='Проба')
