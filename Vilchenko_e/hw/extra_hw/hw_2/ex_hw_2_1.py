n = int(input("Введите число: "))

result = []
for i in range(1, n + 1, 2):
    result.append(i)

print(f"Список из нечётных чисел от одного до N: {result}")
