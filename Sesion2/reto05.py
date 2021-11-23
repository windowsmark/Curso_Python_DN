## Reto 05

i = 1
fi = [0,1]
# fi.append(1)
# n_i = i - 1 
# print(fi[i - 1])
cont = 0
while cont < 1000:
	n_fi = fi[i] + fi[i-1] 
	i = i + 1
	if n_fi > 1000:
		cont = 1000
	else:
		fi.append(n_fi)
print(fi)