from random import randint
import os
import math

# Vidas
VIDA_PIKACHU = 80
VIDA_SQUIRTLE = 90

TAMANO_BARRA = 20

vida_actual_pikachu = 80
vida_actual_squirtle = 90


segmento_pikachu1 = vida_actual_pikachu / VIDA_PIKACHU
segmento_pikachu2 = TAMANO_BARRA * segmento_pikachu1
barra_pikachu = "#" * int(segmento_pikachu2)
espacios_pikachu = " " * math.ceil(int(TAMANO_BARRA - segmento_pikachu2))

segmento_squirtle1 = vida_actual_squirtle / VIDA_SQUIRTLE
segmento_squirtle2 = 10 * segmento_squirtle1
barra_squirtle = "#" * int(segmento_squirtle2)
espacios_squirtle = " " * int(TAMANO_BARRA - segmento_squirtle2)

while vida_actual_pikachu > 0 and vida_actual_squirtle > 0:
    # Ocurre el combate

    # Turno de pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        #Bola voltio
        print("Pikachu ataca con Bola Voltio")
        vida_actual_squirtle -= 10
        segmento_squirtle1 = vida_actual_squirtle / VIDA_SQUIRTLE
        segmento_squirtle2 = TAMANO_BARRA * segmento_squirtle1
        barra_squirtle = "#" * int(segmento_squirtle2)
        espacios_squirtle = " " * int(TAMANO_BARRA - (segmento_squirtle2))

    else:
        print("Pikachu ataca con Onda Trueno")
        vida_actual_squirtle -= 11
        segmento_squirtle1 = vida_actual_squirtle / VIDA_SQUIRTLE
        segmento_squirtle2 = TAMANO_BARRA * segmento_squirtle1
        barra_squirtle = "#" * int(segmento_squirtle2)
        espacios_squirtle = " " * (int(TAMANO_BARRA - segmento_squirtle2))

    if vida_actual_pikachu < 0:
        vida_actual_pikachu = 0

    elif vida_actual_squirtle < 0:
        vida_actual_squirtle = 0

    print("La vida del Pikachu es: [{}{}] ({}/{})\n"
          "la vida de Squirtle es: [{}{}] ({}/{})".format(barra_pikachu, espacios_pikachu, vida_actual_pikachu, VIDA_PIKACHU, barra_squirtle, espacios_squirtle, vida_actual_squirtle, VIDA_SQUIRTLE))

    input("Enter para continuar...\n\n")
    os.system("cls")
    print("(Limpieza de pantalla)")



    if vida_actual_squirtle == 0:
        print("El Pikachu gana el combate")
        exit()

        # Turno Squirtle
    print("Turno Squirtle")
    ataque_squirtle = None
    while ataque_squirtle not in ["P", "A", "B", "N"]:
        ataque_squirtle = input("¿Qué deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja, [N]o atacar: ")

    if ataque_squirtle == "P":
        # Placaje
        print("Squirtle ha usado Placaje")
        vida_actual_pikachu -= 10
        segmento_pikachu1 = vida_actual_pikachu / VIDA_PIKACHU
        segmento_pikachu2 = TAMANO_BARRA * segmento_pikachu1
        barra_pikachu = "#" * int(segmento_pikachu2)
        espacios_pikachu = " " * (int(TAMANO_BARRA - segmento_pikachu2))

    elif ataque_squirtle == "A":
        # Pistola Agua
        print("Squirtle ha usado Pistola de Agua")
        vida_actual_pikachu -= 12
        segmento_pikachu1 = vida_actual_pikachu / VIDA_PIKACHU
        segmento_pikachu2 = TAMANO_BARRA * segmento_pikachu1
        barra_pikachu = "#" * int(segmento_pikachu2)
        espacios_pikachu = " " * (int(TAMANO_BARRA - segmento_pikachu2))

    elif ataque_squirtle == "B":
        # Burbuja
        print("Squirtle ha usado Burbuja")
        vida_actual_pikachu -= 9
        segmento_pikachu1 = vida_actual_pikachu / VIDA_PIKACHU
        segmento_pikachu2 = TAMANO_BARRA * segmento_pikachu1
        barra_pikachu = "#" * int(segmento_pikachu2)
        espacios_pikachu = " " * (int(TAMANO_BARRA - segmento_pikachu2))

    elif ataque_squirtle == "N":
        # No atacar
        print("No atacas")

    if vida_actual_pikachu < 0:
        vida_actual_pikachu = 0

    elif vida_actual_squirtle < 0:
        vida_actual_squirtle = 0

    print("La vida del Pikachu es: [{}{}] ({}/{})\n"
        "la vida de Squirtle es: [{}{}] ({}/{})".format(barra_pikachu, espacios_pikachu, vida_actual_pikachu, VIDA_PIKACHU, barra_squirtle, espacios_squirtle, vida_actual_squirtle, VIDA_SQUIRTLE))

    input("Enter para continuar...\n\n")
    os.system("cls")
    print("(Limpieza de pantalla)")

if vida_actual_pikachu > vida_actual_squirtle:
    print("El Pikachu gana el combate")

else:
    print("El Squirtle gana el combate")

