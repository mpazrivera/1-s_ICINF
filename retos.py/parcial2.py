#A. Crea un diccionario con los datos de los gatos
gatitos = {
    101: {"Nombre": "Luna", "Peso": 1.2, "Edad": 3, "Tamaño": 30},
    102: {"Nombre": "Michi", "Peso": 0.8, "Edad": 2, "Tamaño": 25},
    103: {"Nombre": "Pepito", "Peso": 2.5, "Edad": 5, "Tamaño": 35}
}

# Mostrar el diccionario original
print("Diccionario Inicial de Gatitos:\n")
print(gatitos)

#B. Crear un bucle que recorra el dicionario para añadir la clasificación de peso
#Agregar clave "Clasificación-Peso" según el valor del peso
for gatito in gatitos.values():
    peso = gatitos.get("Peso", 0)
    if peso < 1:
        gatito["Clasificación_Peso"] = "Bajo Peso"
    elif 1 <= peso <= 4:
        gatito["Clasificación_Peso"] = "Normal"
    else:
        gatito["Clasificación_Peso"] = "Sobre Peso"

#C. Crear otro bucle para que se agregue la categoria etaria 
for gatito in gatitos.values():
    try:
        edad = gatito["Edad"]
        if edad < 4:
            gatito["Categoría-Etaria"] = "Cachorro"
        elif 4 <= edad <= 12:
            gatito["Categoría-Etaria"] = "Joven"
        else:
            gatito["Categoría-Etaria"] = "Adulto"
    except Exception:
        gatito["Categoría-Etaria"] = "Desconocida"


#D. Crear una lista de tuplas donde el primer elemento de la tupla tiene que ser el número de ingreso, el segundo valor sea el peso y 
#luego ordenarla de menor a mayor.
lista_pesos = [(ingreso, datos["Peso"]) for ingreso, datos in gatitos.items()]
#Se ordenara el peso de menor a mayor
lista_pesos.sort(key=lambda x: x[1])
# Imprimir la lista ordenada
print("Lista ordenada por peso (menor a mayor): ")
for ingreso, peso in lista_pesos:
    print(f"Ingreso: {ingreso}, Peso: {peso} kg")

#E. Imprementar un bucle que le permita ingresar datos de nuevos gatitos
while True:
    print("Ingrese los datos del nuevo gatito:")
    try:
        ingreso = int(input("N° de Ingreso: "))
        nombre = input("Nombre: ")
        peso = float(input("Peso: "))
        edad = int(input("Edad: "))
        tamaño = int(input("Tamaño: "))

        # Agregar al gatito al diccionario
        gatitos[ingreso] = {
            "Nombre": nombre,
            "Peso": peso,
            "Edad": edad,
            "Tamaño": tamaño
        }

        #Se le clasifica por peso 
        if peso < 1:
            clasif = "Bajo Peso"
        elif 1 <= peso <= 4:
            clasif = "Normal"
        else:
            clasif = "Sobre Peso"
        gatitos[ingreso]["Clasificación-Peso"] = clasif

        #Se le clasifica por su categoria-etaria 
        try:
            if edad < 4:
                gatitos[ingreso]["Categoría-Etaria"] = "Cachorro"
            elif 4 <= edad <= 12:
                gatitos[ingreso]["Categoría-Etaria"] = "Joven"
            else:
                gatitos[ingreso]["Categoría-Etaria"] = "Adulto"
        except:
            gatitos[ingreso]["Categoría-Etaria"] = "Desconocida"
    
     except ValueError:
        print("Entrada inválida. Intente nuevamente.")
        continue

    continuar = input("¿Desea agregar otro gatito? (s/n): ").strip().lower()
    if continuar != 's':
        break

#F. Pedir un numero ingresado de gatito existente y el nuevo tamaño 

#G. generar una lista con todos los valores de peso
peso = [1.2, 0.8, 2.5]
sum_peso = sum (peso)
promedio_peso = sum_peso/3
peso_max = max(peso)
peso_min = min(peso)

print("El peso más alto de los gatitos es: ", peso_max)
print("El peso más bajo de los gatitos es: ", peso_min)

#diccionario nuevo con todas las modificaciones 
print(gatitos)

