n = int(input("Кол-во чисел: "))
seq = []
for _ in range(n):
    seq.append(int(input("Число: ")))

print(f"Последовательность: {seq}")

add = []
for start in range(len(seq)):
    sub = seq[start:]
    if sub == sub[::-1]:
        add = seq[:start][::-1]
        break

print(f"Нужно приписать чисел: {len(add)}")
print(f"Сами числа: {add}")
