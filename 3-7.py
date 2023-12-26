def func(a, b, c):
    return a < b < c or c < b < a


a = int(input("Введите число A "))
b = int(input("Введите число B "))
c = int(input("Введите число C "))
print(func(a, b, c))
