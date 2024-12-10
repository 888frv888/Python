def add_everything_up(a, b):
	try:
		a + b
	except TypeError:
		return f"{a}{b}"
	else:
		return f"{a + b :.3f}"


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
