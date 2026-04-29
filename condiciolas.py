puntaje = int(input("Ingrese su puntaje: "))

if puntaje <= 0:
    print("Error valor incorrecto")
elif puntaje < 60:
    print("Calificacion F")
elif puntaje >= 60 and puntaje <= 69:
    print("Calificacion D")
elif puntaje >= 70 and puntaje <= 79:
    print("Calificacion C")
elif puntaje >= 80 and puntaje <= 89:
    print("Calificacion B")
elif puntaje >= 90 and puntaje <= 100:
    print("Calificacion A")
else:
    print("Error valor incorrecto")