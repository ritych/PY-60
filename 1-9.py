def get_average_geometric(a, b):
    av = (a * b) ** 0.5
    return av


a = int(input("Введите число а "))
b = int(input("Введите число b "))
if a > 0 and b > 0:
    print('Среднее геометрическое =', str(get_average_geometric(a, b)))
else:
    print('Числа должны быть неотрицательными')
