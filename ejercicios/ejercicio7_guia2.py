#Nombre de los integrantes: Hector Tobar y Maria Rivera

#Pedir al usuario el número
n = int(input("Ingrese un número para calcular su factorial: "))

#Inicializar la variable factorial en 1
factorial = 1

# i el número es 0, su factorial es 1
if n == 0:
    factorial = 1
else:
    #Bucle para multiplicar desde n hasta 1
    while n > 0:
        factorial = factorial * n
        n = n - 1
#Mostrar el resultado
print("El factorial es:", factorial)