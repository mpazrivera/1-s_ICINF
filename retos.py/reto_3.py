#Obtener e imprimir los números del rango mayor o igual a 500 al 100,ingrementando de 3 en 3, luego sumar todos los números obtenidos 
#y obtener el promedio de todos los números. Mostrar los resultados en consola 

# Variables
numeros = []
suma_total = 0

# Generamos los números desde 500 hasta 100, bajando de 3 en 3
for i in range(500, 99, -3):
    print(i)
    numeros.append(i)
    suma_total += i

# Cálculo del promedio
cantidad = len(numeros)
promedio = suma_total / cantidad

# Mostrar resultados
print("\nCantidad de números:", cantidad)
print("Suma total:", suma_total)
print("Promedio:", promedio)


