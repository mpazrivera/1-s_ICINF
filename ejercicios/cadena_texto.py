#ingresar una frase de 30 caracteres incluyendo los espacios.
frase = input("Ingrese una frase (máximo 30 caracteres): ")
len(frase) <= 30

#Crear 2 variables, una para la minusculas y otra para las mayusculas
frase_mayuscula = frase.upper()
frase_minuscula = frase.lower()

#Contar cuantas veces esta la a
contar_a = frase_minuscula.count("a")

#Imprimir la longitud de la frase
longitud = len(frase)

# Mostrar resultados
print("\nFrase en mayúsculas:", frase_mayuscula)
print("Frase en minúsculas:", frase_minuscula)
print("Cantidad de letras 'a' o 'A':", contar_a)
print("Longitud de la frase:", longitud)
