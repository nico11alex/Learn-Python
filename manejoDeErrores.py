pedirNum = input("Ingresa tu edad: ")

try:
    pedirNum = int(pedirNum)
    if pedirNum < 18:
        raise Exception("No puedes entrar")
    
    print("Bienvenido")
except ValueError:
    print("Edad invalida")
except Exception as error:
    print(error)
finally:
    print("Fin del programa")