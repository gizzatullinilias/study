# 1. Создайте функцию calculator, которая принимает у пользователя два числа и операцию(+, -, /, *), а возвращает результат. Предусмотрите предупреждение об ошибке при делении на 0.
def calculator():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operator = input("Введите операцию (+, -, /, *): ")

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        if num2 == 0:
            print("Ошибка: нельзя делить на 0!")
        else:
            print(num1 / num2)
    else:
        print("Ошибка: неизвестная операция!")
