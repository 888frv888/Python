numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #
primes: list =[]                                                    # создаем списки
not_primes: list = []                                               #
for i in range(1,len(numbers)):                                     # перебираем исходный список
    is_prime: bool = True                                           # устанавливаем признак простоты
    for j in range(1,i):                                            # перебираем делители
        if numbers[i] % numbers[j] == 0:                            # проверка на остаток от деления
            is_prime = False                                        # при сработке отменяем признак. Составное.
            break                                                   # нет смысла перебирать дальше. За новым делимым.
    if is_prime:                                                    # проверка признака
        primes.append(numbers[i])                                   # в простые
    else:
        not_primes.append(numbers[i])                               # в составные
print('Primes ', primes, '\n')                                      #
print('Not primes ', not_primes)                                    # вывод списков