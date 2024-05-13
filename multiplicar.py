print("Tabla de multiplicar de un número introducido por el usuario")
numero = int(input("Introduzca un número: "))

for i in range(1, 11):
    resultado = numero * i
    if resultado % 2 == 0:
        print ("{} x {} = {}".format(numero, i, resultado))