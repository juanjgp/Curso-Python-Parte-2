import os
import readchar
import random
import math

# MAPA
obstacles = """\
                               &&&&&&&&&&&&&&&&&&&
                               &&&&&&&&&&&&&&&&&&&
                               &&&&&&&&&&&&&&&&&&&
                               &&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&                           
&&&&&&&&&&&&&&&&&&&&&&&                           
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&         
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&         
&&&&&&&&&&&&&&&&&&&&                              
&&&&&&&&&&&&&&&&&&&&                              
                            &&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&        &&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&        &&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&        &&&&&&&&&&&&&&&&&&&&&&
&&&&&&&                     &&&&&&&&&&&&&&&&&&&&&&
&&&&&&&                                           
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                    
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&   
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&   
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\
"""
obstacles = [list(row) for row in obstacles.split("\n")]

# CONSTANTES
POS_X = 0
POS_Y = 1
MAP_WIDTH = 50
MAP_HEIGHT = 20

# VIDAS POKÉMON
bar_size = 30

LIFE_PIKACHU = 100
actual_life_pikachu = 100
pikachu_segment1 = actual_life_pikachu / LIFE_PIKACHU
pikachu_segment2 = bar_size * pikachu_segment1
pikachu_bar = "#" * int(pikachu_segment2)
pikachu_spaces = " " * math.ceil(int(bar_size - pikachu_segment2))

LIFE_CATERPIE = 20
actual_life_caterpie = 20
caterpie_segment1 = actual_life_caterpie / LIFE_CATERPIE
caterpie_segment2 = bar_size * caterpie_segment1
caterpie_bar = "#" * int(caterpie_segment2)
caterpie_spaces = " " * math.ceil(int(bar_size - caterpie_segment2))

LIFE_PIDGEY = 50
actual_life_pidgey = 50
pidgey_segment1 = actual_life_pidgey / LIFE_PIDGEY
pidgey_segment2 = bar_size * pidgey_segment1
pidgey_bar = "#" * int(pidgey_segment2)
pidgey_spaces = " " * math.ceil(int(bar_size - pidgey_segment2))

LIFE_RATTATA = 50
actual_life_rattata = 50
rattata_segment1 = actual_life_rattata / LIFE_RATTATA
rattata_segment2 = bar_size * rattata_segment1
rattata_bar = "#" * int(rattata_segment2)
rattata_spaces = " " * math.ceil(int(bar_size - rattata_segment2))

# FIN DEL JUEGO
endgame = True

# POSICIÓN JUGADOR
my_position = [3, 3]

# ENTRENADORES $
trainers = [[47, 5], [5, 10], [10, 15]]
number_trainers = len(trainers)

while endgame == True:
#---------------------------------------------------TÍTULO--------------------------------------------------------------
    print("~~~~~~~~~~~~~~~~~~~~~RUTA 66~~~~~~~~~~~~~~~~~~~~~~~~")
#-----------------------------------------------DIBUJO EN MAPA----------------------------------------------------------
    print("+" + "-" * MAP_WIDTH + "+")

    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for cordinate_x in range(MAP_WIDTH):
            char = " "

            for trainer in trainers:
                if trainer[POS_X] == cordinate_x and trainer[POS_Y] == cordinate_y:
                    char = "$"

            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char = "€"

            if obstacles[cordinate_y][cordinate_x] == "&":
                char = "&"

            print("{}".format(char), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH + "+")

#-----------------------------------------MOVER AL JUGADOR €------------------------------------------------------------
    move = readchar.readchar()
    next_move = None

    if move == "w":
        next_move = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif move == "s":
        next_move = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif move == "d":
        next_move = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif move == "a":
        next_move = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif move == "esc":
        endgame = False

    if next_move:
        if obstacles[next_move[POS_Y]][next_move[POS_X]] != "&":
            my_position = next_move

    os.system("cls")

