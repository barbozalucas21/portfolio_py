print("----------")
print("@ Calculo de IMC")
print("----------")

#variaveis
peso= float( input("Digite seu peso: ") )
altura= float( input("Digite sua altura: ") )

#calculo do IMC
imc = peso / altura ** 2

print(f"Seu IMC é: {imc:.2f}")

print("--------------------")

if imc < 18.5:
    print("Voce esta abaixo do peso.")

elif imc <= 24.9:
    print("Seu peso e normal")

elif imc <= 29.9:
    print("Voce esta com sobrepeso")

elif imc >= 30:
    print("Voce esta obeso")

print("--------------------")