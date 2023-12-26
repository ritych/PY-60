def get_reverse(a):
    d = a // 10
    u = a % 10
    wrk = u * 10 + d
    return wrk


a = int(input("Введите число A "))
if 9 < a < 100:
    print('Перестановка цифр =', str(get_reverse(a)))
else:
    print('Число должно быть 2-х значным')