#---------------------------------------------- COMBATE POKEMON 1--------------------------------------------------------
    if my_position == trainers[0]:
        print("¡A luchar contra CAZABICHOS JOSÚE!")
        input("Enter para continuar...\n\n")
        os.system("cls")
        print("¡CATERPIE es el pokémon enviado por CAZABICHOS JOSÚE!\n"
                "¡PIKACHU es el único pokémon que tienes. No te queda otra que enviarlo!")
        input("Enter para continuar...\n\n")
        os.system("cls")

        while actual_life_pikachu > 0 and actual_life_caterpie > 0:

            # DESARROLLO DEL COMBATE

            # Turno de pikachu
            print("Turno de pikachu")
            pikachu_attack = None
            while pikachu_attack not in ["A", "I", "P", "G", "V"]:
                print("¿Qué hace PIKACHU?: \n"
                        "A- Ataque rápido\n"
                        "I- Impactrueno\n"
                        "P- Placaje\n"
                        "G- Gruñido\n"
                        "V- Hacer el vago\n")

                pikachu_attack = input("Elige: ")
                pikachu_attack = pikachu_attack.upper()
                os.system("cls")

            if pikachu_attack == "A":
                # Ataque rapido
                print("¡PIKACHU ha usado ATAQUE RÁPIDO!")
                actual_life_caterpie -= 10
                # BARRA VIDA CATERPIE
                caterpie_segment1 = actual_life_caterpie / LIFE_CATERPIE
                caterpie_segment2 = bar_size * caterpie_segment1
                caterpie_bar = "#" * int(caterpie_segment2)
                caterpie_spaces = " " * math.ceil(int(bar_size - caterpie_segment2))

            elif pikachu_attack == "I":
                # Impactrueno
                print("¡PIKACHU ha usado IMPACTRUENO!")
                actual_life_caterpie -= 20
                caterpie_segment1 = actual_life_caterpie / LIFE_CATERPIE
                caterpie_segment2 = bar_size * caterpie_segment1
                caterpie_bar = "#" * int(caterpie_segment2)
                caterpie_spaces = " " * math.ceil(int(bar_size - caterpie_segment2))

            elif pikachu_attack == "P":
                # Placaje
                print("¡PIKACHU ha usado Placaje!")
                actual_life_caterpie -= 15
                caterpie_segment1 = actual_life_caterpie / LIFE_CATERPIE
                caterpie_segment2 = bar_size * caterpie_segment1
                caterpie_bar = "#" * int(caterpie_segment2)
                caterpie_spaces = " " * math.ceil(int(bar_size - caterpie_segment2))

            elif pikachu_attack == "G":
                # Gruñido
                print("¡PIKACHU ha usado GRUÑIDO!\n")
                print("El GRUÑIDO ha sido tan ridículo que CATERPIE y CAZABICHOS JOSÚE se han descojonao de ti")

            elif pikachu_attack == "V":
                # Hacer el vago
                print("¡PIKACHU se ha tumbado a la bartola!\n")
                print("El CATERPIE y el CAZABICHOS miran pasmaos")

            # EVITAR LAS VIDAS NEGATIVAS
            if actual_life_pikachu < 0:
                actual_life_pikachu = 0

            elif actual_life_caterpie < 0:
                    actual_life_caterpie = 0

            print("La vida del PIKACHU es: [{}{}] ({}/{})\n"
                    "la vida de CATERPIE es: [{}{}] ({}/{})".format(pikachu_bar, pikachu_spaces,
                                                                       actual_life_pikachu, LIFE_PIKACHU,
                                                                       caterpie_bar, caterpie_spaces,
                                                                       actual_life_caterpie, LIFE_CATERPIE))
            input("Enter para continuar...\n\n")
            os.system("cls")

#----------------------------------------------GANAS EL COMBATE 1-------------------------------------------------------
            if actual_life_caterpie == 0:
                print("El PIKACHU gana el combate. CAZABICHOS JOSUÉ Ha perdido. Te ha dado 10 pavacos")
                input("Enter para continuar...\n")
                os.system("cls")
                # Eliminar entrenadores $
                trainers[0] = " "
                number_trainers -= 1
                break
