import os
os.system("cls")

login_salvo = "zezinho123"
senha_salva = "mito22"

while True:
    login = input(f"digite o seu login: ")
    senha = input(f"digite sua senha: ")

    if login == login_salvo and senha == senha_salva:
        print("bem-vindo!")
        break
    else:
        print("login ou senha invalida")


    

