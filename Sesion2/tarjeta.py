## Postwork Sesion 2

# Crea una función que itere sobre una lista de tarjetas e imprima los reportes de todas.
# Crea la función pago_recurrente, la cual proyectará una serie de pagos del mismo monto en una tarjeta, para una deuda que no tendrá nuevos cargos. Hasta convertir el valor de la deuda en 0. Para cada mes proyectado se debe imprimir el reporte correspondiente.
# Haz llamadas y prueba las funciones que has creado

print("""==============================
==== Calculadora contable ====
=============================="""	)


def crea_tarjeta(nombre_tarjeta, tasa_interes, deuda, pago_realizar, nuevos_cargos):
	""" Recibe los datos de una tarjeta y devuelve un diccionario con la informacion de entrada """
	diccionario = { "nombre_tarjeta" : nombre_tarjeta, "tasa_interes" : tasa_interes,
	"deuda" : deuda, "pago_realizar" : pago_realizar, "nuevos_cargos" : nuevos_cargos }

	if pago_realizar > deuda:
		print("Error: El pago a realizar es mayor a la deuda actual, por favor ingrese sus datos nuevamente")
	else:
		return diccionario

def captura_nueva_deuda(diccionario):
	""" 
	Recibe diccionario con informacion de la tarjeta, realiza los calculos y devuelve diccionario con la nueva deuda como campo adicional
	"""
	interes_mensual = diccionario["tasa_interes"]/12
	deuda_recalculada = (diccionario["deuda"] - diccionario["pago_realizar"]) * (1 + interes_mensual)
	nueva_deuda = deuda_recalculada + diccionario["nuevos_cargos"]
	diccionario["nueva_deuda"] = nueva_deuda

	return diccionario


def generar_reporte(diccionario):
	""" Recibe diccionario con la informacion de la transaccion e imprime un resumen de la transaccion realizada """
	print("""
		#################################
		##  Resumen de la transacción  ##
		#################################
		""")
	print(" Nombre de tarjeta: {0} \n Tasa de interes anual (%): {1}% \n Deuda actual: {2}".format(diccionario["nombre_tarjeta"],diccionario["tasa_interes"] 
		,diccionario["deuda"]))
	print(" El pago a realizar es de {} con un cargo de {}".format(diccionario["pago_realizar"],diccionario["nuevos_cargos"]))
	print(" Despues del pago, la nueva deuda del mes es de {}".format(diccionario["nueva_deuda"]))


def reportes(lista):
	""" Recibe una lista con la informacion de diferentes tarjetas e imprime el resumen de cada transaccion """
	for i in range(len(lista)):
		a = crea_tarjeta(lista[i][0], lista[i][1], lista[i][2], lista[i][3], lista[i][4])
		a = captura_nueva_deuda(a)	
		generar_reporte(a)
		#generar_reporte()


# Solicitud de datos
a = []
listas_tar = []

while type(a) != dict:
	nombre_tarjeta = input("Digite el nombre de la tarjeta: ")
	tasa_interes = float(input("Digite su tasa de interes: "))
	deuda = int(input("Digite la deuda actual: "))
	pago_realizar = int(input("Digite el pago a realizar: "))
	nuevos_cargos = int(input("Digite los nuevos cargos: "))
	a = crea_tarjeta(nombre_tarjeta, tasa_interes, deuda, pago_realizar, nuevos_cargos)	
	print("=----------------------------------------------------------------=")
	lista_tar = [nombre_tarjeta, tasa_interes, deuda, pago_realizar, nuevos_cargos]
	listas_tar.append(lista_tar)
	if type(a) == dict:
		flag_mas_tarjetas = input("¿Desea ingresar otra tarjeta? Responda SI o NO: ")
		if flag_mas_tarjetas == "SI" or flag_mas_tarjetas == "Si" or flag_mas_tarjetas == "si":
			a = []
		else:
			print("--- no mas tarjetas ---")			
	else:
		listas_tar = []
		print("=----------------------------------------------------------------=")
		
print(listas_tar)
reportes(listas_tar)
	# else:
	# 	a = crea_tarjeta(nombre_tarjeta, tasa_interes, deuda, pago_realizar, nuevos_cargos)	
		


# a = captura_nueva_deuda(a)
# generar_reporte(a)
#print(crea_tarjeta(nombre_tarjeta, tasa_interes, deuda, pago_realizar, nuevos_cargos))




