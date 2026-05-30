def my_fuctions(primerValor,segundoValor):
    print(primerValor+segundoValor)

my_fuctions(2,3)

def variosDatos(*datos):
    for dato in datos:
        print(dato.upper())

variosDatos("hola","soy")