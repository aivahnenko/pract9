n = int(input('введите число n '))
i = 1
while i <= n:
    if i < 5 or (i > 9 and i < 17) or (i > 37 and i < 78) or i > 87:
        print(i)
    i += 1