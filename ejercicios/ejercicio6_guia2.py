# Simulación de un reloj digital de 00:00:00 a 23:59:59

for hora in range(24):           # Horas: 0 a 23
    for minuto in range(60):     # Minutos: 0 a 59
        for segundo in range(60):  # Segundos: 0 a 59
            print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")
