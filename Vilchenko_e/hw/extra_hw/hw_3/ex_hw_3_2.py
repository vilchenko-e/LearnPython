def merge_sorted_lists(list1, list2):
    merged = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            if not merged or merged[-1] != list1[i]:
                merged.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            if not merged or merged[-1] != list2[j]:
                merged.append(list2[j])
            j += 1
        else:
            if not merged or merged[-1] != list1[i]:
                merged.append(list1[i])
            i += 1
            j += 1

    while i < len(list1):
        if not merged or merged[-1] != list1[i]:
            merged.append(list1[i])
        i += 1

    while j < len(list2):
        if not merged or merged[-1] != list2[j]:
            merged.append(list2[j])
        j += 1

    return merged


n1 = int(input("Количество элементов первого списка: "))
list1 = []
for i in range(n1):
    list1.append(int(input(f"Элемент {i + 1}: ")))

n2 = int(input("Количество элементов второго списка: "))
list2 = []
for i in range(n2):
    list2.append(int(input(f"Элемент {i + 1}: ")))

merged = merge_sorted_lists(list1, list2)
print(f"Объединённый список: {merged}")
