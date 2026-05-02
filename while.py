contador = 1
while contador <= 5:
    print(contador)
    contador += 1

print("¡Fin de la ejecución")

clave = input("Ingrese la palabra clave para salir del programa:(salir)")
while clave != "salir":
    print("Esa no es la palabra")
    clave = input("Ingrese la palabra clave para salir del programa:")

print("SALISTE DEL BUCLE")

#ACTIVIDAD

suma = 0
contador = 0
while True:
    num= int(input("Ingrese un número: "))
    if num == 0:
        break
    else:
        suma += num
        contador += 1

if contador > 0 :
    promedio = suma/contador
    print(promedio)
else:
    print("No se puede dividir por 0.")

print(suma)
print(contador)

