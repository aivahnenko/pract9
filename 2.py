print('Введи имена, пустая строка - стоп')
name = input('Имя: ')
nomer = 0
a_gde = -1
l_gde = -1
while name != "":
    if name == 'Александра':
        a_gde = nomer
    if name == 'Левон':
        l_gde = nomer
    nomer += 1
    name = input('Имя: ')
if a_gde >= 0 and l_gde > a_gde:
    mezhdu = l_gde - a_gde - 1
else:
    mezhdu = 0

print(f'Между ними {mezhdu}')
