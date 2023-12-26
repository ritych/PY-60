def func(a, b):
    return a % 2 != 0 or b % 2 != 0


a = int(input("Введите число A "))
b = int(input("Введите число B "))
print(func(a, b))
