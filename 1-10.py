def get_sum(a, b):
    sum = a ** 2 + b ** 2
    return sum


def get_sub(a, b):
    sub = a ** 2 - b ** 2
    return sub


def get_mul(a, b):
    mul = a ** 2 * b ** 2
    return mul


def get_div(a, b):
    div = a ** 2 / b ** 2
    return div


a = int(input("Введите число а "))
b = int(input("Введите число b "))
if a != 0 and b != 0:
    print('Сумма квадратов =', str(get_sum(a, b)))
    print('Разность квадратов =', str(get_sub(a, b)))
    print('Произведение квадратов =', str(get_mul(a, b)))
    print('Частное квадратов =', str(get_div(a, b)))
else:
    print('Числа должны быть не равными нулю')
