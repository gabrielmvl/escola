import bcrypt
import uuid
import csv
import getpass

Dados = {}

def gerarSalt():
    salt = bcrypt.gensalt()
    return salt

def gerar_id():
    id = str(uuid.uuid4())
    return id

def BancoDeDados():

    with open('Usuarios.csv', 'r', encoding='utf-8') as f:
        BancoDeDados = csv.reader(f, delimiter=';')
        for usuario in BancoDeDados:
            Email = usuario[0]
            UserName = usuario[1]
            Senha = usuario[2]
            Id = usuario[3]
            Dados[Email] = [UserName, Senha, Id]

def ColetarDados(metodo):
    Email = input("Digite seu e-mail: ")

    if metodo != "registro":
        UserName = input("Digite seu username: ")

    while True:
        Senha = getpass.getpass("Digite sua senha: ")
        ComfirmarSenha = getpass.getpass("Confirme sua senha: ")

        if Senha != ComfirmarSenha:
            print("Senhas não coencidem")

        else: break

    return UserName, Email, Senha

def registro(Username, Email, Senha):
    with open('Usuarios.csv', 'a', encoding='utf-8') as f:
        file = csv

def Menu():
    Menu = input("""Bem vindo ao menu:

    1 - Registrar-se
    2 - Login
    3 - Esqueci a senha

    Qual Opção deseja: 
""")

    match Menu:
        case '1':
            