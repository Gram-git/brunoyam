x = str(input('Введите целое число: '))
summ = 0
for i in x:
    summ +=int(i)
print(f'Сумма цифр числа {x} равна - {summ}')