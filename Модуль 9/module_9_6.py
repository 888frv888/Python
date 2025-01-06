def func_1(text):
	for i in range(1, len(text)+1):
		fin=len(text)-i+1
		for j in range(fin):
			string = text[j:j+i]
			yield string

for i in func_1("abc"):
	print(i)