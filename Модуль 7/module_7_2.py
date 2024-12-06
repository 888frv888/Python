def custom_write(file_name, strings):
    """Функция принимает параметрами имя файла и список строк.
    Производится запись строк в указанный файл. Каждая с новой строки.
    Функция возвращает словарь """
    strings_positions = dict()
    file = open(file_name, "w", encoding="utf-8")
    for string in strings:
        str_position = file.tell()
        file.write("".join((string, "\n")))
        strings_positions[(strings.index(string) + 1, str_position)] = string
    file.close()
    return strings_positions


if __name__ == '__main__':

    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
