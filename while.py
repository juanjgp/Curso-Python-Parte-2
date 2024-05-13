opcion = None

while opcion != "A" and opcion != "B" and opcion != "C" and opcion != "D":
    print("Eres tontismo, hasta que no digas A,B,C o D no te levantas de aquí\n")

    print("A-Madrid\n"
        "B-Barcelona\n"
        "C-Albacete\n"
        "D-Guadalajara\n")

    opcion= input("¿Qué ciudad te gusta más?: ")
    opcion = opcion.upper()


if opcion == "A":
    print("\nHas elegido Madrid")

if opcion == "B":
    print("\nHas elegido Barcelona")

if opcion == "C":
    print("\nHas elegido Albacete")

if opcion == "D":
    print("\nHas elegido Guadalajara")


