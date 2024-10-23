def get_matrix(n, m, value):                # объявляем функцию
    matrix = []                             # пустой список
    for i in range(n):                      # перебор строк
        matrix.append([])                   # добавляем пустые встроенные списки
        for j in range(m):                  # перебор столбцов
            matrix[i].append(value)         # добавляем столбцовое заполнение
    return matrix                           # возврат готовой матрицы

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)                              # magic 1
print(result2)                              # magic 2
print(result3)                              # magic 3