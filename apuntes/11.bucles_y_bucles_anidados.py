#un ejemplo de bucle utilizando el FOR, este bucle contiene una lista adentro, que este mostrará
#las frutas de la lista, uno por uno diciendo que fruta le gustan.
frutas = ["manzana", "plátano", "pera"]

for fruta in frutas:
    print("Me gusta la", fruta)

#ejemplo de bucles utilizando For con range, este mostrará el rango de 1 al 5
# el "i" es un contador 
for i in range(1, 6):
    print("Número:", i)
 
#ejemplo de bucle WHILE, este bucle ira contando los numeros hasta llegar a 5 
contador = 1
while contador <= 5:
    print("Contando:", contador)
    contador += 1

#Ejemplo con bucle FOR, este recorrera los items del diccionario
persona = {
    "nombre": "Sofía", 
    "edad": 20, 
    "ciudad": "Castro"
}

for clave, valor in persona.items():
    print(clave, ":", valor)

#Bucle WHILE, este permitira escribir, hasta que ingresen la palabra SALIR, 
#haciendo que el bucle termine
respuesta = ""

while respuesta != "salir":
    respuesta = input("Escribe algo (o 'salir' para terminar): ")
    print("Escribiste:", respuesta)





'''
Ahora se mostraran ejemplos de bucles anidados 
'''
#bucle utilizando BREACK, este hace que se pause el bucle para que no sea infinito
print("Ejemplo con break:")

for i in range(1, 4):  # Primer bucle: 1 a 3
    for j in range(1, 6):  # Segundo bucle: 1 a 5
        if j == 3:
            print(f"Se rompe el bucle interior en i={i}, j={j}")
            break  # Sale del bucle interno
        print(f"i={i}, j={j}")

#bucle utilizando CONTINUE, para que siga el bucle que se hacia pausado
print("\nEjemplo con continue:")

for fila in range(1, 4):  # 1 a 3
    for columna in range(1, 6):  # 1 a 5
        if columna == 2:
            continue  # Salta el número 2 y sigue
        print(f"Fila {fila}, Columna {columna}")

'''Ejemplo: Buscar un número en una matriz
Vamos a simular una matriz (una lista de listas), recorrerla, y:
Usar continue para saltar ceros.
Usar break para detenerse cuando encuentra el número 5
'''
'''Recorre cada número en la matriz.
No muestra los ceros (continue).
Cuando encuentra el número 5, lo muestra y detiene ambos bucles (break anidado).
'''
matriz = [
    [1, 0, 3],
    [4, 0, 5],
    [6, 7, 8]
]

print("Buscando el número 5 en la matriz:")

for fila in matriz:
    for numero in fila:
        if numero == 0:
            continue  # Saltar los ceros, no los mostramos
        print("Número:", numero)
        if numero == 5:
            print("¡Encontrado el número 5!")
            break  # Detener el bucle interior al encontrar el 5
    else:
        continue  # Si no se rompe el bucle interior, seguir
    break  # Si se rompió el bucle interior, romper también el exterior
