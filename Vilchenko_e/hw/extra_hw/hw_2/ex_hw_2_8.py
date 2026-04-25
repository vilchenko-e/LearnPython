n = int(input("Количество чисел: "))
lst = []
for i in range(n):
    lst.append(int(input("Введите число: ")))


# сортировка вставками
for i in range(1, len(lst)):
    key = lst[i]
    j = i - 1
    while j >= 0 and lst[j] > key:
        lst[j + 1] = lst[j]
        j -= 1
    lst[j + 1] = key

print(f"Отсортированный список: {lst}")
