print("Mayor y menor de una lista de numeros")

tamano_lista = int(input("Dime cuantos valores quieres introducir en la lista de números: "))

lista_numeros = []

for numeros in range(1, tamano_lista + 1):
    valor = int(input("numero {}: ".format(numeros)))
    lista_numeros.append(valor)
    print(lista_numeros)

maximo = max(lista_numeros)

minimo = min(lista_numeros)

print("Nº pequeño: {}".format(minimo))
print("Nº grande: {}".format(maximo))
