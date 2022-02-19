def senhasegura(psw):
    esp = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
    val = True
    fal = 6 - len(psw)

    if len(psw) < 6:
        val = False
        print(fal)
        #print(f'Você precisa adicionar {6 - len(psw)} caracteres, o mínimo é 6 para ter uma senha segura.')

    if not any(cara.isdigit() for cara in psw):
        val = False
        #print('Sua senha precisa conter no mínimo 1 digito numérico.')

    if not any(cara.isupper() for cara in psw):
        val = False
        #print('Sua senha precisa conter no mínimo 1 letra maiúscula.')

    if not any(cara.islower() for cara in psw):
        val = False
        #print('Sua senha precisa conter no mínimo 1 letra minúscula.')

    if not any(cara in esp for cara in psw):
        val = False
        #print('Sua senha precisa conter no mínimo 1 caractere especial: ! @ # $ % ^ & * ( ) - +')

    return fal

psw = str(input('Digite sua senha: ')).strip()
senhasegura(psw)
