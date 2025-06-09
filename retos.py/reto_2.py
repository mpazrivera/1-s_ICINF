# Definir el inventario con tres precios por fruta (en pesos chilenos)
inventario = {
    "Manzana": (800, 820, 800),
    "Platano": (500, 500, 550),  # Dos precios repetidos
    "Cereza": (1000, 1050, 1100)
    }

# Obtener precios únicos del platano
precios_unicos_platano = set(inventario["Platano"])

# Crear la lista con los tipos de frutas
tipos_frutas = list(inventario.keys())

# Calcular el promedio de los precios únicos del platano
promedio_platano = sum(precios_unicos_platano) / len(precios_unicos_platano)

# Mostrar los resultados
print("Inventario completo:", inventario)
print("Precios únicos del platano:", precios_unicos_platano)
print("Tipos de frutas:", tipos_frutas)
print(f"Promedio de precios únicos del platano: {promedio_platano:.3f}")
