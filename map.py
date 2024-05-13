import random
numero = 1
objeto = []
while numero < 11:
    lista_aleatoria = [random.randint(1, 15) for _ in range(2)]
    numero += 1
    objeto.append(lista_aleatoria)

print(objeto)

