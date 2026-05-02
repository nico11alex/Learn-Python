#for i in range(inicio,final,salto):
   #valor


#ACTIVIDAD

num = [1,2,5,7,23,33]

print("Lista original")

for i in range(len(num)):
    print(f'indice {i}: {num[i]}')

suma=0
cantidadNum=len(num)

for i in num:
    suma += i

promedio = suma / cantidadNum
print(f'La suma de los números de la lista es de {suma}.')
print(f'El promedio de los números de la lista es de {promedio}.')