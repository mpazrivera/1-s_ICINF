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