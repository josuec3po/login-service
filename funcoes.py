import os
import subprocess
import sqlite3

def limpar_tela():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

# CREATE
def cadastro(usuario:str, senha:str):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("""INSERT INTO login_info
                            (usuario, senha) VALUES
                            (?, ?)
            """, (usuario, senha))
        conexao.commit() 
        conexao.close()
        print("Cadastro feito com sucesso!")
        print()
    except sqlite3.Error as erro:
        print(f"Erro no banco: {erro}") 
        return False
    
    

# READ
def login(usuario:str, senha:str):
    limpar_tela()
    print("LOGIN", "="*30)

    
