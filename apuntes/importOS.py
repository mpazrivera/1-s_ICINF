import os
print("Directorio de trabajo actual:",os.getcwd()) # MUESTRA LA UBICACION DEL DIRECTORIO ACTUAL

try:
    archivo = open("Semestre-1-python/Primer-semestre-en-python/data/datos.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")
else:
    print("Lectura exitosa.")
finally:
    try:
        archivo.close()
        print("Archivo cerrado")
    except NameError:
        print("Finalizacion de bloque")