def get_square(a, b, c):
    s = 2*(a*b+b*c+a*c)
    return s


def get_volume(a, b, c):
    v = a*b*c
    return v


length_a = int(input("Введите длину параллелепипеда a "))
length_b = int(input("Введите длину параллелепипеда b "))
length_c = int(input("Введите длину параллелепипеда c "))

print('Площадь поверхности =', str(get_square(length_a, length_b, length_c)), 'Объем =', str(get_volume(length_a, length_b, length_c)))
