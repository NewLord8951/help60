def isPrime(X):
    x = str(X)
    n = 2
    i = 0
    while X >= n:
        i += 1
        n *= 10
    if i == 3:
        num = int(x[i-1])
        if num % 2 != 0:
            D = X // 10
            if D % 2 != 0:
                print("Да, число гиперпростое.")
            else:
                print("Нет, число не гиперпростое.")
