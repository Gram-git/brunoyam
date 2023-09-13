import json

data_register: dict = {'admin': 'admin'}
with open('data_register', 'w') as f:
    json.dump(data_register, f)


def register(login, passwrd):
    with open('data_register', 'r') as f:
        data_register = json.load(f)
    if login not in data_register.keys():
        data_register[login] = passwrd
        with open('data_register', 'w') as f:
            json.dump(data_register, f)
    else:
        print('Пользователь с таким именем уже существует!')


register(input('Введите логин: '), input('Введите пароль: '))
