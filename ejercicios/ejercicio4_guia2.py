#Nombres de los integrantes: Hector Tobar y Maria Rivera

#Pedir al usuario cuántos cubos quiere ver
n = int(input("Ingrese la cantidad de cubos que desea ver: "))

#Variable para el primer número impar
impar = 1

#Recorrer desde 1 hasta n
for i in range(1, n + 1):
    suma = 0
    print(f"{i}^3 =", end=" ")

    #Sumar los siguientes i impares
    for j in range(i):
        print(impar, end=" ")
        suma += impar
        impar += 2  # Pasar al siguiente número impar
        if j < i - 1:
            print("+", end=" ")

    print("=", suma)