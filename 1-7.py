def get_length(r):
    l = 2*3.14*r
    return l


def get_square(r):
    s = 3.14*r**2
    return s


radius = int(input("Введите радиус окружности "))
print('Длина окружности =', str(get_length(radius)), 'Площадь круга =', str(get_square(radius)))
