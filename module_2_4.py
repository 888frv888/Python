numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #
primes: list =[]                                                    # создаем списки
not_primes: list = []                                               #
for i in numbers:                                                   # перебираем исходный список
    if i == 1: continue                                             # 1 пропускаем
    is_prime: bool = True                                           # устанавливаем признак простоты
    for j in range(2, i):                                           # перебираем делители
        if i % j == 0:                                              # проверка на остаток от деления
            is_prime = False                                        # при сработке отменяем признак. Составное.
            break                                                   # нет смысла перебирать дальше. За новым делимым.
    if is_prime:                                                    # проверка признака
        primes.append(i)                                            # в простые
    else:
        not_primes.append(i)                                        # в составные
print('Primes ', primes, '\n')                                      #
print('Not primes ', not_primes)                                    # вывод списков