# Ejercicio25. Realizar las tablas de multiplicar de 1 hasta el 5 y
# multiplique hasta cinco, debe imprimir lo siguientes resultados
# a.
# 1x1=1
# 1x2=2
# 5x5=25
# b. Cuando los resultados sean pares debe imprimir buzz y si son impares debe imprimir bass
# c. Debe imprimir cuanto números pares e impares hay en los resultados de las mult iplicaciones.

#FOR
iteracion1 = 0
iteracion2 = 0
pares = 0
impares = 0
for iteracion1 in range(1, 6):
    iteracion2 = 0
    print(f'tabla: {iteracion1}')
    for iteracion2 in range(1,6):
        resultado = iteracion1 * iteracion2
        if resultado % 2 == 0:
            print(f'{iteracion1}x {iteracion2} = {resultado} buzz')
            pares += 1
        else:
            print(f'{iteracion1}x {iteracion2} = {resultado} bass')
            impares += 1
print(f'pares: {pares}, impares: {impares}')
            