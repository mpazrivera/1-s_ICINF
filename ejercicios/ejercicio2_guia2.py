# Inicialización de variables
suma = 0
ascendente = 500
descendente = 456

while ascendente <= 800:
    print(ascendente)
    print(descendente)
    suma = suma + ascendente     
    suma = suma + descendente     

    ascendente = ascendente + 10   # Aumenta el número ascendente
    descendente = descendente - 2       # Disminuye el número descendente

# Imprimir resultado final 
print("La sumatoria es:", suma)
