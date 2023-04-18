def login():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    if login in users:
        if users[login] == password:
            print('Доступ разрешен')
        else:
            print('Доступ запрещен')
    else:
        users[login] = password
        print('Регистрация прошла успешно')
