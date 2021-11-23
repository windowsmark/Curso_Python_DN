zodiaco = {
    "Aries": ["Sagitario", "Leo", "Acuario"],
    "Tauro": ["Cáncer", "Libra", "Virgo"],
    "Géminis": ["Leo", "Libra", "Géminis", "Capricornio", "Sagitario"],
}

# lee un signo desde el usuario
signo = input("Dame un signo del zodiaco: ")
signo = signo.title()

# obten signos compatibles
if signo in zodiaco.keys():
	# genera una cadena con todos los signos
	signos_afines: list = zodiaco[signo]
	signos_afines: str = "\n".join(signos_afines)
# imprime el resultado
else:
	print("Error: signo no encontrado!")
