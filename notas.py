#listas
"""lista_numeros = [1, 2, 3]
lista_numeros[0] = 5

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])

lista_vazia = []

lista_vazia.append("Ola")
lista_vazia.append("Mundo")

print(lista_vazia)"""

#repeticoes com for
"""notas = []
for x in range(5):
    codigo_aluno = input("Matricula: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print("quantidade de notas:", len(notas) )

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print(f"Matricula {codigo_aluno} tirou a nota: {nota}")"""

#repeticoes com while
"""notas = []

contador = 1

while contador <= 5:
    codigo_aluno = input("Matricula: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    contador = contador + 1

print("quantidade de notas:", len(notas) )"""

#dicionario
"""pessoa = {
    "nome" : "Lucas",
    "idade" : 21,
    "peso" : 69.9
}

print( pessoa['nome'] )
print( pessoa['idade'] )
print( pessoa['peso'] )"""

player = {
    "nome" : "BarboZa",
    "level" : 1,
    "hp" : 100,
    "exp" : 0,
    "dano" : 5,
}

npcs = [
    {"nome" : "Herege", "dano" : 2, "hp" : 50, "exp" : 5},
    {"nome" : "Cataro", "dano" : 5, "hp" : 100, "exp" : 10},
    {"nome" : "Revolucionario", "dano" : 10, "hp" : 150, "exp" : 15},
    {"nome" : "Anjo caido", "dano" : 25, "hp" : 200, "exp" : 20}
]