def get_numeric(a):
    digit2 = a%100
    d = digit2//10
    u = digit2%10
    return u, d


a = int(input("Введите число A "))
if 99 < a < 1000:
    print('Полученные числа =', str(get_numeric(a)))
else:
    print('Число должно быть 3-х значным')
