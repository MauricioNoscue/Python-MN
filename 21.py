# Ejercicio21. Realizar la tabla del 9 que multiplique hasta 5 y que me imprima los números pares e impares.


hasta = 5
tabla = 9
for multiplicado in range(1, hasta +1):
    resultado = tabla * multiplicado
    if resultado % 2 == 0:
        print(f'{tabla} x {multiplicado} = {resultado} es par')
    else:
        print(f'{tabla} x {multiplicado} = {resultado} es impar')
