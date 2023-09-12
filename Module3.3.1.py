a = float(input('Введите сторону треугольника: '))
b = float(input('Введите сторону треугольника: '))
c = float(input('Введите сторону треугольника: '))


def area(a, b, c):
    p: float = (a + b + c) / 2
    s: float = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s


print(f'Площадь треугольника равна {area(a, b, c)}')
