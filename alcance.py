#SCOPE

"""
Las variables globales se usan mejor como 
constantes.
"""

x = 10 

def funcion():
    y = 5
    print(y)

funcion()

def saludar(nombre,saludo="Hola"):
    print(f"{saludo}, {nombre}")

saludar("Nicolas")
saludar("Nicolas","Buenas")

contador_global = 0 #global

def incrementar(valor, cantidad=1):
    #cantidad tiene valor por defecto 1
    resultado = valor + cantidad
    return resultado

a = 5
print(incrementar(a))
print(incrementar(a,3))

# ACTIVIDAD FORMATEAR MONEDA

def formatear_moneda(cantidad, simbolo="$", pais="Desconocido"):
    return f"Cantidad: {simbolo} {cantidad:.2f} - País: {pais}"


numero = float(input("Ingrese el monto: "))
simbolo = str(input("Ingrese el símbolo (por defecto $): "))

if simbolo == "":
    simbolo = "$"

pais = str(input("Ingrese el país (por defecto Desconocido): "))

if pais == "":
    pais = "Desonocido"


print(f"Resultado: {formatear_moneda(numero,simbolo,pais)}")