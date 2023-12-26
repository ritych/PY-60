def get_tons(a):
    tons = a // 1000
    return tons


a = int(input("Введите массу в килограммах "))
print('Количество тонн =', str(get_tons(a)))
