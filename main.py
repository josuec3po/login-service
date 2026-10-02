import funcoes

resposta = 0

def menu():
    print("Bem vindo ao login de JOSH.COM ==============")
    print("[1] Login")
    print("[2] Cadastro")
    print("[3] Sair")

while resposta != 3:
    
    menu()
    try:
        resposta = int(input("Digite a opção desejada: "))

        if resposta == 1:
            funcoes.limpar_tela()
            print("1")
            print("LOGIN", "="*30)
            usuario = str(input("Usuario: "))
            senha = str(input("Senha: "))
        elif resposta == 2:
            funcoes.limpar_tela()
            print("CADASTRO", "="*20)
            usuario = str(input("Usuario: "))
            senha = str(input("Senha: "))
            funcoes.cadastro(usuario, senha)
        elif resposta == 3:
            break
        else:
            print("Valor fora do range! Opção entre 1, 2 e 3")
    except ValueError:
        print("Valor inválido! Por favor digite um número.")




    


    