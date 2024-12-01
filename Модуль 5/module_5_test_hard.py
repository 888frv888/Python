from time import sleep

class Video:
	"""Класс описывает видео"""
	def __init__(self, title: str = '', duration: int = 0, time_now: int = 0, adult_mode: bool = False):
		self.title = title
		self.duration = duration
		self.time_now = time_now
		self.adult_mode = adult_mode

	def __str__(self):
		return self.title


class User:
	"""Класс описывает пользователей"""
	def __init__(self, nickname: str, password: int, age: int):
		self.nickname = nickname
		self.password = password  # Hashed
		self.age = age

	def __str__(self):
		"""Для удобства переопределяем неформальный ответ"""
		return self.nickname

	def __repr__(self):
		"""Переопределяем формальный ответ"""
		return [self.nickname, self.password, self.age]


class UrTube:
	"""Поздравляю !!! Этот класс описывает нового
	стопроцентного конкурента ютуба от личинок Питон-разработчиков)))"""
	_instance = None

	def __new__(cls, *args, **kwargs):				#
		if not cls._instance:						# "There can be only one"
			cls._instance = super().__new__(cls)	#
		return cls._instance						#

	def __init__(self):
		self.users = []
		self.videos = []
		self.current_user = None

	def __contains__(self, item: object):
		"""Определяем проверку наличия видео"""
		spisok = [str(vidos) for vidos in self.videos]
		return str(item) in spisok

	def log_in(self, nickname: str, password: str):
		"""Метод аутентификации пользователя"""
		for user in self.users:
			if nickname == user.nickname and hash(password) == user.password:
				self.current_user = user
				break

	def register(self, nickname: str, password: str, age: int):
		"""Метод регистрации нового пользователя"""
		name_list: list = [name.__str__() for name in self.users if nickname == name.__str__()]
		if not name_list:
			self.users.append(User(nickname, hash(password), age))
			self.log_in(nickname, password)
		else:
			print(f'Пользователь {nickname} уже существует')

	def log_out(self):
		"""Выход пользователя из УрТюба"""
		self.current_user = None

	def add(self, *vidos: object):  # Add videos in self.videos
		"""Метод добавляет новое видео в УрТюб"""
		for element in vidos:  # проходим по аргументам
			if not self.__contains__(element.__str__()):
				self.videos.append(element)

	def get_videos(self, find_video_name):
		"""Метод ищет строку в названиях видео. Выводит список найденных фильмов"""
		spisok = [str(vidos)
				  for vidos in self.videos
				  if find_video_name.lower() in str(vidos).lower()]
		return spisok

	def watch_video(self, video_name: str):
		"""Метод проигрывает видео. Перед этим проводит ряд проверок"""
		if self.current_user is None:
			print('Войдите в аккаунт, чтобы смотреть видео')
			return
		for film in self.videos:
			if film.title.lower() == video_name.lower():
				if self.current_user.age < 18:
					print('Вам нет 18 лет, пожалуйста покиньте страницу')
					break
				for now_playing in range(film.time_now + 1, film.duration + 1):
					print(now_playing, end=' ')
					sleep(1)
				film.time_now = 0
				print('Конец видео')
				break



if __name__ == '__main__':
	ur = UrTube()
	v1 = Video('Лучший язык программирования 2024 года', 200)
	v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

	# Добавление видео
	ur.add(v1, v2)

	# Проверка поиска
	print(ur.get_videos('лучший'))
	print(ur.get_videos('ПРОГ'))
	ur.watch_video('Для чего девушкам парень программист?')
	ur.register('vasya_pupkin', 'lolkekcheburek', 13)
	ur.watch_video('Для чего девушкам парень программист?')
	ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
	ur.watch_video('Для чего девушкам парень программист?')

	# Проверка входа в другой аккаунт
	ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
	print(ur.current_user)

	# Попытка воспроизведения несуществующего видео
	ur.watch_video('Лучший язык программирования 2024 года!')