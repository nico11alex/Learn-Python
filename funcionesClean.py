def total_producto(precio,cantidad):
    return precio * cantidad

def datos_validos(precio,cantidad):
    return precio > 0 and cantidad > 0

# intenta ingresar productos si ingresa un tipo de dato incorrecto lo atrapa
try:
    producto = input("Producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    if datos_validos(precio,cantidad):
        total = total_producto(precio,cantidad)
        print(f"Producto: {producto}")
        print(f"Total: {total}")
    else:
        print("Error: valores invalidos")
except ValueError:
    print("Error tipo de dato erroneo")

 