#-----------------------------------------------------------------------------------------------------------------------
            # Turno de CATERPIE
            print("Turno de CATERPIE")
            caterpie_attack = random.randint(1, 2)
            # Placaje
            if caterpie_attack == 1:
                print("CATERPIE ha usado PLACAJE")
                actual_life_pikachu -= 15
                pikachu_segment1 = actual_life_pikachu / LIFE_PIKACHU
                pikachu_segment2 = bar_size * pikachu_segment1
                pikachu_bar = "#" * int(pikachu_segment2)
                pikachu_spaces = " " * math.ceil(int(bar_size - pikachu_segment2))

            elif caterpie_attack == 2:
                print("CATERPIE ha usado DISPARO DEMORA")
                print("La tela del CATERPIE es tan pequeña que PIKACHU se la quita de un soplido")

            # EVITAR LAS VIDAS NEGATIVAS
            if actual_life_pikachu < 0:
                actual_life_pikachu = 0

            elif actual_life_caterpie < 0:
                actual_life_caterpie = 0

            print("La vida del PIKACHU es: [{}{}] ({}/{})\n"
                    "la vida de CATERPIE es: [{}{}] ({}/{})".format(pikachu_bar, pikachu_spaces,
                                                                          actual_life_pikachu, LIFE_PIKACHU,
                                                                          caterpie_bar, caterpie_spaces,
                                                                          actual_life_caterpie, LIFE_CATERPIE))
            input("Enter para continuar...\n\n")
            os.system("cls")
# ----------------------------------------------GANAS EL COMBATE 1------------------------------------------------------
            if actual_life_caterpie == 0:
                print("El PIKACHU gana el combate. CAZABICHOS JOSUÉ Ha perdido. Te ha dado 10 pavacos")
                input("Enter para continuar...\n")
                os.system("cls")
                # Eliminar entrenadores $
                trainers[0] = " "
                number_trainers -= 1
                break
# --------------------------------------HAS PERDIDO EL COMBATE 1. FIN DEL JUEGO-----------------------------------------
            elif actual_life_pikachu == 0:
                print("Te ha ganado un CATERPIE el juego acaba porque te retiras avergonzado. FIN DEL JUEGO")
                input("Enter para terminar...\n")
                endgame = False
                os.system("cls")




