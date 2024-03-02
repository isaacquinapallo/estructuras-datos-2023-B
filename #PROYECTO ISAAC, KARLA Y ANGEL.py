#PROYECTO ISAAC, KARLA Y ANGEL
#LINK VIDEO: https://youtu.be/TPMuXvT-H_k?si=l06xCOFMwh5Iy3XM

def iniciar_sesion():
    intentos = 0
    while intentos < 3:
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        if usuario == "docente@esfot.edu.ec" and contrasena == "Docente2023*":
            return True
        else:
            print("Credenciales incorrectas. Inténtelo de nuevo.")
            intentos += 1
    print("Número máximo de intentos alcanzado. Saliendo del sistema...")
    return False

def registrar_calificaciones():
    institucion = input("Ingrese el nombre de la institución (Colegio o Universidad): ")
    materia = input("Ingrese la materia: ")
    nombre_docente = input("Ingrese su nombre y apellido (docente): ")
    num_estudiantes = int(input("Ingrese el número de estudiantes: "))

    estudiantes = []
    for i in range(1, num_estudiantes + 1):
        nombre = input(f"Ingrese el nombre del estudiante {i}: ")
        apellido = input(f"Ingrese el apellido del estudiante {i}: ")
        correo = input(f"Ingrese el correo electrónico del estudiante {i}: ")
        nota1 = float(input(f"Ingrese la nota 1 del estudiante {i}: "))
        nota2 = float(input(f"Ingrese la nota 2 del estudiante {i}: "))
        total = nota1 + nota2
        estudiantes.append((nombre, apellido, correo, nota1, nota2, total))

    print("Guardando información en archivo de calificaciones.txt")

    with open("calificaciones.txt", "w") as file:
        file.write(f"COLEGIO O UNIVERSIDAD: {institucion}\n")
        file.write("REPORTE DE CALIFICACIONES\n")
        file.write("\n")
        file.write(f"Año lectivo o Semestre: 2024-2025\n")
        file.write(f"Materia: {materia}\n")
        file.write("\n")
        file.write("N.º\tEstudiante\tApellido\tCorreo\tNota 1\tNota 2\tTotal\n")
        for i, estudiante in enumerate(estudiantes, start=1):
            file.write(f"{i}\t{estudiante[0]}\t\t{estudiante[1]}\t{estudiante[2]}\t{estudiante[3]}\t{estudiante[4]}\t{estudiante[5]}\n")
        file.write("...........................................................\n")
        file.write("\n")
        file.write("RESUMEN\n")

        # Cálculo del promedio
        promedio = sum(estudiante[5] for estudiante in estudiantes) / num_estudiantes
        file.write(f"Promedio del curso: {promedio}\n")

        # Conteo de aprobados, suspendidos y reprobados
        aprobados = sum(1 for estudiante in estudiantes if estudiante[5] >= 14)
        suspendidos = sum(1 for estudiante in estudiantes if 9 <= estudiante[5] < 14)
        reprobados = sum(1 for estudiante in estudiantes if estudiante[5] < 9)

        file.write(f"Aprobados (14 - 20): {aprobados}\n")
        file.write(f"Suspenso (09 - 13): {suspendidos}\n")
        file.write(f"Reprobados (01 - 08): {reprobados}\n")
        file.write("\n")
        file.write(f"DOCENTE: {nombre_docente}\n")
    return nombre_docente, estudiantes

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][1] < R[j][1]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][1]
    left = [x for x in arr if x[1] < pivot]
    middle = [x for x in arr if x[1] == pivot]
    right = [x for x in arr if x[1] > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def ordenar_calificaciones(nombre_docente, calificaciones):
    algoritmo = input("Seleccione el algoritmo de ordenamiento (Burbuja, Inserción, Selección, MergeSort, QuickSort): ").lower()

    if algoritmo == 'burbuja':
        for i in range(len(calificaciones) - 1):
            for j in range(len(calificaciones) - 1 - i):
                if calificaciones[j][5] > calificaciones[j+1][5]:
                    calificaciones[j], calificaciones[j+1] = calificaciones[j+1], calificaciones[j]
    elif algoritmo == 'insercion':
        for i in range(1, len(calificaciones)):
            key = calificaciones[i]
            j = i - 1
            while j >= 0 and calificaciones[j][5] > key[5]:
                calificaciones[j + 1] = calificaciones[j]
                j -= 1
            calificaciones[j + 1] = key
    elif algoritmo == 'seleccion':
        for i in range(len(calificaciones)):
            min_idx = i
            for j in range(i+1, len(calificaciones)):
                if calificaciones[j][5] < calificaciones[min_idx][5]:
                    min_idx = j
            calificaciones[i], calificaciones[min_idx] = calificaciones[min_idx], calificaciones[i]
    elif 'mergesort' in algoritmo:
        merge_sort(calificaciones)
    elif 'quicksort' in algoritmo:
        calificaciones = quick_sort(calificaciones)
    else:
        print("Algoritmo de ordenamiento no válido.")
        return

    with open("ordenamiento.txt", "w") as file:
        file.write(f"| Algoritmo de ordenamiento seleccionado: {algoritmo}\n")
        for estudiante in calificaciones:
            file.write(f"{estudiante[0]}: {estudiante[5]}\n")

    print("-" * 50)
    with open("calificaciones.txt", "r") as file:
        institucion = file.readline().split(": ")[1].strip()
    print(f"| {'Colegio o Universidad:':<30} {institucion}")
    print(f"| {'El algoritmo que escogió:':<30} {algoritmo}")
    print("-" * 50)
    print("|      NOMBRE      | NOTA TOTAL |")
    print("-" * 50)
    for estudiante in calificaciones:
        print(f"| {estudiante[0]:<17} | {estudiante[5]:^11.2f} |")
    print("-" * 50)

def buscar_calificaciones():
    with open("calificaciones.txt", "r") as file:
        calificaciones = file.readlines()[7:-4]

    busqueda = input("Ingrese el nombre del estudiante a buscar: ").strip().lower()

    encontrados = []

    for calificacion in calificaciones:
        if busqueda in calificacion.lower():
            encontrados.append(calificacion.strip())

    if encontrados:
        with open("busqueda.txt", "w") as file:
            for i in range(len(encontrados)):
                file.write(encontrados[i] + "\n")
            print("Se ha generado el archivo 'busqueda.txt' con los resultados de la búsqueda.")
    else:
        print("No se encontraron resultados para la búsqueda especificada.")

def main():
    print("Bienvenido al sistema de gestión de calificaciones.")
    if iniciar_sesion():
        print("Sesión iniciada con éxito.")
        opcion = ""
        while opcion != "4":
            print("\nMenú:")
            print("1. Registrar calificaciones")
            print("2. Ordenar calificaciones")
            print("3. Buscar calificaciones")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre_docente, calificaciones = registrar_calificaciones()
            elif opcion == "2":
                if 'nombre_docente' in locals() and 'calificaciones' in locals():
                    ordenar_calificaciones(nombre_docente, calificaciones)
                else:
                    print("Primero registre las calificaciones.")
            elif opcion == "3":
                buscar_calificaciones()
            elif opcion == "4":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida.")
    else:
        print("Sesión no iniciada. Saliendo del sistema...")

if _name_ == "_main_":
    main()
