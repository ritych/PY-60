def get_bina(a, b):
    # BinA = a//b
    # wrk = a - (BinA * b)
    wrk = a % b
    return wrk


a = int(input("Введите число A "))
b = int(input("Введите число B "))
if a > b:
    print('Длина не занятой части =', str(get_bina(a, b)))
else:
    print('A должно быть больше B')
