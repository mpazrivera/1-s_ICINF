# Sueldo base en Chile 2025
sueldo_base = 529000

#Diccionario con ventas diarias
ventas_vendedores = {
    "Carlos":   [200000, 180000, 250000, 190000, 210000],
    "Marcela":  [300000, 350000, 320000, 280000, 310000],
    "Tomás":    [100000, 150000, 120000, 110000, 130000]
}

# Reporte de sueldos
print("REPORTE SEMANAL DE SUELDOS ")

for vendedor, ventas in ventas_vendedores.items():
    total_ventas = sum(ventas)

    #Calcular bono según ventas
    if total_ventas > 1500000:
        bono = 0.20 * sueldo_base
    elif total_ventas > 1000000:
        bono = 0.10 * sueldo_base
    elif total_ventas > 500000:
        bono = 0.05 * sueldo_base
    else:
        bono = 0

    #Calcular promedio de ventas
    promedio = total_ventas / len(ventas)

    #Calcular sueldo total
    sueldo_total = sueldo_base + bono

    # Imprimir reporte individual
    print(f"Vendedor: {vendedor}")
    print(f"  Ventas diarias: {ventas}")
    print(f"  Total semanal de ventas: ${total_ventas:,}")
    print(f"  Promedio diario: ${promedio:,.0f}")
    print(f"  Bono asignado: ${bono:,.0f}")
    print(f"  Sueldo total a pagar: ${sueldo_total:,.0f}")
    