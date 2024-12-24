first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(fst) - len(scnd) for fst, scnd in zip(first, second) if not len(fst) == len(scnd))
second_result = (len(first[index]) == len(second[index]) for index in range(len(first)))

print(list(first_result))
print(list(second_result))
