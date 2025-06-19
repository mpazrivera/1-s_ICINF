#A. Crear un diccionario dentro de este sub-dicciónarios 

datos_climaticos = {
    5700000: {
        "Ciudad": "Castro",
        "Temperatura": 11.8,
        "Precipitación": 2000
    },
    5770000: {
        "Ciudad": "Chonchi",
        "Temperatura": 8.3,
        "Precipitación": 2800
    },
    5790000: {
        "Ciudad": "Quellón",
        "Temperatura": 10.2,
        "Precipitación": 2950
    }
}

# Imprimir el diccionario
print("Diccionario original:")
print(datos_climaticos)

# Parte B - Castro
try:
    temp = datos_climaticos[5700000]["Temperatura"]
    if temp < 10:
        clima = "Frío"
    elif 10 <= temp <= 15:
        clima = "Templado"
    else:
        clima = "Cálido"
except:
    clima = "Desconocida"
datos_climaticos[5700000]["Clima"] = clima

# Chonchi
try:
    temp = datos_climaticos[5770000]["Temperatura"]
    if temp < 10:
        clima = "Frío"
    elif 10 <= temp <= 15:
        clima = "Templado"
    else:
        clima = "Cálido"
except:
    clima = "Desconocida"
datos_climaticos[5770000]["Clima"] = clima

# Quellón
try:
    temp = datos_climaticos[5790000]["Temperatura"]
    if temp < 10:
        clima = "Frío"
    elif 10 <= temp <= 15:
        clima = "Templado"
    else:
        clima = "Cálido"
except:
    clima = "Desconocida"
datos_climaticos[5790000]["Clima"] = clima

#C. Agregar una nueva clase al sub-diccionario Castro 
datos_climaticos[5700000]["Meses Más Lluviosos"] = []

datos_climaticos[5700000]["Meses Más Lluviosos"].append("Mayo")
datos_climaticos[5700000]["Meses Más Lluviosos"].append("Junio")
datos_climaticos[5700000]["Meses Más Lluviosos"].append("Julio")

# Eliminar el mes de junio 
datos_climaticos[5700000]["Meses Más Lluviosos"].remove("Junio")

#D. Cambiar el nombre de la ciudad de chonchi 
datos_climaticos[5770000].update({"Ciudad": "Ciudad de los Tres Pisos"})

#E. crear una lista llamada lluvia y mostrar la suma de todos los datos,
# mostrar el dato mayor y menor
lluvias = [2000, 2800, 2950]
suma_lluvias = sum(lluvias)
print(suma_lluvias)
lluvia_min = min( lluvias)
lluvias_max = max(lluvias)
print("La precipitación más alta", lluvias_max)
print("La precipitacion mas baja", lluvia_min)
#Ver el indic
indice_mayor = lluvias.index(lluvias_max)
print("Índice de la precipitación más alta:", indice_mayor)
#F. Imprimir el diccionrio nuevo
print("Diccionario completo actualizado:")
print(datos_climaticos)
#G. Obtener la lista de tuplas (clave, valor)
lista_tuplas = list(datos_climaticos.items())
# Imprimir la lista
print(lista_tuplas)