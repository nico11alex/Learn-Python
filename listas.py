carros = ['Mazda','Camaro','Mustang']

print(carros[2])
print(carros[0])

carros.append('Raptor')
print(carros)

carros.insert(1,'BMW')
print(carros)

carroElgido = carros.pop()
print(carroElgido)

carros.remove('Camaro')
print(carros)

print(len(carros))
carros.sort()

print(carros)

#ACTIVIDAD

numeros = [10,25,3,48,15]

print(numeros[0])
print(numeros[-1])

numeros.append(99)
print(numeros)

numeros.insert(1,50)
print(numeros)

numeros.remove(3)
print(numeros)

print("Hay " + str(len(numeros)) + " números en la lista")