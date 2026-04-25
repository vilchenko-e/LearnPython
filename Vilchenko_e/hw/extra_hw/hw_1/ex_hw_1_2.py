def sum_of_digits(n: int) -> int:
    """сумма всех цифр числа"""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def count_of_digits(n: int) -> int:
    """количество цифр в числе"""
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


num = int(input("Введите число: "))

s = sum_of_digits(num)
c = count_of_digits(num)

print(f"Сумма чисел: {s}")
print(f"Количество цифр в числе: {c}")
print(f"Разность суммы и количества цифр: {s - c}")
