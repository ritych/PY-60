def get_metr(a):
    metr = a // 100
    return metr


a = int(input("Введите расстояние в сантиметрах "))
print('Количество целых метров =', str(get_metr(a)))
