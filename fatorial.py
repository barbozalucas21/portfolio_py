#funcao
def fatorial(n):
    resultado = n
    for i in range(n - 1, 0, -1):
        resultado *= i
    return resultado

while True:

    #variaveis
    n = input("Digite um numero para descobrir seu fatorial(ou 'sair' para encerrar ): ").lower()

    #logica
    if n == "sair":
        break

    else:
        n = int(n)
        if n >0:
            final = fatorial(n)
            print(f"O Fatorial do número {n} é: {final}")

        else:
            print(f"O Fatorial do número {n} é: 1")
