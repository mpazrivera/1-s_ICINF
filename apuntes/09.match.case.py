print("MENU")
print("1","Hamburguesa")
print("2","Pizza")
print("3","Completo")

opcion = input("Por favor, elige una opcion (1, 2 o 3): ")

match opcion:
    case "1": print("Eligio la hamburguesa, Tiene un total de $5500 pesos")
    
    case "2": print("Eligio la pizza, Tiene un total de $3500 pesos")
    
    case "3": print("Eligio el completo, Tiene un total de $2500 pesos")
    
    
# DETERMINAR ESTACION SEGUN MES
mes = 4 # ABRIL
match mes:
    case 12 | 1 | 2:
        print("Verano")
        
    case 3 | 4 | 5:
        print("Otoño")
    case 6 | 7 | 8:
        print("Primavera")
    case 9 | 10 | 11:
        print("Invierno")
    case _:
        print("Mes mal ingresado")
        
        
# PATRONES COMPUESTOS 
x = [1, 2, 3]
match x:
    case [a, b, c]:
        print("Elementos de la lista x: ",a,b,c)
        
datos = {"Nombre": "Victor", "Edad": 31}
match datos:
    case {"Nombre": n,"Edad": e}: 
        print("Nombre: ",n,"Edad: ",e)



# Ejemplo con match case - días de la semana
dia = input("Ingresa un día de la semana: ").lower()

match dia:
    case "lunes":
        print("Comienza la semana. ¡Ánimo!")
    case "martes":
        print("Segundo día... ya falta menos.")
    case "miércoles":
        print("¡Mitad de semana!")
    case "jueves":
        print("Ya casi es viernes.")
    case "viernes":
        print("¡Por fin viernes!")
    case "sábado" | "domingo":
        print("Es fin de semana, a descansar.")
    case _:
        print("No es un día válido.")
'''
Compara el valor ingresado (dia) contra varias opciones.
Si se escribe "sábado" o "domingo", se usa | (pipe) para agrupar esos dos casos.
El caso _ es el comodín (como default), se ejecuta si no coincide con ningún otro.
'''
#Se le va a pedir al usuario que ingrese una figura y se le mostrará sus lados
#En el caso de que no se encuentre la figura se le arrojara un mensaje diciendo que no se tiene 
#la información de la figura 
figura = input("Ingresa una figura geométrica: ").lower()
match figura:
    case "triángulo":
        print("Tiene 3 lados.")
    case "cuadrado":
        print("Tiene 4 lados.")
    case "pentágono":
        print("Tiene 5 lados.")
    case "hexágono":
        print("Tiene 6 lados.")
    case "círculo":
        print("No tiene lados, es una figura curva.")
    case _:
        print("No tengo información sobre esa figura.")
