#Nombre de los integrantes: Hector Tobar y Maria Rivera

#Diccionario para las piezas con símbolos
simbolos = {
    "TorreB": "R", "CaballoB": "N", "AlfilB": "B", "ReinaB": "Q", "ReyB": "K", "PeonB": "P",
    "TorreN": "r", "CaballoN": "n", "AlfilN": "b", "ReinaN": "q", "ReyN": "k", "PeonN": "p"
}

#Iniciar tablero
tablero = {}

#Iniciar filas y columnas
columnas = "abcdefgh"

#Piezas blancas (fila 1 y 2)
piezas_blancas = ["TorreB", "CaballoB", "AlfilB", "ReinaB", "ReyB", "AlfilB", "CaballoB", "TorreB"]
for i in range(8):
    tablero[columnas[i] + "1"] = piezas_blancas[i]
    tablero[columnas[i] + "2"] = "PeonB"

#Piezas negras (fila 7 y 8)
piezas_negras = ["TorreN", "CaballoN", "AlfilN", "ReinaN", "ReyN", "AlfilN", "CaballoN", "TorreN"]
for i in range(8):
    tablero[columnas[i] + "8"] = piezas_negras[i]
    tablero[columnas[i] + "7"] = "PeonN"

#Lista para piezas capturadas
capturadas = []

#Bucle del juego
while True:
    # Mostrar tablero
    print("a b c d e f g h")
    for fila in range(8, 0, -1):
        linea = str(fila) + " "
        for columna in columnas:
            casilla = columna + str(fila)
            if casilla in tablero:
                pieza = tablero[casilla]
                print(simbolos[pieza], end=" ")
            else:
                print(".", end=" ")
        print()
    print()

    #Mostrar piezas capturadas
    print("Piezas capturadas: ", end="")
    for pieza in capturadas:
        print(simbolos[pieza], end=" ")
    print("\n")

    #Pedir al usuario la casilla de origen
    origen = input("Ingresa la casilla de origen (ej: e2) o 'salir': ").lower()
    if origen == "salir":
        print("Juego terminado.")
        break

    if origen not in tablero:
        print("❌ No hay pieza en esa casilla.\n")
        continue

    #Pedir la casilla de destino
    destino = input("Ingresa la casilla de destino (ej: e4): ").lower()
    if destino not in [c + str(f) for c in columnas for f in range(1, 9)]:
        print("❌ Casilla destino inválida.\n")
        continue

    pieza_origen = tablero[origen]

    #Verificar si hay pieza en destino
    if destino in tablero:
        pieza_destino = tablero[destino]
        # Si es de distinto color se captura
        if pieza_origen[-1] != pieza_destino[-1]:
            capturadas.append(pieza_destino)
            print("✅ Capturó a", pieza_destino, "en", destino.upper(), "\n")
        else:
            print("❌ No puedes capturar tu propia pieza.\n")
            continue

    #Mover la pieza
    tablero[destino] = pieza_origen
    del tablero[origen]