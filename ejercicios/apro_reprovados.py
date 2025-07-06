# 1. Cantidad de estudiantes
while True:
    try:
        cantidad = int(input("¿Cuántos estudiantes desea registrar?: "))
        if cantidad > 0:
            break
        else:
            print("Debe ingresar un número mayor que 0.")
    except:
        print("Entrada inválida. Intente de nuevo.")

# 2. Nombre de la asignatura
asignatura = input("Ingrese el nombre de la asignatura: ")

# Lista para guardar los estudiantes
estudiantes = []

# 3. Ingreso de datos
for i in range(cantidad):
    print("\nEstudiante", i + 1)
    nombre = input("Nombre: ")
    notas = []

    j = 1
    while j <= 3:
        try:
            nota = float(input("Nota " + str(j) + ": "))
            if 0.0 <= nota <= 7.0:
                notas.append(nota)
                j += 1
            else:
                print("La nota debe estar entre 0.0 y 7.0")
        except:
            print("Entrada inválida. Intente de nuevo.")

    promedio = (notas[0] + notas[1] + notas[2]) / 3

    estudiante = {
        "nombre": nombre,
        "notas": notas,
        "promedio": promedio
    }

    estudiantes.append(estudiante)

# 4. Buscar mayor y menor promedio
mayor = estudiantes[0]["promedio"]
menor = estudiantes[0]["promedio"]
mejor = estudiantes[0]["nombre"]
peor = estudiantes[0]["nombre"]

for e in estudiantes:
    if e["promedio"] > mayor:
        mayor = e["promedio"]
        mejor = e["nombre"]
    if e["promedio"] < menor:
        menor = e["promedio"]
        peor = e["nombre"]

# 5. Mostrar resultados
print("\n--- RESULTADOS ---")
for e in estudiantes:
    print("Nombre:", e["nombre"])
    print("  Promedio:", round(e["promedio"], 2))

    if e["promedio"] < 4.0:
        rendimiento = "Bajo"
    elif e["promedio"] <= 6.0:
        rendimiento = "Regular"
    else:
        rendimiento = "Alto"

    beca = ""
    if e["promedio"] > 5.0:
        beca = "(Becado)"

    print("  Rendimiento:", rendimiento, beca)

# 6. Estudiante con mejor y peor promedio
print("\nMejor promedio:", mejor, "con", round(mayor, 2))
print("Peor promedio:", peor, "con", round(menor, 2))

# 7. Reprobados
print("\n--- Reprobados ---")
for e in estudiantes:
    if e["promedio"] < 4.0:
        print(e["nombre"], "- Promedio:", round(e["promedio"], 2))
