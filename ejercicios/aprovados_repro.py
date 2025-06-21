#PARTE 1: Solicitud de cantidad de estudiantes
while True:
    try: 
        cantidad = int(input("¿Cuántos estudiantes deseas registrar? "))
        if cantidad < 1:
          print("Debe de ser al menos un estudiante.")
    except ValueError:     
           print("Por favor, ingresa un número entero válido.")

#PARTE 2: Ingrese asigantura
asignatura = str(input("Ingrese su asignatura: "))
