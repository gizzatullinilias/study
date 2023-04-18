# Решение задачи с помощью цикла while:
def fibonacci():
    fib_list = [0, 1]
    while True:
        next_fib = fib_list[-1] + fib_list[-2]
        if next_fib >= 100:
            break
        fib_list.append(next_fib)
    return fib_list


# Решение задачи с помощью рекурсии:
def fibonacci(n=0, fib_list=[0, 1]):
    if fib_list[-1] >= 100:
        return fib_list[:-1]
    next_fib = fib_list[-1] + fib_list[-2]
    fib_list.append(next_fib)
    return fibonacci(n+1, fib_list)
