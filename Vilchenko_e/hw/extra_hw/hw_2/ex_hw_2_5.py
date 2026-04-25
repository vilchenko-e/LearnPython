n = int(input("Количество контейнеров: "))
containers = []

for _ in range(n):
    weight = int(input("Введите вес контейнера: "))
    if weight > 200:
        weight = 200
    containers.append(weight)

new_weight = int(input("Введите вес нового контейнера: "))
if new_weight > 200:
    new_weight = 200

# ищем позицию: как только вес в списке стал меньше нового, вставляем перед ним
position = 1
for i in range(len(containers)):
    if containers[i] < new_weight:
        position = i + 1
        break
else:
    position = len(containers) + 1  # легче всех, в конец

print(f"Номер, который получит новый контейнер: {position}")
