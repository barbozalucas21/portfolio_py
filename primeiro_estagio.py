fluxo_caixa = []

def fluxo_c(): 
    nome = input("Nome: ")
    valor = float( input("Valor: ") )
    fluxo_caixa.append({
        "nome" : nome,
        "valor" : valor
    })

print("-----------")
print("@ Fluxo Caixa")
print("-----------")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("\n# Digite outro numero para encerrar #\n")

while True:

    opcao = int( input("Digite a opcao: ") )

    if opcao == 1: 
        fluxo_c()
    elif opcao == 2:
        fluxo_c()
    else:
        break

#nota fiscal
total = 0 
for fc in fluxo_caixa:
    print("Nome:", fc['nome'], ", Valor R$", fc['valor'])
    total = total + fc['valor']

print(f"Saldo atual: R$ {total}")