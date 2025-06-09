m: list = [56, 9, 11, 2, 9, 3]


def sort_max(arg1):
    exc = []
    result = ''
    while len(exc) < len(arg1):
        var1: int = 0
        for i in arg1:
            if i not in exc:
                if len(str(i)) == len(str(var1)):
                    if var1 < i:
                        var1 = i
                elif len(str(i)) > len(str(var1)):
                    x = int(str(var1) + (len(str(i)) - len(str(var1))) * '9')
                    if x < i:
                        var1 = i
                elif len(str(i)) < len(str(var1)):
                    x = int(str(i) + (len(str(var1)) - len(str(i))) * '9')
                    if var1 < x:
                        var1 = i
        for i in range(arg1.count(var1)):
            exc.append(var1)
    for i in exc:
        result += str(i)
    return int(result)


print(m)
print(sort_max(m))


def largestNumber(nums):
    # Преобразование чисел в строки
    nums = [str(num) for num in nums]

    # Функция сравнения для сортировки
    def custom_compare(x, y):
        return int(x + y) - int(y + x)

    # Реализация сортировки пузырьком
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):
            if custom_compare(nums[j], nums[j + 1]) < 0:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    # Объединение отсортированных чисел в строку
    result = ''.join(nums)

    # Удаление ведущих нулей
    result = result.lstrip('0')

    # Если строка пуста (все числа были нулями), вернуть '0'
    if not result:
        return '0'

    return result


# Пример использования
nums = [56, 9, 11, 2, 45, 9, 91, 54, 56, 5]
result = largestNumber(nums)
print(result)  # Вывод: '956211'
