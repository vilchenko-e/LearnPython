text = input("Введите текст: ")

vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
result = []

for ch in text:
    if ch.lower() in vowels:
        result.append(ch)

print(f"Список гласных букв: {result}")
print(f"Длина списка: {len(result)}")
