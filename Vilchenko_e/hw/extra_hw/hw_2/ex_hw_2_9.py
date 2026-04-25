n = int(input("Количество чисел: "))
lst = []
for i in range(n):
    lst.append(int(input("Введите число: ")))

print("Чётные в обратном порядке:")
for i in range(len(lst) - 1, -1, -1):
    if lst[i] % 2 == 0:
        print(lst[i])
