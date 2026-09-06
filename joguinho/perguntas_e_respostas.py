import random
from perguntas import perguntas

while True:
    print("-----------------")
    print("1. Necessário  ")
    print("2. Normais     ")
    print("3. Diferentes  ")
    print("4. Desconfortáveis")
    print("5. sair        ")
    print("-----------------")

    op = int(input("Digite a opção que deseja jogar: "))

    match op:
        case 1: 
            while True:
                print(random.choice(perguntas["necessarias"]))

                n = int(input("Digite 1 para continuar ou 2 para sair: "))

                if n == 1:
                    continue

                else: 
                    break

        case 2: 
                    while True:
                        print(random.choice(perguntas["normais"]))
        
                        n = int(input("Digite 1 para continuar ou 2 para sair: "))
        
                        if n == 1:
                            continue
        
                        else: 
                            break

        case 3: 
                    while True:
                        print(random.choice(perguntas["diferentes"]))
        
                        n = int(input("Digite 1 para continuar ou 2 para sair: "))
        
                        if n == 1:
                            continue
        
                        else: 
                            break

        case 4: 
                    while True:
                        print(random.choice(perguntas["desconfortaveis"]))
        
                        n = int(input("Digite 1 para continuar ou 2 para sair: "))
        
                        if n == 1:
                            continue
        
                        else: 
                            break    

        case 5:
              break     

        case 6:
              print("Opção inválida!")
              continue       