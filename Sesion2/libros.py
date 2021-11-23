libros = (
    "El señor de los anillos",
    "El árte de la guerra",
    "Triptofanito",
    "La Meta",
    "El árte de la guerra",
    "La Meta",    
)

# Eliminando duplicados

# Ordenando
libros: set = set(libros)
libros: list = list(libros)
libros.sort()
# Uniendo lineas de texto, en una sola línea de texto:
texto = "\n".join(libros)

# Imprimiendo la lista final
print(texto)