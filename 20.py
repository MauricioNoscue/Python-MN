# Ejercicio20. Realizar un diagrama de flujo que imprima la tabla del 5 y que cuente hasta 5


tabla = 5
multiplicado = 1
for multiplicado in range(1,tabla+1):
    print(f'{multiplicado} x {tabla} = {multiplicado * tabla}')
