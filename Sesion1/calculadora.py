print("""===========================
======  Calculadora  ======
===========================""")

print("Por favor digite dos numeros")
numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segundo numero: "))
print("""De las siguientes operaciones:
	1. +
	2. -
	3. *
	4. /
	""")
operador = input("Digite la operacion que desea realizar: ")

if operador == '+':
	operacion = numero1 + numero2
elif operador == '-':
	operacion = numero1 - numero2
elif operador == '*':
	operacion = numero1 * numero2
elif operador == '/':
	if numero1 == 0:
		operacion = "Error: No se puede dividir entre 0"
	else:
		operacion = numero1 / numero2
else:
	operacion = "La operacion digitada no se encuentra definida"

print(f"El resultado es {numero1} {operador} {numero2} = {operacion}")
