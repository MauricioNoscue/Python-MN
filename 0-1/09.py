# Ejercicio9. Calcular el área de 3 cuadrados e imprimir si las áreas son iguales y/o cual es mayor.

lado1 = 5
lado2 = 8
lado3 = 4

cuadrado1 = lado1 * lado1
cuadrado2 = lado2 * lado2
cuadrado3 = lado3 * lado3

if(cuadrado1 > cuadrado2 and cuadrado1>cuadrado3):
    print("El cuadrado 1 es el mayor")
elif(cuadrado2 > cuadrado1 and cuadrado2>cuadrado3):
    print("El cuadrado 2 es el mayor", cuadrado2)
else:
    print('el tres es mayor')
