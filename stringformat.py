team1_num = input()
team2_num = input()
score_1 = input()
score_2 = input()
team1_time = input()
team2_time = input()
time_avg = (int(team1_time) + int(team2_time)) / 2
tasks_total = int(score_1) + int(score_2)

print("В команде мастера кода участников : %s" % team1_num)
print("Итого сегодня в командах участников : %s" % team1_num,"и %s" % team2_num)
print("Команда волшебники данных решила задач: {}".format(score_2))
print("Волшебники данных решили задачи за {}".format(team2_time),"с !")
print(f"Команды решили : {score_1} и {score_2} задач")

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(f"Результат битвы : {result}")
print(f"Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")