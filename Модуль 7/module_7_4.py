# данные первой команды
team1_name = "Мастера кода"
team1_num: int = 5
team1_time = 1552.512
score_1: int = 40

# данные второй команды
team2_name = "Волшебники данных"
team2_num: int = 6
team2_time  = 2153.31451
score_2: int = 42

# итоговые данные
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
	challenge_result = f"победа команды {team1_name}!"
elif score_2 > score_1 or score_1 == score_2 and team1_time > team2_time:
	challenge_result = f"победа команды {team2_name}!"
else:
	challenge_result = "ничья!"


# использование %
print("В команде %s участников: %s!" % (team1_name, team1_num))
print("Итого сегодня в командах участников: %d и %d!" % (team1_num, team2_num))

# использование format
print("Команда {} решила задач: {} !".format(team2_name, score_2))
print("Команда {name} решила задачи за {time} с!".format(name=team2_name, time=team2_time))

# использование f строк
print(f"Команды решили {score_1} и {score_2} задач")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")