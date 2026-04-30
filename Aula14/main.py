
usuarios = {
        "admin": ["admin", True],
        "joao123": ["123",False],
        "maria_dev": ["mariazinha",True]
}

def login(login, senha):
    if login in usuarios:
        values = usuarios.get(login); #valores associados à chave
        pswd = values[0] #em 0 está a senha, em 1 o status de administrador
        if senha == pswd:
            return True
        else:
            raise PermissionError("Senha inválida")
    else:
        raise KeyError("Usuário não encontrado")
    
#-------------Principal------------
try:
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    teste = login(usuario, senha)
    if (teste==True):
        print("Login bem-sucedido!")
except PermissionError as pe:
    print(pe)
except KeyError as ke:
    print(ke)