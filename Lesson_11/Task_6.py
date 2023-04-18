# Решение задачи с помощью цикла while:
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Решение задачи с помощью рекурсии:
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
