
# Ejercicio 11. Realizar un diagrama de flujo que calcule el pago total del sueldo de un diagrama, debe calcular e imprimir lo siguiente:
# a. Salario de la persona = valorDia * diasTrabajados
# b. Si la persona gana menos de dos salarios mínimos se suma 114000$
# c. Su sueldo por el subsidio de transporte de lo contrario se suma 0
# d. Calcular la salud, pensión y arl sabiendo que
# Salud= salario * 0.12
# Pensión = salario * 0.16
# Arl = salario *0.052
# e. Si la persona gana mas de 4 salarios mínimos debe hacer una retención del 0.04 de su salario
# f.
# Sumar los deducibles que son salud, pensión y arl y restar el deducible al salario de la persona
# g. Calcular e imprimir el total.


dias = 30
valorDia = 50000
transporte = 0
minimo = 1300000
retencion = 0

Salario = dias * valorDia

if(Salario <= minimo *2):
    transporte += 114000
else:
    transporte = 0

if(Salario >= minimo *4):
    retencion = retencion - 0.04
else:
    retencion = 0

Salud = Salario *0.12
Pensión = Salario *0.16
Arl = Salario * 0.052
Descuento = Salud + Pensión + Arl
pagototal = Salario - Descuento

print("dias:", dias)
print("valorDia:", valorDia)
print("transporte:", transporte)
print("minimo:", minimo)
print("retencion:", retencion)
print("Salario:", Salario)
print("Salud:", Salud)
print("Pensión:", Pensión)
print("Arl:", Arl)
print("Descuento:", Descuento)
print("pagototal:", pagototal)