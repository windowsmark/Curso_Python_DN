print("""==============================
==== Calculadora contable ====
=============================="""	)

# Solicitud de datos
nombre_tarjeta = input("Digite el nombre de la tarjeta: ")
tasa_interes = int(input("Digite su tasa de interes: "))
deuda = int(input("Digite la deuda actual: "))
pago_realizar = int(input("Digite el pago a realizar: "))
nuevos_cargos = int(input("Digite los nuevos cargos: "))



if pago_realizar > deuda:
	print("No es posible hacer un pago mayor a la deuda")
else:
#Calculos
	interes_mensual = tasa_interes/12
	deuda_recalculada = (deuda - pago_realizar) * (1 + interes_mensual)
	nueva_deuda = deuda_recalculada + nuevos_cargos
	#Resumen
	print("""
#################################
##  Resumen de la transacción  ##
#################################
		""")
	print("La tarjeta {0} con tasa de interes de {1} tiene una deuda actual de {2}".format(nombre_tarjeta, tasa_interes, deuda))
	print("El pago a realizar es de {} con un cargo de {}".format(pago_realizar, nuevos_cargos))
	print("Despues del pago, la nueva deuda para el proximo mes es de {}".format(nueva_deuda))
