def calcular_horas(segundos):
    horas=segundos//3600
    minutos=(segundos%3600)//60
    segundos=segundos%60
    return horas,minutos,segundos

def calcular_segundos(horas,minutos,segundos):
    segundos=horas*3600+minutos*60+segundos
    return segundos

def reloj(segundos: int, horas: int = None,minutos: int = None) -> str:
    """
    Devuelve una cadena con el formato de un reloj.
    :param segundos: segundos a convertir
    :param horas: horas a convertir (opcional)
    :param minutos: minutos a convertir (opcional)
    :return: cadena con el formato de un reloj
    """
    if horas is None and minutos is None:
        return calcular_horas(segundos)
    else:
        if horas < 0 or horas > 23:
            return False
        if minutos < 0 or minutos > 59:
            return False
        if segundos < 0 or segundos > 59:
            return False
        return calcular_segundos(horas,minutos,segundos)

print(reloj(3600))
print(reloj(horas=1,minutos=2,segundos=50))

def calcular(*args):
	if len(args)==1:
		return calcular_horas(args[0])
	elif len(args)==3:
		return calcular_segundos(*args)
	else:
		print("Se espera 1 o 3 parámetros")



print(calcular(3600, 2))
print(calcular(1,2,50))