#------------------------------------------ COMBATE POKEMON 2-----------------------------------------------------------
    if my_position == trainers[1]:
        print("¡A luchar contra ORNITÓLOGO MANUÉ!")
        input("Enter para continuar...\n\n")
        os.system("cls")
        print("¡PIDGEY es el pokémon enviado por ORNITÓLOGO MANUÉ!\n"
                "¡Envías a PIKACHU!")
        input("Enter para continuar...\n\n")
        os.system("cls")

        while actual_life_pikachu > 0 and actual_life_pidgey > 0:

            # DESARROLLO DEL COMBATE

            # Turno de pikachu
            print("Turno de pikachu")
            pikachu_attack = None
            while pikachu_attack not in ["A", "I", "P", "G", "V"]:
                print("¿Qué hace PIKACHU?: \n"
                        "A- Ataque rápido\n"
                        "I- Impactrueno\n"
                        "P- Placaje\n"
                        "G- Gruñido\n"
                        "V- Hacer el vago\n")

                pikachu_attack = input("Elige: ")
                pikachu_attack = pikachu_attack.upper()
                os.system("cls")

            if pikachu_attack == "A":
                # Ataque rapido
                print("¡PIKACHU ha usado ATAQUE RÁPIDO!")
                actual_life_pidgey -= 10
                # BARRA VIDA PIDGEY
                pidgey_segment1 = actual_life_pidgey / LIFE_PIDGEY
                pidgey_segment2 = bar_size * pidgey_segment1
                pidgey_bar = "#" * int(pidgey_segment2)
                pidgey_spaces = " " * math.ceil(int(bar_size - pidgey_segment2))

            elif pikachu_attack == "I":
                # Impactrueno
                print("¡PIKACHU ha usado IMPACTRUENO!")
                actual_life_pidgey -= 20
                pidgey_segment1 = actual_life_pidgey / LIFE_PIDGEY
                pidgey_segment2 = bar_size * pidgey_segment1
                pidgey_bar = "#" * int(pidgey_segment2)
                pidgey_spaces = " " * math.ceil(int(bar_size - pidgey_segment2))

            elif pikachu_attack == "P":
                # Placaje
                print("¡PIKACHU ha usado Placaje!")
                actual_life_pidgey -= 15
                pidgey_segment1 = actual_life_pidgey / LIFE_PIDGEY
                pidgey_segment2 = bar_size * pidgey_segment1
                pidgey_bar = "#" * int(pidgey_segment2)
                pidgey_spaces = " " * math.ceil(int(bar_size - pidgey_segment2))

            elif pikachu_attack == "G":
                # Gruñido
                print("¡PIKACHU ha usado GRUÑIDO!\n")
                print(
                    "El GRUÑIDO ha sido tan ridículo que PIDGEY y ORNITÓLOGO MANUÉ se han descojonao de ti")

            elif pikachu_attack == "V":
                # Hacer el vago
                print("¡PIKACHU se ha tumbado a la bartola!\n")
                print("El PIDGEY y el ORNITÓLOGO no dan crédito a lo que pasa")

            # EVITAR LAS VIDAS NEGATIVAS
            if actual_life_pikachu < 0:
                actual_life_pikachu = 0

            elif actual_life_pidgey < 0:
                actual_life_pidgey = 0

            print("La vida del PIKACHU es: [{}{}] ({}/{})\n"
                    "la vida de PIDGEY es: [{}{}] ({}/{})".format(pikachu_bar, pikachu_spaces,
                                                                      actual_life_pikachu, LIFE_PIKACHU,
                                                                      pidgey_bar, pidgey_spaces,
                                                                      actual_life_pidgey, LIFE_PIDGEY))
            input("Enter para continuar...\n\n")
            os.system("cls")
#-----------------------------------------------GANAS EL COMBATE 2------------------------------------------------------
            if actual_life_pidgey == 0:
                print("El PIKACHU gana el combate. ORNITÓLOGO MANUÉ Ha perdido. Te ha dado 20 pavacos")
                input("Enter para continuar...\n")
                os.system("cls")
                # Eliminar entrenadores $
                trainers[1] = " "
                number_trainers -= 1
                break
#-----------------------------------------------------------------------------------------------------------------------
            # Turno de PIDGEY
            print("Turno de PIDGEY")
            pidgey_attack = random.randint(1, 2)
            # Picotazo
            if pidgey_attack == 1:
                print("PIDGEY ha usado PICOTAZO")
                actual_life_pikachu -= 20
                pikachu_segment1 = actual_life_pikachu / LIFE_PIKACHU
                pikachu_segment2 = bar_size * pikachu_segment1
                pikachu_bar = "#" * int(pikachu_segment2)
                pikachu_spaces = " " * math.ceil(int(bar_size - pikachu_segment2))

            elif pidgey_attack == 2:
                print("Pidgey ha usado ATAQUE ALA")
                actual_life_pikachu -= 15
                pikachu_segment1 = actual_life_pikachu / LIFE_PIKACHU
                pikachu_segment2 = bar_size * pikachu_segment1
                pikachu_bar = "#" * int(pikachu_segment2)
                pikachu_spaces = " " * math.ceil(int(bar_size - pikachu_segment2))

            # EVITAR LAS VIDAS NEGATIVAS
            if actual_life_pikachu < 0:
                actual_life_pikachu = 0

            elif actual_life_pidgey < 0:
                actual_life_pidgey = 0

            print("La vida del PIKACHU es: [{}{}] ({}/{})\n"
                  "la vida de   PIDGEY es: [{}{}] ({}/{})".format(pikachu_bar, pikachu_spaces,
                                                                  actual_life_pikachu, LIFE_PIKACHU,
                                                                  pidgey_bar, pidgey_spaces,
                                                                  actual_life_pidgey, LIFE_PIDGEY))
            input("Enter para continuar...\n\n")
            os.system("cls")
