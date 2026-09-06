#funcao para verificar multiplos
def multiplo(numero, n):
    if numero % n == 0:
        return True
    return False

#laco para teste de numeros
for numero in range(1,101):
    if multiplo(numero, 3) and multiplo(numero, 5):
        print(f"O número {numero} é: FizzBuzz")

    elif multiplo(numero, 3):
        print(f"O número {numero} é: Fizz")

    elif multiplo(numero, 5):
        print(f"O número {numero} é: Buzz")