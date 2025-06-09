#Precio unitario
hola = input("Hola que desea: ")
#El usuario pide los precios unitario y se los damos 
Martillo = (float("2500"))
Clavos = (float("300"))
Serrucho = (float("3000"))
Tornillos = (float("200"))
print("El precio de los productos son: ")
print("Martillo", Martillo)
print("Clavos: ", Clavos)
print("Serrucho: ", Serrucho)
print("Tornillos: ", Tornillos)

#CANTIDAD PRODUCTOS
a = int(input("Ingrese la cantidad de Martillo: "))
cantidad_martillo = (Martillo * a)
print("El total de Martillo es: ", cantidad_martillo)

b = int(input("Ingrese cantidad de Clavos: "))
cantidad_clavos = (Clavos * b)
print("El total de clavos es: ", cantidad_clavos)

c = int(input("Ingrese cantidad de Serrucho: "))
cantidad_serrucho = (Serrucho * c)
print("El total de Serrucho es: ", cantidad_serrucho)

d = int(input("Ingrese cantidad de Tornillos: "))
cantidad_tornillos = (Tornillos * d)
print("El total de Tornillos es: ", cantidad_tornillos)

#TOTAL DE PRODUCTOS COMPRADOS
cantidad_total = (cantidad_martillo + cantidad_clavos + cantidad_serrucho + cantidad_tornillos)
print("El precio total es de: ", cantidad_total)

#VALOR MINIMO Y MAXIMO
valor_minimo = min(cantidad_martillo, cantidad_clavos, cantidad_serrucho, cantidad_tornillos)
print("El valor minimo seria: ", valor_minimo)
valor_maximo = max(cantidad_clavos, cantidad_martillo, cantidad_serrucho, cantidad_tornillos)
print("El valor maximo seria: ", valor_maximo)

#OBTENER EL IVA (19%)
iva = 0.19
total_iva = cantidad_total * iva
total_precio_iva = total_iva + cantidad_total
print("El total de iva es: ", total_iva)
print("El precio total con el IVA es: ", total_precio_iva)