#agenda para turnos de servicios de uñas idealizada donde organizo segun el dia un servicio a realizar
from detalles import multiplicar,multiplicar2

dias = str(input("ingrese los dias disponibles para agendar turnos: "))#dias en palabras que tengo disponibles
horarios = int(input("ingrese los horarios disponibles para agendar turnos: "))#cantidad de horarios que tengo disponibles
precios = int(input("ingrese el precio del servicio a realizar: "))
dias_totales = int(input("ingrese la cantidad total de dias disponibles: "))#cantidad de dias en la semana que realice tal servicio
ganancia_por_dia = multiplicar(horarios,precios)#le pido que me calcule la ganancia de tal dia en que realize tal servicio (ejemplo:lunes realize 5 servicios de kapping y quiero saber cuanto gane)
ganancia_total = multiplicar2(dias_totales,horarios,precios)#le pido que calcule la ganancia total multiplicando los dias que realize tal servicio por la cantidad de horarios y su precio
#(ejemplo: lunes,miercoles y viernes realize en total 20 servicios de soft gel y quiero saber cuanto gane en total)

print("los dias disponibles son: ",dias)
print("los horarios disponibles son: ",horarios)
print("el precio del servicio es : ",precios)
print("el total de ganancias por dia es: ",ganancia_por_dia)

print("el total de ganancias es de : ",ganancia_total)
