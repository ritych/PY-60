def get_kb(a):
    kb = a // 1024
    return kb


a = int(input("Введите размер файла в байтах "))
print('Количество килобайт =', str(get_kb(a)))
