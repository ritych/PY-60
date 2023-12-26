def get_bina(a, b):
    BinA = a // b
    return BinA


a = int(input("Введите число A "))
b = int(input("Введите число B "))
if a > b:
    print('Количество B в А =', str(get_bina(a, b)))
else:
    print('A должно быть больше B')
