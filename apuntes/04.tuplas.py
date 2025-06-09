#Caracteristicas de una tupla: Ordenada, Inmutable, Dinamica, Eficientes
#iniciando una tupla
#forma 1
new_tupla = tuple()
#forma 2
new_tupla = ("messi","vicho",340)

#creando una tupla
estudiantes = ('Ian','hector','isi','pachi','ana','vale')
print(estudiantes)
#Función index en tuplas
print(estudiantes.index("vale"))

#Crear una tupla con precios
precios_manzana = (800, 820, 800)
print("Precios de la manzana:", precios_manzana)
#Las tuplas son inmutables (no se pueden modificar una vez creadas)
#y pueden contener valores repetidos.

#Acceder a elementos por índice
precios_platano = (500, 500, 550)
print("Primer precio del platano:", precios_platano[0])
print("Último precio del platano:", precios_platano[-1])
#Puedes acceder a los elementos igual que con una lista, usando índices.

#Recorrer una tupla con un bucle
precios_cereza = (1000, 1050, 1100)
print("Precios de la cereza:")
for precio in precios_cereza:
    print(precio)
#Ideal para leer todos los precios registrados para una fruta.

# Eliminar precios repetidos con set()
colores = ('rosado', 'amarillo','verde','azul','blanco','verde')
colores_unicos = set(colores)
print("Precios únicos del platano:", colores_unicos)
#Convertimos la tupla a un set para eliminar valores duplicados.

#Calcular promedio de precios únicos
platanos= (500,500,550,600)
print('precios de los platanos', platanos)
precios_unicos = set((500, 500, 550,600))
print('precios unicos', precios_unicos)
promedio = sum(precios_unicos) / len(precios_unicos)
print(f"Promedio de precios únicos del platano: {promedio:.2f}")

#Tuplas dentro de un diccionario (inventario de frutería)
inventario = {
    "Manzana": (800, 820, 800),
    "Platano": (500, 500, 550),
    "Cereza": (1000, 1050, 1100)
}
print("Precios de la manzana:", inventario["Manzana"])
#Así puedes usar tuplas como valores en un diccionario

#len(tupla) Devuelve la longitud (cantidad de elementos) de la tupla.
frutas = ("Manzana", "Plátano", "Cereza")
print(len(frutas))  # Resultado: 3

#tupla.count(valor) Cuenta cuántas veces aparece un valor específico en la tupla.
precios = (500, 500, 550)
print(precios.count(500))  # Resultado: 2

#tupla.index(valor) devuelve el índice de la primera vez que aparece un valor
colores = ("rojo", "verde", "azul", "verde")
print(colores.index("verde"))  # Resultado: 1

#Convertir tupla en lista (para modificarla) Si necesitas
#cambiarla, puedes convertirla a lista:
numeros = (1, 2, 3)
lista = list(numeros)
lista.append(4)
nueva_tupla = tuple(lista)
print(nueva_tupla)  # Resultado: (1, 2, 3, 4)

#in (Verificar si un valor está en la tupla)
dias = ("lunes", "martes", "miércoles")
print("martes" in dias)  # Resultado: True
