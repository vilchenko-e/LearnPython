word = input("Введите слово: ")

# проверка на палиндром
is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")
