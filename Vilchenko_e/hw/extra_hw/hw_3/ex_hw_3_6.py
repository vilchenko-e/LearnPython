n_skates = int(input("Кол-во коньков: "))
skates = []
for i in range(1, n_skates + 1):
    size = int(input(f"Размер {i}-й пары: "))
    skates.append(size)

n_people = int(input("Кол-во людей: "))
people = []
for i in range(1, n_people + 1):
    size = int(input(f"Размер ноги {i}-го человека: "))
    people.append(size)

skates.sort()
people.sort()

count = 0
i, j = 0, 0
while i < len(skates) and j < len(people):
    if skates[i] >= people[j]:
        count += 1
        i += 1
        j += 1
    else:
        i += 1

print(f"Наибольшее кол-во людей, которые могут взять ролики: {count}")
