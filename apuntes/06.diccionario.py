#Caracteristicas de los diccionarios 
#Son desordenadas, son mutables, tiene claves unicas y tienen acceso con llaves:un diccionario 
#pueden ser accedidos mediante su clave, en lugar de un índice, como se hace en las listas o tuplas
#Hay dos formas de hacer un diccionario
#forma 1
estudiante = dict(
    nombre = "Maria Paz Rivera",
    universidad = "Universidad de Los Lagos",
    carrera = "Ingenieria Civil Informática",
    sede = "Sede Chiloé",
    semestre = "Semestre 1"
)
print(estudiante)

#Forma 2
datos = {
    "Nombre": "Maria Paz",
    "Edad": 18,
    "Apodo": "Pachi",
    "Hobbies": ["Jugar futbol", "Escuchar musica"]#agregue una lista para colocar 2 hobbies
}
print(datos)

#ejemplos de diccionarios con algunas funciones
#ejemplo 1
persona = {
    "Nombre": "Puchi",
    "Edad": 18,
    "Ciudad": "Castro"
}

# Usando funciones del diccionario
print(persona.keys())     # Muestra todas las claves
print(persona.values())   # Muestra todos los valores
print(persona.items())    # Muestra una lista de tuplas (clave, valor)

#ejemplo 2
estudiante = {
    "Nombre": "Camila",
    "Cursos": ["Matemáticas", "Lenguaje", "Ciencias"],
    "Promedio": 6.3
}
print(estudiante)
# Agregar un nuevo curso usando append()
estudiante["Cursos"].append("Historia")

# Mostrar los cursos actualizados
print("diccionario actualizado")
print(estudiante)
print("cursos actualizados")
print(estudiante["Cursos"])

#ejemplo 3
producto = {
    "Nombre": "Notebook",
    "Precio": 450000
}

# Obtener valor de una clave existente
print(producto.get("Precio"))  # 450000

# Obtener valor de una clave que NO existe, sin error
print(producto.get("Color", "No especificado"))  # "No especificado"

#ejemplo 4
animal = {
    "Especie": "Perro",
    "Nombre": "Firulais",
    "Edad": 4
}
print(animal)
# Actualizar edad
animal.update({"Edad": 5})

# Eliminar clave "Nombre"
animal.pop("Nombre")
print(animal)

#ejemplo 5 
#un diccionario dentro de otro diccionario
familia = {
    "Padre": {
        "Nombre": "Carlos",
        "Edad": 45},
    "Madre": {
        "Nombre": "Ana",
        "Edad": 43},
    "Hijo": 
    {"Nombre": "Lucas", 
     "Edad": 15}
}

# Acceder al nombre del hijo
print(familia)
print("nombre del hijo")
print(familia["Hijo"]["Nombre"])

#Un ejemplo usando la funcion keys
persona = {
    "Nombre": "Lucía",
    "Edad": 30,
    "Ciudad": "Ancud",
    "Profesión": "Ingeniera"
}

# Obtener solo las claves del diccionario
claves = persona.keys()

# Mostrar claves
print("Claves del diccionario:")
print(claves)

# Convertir a lista (opcional)
lista_claves = list(claves)
print("Claves como lista:")
print(lista_claves)