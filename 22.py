# Ejercicio25. Realizar las tablas de multiplicar de 1 hasta el 5 y
# multiplique hasta cinco, debe imprimir lo siguientes resultados
# a.
# 1x1=1
# 1x2=2
# 5x5=25
# b. Cuando los resultados sean pares debe imprimir buzz y si son impares debe imprimir bass
# c. Debe imprimir cuanto números pares e impares hay en los resultados de las mult iplicaciones.


#WHILE

iteracion1 = 0
iteracion2 = 0
pares = 0
impares = 0
while iteracion1 < 5:
    iteracion1 += 1
    iteracion2 = 0
    print(f'tabla del {iteracion1}')
    while 5 > iteracion2:
        iteracion2 += 1
        resultado = iteracion1 * iteracion2
        if resultado % 2 == 0:
            print(f"{iteracion1}x {iteracion2} = {resultado} buzz")
            pares += 1
        else:
            print(f"{iteracion1}x {iteracion2} = {resultado} bass")
            impares += 1
print(f'pares: {pares}, impares: {impares}')