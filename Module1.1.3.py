num1 = float(input('Введите первое число для сравнения: '))
num2 = float(input('Введите второе число для сравнения: '))
max0 = (num1>=num2)*num1 + (num1<num2)*num2
print(f'Наибольшее значение: {max0}')