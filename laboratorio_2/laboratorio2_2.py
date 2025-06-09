#Primer paso: ingresar datos por consola
resumen = str(input("Ingrese su resumen: "))

#Segundo paso : determinar si el resumen esta dentro del rango de caracteres
cumplecon_rango = len(resumen) <= 50
print(f"Cumple con el límite de 50 caracteres: {cumplecon_rango}")

#Mostrar datos solicitados
print ("Informacion del informe")
print(f"Longitud total del resumen: {len(resumen)}")
print(f"Resumen en mayúsculas: {resumen.upper()}")
print(f"Resumen en minúsculas: {resumen.lower()}")
print(f"Número de veces que aparece la vocal 'e': {resumen.count('e')}")
print(f"Primeros 15 caracteres: {resumen[:15]}")
print(f"Últimos 15 caracteres: {resumen[-15:]}")
print(f"Resumen con palabras unidas por comas: {', '.join(resumen.split())}")