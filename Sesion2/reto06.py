## Reto 06
# Programa que calcula el minimo común múltiplo 

def mcm(a,b):
	if b%a == 0:
		m = b
	elif a%b == 0:
		m = a
	else:
		d = max([a,b]) * 2
		while d%a != 0 or d%b != 0:
			d = d + 1
		m = d	
	return m

a = input("digite el valor de a: ")
b = input("digite el valor de b: ")
a = int(a)
b = int(b)


print(f"El minimo común múltiplo entre {a} y {b} es {mcm(a,b)}")