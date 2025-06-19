from colorama import init, Fore # COLORES PARA LA TERMINAR DEPENDIENDO EN DONDE LO QUIERA COLOCAR
init()


print(Fore.GREEN + "#### 01- CONDICIONALES IF, ELSE, ELIF ####")

licencia = input("¿Tienes licencia de conducir?: (Si) o (No)")
edad = int(input("Ingresa tu edad: "))
automovil = input("¿Tienes automovil?")

print(Fore.YELLOW +"## Testeando comparadores y el IF ##")
if licencia: # SI EL VALOR ES VERDADERO O FALSO
    print("Puedo conducir porque tengo licencia")
else:
    print("No tengo licencia para conducir")
    
# ESTO IMPRIME EL CASO CORRESPONDIENTE DE ACUERDO A SI ES FALSO O VERDADERO (True o False)


if edad >= 18:
    print("Puedo conducir porque soy mayor de edad")
else:
    print("No puedo conducir porque no soy mayor de edad")
    
    
if licencia and edad >= 18:
    print("Puedo conducir porque tengo licencia y la edad")
elif licencia and edad < 18:
    print("No puedo conducir porque no tengo la licencia ni la edad")
else:
    print("No puedo conducir porque no tengo el auto, la edad ni la licencia")
