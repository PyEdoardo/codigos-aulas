def procLogin(login, usuarios):
    usuarios = {}
    if login not in usuarios:
        return 'Não existe este usuário!'
    else:
        return usuarios[login]