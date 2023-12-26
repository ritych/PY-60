def get_dozens(a):
    wrk = a // 10
    return wrk


def get_units(a):
    wrk = a % 10
    return wrk


a = int(input("Введите число A "))
if 9 < a < 100:
    print('Десятки =', str(get_dozens(a)))
    print('Еденицы =', str(get_units(a)))
else:
    print('Число должно быть 2-х значным')
