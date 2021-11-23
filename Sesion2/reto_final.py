## Reto_final sesion 2

def listas(a):
	""" Ordena la lista y elimina duplicados """
	a = set(a)
	a = list(a)
	a.sort()
	return a


b = [1,2,3,5,5,2,1,5,34,5345,1,1,9]
new_b = listas(b)

for i in new_b:
	print(i)
