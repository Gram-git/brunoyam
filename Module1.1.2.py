road_length = 109
v=int(input('Введите скорость байкера: '))
t=int(input('Укажите время остановки байкера: '))
result = v*t % road_length
print(f'Байкер Вася остановиться на отметке {result}км через {t} часов.')