price = int(input('Сколько надо заплатить '))
vsego = 0

vsego += price // 25
price = price % 25

vsego += price // 10
price = price % 10

vsego += price // 5
price = price % 5

vsego += price // 1

print(f'Нужно монет {vsego}')

