# Ejercicio8. Realizar un diagrama de flujo que imprima el pago de una persona sabiendo
# que el sueldo que es igual a los
# días trabajados por el valor del día, imprimir
# la salud, pensión y arl, sabiendo que la suma de la salud, la pensión y el arl se
# descuentan del sueldo de la persona.
# Salario = diasTrabajados * valorDia
# Salud = sueldo *0.12
# Pensión = sueldo *0.16
# Arl = sueldo * 0.052
# Descuento = salud + pensión + arl


dias = 30
valorDia = 50000
Salario = dias * valorDia
Salud = Salario *0.12
Pensión = Salario *0.16
Arl = Salario * 0.052
Descuento = Salud + Pensión + Arl
pagototal = Salario - Descuento

print(Salario, Salud, Pensión, Arl, Descuento, pagototal)