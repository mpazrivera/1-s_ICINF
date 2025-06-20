#Las listas no es lo mismo arreglos(ARRAY)
#caracteristicas de la lista : Ordenada, Editable, Dinamica, NO unica
#listas[] tuplas() set{}

lista1= [ "pachi", 18, True]
print (lista1)

#Lista de solo numeros 
n =[1,2,3,4,5,6]

#Lista de solo strings - UTILIZANDO LIST
ramos = list (["programación", "Química", "poo"])
print(ramos)

#Imprime el la posición del primer elemento de la lista 
estudiantes = ["vale", "pachi", "messi", "vale"]
print(estudiantes[0])
'''
Esta función es count( ). Queremos saber la cantidad de ocurrencias del elemento
“Vale” en la lista estudiantes, en este caso el resultado que debe arrojarnos
la terminal sería 2 ocurrencias
'''
print(estudiantes. count ("vale"))

#Funcion para unir dos listas, tuplas,ect.
jugadores_euro = ["messi", "ronaldo", "modric", "kross", "pedri", "lewandowski"]
jugadores_chilenos = ["paredes", "fierro","vidal","sanchez", "pizarro","bravo"]
print(jugadores_euro)
print(jugadores_chilenos)
jugadores = list(zip(jugadores_euro,jugadores_chilenos))
print(jugadores)