'''FLOAT= FLOTANES(SON NÚMEROS DECIMALES EJ: 32.45) SE PUEDE USAR PARA MEDIR LA ESTATURA DE 
UNA PERSONA 
'''
#DECLARANDO 2 VARIABLES TIPO ENTEROS (INT)
#No podemos comenzar un número entero por 0
edad = 18
año_de_nac = 2006
#IMPRESIÓN DE VARIABLES
print(edad)
print("Hola tengo ", edad, "años y naci en el año", año_de_nac)

#DECLARANDO 2 VARIABLES TIPO FLOTANTE (FLOAT)
estatura = 1.56
peso = 65.7
#IMPRESIÓN DE LAS VARIABLES
#Los números en coma flotante son números con decimales (números reales en pseint) 
print("Mi estatura es", estatura, "cm y mi peso es" , peso, "kg")

#NÚMEROS COMPLEJOS(COMPLEX)
complejo = 4 + 5j #se esta declarando un numero complejo
comp = complex(8,12)#Otra forma de declarar complejo 
#Ingresado por consola 
complejo = complex(input("Ingrese un número complejo: "))

#formateando la salida de los números
"pi" = 3.14159
#forma 1
print("el valor de pi es aproximadamente {:.2f}". format(pi))
#forma 2
print(f"El valor de pi es aproximadamente: {pi:.2f}")
#forma 3
print("la velocidad del obketo en caida libre es de:","%.2f" % pi)

