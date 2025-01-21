# target_of_module = """Цель задания:
# Закрепить знания об интроспекции в Python.
# Создать персональную функции для подробной интроспекции объекта.
# Задание:
# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит
# интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#   - Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию).
# Пример работы:
# number_info = introspection_info(42)
# print(number_info)
# Вывод на консоль:
# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
# Рекомендуется создавать свой класс и объект для лучшего понимания
# Файл с кодом прикрепите к домашнему заданию."""


def introspection_info(object_for_introspect) -> dict[str, list | str]:
    introspect_dict = {"type": type(object_for_introspect),
                       "attributes": [],
                       "methods": [],
                       "module": globals()['__name__']}
    for element in dir(object_for_introspect):
        match callable(getattr(object_for_introspect, element)):
            case True:
                introspect_dict["methods"].append(element)
            case False:
                introspect_dict["attributes"].append(element)
    return introspect_dict


if __name__ == '__main__':
    print(introspection_info(42))
