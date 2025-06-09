#Ingresar tres valores numéricos diferentes
entero = int(input("Ingresa un número entero: "))
flotante = float(input("Ingresa un número flotante: "))
complejo = complex(input("Ingrese un número complejo: "))

#Se calcula la potencia compleja
potencia_compleja = complejo ** entero
print(f"Potencia Compleja: {potencia_compleja}")
#Suma Mixta (Complejo y Flotante)
suma_mixta = complejo + flotante
print(f"Suma Mixta: {suma_mixta}")
#Producto Mixto (Complejo y Entero)
producto_mixto = complejo * entero
print(f"Producto Mixto: {producto_mixto}")

abs_potencia = abs(potencia_compleja)
print(f"modulo de potencia compleja: {abs_potencia: .3f}")