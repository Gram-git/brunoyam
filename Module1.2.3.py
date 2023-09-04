status: bool = False
password: str = ''
while status == False:
    if len(password) > 8:
        if password.islower() == False:
            if password.isupper() == False:
                status = True
            else:
                password: str = input(
                    'Пароль должен содержать более 8 символов и включать как прописные так и заглавные буквы. '
                    '\nВведите пароль: ')
        else:
            password: str = input(
                'Пароль должен содержать более 8 символов и включать как прописные так и заглавные буквы. \nВведите '
                'пароль: ')
    else:
        password: str = input(
            'Пароль должен содержать более 8 символов и включать как прописные так и заглавные буквы. \nВведите '
            'пароль: ')

print (f'Пароль: "{password}" принят.')

