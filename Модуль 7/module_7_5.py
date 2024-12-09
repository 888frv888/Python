import os, time

directory = "."
for root, dirs, files in os.walk(directory):
	for file in files:
		filepath = f"{os.path.join(directory)}\\{file}"
		filetime = os.path.getmtime(file)
		formatted_time = time.strftime("%d.%m.%Y %h:%m", time.localtime(filetime))
		filesize = os.path.getsize(file)
		parent_dir = os.getcwd()
		print(f"Обнаружен файл: {file}, "
			  f"Путь: {filepath}, "
			  f"Размер: {filesize} байт, "
			  f"Время изменения: {formatted_time}, "
			  f"Родительская директория: {parent_dir}")
