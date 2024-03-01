#PROYECTO ISAAC, KARLA Y ANGEL
#LINK VIDEO: https://youtu.be/TPMuXvT-H_k?si=l06xCOFMwh5Iy3XM

# Contraceña e inicio del Docente
def iniciar_sesion():
    intentos = 0
    while intentos < 3:
        usuario = input("Usuario: ")
        contrasena = input("Contrasena: ")
        if usuario == "docente@esfot.edu.ec" and contrasena == "Docente2023*":
            return True
        else:
            print("Credenciales incorrectas. Inténtelo de nuevo.")
            intentos += 1
    print("Numero maximo de intentos alcanzado. Saliendo del sistema...")
    return False

# Función para registrar calificaciones
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
    print("Guardando informacion en archivo de calificaciones.txt")

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

# Función de Merge Sort
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

# Función de Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][1]
    left = [x for x in arr if x[1] < pivot]
    middle = [x for x in arr if x[1] == pivot]
    right = [x for x in arr if x[1] > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Función para ordenar calificaciones
def ordenar_calificaciones(nombre_docente, calificaciones):
    algoritmo = input("Seleccione el algoritmo de ordenamiento (Burbuja, Inserción, Selección, MergeSort, QuickSort): ").lower()

    if algoritmo == 'burbuja':
        for i in range(len(calificaciones) - 1):
            for j in range(len(calificaciones) - 1 - i):
                if calificaciones[j][1] > calificaciones[j+1][1]:
                    calificaciones[j], calificaciones[j+1] = calificaciones[j+1], calificaciones[j]
    elif algoritmo == 'insercion':
        for i in range(1, len(calificaciones)):
            key = calificaciones[i]
            j = i - 1
            while j >= 0 and calificaciones[j][1] > key[1]:
                calificaciones[j + 1] = calificaciones[j]
                j -= 1
            calificaciones[j + 1] = key
    elif algoritmo == 'seleccion':
        for i in range(len(calificaciones)):
            min_idx = i
            for j in range(i+1, len(calificaciones)):
                if calificaciones[j][1] < calificaciones[min_idx][1]:
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
        for estudiante, calificacion in calificaciones:
            file.write(f"{estudiante}: {calificacion}\n")

    print("-" * 50)
    with open("calificaciones.txt", "r") as file:
        institucion = file.readline().split(": ")[1].strip()
    print(f"| {'Colegio o Universidad:':<30} {institucion}")
    print(f"| {'El algoritmo que escogiste fue:':<30} {algoritmo}            |")

    print("|", "-" * 50, "|")
    print("| Notas ordenadas:","                                  |")
    for estudiante, calificacion in calificaciones:
        print("|", "-"*50, "|")
        print(f"| {estudiante} | : |{calificacion} |")
        print("|", "-"*50, "|")

    print("|", "-" * 50, "|")
    print(f"|{'docente':<15} |{nombre_docente}|")
    print("|", "-" * 50, "|")

# Función para buscar una calificación
def buscar_calificacion():
    with open("buscar.txt", "r") as file:
         # Leer todas las líneas del archivo y saltar las dos primeras líneas
        lineas = file.readlines()[8:]
    # Crear una lista de tuplas donde cada tupla contiene el nombre del estudiante y su calificación
    calificaciones = []
    for linea in lineas:
        # Dividir cada línea en dos partes usando ": " como separador
        partes = linea.split(": ")
        # El primer elemento es el nombre del estudiante y el segundo es la calificación
        nombre_estudiante = partes[1]
        calificacion = float(partes[-1].strip())
        # Agregar el nombre del estudiante y su calificación como una tupla a la lista de calificaciones
        calificaciones.append((nombre_estudiante, calificacion))
    calificacion_buscada = float(input("Ingrese la calificación que desea buscar: "))
    algoritmo_busqueda = input("Seleccione el algoritmo de búsqueda (Lineal, Binaria, Interpolación, etc.): ").lower()

    if algoritmo_busqueda == 'lineal':
        encontrado = False
        for estudiante, calificacion in calificaciones:
            if calificacion == calificacion_buscada:
                print("La calificación",calificacion_buscada," fue encontrada para el estudiante", estudiante)
                encontrado = True
                break
        if not encontrado:
            print("La calificación",calificacion_buscada," no fue encontrada.")
    else:
        print("Algoritmo de búsqueda no válido.")

    with open("busqueda.txt", "w") as file:
        file.write("COLEGIO o UNIVERSIDAD ___\n")
        file.write("\n")
        file.write("REPORTE DE CALIFICACIONES\n")
        file.write("\n")
        file.write("Búsqueda de Calificaciones\n")
        file.write("\n")
        file.write(f"ALGORITMO: {algoritmo_busqueda.capitalize()}\n")
        file.write("\n")
        file.write(f"La calificación a buscar fue de: {calificacion_buscada}\n")
        file.write("\n")
        if encontrado:
            file.write(f"Corresponde al estudiante: {estudiante}, {calificacion}\n")
        file.write("\n")
        file.write("_" * 100)
        file.write("\n")
        file.write("Docente\n")
        file.write("\n")
        file.write("____\n")
        file.write("____\n")

    print("\nArchivo 'busqueda.txt' creado satisfactoriamente.")

# Función principal del sistema
def sistema_gestion_calificaciones():
    # Crear archivos de texto
    with open("buscar.txt", "w"):
        pass
    with open("ordenamiento.txt", "w"):
        pass

    # Solicitar inicio de sesión
    if not iniciar_sesion():
        return

    # Si las credenciales son correctas, mostrar el menú
    while True:
        print("\n ----------------MENU-----------------")
        print("1. Ingresar datos, notas")
        print("2. Ordenar notas")
        print("3. Buscar nota")
        print("4. Salir\n")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_docente, calificaciones = registrar_calificaciones()
        elif opcion == "2":
            ordenar_calificaciones(nombre_docente, calificaciones)
        elif opcion == "3":
            buscar_calificacion()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Ejecutar el sistema
sistema_gestion_calificaciones()
buscar_calificacion()