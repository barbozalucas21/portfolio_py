def soma(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input("Valor1: "))
    valor2 = int(input("Valor2: "))
    resposta = soma(valor1, valor2)

    print(f"{valor1} + {valor2} = {resposta}")