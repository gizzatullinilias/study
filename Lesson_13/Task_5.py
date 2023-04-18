import random

def countdown(numbers):
    for number in numbers:
        for i in range(number, -1, -1):
            print(i)
        print("Пуск!")
numbers = [random.randint(0, 10) for _ in range(5)]
countdown(numbers)
