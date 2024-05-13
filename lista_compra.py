print("Programa lista de la compra")

lista_compra = []

salir = True

while salir == True:
    opcion = input("¿Qué deseas comprar? [Q] para salir: ")

    if opcion != "Q":
        afirmativo = input("¿Seguro que quieres añadir {}? S/N ".format(opcion))
        if afirmativo == "S":
            repetido = opcion in lista_compra
            if repetido == False:
                lista_compra.append(opcion)
                print("!Añado {} a la lista de la compra¡".format(opcion))
                print(lista_compra)

            else:
                print("{} ya se encuentra en la lista de la compra".format(opcion))
                print(lista_compra)

        elif afirmativo == "N":
            print("No añades {} a la lista de la compra".format(opcion))
            print(lista_compra)

    elif opcion == "Q":
        print("Sales del programa.")
        print(lista_compra)
        salir = False