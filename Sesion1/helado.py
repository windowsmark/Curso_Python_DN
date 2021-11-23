menu = """
1. Helado con oreo
2. Helado con m&m
3. Helado con fresas
4. Helado con brownie
"""

print(menu)
opcion: str = input("Elije una opción: ")
opcion: int = int(opcion)

if opcion == 1:		#Oreo
	precio = 19
elif opcion == 2:	#M&M
	precio = 25
elif opcion == 3:	#Fresas
	precio = 22
else:
	precio = None

if precio == None:
	print('El healdo no esta disponible')
else:
	print(f"El precio del Helado es de ${precio} M.N.")