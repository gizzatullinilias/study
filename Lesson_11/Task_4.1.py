# Решение задачи с помощью цикла `while`:
def count():
    even_count = 0
    odd_count = 0
    i = 0
    while i <= 10:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        i += 1
    print("Количество четных чисел:", even_count)
    print("Количество нечетных чисел:", odd_count)


# Решение задачи с помощью рекурсии:
def count(n=0, even_count=0, odd_count=0):
    if n > 10:
        print("Количество четных чисел:", even_count)
        print("Количество нечетных чисел:", odd_count)
        return
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    count(n+1, even_count, odd_count)
