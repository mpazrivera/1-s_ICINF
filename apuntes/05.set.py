#un set vacio
#forma 1
conjunto_vicio = set()
#forma 2
conjunto_vacio = {}

#Un set de frutas
frutas = {"manzana", "plátano", "cereza"}
print(frutas)

#Algunos ejemplos con sus funciones
# Agregar un elemento a un set con .add()
frutas = {"manzana", "plátano"}
frutas.add("naranja")
print(frutas)  # Resultado: {"manzana", "plátano", "naranja"}

#Eliminar un elemento con .remove()
frutas = {"manzana", "plátano", "naranja"}
frutas.remove("plátano")
print(frutas)  # Resultado: {"manzana", "naranja"}
#Lanza error si el elemento no está

#Eliminar un elemento sin error con .discard()
frutas = {"manzana", "naranja"}
frutas.discard("uva")  # No lanza error
print(frutas)

# Verificar si un elemento está en el set
print("cereza" in {"manzana", "cereza"})  # Resultado: True

#Unión de dos sets (| o .union())
frutas_1 = {"manzana", "plátano"}
frutas_2 = {"cereza", "manzana"}
union = frutas_1 | frutas_2
print(union)  # Resultado: {"manzana", "plátano", "cereza"}

#Intersección de sets (&)
comunes = frutas_1 & frutas_2
print(comunes)  # Resultado: {"manzana"}

#Diferencia de sets (-)
solo_frutas_1 = frutas_1 - frutas_2
print(solo_frutas_1)  # Resultado: {"plátano"}

#Convertir un set en una lista y en una tupla
set_frutas = {"pera", "melón", "sandía"}
lista_frutas = list(set_frutas)
tupla_frutas = tuple(set_frutas)
print(lista_frutas)
print(tupla_frutas)
