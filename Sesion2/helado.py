### Version 1.

# menu = (
# (1, "Helado con oreo"),
# (2, "Helado con m&m"),
# (3, "Helado con fresas"),
# (4, "Helado con brownie")
# )

# print(menu)
# opcion: str = input("Elije una opción: ")
# opcion: int = int(opcion)

# if opcion == 1:		#Oreo
# 	precio = 19
# elif opcion == 2:	#M&M
# 	precio = 25
# elif opcion == 3:	#Fresas
# 	precio = 22
# else:
# 	precio = None

# if precio == None:
# 	print('El healdo no esta disponible')
# else:
# 	print(f"El precio del Helado es de ${precio} M.N.")

### Version 2.

menu = (
(1, "Helado con oreo"),
(2, "Helado con m&m"),
(3, "Helado con fresas"),
(4, "Helado con brownie")
)

def imprime_menu(menu):
	"""
	Imprime la lista de topings en la salida estandar
	"""
	print(f"{menu[0][0]}. {menu[0][1]}")
	print(f"{menu[1][0]}. {menu[1][1]}")
	print(f"{menu[2][0]}. {menu[2][1]}")
	print(f"{menu[3][0]}. {menu[3][1]}")

def lee_opcion():
	"""
	Lee la opcion elegida por el usuario desde la entrada
	"""	
	opcion: str = input("Elije una opción: ")
	opcion: int = int(opcion)

	return opcion

def imprime_precio():
	"""imprime el precio estandar"""
	if precio == None:
		print('El healdo no esta disponible')
	else:
	print(f"El precio del Helado es de ${precio} M.N.")



if opcion == 1:		#Oreo
	precio = 19
elif opcion == 2:	#M&M
	precio = 25
elif opcion == 3:	#Fresas
	precio = 22
else:
	precio = None

