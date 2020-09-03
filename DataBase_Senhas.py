import sqlite3

MASTER_PASSWORD = "123456" #JAMAIS ARMAZENAR SENHA ASSIM, AINDA MAIS NO CÓDIGO,MAS COMO É UM PROJETO SIMPLES PARA APRENDIZADO NÃO HÁ PROBLEMA

senha = input("Insira sua senha master: ")
if senha != MASTER_PASSWORD:
    print("Senha Inválida! Encerrando...")
    exit()


conn = sqlite3.connect("testedb.db")

cursor = conn.cursor()

cursor.execute: ("""
CREATE TABLE IF NOT EXISTS `users` (
	`Service`	TEXT NOT NULL,
	`Username`	TEXT NOT NULL,
	`Password`	TEXT NOT NULL
);
);
""")

def menu ():
    print("**********************************")
    print("* i : inserir nova senha         *")
    print("* l : listar serviços salvos     *")
    print("* r : recuperar uma senha        *")
    print("* s : sair                       *")
    print("**********************************")

def get_password (Service): 
    cursor.execute(f'''
        SELECT Username, Password FROM users 
        WHERE Service = '{Service}'
    ''')

#SELECT UTILIZADO PARA BUSCAR ALGO NO BANCO DE DADOS, 
#WHERE SENDO O LUGAR ONDE VAI PEGAR A INFORMAÇÃO, NESSE CASO A SENHA.

    if cursor.rowcount == 0:
        print ("Serviço não cadastrado (Use 'l' para verificar os serviços).")

    for user in cursor.fetchall():
        print(user)

def insert_password(Service, Username, Password):
    cursor.execute(f'''
        INSERT INTO users (Service, Username, Password)
        VALUES ('{Service}', '{Username}', '{Password}')
    ''')
    conn.commit()

def show_services():
    cursor.execute('''
        SELECT Service, Username, Password FROM users;
    ''')
    for Service, Username, Password in cursor.fetchall():

        print(Service, Username, Password )
        

while True:
    menu()
    op = input("O que deseja fazer?")
    if op not in ["i", "l", "r", "s"]:
        print("Opção Inválida!!")
        continue

    if op == "s":
        break

    if op == "i":
        Service = input("Qual o nome do serviço? ")
        Username = input("Qual o nome do usuário? ")
        Password = input("Qual a senha? ")
        insert_password(Service, Username, Password)

    if op == "l":
        show_services()

    if op == "r":
        Service = input("Qual o serviço para o qual quer a senha?")
        get_password(Service)


conn.close()

