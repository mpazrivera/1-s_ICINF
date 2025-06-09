#Le pedimos al usuario que ingrese los grados celsius 
grados_c = float(input("Ingrse los Grados Celsius  "))

grados_f = grados_c* 1.8 + 32
grados_k = grados_c + 273.15

print("Los grados celsius en grados Fahrenheit seria: ")
print(round(grados_f, 2))
print("En grados kelvin seria: ")
print(grados_k)

