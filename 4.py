number = int(input('Введите натуральное число: '))
original = number
last_digit = original % 10
count_3 = 0
count_last = 0
count_even = 0
sum_over5 = 0
product_over7 = 1
found_over7 = False
count_0_5 = 0
while original > 0:
    digit = original % 10
    if digit == 3:
        count_3 += 1
    if digit == last_digit:
        count_last += 1
    if digit % 2 == 0:
        count_even += 1
    if digit > 5:
        sum_over5 += digit
    if digit > 7:
        product_over7 *= digit
        found_over7 = True
    if digit == 0 or digit == 5:
        count_0_5 += 1
    original //= 10
if not found_over7:
    product_over7 = 1
print(f'Количество цифр 3: {count_3}')
print(f'Количество последних цифр: {count_last - 1}')
print(f'Количество четных цифр: {count_even}')
print(f'Сумма цифр больше 5: {sum_over5}')
print(f'Произведение цифр больше 7: {product_over7}')
print(f'Количество цифр 0 и 5: {count_0_5}')