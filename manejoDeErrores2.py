try:
    cantidadDeProducto = input("Ingrese la cantidad del producto: ")
    precio = input("Ingrese el precio del producto: ")

    cantidadDeProducto = int(cantidadDeProducto)
    precio = float(precio)

    if cantidadDeProducto == 0:
        raise Exception("Cantidad invalidad")
    
    resultado = cantidadDeProducto * precio
    print(f"Debes pagar ${resultado:.2f}")

except ValueError:
    print("Dato invalido")

except Exception as error:
    print(error)

finally:
    print("Proceso terminado")