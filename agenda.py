from detalles import multiplicar,multiplicar2

dias = str(input("ingrese los dias disponibles para agendar turnos: "))
horarios = int(input("ingrese los horarios disponibles para agendar turnos: "))
precios = int(input("ingrese el precio del servicio a realizar: "))
dias_totales = int(input("ingrese la cantidad total de dias disponibles: "))
ganancia_por_dia = multiplicar(horarios,precios)
ganancia_total = multiplicar2(dias_totales,horarios,precios)

print("los dias disponibles son: ",dias)
print("los horarios disponibles son: ",horarios)
print("el precio del servicio es : ",precios)
print("el total de ganancias por dia es: ",ganancia_por_dia)
print("el total de ganancias es de : ",ganancia_total)