grades: list = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students: set = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_dict: dict = {} # Создаем пустой словарь
students_list: list = sorted(list(students)) # преобразуем хаотичное множество в упорядоченный список
for name in students_list: # перебираем имена студентов по списку
    name_index: int = students_list.index(name) # вычисляем индекс имени в списке
    my_dict[name] = sum(grades[name_index]) / len(grades[name_index]) # заполняем словарь
print(my_dict) # вывод словаря