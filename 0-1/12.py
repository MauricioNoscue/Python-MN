# Ejercicio12. Calcular tres notas e imprimir lo siguiente
# a. El 20% de la nota 1
# b. El 35% de la nota 2
# c. El 45% de la nota 3
# d. Sumar los porcentajes de las notas e imprimir lo siguiente:
# d1. Si la suma del porcentaje es mayor es 4.5 es una nota superior.
# d2. Si la suma de el porcentaje está entre menor igual 4.5 y es mayor a 3.5 es buena.
# d3. Si la suma del porcentaje está entre menor igual a 3.5 y es mayor a 3 la nota es media.
# d4. Si la suma del porcentaje es menor de 3 la nota es mala.

nota1 =  4 * 0.2
nota2 =  3 * 0.35
nota3 =  5 * 0.45

suma = nota1  + nota2 + nota3

if(suma> 4.5):
    print("Nota superior")
elif(suma <= 4.5 and suma >3.5 ):
    print('nota buena', suma)
elif(suma <= 3.5 and suma > 3):
    print('Nota media', suma)
else:
    print('Nota mala')
