from operaciones2 import costo_total,costo_aberturas

ambientes = int(input("ingrese la cantidad de ambientes: "))
puertas = int(input("ingrese la cantidad de puertas: "))
ventanas= int(input("ingrese la cantidad de ventanas: "))
ventanal = int(input("ingrese la cantidad de ventanales: "))
maderas = int(input("ingrese el precio de la madera x m2: "))

costo_puertas = costo_aberturas(puertas,maderas)
costo_ventanas = costo_aberturas(ventanas,maderas)
costo_ventanal = costo_aberturas(ventanal,maderas)
total = costo_total(costo_puertas,costo_ventanas,costo_ventanal,ambientes)

print("el costo de las puertas es: ",costo_puertas)
print("el costo de las ventanas es: ",costo_ventanas)
print("el costo de los ventanales es: ",costo_ventanal)
print("el costo total de las aberturas es: ",total)