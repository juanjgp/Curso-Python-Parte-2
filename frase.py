texto = "Hola, me llamo Nate. ¿Tu como te llamas?"

espacios = 0
puntos = 0
comas = 0
mayusculas = 0
for caracter in texto:
    if " " in caracter:
        espacios += 1

    elif "," in caracter:
        comas += 1

    elif "." in caracter:
        puntos +=1

    elif caracter.isupper() == True:
        mayusculas += 1

print("El número de espacios en el texto es de {}".format(espacios))
print("El número de puntos en el texto es de {}".format(puntos))
print("El número de comas en el texto es de {}".format(comas))
print("El número de mayúsculas en el texto es de {}".format(mayusculas))