n = int( input("Digite um número para verificar se é par ou ímpar: ") )

resultado = n % 2

if resultado == 0:
    print("É par!")

else:
    print("É ímpar!")