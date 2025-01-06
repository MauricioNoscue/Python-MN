# Ejercicio16. Realizar la tabla de multiplicar del 5 que multiplique hasta 5 y muestre los siguientes resultados.

# 1 x 2 = 2
# 2 x 2 = 4

tabla = 5
multiplicado = 1

while multiplicado <= tabla:
    print(f'{multiplicado} x {tabla} = {multiplicado * tabla}')
    multiplicado += 1