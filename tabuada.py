import time

#variaveis
numero = int( input("Calcular a tabuada de: ") )
limite = int( input("Calcular ate: ") )

print(f"Tabuada de {numero}")

#logica
for mult in range(1, limite + 1):
    resultado = numero * mult
    print (f"{numero} x {mult} = {resultado}")
    time.sleep(0.5)

