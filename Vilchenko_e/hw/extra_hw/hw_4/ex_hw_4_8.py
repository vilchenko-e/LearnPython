message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
encrypted = ''

for ch in message:
    if ch.lower() in alphabet:
        is_upper = ch.isupper()
        idx = alphabet.index(ch.lower())
        new_idx = (idx + shift) % len(alphabet)
        new_ch = alphabet[new_idx]
        encrypted += new_ch.upper() if is_upper else new_ch
    else:
        encrypted += ch

print(f"Зашифрованное сообщение: {encrypted}")
