import subprocess
import os
resposta = 0

def menu():
    print("Bem vindo ao login de JOSH.COM ==============")
    print("[1] Login")
    print("[2] Cadastro")
    print("[3] Sair")

def limpar_tela():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

while resposta != 3:
    
    menu()
    try:
        resposta = int(input("Digite a opção desejada: "))

        if resposta == 1:
            print("1")
        elif resposta == 2:
            print("2")
        elif resposta == 3:
            break
        else:
            print("Valor fora do range! Opção entre 1, 2 e 3")
    except ValueError:
        print("Valor inválido! Por favor digite um número.")




    


    