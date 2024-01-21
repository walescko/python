#Programa 9.6 - Controle de uma agenda de telefone
agenda = []
def pede_nome():
    return input("Nome: ")
def pede_telefone():
    return input("Telefone: ")

def mostra_dados(nome, telefone):
    print(f"Nome: {nome} Telefone: {telefone}")

def pede_nome_arquivo():
    return input("Nome do arquivo: ")

def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
        return None

def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])

def apaga():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        del agenda[p]
    else:
        print("Nome não encontrado.")

def altera():
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado:")
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome, telefone]
    else:
        print("Nome não encontrado.")

def listar():
    print("\nAgenda\n\n------")
    for e in agenda:
        mostra_dados(e[0], e[1])
    print("--------\n")

def read():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        agenda = []
        for l in arquivo.readlines():
            nome, telefone = l.strip().strip("#")
            agenda.append([nome, telefone])

def gravar():
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}\n")

def valida_faixa_inteiro(pergunta, begin, end):
    while True:
        try:
            value = int(input(pergunta))
            if begin <= value <= end:
                return value
        except ValueError:
            print(f"Valor inválido, por favor digitar entre {begin} e {end}")

def menu():
    print("""
        1 - Novo
        2 - Alterar
        3 - Apagar
        4 - Listar
        5 - Gravar
        6 - Ler
        0 - Sair
    """)
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)

while True:
    option = menu()
    if option == 0:
        break
    elif option == 1:
        novo()
    elif option == 2:
        altera()
    elif option == 3:
        apaga()
    elif option == 4:
        listar()
    elif option == 5:
        gravar()
    elif option == 6:
        read()
