def get_hundred(a):
    wrk = a//100
    return wrk


a = int(input("Введите число A "))
if 99 < a < 1000:
    print('Количество сотен =', str(get_hundred(a)))
else:
    print('Число должно быть 3-х значным')
