# n: int = int(input('Ввести число от 3 до 20 включительно\n'))
# numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# spisok: list = []
# result: str = ''
# for i in range(1, n):
# 	for j in numbers:
# 		if i == j: continue
# 		if n % (i + j) == 0:
# 			spisok.extend([i, j])
# 	numbers.remove(i)
# result = result.join(map(str, spisok))
# print(result)

############## Вариант от преподавателя ################
n: int = int(input('Ввести число от 3 до 20 включительно\n'))
numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result: str = ''
for i in range(1, n):
	for j in range(i+1, n):
		if n % (i + j) == 0:
			result += str(i) + str(j)
print(result)