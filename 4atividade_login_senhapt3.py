import os 
os.system("cls")

login_salvo ="giuzepcomédia"
senha_salva  = "mylonzete"
tentativas = 0

for i in range(3):
    while True:
        if tentativas >- 3:
            break
        print(f"\ntantativa: {tentativas}")
        login = input(f"informe seu login: ")
        senha = input(f"digite sua senha: ")

        if login == login_salvo and senha == senha_salva:
            print("Bem vindo! ")
            break
        else:
            ("login ou senha invalida")
            tentativas += 1



