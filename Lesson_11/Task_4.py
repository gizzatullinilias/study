# Реализация функции count с помощью цикла while:
def count():
    i = 0
    while i <= 10:
        print(i)
        i += 1


# Реализация функции count с помощью рекурсии:
def count(n=0):
    print(n)
    if n < 10:
        count(n+1)

