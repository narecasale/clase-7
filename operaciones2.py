def costo_aberturas (aberturas,maderas):
    total = aberturas*maderas*1.6
    return  total

def costo_total (ambientes,puertas,ventanas,ventanal):
    total = ambientes*puertas*ventanal*ventanas
    return total
