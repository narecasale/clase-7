from operaciones import sumar,restar,costo_producto,ganancia_max

cantidad_mayo = int(input("INGRESE LA CANTIDAD  VENDIDA EN MAYO:"))
cantidad_junio = int(input("INGRESE LA CANTIDAD  VENDIDA EN JUNIO:"))
precio = float(input("ingrese el precio unitario:"))

cantidad_vendida= sumar(cantidad_mayo,cantidad_junio)
dif_mensual= restar(cantidad_junio,cantidad_mayo)
costo_mayo = costo_producto(cantidad_mayo,precio)
costo_junio = costo_producto(cantidad_junio,precio)
ganancia_mayo = ganancia_max(cantidad_mayo,precio,costo_mayo)
ganancia_junio = ganancia_max(cantidad_junio,precio,costo_junio)
ganancia_total = ganancia_max(ganancia_mayo,ganancia_junio)

print("la cantidad vendida total es de: ",cantidad_vendida)
print("la cantidad vendida en mayo es de: ",cantidad_mayo)
print("la cantidad vendida en junio es de: ",cantidad_junio)
print("la diferencia mensual es de: ",dif_mensual)
print("el costo del mes de mayo fue de: ",costo_mayo)
print("el costo del mes de junio es de: ",costo_junio)
print("la ganacia del mes de mayo fue de un total de: ",ganancia_mayo)
print("la ganacia del mes de junio es de un total de: ",ganancia_junio)
print("la ganacia total fue de: ",ganancia_total)