#-----------------------------------------------GANAS EL COMBATE 2------------------------------------------------------
            if actual_life_pidgey == 0:
                print("El PIKACHU gana el combate. ORNITÓLOGO MANUÉ Ha perdido. Te ha dado 20 pavacos")
                input("Enter para continuar...\n")
                os.system("cls")
                # Eliminar entrenadores $
                trainers[1] = " "
                number_trainers -= 1
                break

# --------------------------------------HAS PERDIDO EL COMBATE 2. FIN DEL JUEGO------------------------------------------
            elif actual_life_pikachu == 0:
                print("Te ha ganado un pajarraco el juego acaba porque das lástima. FIN DEL JUEGO")
                input("Enter para terminar...\n")
                endgame = False
                os.system("cls")

#------------------------------------------------- COMBATE POKEMON 3----------------------------------------------------
    if my_position == trainers[2]:
        print("¡A luchar contra ENTRENADOR GUAY PACO!")
        input("Enter para continuar...\n\n")
        os.system("cls")
        print("¡RATTATA es el pokémon enviado por ENTRENADOR GUAY PACO!\n"
              "¡PIKACHU va pero está un poco harto ya!")
        input("Enter para continuar...\n\n")
        os.system("cls")

        while actual_life_pikachu > 0 and actual_life_rattata > 0:

            # DESARROLLO DEL COMBATE

            # Turno de pikachu
            print("Turno de pikachu")
            pikachu_attack = None
            while pikachu_attack not in ["A", "I", "P", "G", "V"]:
                print("¿Qué hace PIKACHU?: \n"
                      "A- Ataque rápido\n"
                      "I- Impactrueno\n"
                      "P- Placaje\n"
                      "G- Gruñido\n"
                      "V- Hacer el vago\n")

                pikachu_attack = input("Elige: ")
                pikachu_attack = pikachu_attack.upper()
                os.system("cls")

            if pikachu_attack == "A":
                # Ataque rapido
                print("¡PIKACHU ha usado ATAQUE RÁPIDO!")
                actual_life_rattata -= 10
                # BARRA VIDA RATTATA
                rattata_segment1 = actual_life_rattata / LIFE_RATTATA
                rattata_segment2 = bar_size * rattata_segment1
                rattata_bar = "#" * int(rattata_segment2)
                rattata_spaces = " " * math.ceil(int(bar_size - rattata_segment2))

            elif pikachu_attack == "I":
                # Impactrueno
                print("¡PIKACHU ha usado IMPACTRUENO!")
                actual_life_rattata -= 20
                rattata_segment1 = actual_life_rattata / LIFE_RATTATA
                rattata_segment2 = bar_size * rattata_segment1
                rattata_bar = "#" * int(rattata_segment2)
                rattata_spaces = " " * math.ceil(int(bar_size - rattata_segment2))

            elif pikachu_attack == "P":
                # Placaje
                print("¡PIKACHU ha usado Placaje!")
                actual_life_rattata -= 15
                rattata_segment1 = actual_life_rattata / LIFE_RATTATA
                rattata_segment2 = bar_size * rattata_segment1
                rattata_bar = "#" * int(rattata_segment2)
                rattata_spaces = " " * math.ceil(int(bar_size - rattata_segment2))

            elif pikachu_attack == "G":
                # Gruñido
                print("¡PIKACHU ha usado GRUÑIDO!\n")
                print(
                    "El GRUÑIDO ha sido tan ridículo que RATTATA y ENTRENADOR GUAY PACO se han descojonao de ti")

            elif pikachu_attack == "V":
                # Hacer el vago
                print("¡PIKACHU se ha tumbado a la bartola!\n")
                print("El RATTATA y el ENTRENADOR GUAY miran pasmaos")

            # EVITAR LAS VIDAS NEGATIVAS
            if actual_life_pikachu < 0:
                actual_life_pikachu = 0

            elif actual_life_rattata < 0:
                actual_life_rattata = 0

            print("La vida del PIKACHU es: [{}{}] ({}/{})\n"
                  "la vida de RATTATA  es: [{}{}] ({}/{})".format(pikachu_bar, pikachu_spaces,
                                                                  actual_life_pikachu, LIFE_PIKACHU,
                                                                  rattata_bar, rattata_spaces,
                                                                  actual_life_rattata, LIFE_RATTATA))
            input("Enter para continuar...\n\n")
            os.system("cls")
