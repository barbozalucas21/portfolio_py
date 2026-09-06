import time

#definições
usuario = {}

def cadastrar():
    matricula = input("\nDigite a matrícula: ")
    nome = input("Digite o nome: ")
    idade = int( input("Digite a idade: ") )
    usuario[matricula] = nome, idade
    
def verificar():
    for matricula, dados in usuario.items():
        nome, idade = dados
        print(f"\nMatrícula {matricula}: \n Nome: {nome} \n idade: {idade}")
        print("-----------------------------------------")
        
def buscar_matricula():
    busca = input("\nDigite a matricula que deseja buscar: ")
    
    if busca in usuario:
        nome, idade = usuario[busca]
        print("\nResultado da busca: ")
        print(f"Matricula: {busca}")
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        
    else:
        print("Matrícula não encontrada.")
        
#estilização e utilização das definições

while True:
    
    print("\n=--------------------=")
    print("@ Cadastro @")
    print("------------")
    print("1. cadastrar/alterar")
    print("2. Verificar")
    print("3. Buscar")
    print("4. sair")
    print("=--------------------=") 
    
    op = int( input("Digite a opção que deseja: ") )
    
    match op: 
        case 1:
            cadastrar()
            
        case 2:
            verificar()
            
        case 3: 
            buscar_matricula()
            
        case 4:
            print("saindo", end = '\r' )
            time.sleep(0.3)
            print("saindo.", end = '\r' )
            time.sleep(0.3)
            print("saindo..", end = '\r' )
            time.sleep(0.3)
            print("saindo...", end = '\r' )
            time.sleep(0.3)
            break
        
        case _:
            print("opção inválida.")