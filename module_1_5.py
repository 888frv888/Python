<<<<<<< Updated upstream
immutable_var = (0, 1, 56, "String1", "String2", ["Ptr", "mem", 24, 42])
print()
print("Неизменный кортеж: ", immutable_var)
# immutable_var[0] = 1
# при попытке изменить элемент кортежа типа 'int' или 'str' появляется
# ошибка "TypeError: 'tuple' object does not support item assignment"
# но если одним из элементов кортежа будет список - то вот элементы этого списка мы поменять можем!!
immutable_var[5][1] = "MeM"
print("Почти неизменный кортеж: ", immutable_var, type(immutable_var))
print()
mutable_var = ["Str", "Obj", 24, 42]
print("Изменяемый список: ", mutable_var)
mutable_var[0] = "Строка"
mutable_var[2] = 42
mutable_var[3] = 24
=======
immutable_var = (0, 1, 56, "String1", "String2", ["Ptr", "mem", 24, 42])
print()
print("Неизменный кортеж: ", immutable_var)
# immutable_var[0] = 1
# при попытке изменить элемент кортежа типа 'int' или 'str' появляется
# ошибка "TypeError: 'tuple' object does not support item assignment"
# но если одним из элементов кортежа будет список - то вот элементы этого списка мы поменять можем!!
immutable_var[5][1] = "MeM"
print("Почти неизменный кортеж: ", immutable_var, type(immutable_var))
print()
mutable_var = ["Str", "Obj", 24, 42]
print("Изменяемый список: ", mutable_var)
mutable_var[0] = "Строка"
mutable_var[2] = 42
mutable_var[3] = 24
>>>>>>> Stashed changes
print("Изменённый список: ", mutable_var, type(mutable_var))