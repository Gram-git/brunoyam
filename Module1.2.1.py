num1 = int(input('Введите первое целое число: '))
num2 = int(input('Введите второе целое число: '))
num3 = int(input('Введите третье целое число: '))

if (num1 == num2) and (num1 == num3):
    print(3)
elif (num1 == num2) or (num2 == num3) or (num1 == num3):
    print(2)
else:
    print(0)