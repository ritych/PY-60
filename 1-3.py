def get_square(a, b):
    s = a*b
    return s


def get_perimetr(a, b):
    p = 2*(a+b)
    return p


length_a = int(input("Введите длину cтороны a "))
length_b = int(input("Введите длину cтороны b "))
print('Площадь =', str(get_square(length_a, length_b)), 'Периметр =', str(get_perimetr(length_a, length_b)))
