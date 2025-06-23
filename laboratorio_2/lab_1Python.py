#Labratorio 1 de pseint pasado a python

#LE DAMOS LA BIENVENIDA AL USUARIO Y LE DECIMOS QUE INGRESE EL PRECIO UNITARIO
# DE LOS LIBROS QUE QUIERA COMPRAR Y LA CANTIDAD  
print("Hola, bienvenido :)")
precio_libro = float(input("Ingrese el precio unitario del libro: $"))
cantidad_libro = int(input("Ingrese la cantidad de libros: "))

#VEMOS SI EL PRECIO Y LA CANTIDAD SEAN NUMEROS POSITIVOS 
if precio_libro<=0 or cantidad_libro<= 0:
    raise ValueError("EL precio y la cantidad deben de ser positivo :)")

#LE PREGUNTAMOS SI ES UN TEXTO ACADEMICO Y SI ESTÁ AFILIADO A LA UNIVERSIDAD PARA QUE SE LE 
#AGREGUE UN DESCUENTO
es_academico = str(input("¿Es un texto académico? (s/n): ")).strip().lower() == "s"
es_afiliado = str(input("¿Está afiliado/a a la Universidad de Los Lagos? (s/n): ")).strip().lower() == "s"

#SACAMOS EL SUBTOTAL QUE TENDRA 
sub_total = precio_libro * cantidad_libro

#Se hace la comparativa dependiendo de lo haya ingresado el usuario,para que 
#se le aplique un descuento 
if es_academico: 
    descuento_academico = sub_total * 0.15
else:
    descuento_academico = 0

monto_post_academico = sub_total - descuento_academico

if es_afiliado:
    descuento_afiliado = monto_post_academico *0.05
else:
    descuento_afiliado = 0

monto_post_afiliado = monto_post_academico - descuento_afiliado

if monto_post_afiliado >50000:
    descuento_vol = monto_post_afiliado*0.05
else: 
    descuento_vol = 0

monto_post_vol = monto_post_afiliado - descuento_vol

#Se saca el total de los descuentos y el total a pagar
total_descuento = descuento_academico + descuento_afiliado + descuento_vol
total_pagar = sub_total - total_descuento

#Se le desglosara la boleta con los descuentos aplicados si es que cumplia las condiciones 
#y el total a pagar 
print("============= Desglose de la compra =============")
print("Subtotal de la compra sin descuentos: $",sub_total)
print("Descuento por libro academico: $", descuento_academico)
print("Descuento por afiliación Ulagos: $", descuento_afiliado)
print("Descuento por volumen de compra: $", descuento_vol)
print("Descuento total", total_descuento)
print("Total a pagar", total_pagar)