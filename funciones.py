# def nombreFuncion(parametros)
"""
Devuelve con return
y si no es none
"""

def saludar(nombre):
    print("Hola,", nombre)

saludar("Nicolas")

def doblar(numero):
    return numero * 2

resultado = doblar(5)
print(resultado)

def area_triangulo(base , altura):
    area = (base * altura) / 2
    return area

b = float(input("Base: "))
h = float(input("Altura: "))
a = area_triangulo(b,h)
print("El área es",a)

#ACTIVIDAD

def es_par(numero):
    return numero % 2 == 0
    
def calcular_media(lista_numeros):
    if len(lista_numeros) == 0:
        return 0
    suma = sum(lista_numeros)
    longitud = len(lista_numeros)
    return suma / longitud

lista = []
for i in range(5):
    numero = int(input(f"Dame un numero {i+1}: "))
    lista.append(numero)

media = calcular_media(lista)
print(f"Media de la lista: {media}")

for i in lista:
    if es_par(i):
        print(f"{i} es par")
    else:
        print(f"{i} es impar")

