def get_square(a):
    s = a*a
    return s


length = int(input("Введите длину стороны квадрата "))
print('Площадь =', str(get_square(length)))
