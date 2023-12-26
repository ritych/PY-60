def get_square(a):
    s = 6*a*a
    return s


def get_volume(a):
    v = a**3
    return v


length_a = int(input("Введите длину ребра куба "))
print('Площадь поверхности =', str(get_square(length_a)), 'Объем =', str(get_volume(length_a)))
