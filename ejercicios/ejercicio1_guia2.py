print("Ingrese a continuación un párrafo: ")
texto = input("Ingrese su texto aqui: ")
if len(texto) == 0:
    raise ValueError("El texto no debe quedar vacio")
parrafo_nuevo = texto.split()
print(parrafo_nuevo)
print("")
palabra = input("Ahora indique una palabra a buscar: ")
contador_de_palabras = 0
for i in parrafo_nuevo:
    if palabra == i:
        contador_de_palabras = contador_de_palabras+1

if contador_de_palabras == 0:
    resultado = "El párrafo está vacío"
else:
    resultado = f"La palabra se repite: {contador_de_palabras} veces."

print(resultado)
