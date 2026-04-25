n = int(input("Количество элементов: "))
lst = []
for i in range(n):
    lst.append(int(input("Введите элемент: ")))
k = int(input("Сдвиг: "))

k = k % len(lst)
lst[:] = lst[-k:] + lst[:-k]

print(f"Сдвинутый список: {lst}")
