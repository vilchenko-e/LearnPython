s = input("Введите строку: ")

first = s.find('h')
last = s.rfind('h')

middle = s[first + 1:last]
reversed_middle = middle[::-1]

print(f"Развёрнутая последовательность между первым и последним h: {reversed_middle}")
