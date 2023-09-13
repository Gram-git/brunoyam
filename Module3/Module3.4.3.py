import json


def login_function(login, passwrd):
    with open('data_register', 'r') as f:
        data_register = json.load(f)
    if login in data_register.keys():
        if passwrd == data_register[login]:
            print('Логин и пароль верны')
        else:
            print('Неверный пароль')
    else:
        print('Пользователь с таким именем не найден')

login_function(input('Введите логин: '), input('Введите пароль: '))