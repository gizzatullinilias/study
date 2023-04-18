names_list = []
def hello():
    name = input("Введите ваше имя: ")
    if name in names_list:
        print("Привет, {0}!".format(name))
    else:
        names_list.append(name)
        print("Привет, {0}! Рад знакомству!".format(name))

hello()
