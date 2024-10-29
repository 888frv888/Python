def single_root_words(root_word: str, *other_words: str) -> list:			# немного оформления функции
	"""
	Функция single_root_words() возвращает список однокоренных слов
	:rtype: list
	:param root_word: str тип. Слово, предположительно являющееся однокоренным.
	:param other_words: str тип. Список слов для проверки на однокоренное
	:return: Список однокоренных слов
	"""
	same_words: list = []													# пустой список для ответа
	for word in other_words:													# перебор списка поэлементно
		# if root_word.lower() in word.lower():									# проверка с использованием in
		# 	same_words.append(word)
		# elif root_word.lower().count(word.lower()):							# проверка с использованием count
		# 	same_words.append(word)
		if root_word.lower() in word.lower() or word.lower() in root_word.lower():	#вариант от преподавателя
			same_words.append(word)
	return same_words														# возврат ответа
result1: list = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2: list = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
