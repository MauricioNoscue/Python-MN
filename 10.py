# Ejercicio10. Realizar un diagrama de flujo que calcule la edad de 3 personas e imprimir
# si cada persona es mayor de edad, calcular e imprimir en el mismo diagrama
# el promedio de las tres edades y si el promedio de edades de las personas está en el promedio de la mayoría de edad.


def calcular(edad):
    actual = 2024
    return actual - edad


uno = calcular(2000)
dos = calcular(1999)
tres = calcular(2008)
total = (uno + dos + tres) / 3

if(uno>=18):
    print("Persona 1 es mayor de edad")
else:
    print("Persona 1 no es mayor de edad")

if(dos>=18):
    print("Persona 2 es mayor de edad")
else:
    print("Persona 2 no es mayor de edad")

if(tres >= 18):
    print("Persona 3 es mayor de edad")
else:
    print("Persona no 3 es mayor de edad")

if(total >= 18):
    print("El promedio de las edades es mayor de edad")
else:
    print("El promedio de las edades no es mayor de edad")