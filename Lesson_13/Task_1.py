def calculate():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operator = input("Введите операцию (+, -, *, /): ")

    if operator not in ["+", "-", "*", "/"]:
        return "Неверный оператор!"

    try:
        result = eval(f"{num1} {operator} {num2}")
        return  {result}
    except ZeroDivisionError:
        return "Деление на ноль невозможно!"
    except Exception as e:
        return f"Ошибка: {str(e)}"
