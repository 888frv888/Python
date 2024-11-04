def send_email(message: str, recipient: str, sender: str = "university.help@gmail.com"):
	flag1: bool = not (('@' in recipient) and ('@' in sender))
	flag2: bool = not (
			recipient.endswith(('.com', '.ru', '.net'))
			and
			sender.endswith(('.com', '.ru', '.net')))
	if flag1 or flag2:
		print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
		return '0'
	if recipient == sender:
		print('Нельзя отправить письмо самому себе!')
		return '0'
	if sender == 'university.help@gmail.com':
		print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
	else:
		print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
########################### Вариант преподавателя ##########################################
	# if flag1 or flag2:
	# 	print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
	# elif recipient == sender:
	# 	print('Нельзя отправить письмо самому себе!')
	# elif sender == 'university.help@gmail.com':
	# 	print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
	# else:
	# 	print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
