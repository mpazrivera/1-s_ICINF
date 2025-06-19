entrada = input("Ingrese un valor entero")

try: # INTENTA LO SIGUIENTE
    numero = int(entrada)
    print(f"Numero ingresado:{numero}")
except ValueError: # ERROR POR TIPO DE DATO
    print("Error de valor: el valor ingresado no es entero")
except Exception as e: # SE PUEDE AGREGAR MAS DE UN EXCEPT
    print(f"Error inesperado:{e}") # ERROR GENERICO E INESEPRADO
else:
    print("¡La conversion fue exitosa!")
finally: # CORROBORACION DE QUE LO ANTERIOR SE EJECUTO CORRECTAMENTE
    print("Finalizacion de bloque")