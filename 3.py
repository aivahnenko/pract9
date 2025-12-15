price = int(input('Сколько надо заплатить: '))
monety = [25, 10, 5, 1]
vsego = 0
i = 0
while price > 0:
    m = monety[i]
    vsego += price // m
    price = price % m
    i += 1
print('Нужно монет:', vsego)