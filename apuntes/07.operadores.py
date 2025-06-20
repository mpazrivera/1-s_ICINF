bencina = True
encendido = True
edad = 19

#Utilizando el operador AND
if bencina and encendido: 
    print("El vehiculo puede avanzar")
else: 
    print("El vehiculo NO puede avanzar")

#Utilizando el operador OR
if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo o puede arrancar")

#Utilizando el operador NOT junto con el AND
if not bencina and encendido:
    print("El auto puede avanzar")
else:
    print("El auto no puede avanzar")