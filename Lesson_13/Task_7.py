def hello(func):
    def wrapper():
        name = func()
        print("Привет,", name + "!")
    return wrapper
@hello
def get_name():
    name = input('Введите имя: ')
    return name
get_name()

