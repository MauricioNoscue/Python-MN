# Ejercicio17. Realizar la tabla del 9 que multiplique hasta 5 y
# de los resultados me imprima los resultados que son pares y que resultados son impares.

tabla = 9
hasta = 5
multiplicado = 0

while multiplicado < hasta:
    multiplicado += 1
    resultado = tabla * multiplicado
    if resultado % 2 == 0:
        print(f'{tabla} x {multiplicado} = {resultado} es par')
    else:
        print(f'{tabla} x {multiplicado} = {resultado} es impar')

