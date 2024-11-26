def sum_of_digits(a):
    s = 0
    while a > 0:
        s += a % 10
        a = a // 10
    return s


a = int(input("Введите число:"))
for i in range(0, a + 1):
    s = sum_of_digits(i)
    for j in range(2, 10):
        s1 = sum_of_digits(i * j)
        if s != s1:
            break
    else:
        print("%d " % i, end="")
