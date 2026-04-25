names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']

first_day = []
for i in range(0, len(names), 2):  # чётные индексы: 0, 2, 4, 6
    first_day.append(names[i])

print(f"Первый день: {first_day}")
