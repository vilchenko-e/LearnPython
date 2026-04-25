n = int(input("Кол-во человек: "))
k = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {k}-й человек")

circle = list(range(1, n + 1))
current = 0

while len(circle) > 1:
    print(f"\nТекущий круг людей: {circle}")
    print(f"Начало счёта с номера {circle[current]}")

    remove_idx = (current + k - 1) % len(circle)
    removed = circle.pop(remove_idx)
    print(f"Выбывает человек под номером {removed}")

    current = remove_idx % len(circle) if circle else 0

print(f"\nОстался человек под номером {circle[0]}")
