```python
number = int(input('Введите натуральное число '))
original = number
last_digit = original % 10

count_3 = 0
count_last = 0
count_even = 0
sum_over5 = 0
product_over7 = 1
count_over7 = 0
count_0_5 = 0

while original > 0:
    digit = original % 10
    count_last += (digit == last_digit)
    count_even += (digit % 2 == 0)
    count_0_5 += (digit == 0) + (digit == 5)
    count_3 += (digit == 3)
    sum_over5 += (digit > 5) * digit
    product_over7 *= (digit > 7) * digit + (digit <= 7)
    count_over7 += (digit > 7)
    original //= 10

product_over7 = product_over7 if count_over7 > 0 else 0

print(f'Количество цифр 3: {count_3}')
print(f'Количество последних цифр: {count_last}')
print(f'Количество четных цифр: {count_even}')
print(f'Сумма цифр больше 5: {sum_over5}')
print(f'Произведение цифр больше 7: {product_over7}')
print(f'Количество цифр 0 и 5: {count_0_5}')
```