#-----------------------------------------------GANAS EL COMBATE 3------------------------------------------------------
            if actual_life_rattata == 0:
                print("El PIKACHU gana el combate. ENTRENADOR GUAY PACO HA PERDIDO. Te ha sacudido 50 pavacos")
                input("Enter para continuar...\n")
                os.system("cls")
                # Eliminar entrenadores $
                trainers[2] = " "
                number_trainers -= 1
                break
#-----------------------------------------------------------------------------------------------------------------------
            # Turno de RATTATA
            print("Turno de RATTATA")
            rattata_attack = random.randint(1, 2)
            # Derribo
            if rattata_attack == 1:
                print("RATTATA ha usado DERRIBO")
                actual_life_pikachu -= 25
                pikachu_segment1 = actual_life_pikachu / LIFE_PIKACHU
                pikachu_segment2 = bar_size * pikachu_segment1
                pikachu_bar = "#" * int(pikachu_segment2)
                pikachu_spaces = " " * math.ceil(int(bar_size - pikachu_segment2))

            elif rattata_attack == 2:
                print("RATTATA ha usado ATAQUE ARENA")
                print("La arenilla que tira el RATTATA hace toser al PIKACHU pero nada más")

            # EVITAR LAS VIDAS NEGATIVAS
            if actual_life_pikachu < 0:
                actual_life_pikachu = 0

            elif actual_life_rattata < 0:
                actual_life_rattata = 0

            print("La vida del PIKACHU es: [{}{}] ({}/{})\n"
                  "la vida de RATTATA  es: [{}{}] ({}/{})".format(pikachu_bar, pikachu_spaces,
                                                                  actual_life_pikachu, LIFE_PIKACHU,
                                                                  rattata_bar, rattata_spaces,
                                                                  actual_life_rattata, LIFE_RATTATA))
            input("Enter para continuar...\n\n")
            os.system("cls")
#-----------------------------------------------GANAS EL COMBATE 3------------------------------------------------------
            if actual_life_rattata == 0:
                print("El PIKACHU gana el combate. ENTRENADOR GUAY PACO HA PERDIDO. Te ha sacudido 50 pavacos")
                input("Enter para continuar...\n")
                os.system("cls")
                # Eliminar entrenadores $
                trainers[2] = " "
                number_trainers -= 1
                break
#--------------------------------------HAS PERDIDO EL COMBATE 3. FIN DEL JUEGO------------------------------------------
            elif actual_life_pikachu == 0:
                print("Te ha ganado un RATÓN el juego acaba porque no puedes dar más pena. FIN DEL JUEGO")
                input("Enter para terminar...\n")
                endgame = False
                os.system("cls")
#-------------------------------------ENTRENADORES VENCIDOS. ¡HAS GANADO!-----------------------------------------------
    if number_trainers == 0:
        print("HAS VENCIDO A TODOS LOS ENTRENADORES. ¡FELICIDADES!. HAS SUPERADO EL POKEMON SNAKE")
        input("Enter para terminar por la puerta grande...\n")
        endgame = False
