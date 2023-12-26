def get_sum(a):
    d = a // 10
    u = a % 10
    wrk = d + u
    return wrk


def get_mul(a):
    d = a // 10
    u = a % 10
    wrk = d * u
    return wrk


a = int(input("Введите число A "))
if 9 < a < 100:
    print('Сумма цифр =', str(get_sum(a)))
    print('Произведение цифр =', str(get_mul(a)))
else:
    print('Число должно быть 2-х значным')
