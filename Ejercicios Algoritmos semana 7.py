
#Ejercicio1
#Realice un programa, para calcular la suma de los N primeros números pares. Es decir, si insertamos un 8, nos haga la suma de 2+4+6+8. Recuerda utilizar la sentencia de repetición. 
numero1= int(input("Ingresa un número para calcular la suma de los primeros números pares: "))
suma1= 0
for i in range(2, numero1+1, 2):
    suma1 += i
print("La suma de los números pares hasta el ", numero1, " es: ", suma1)

#Ejercicio2
correo=str(input("Ingrese su correo electronico: "))
talleresmecanicos=3
contadorfugas=0
while True:
    for taller in range(1, talleresmecanicos + 1):
        lecturasensor = int(input("Escriba la lectura del sensor para taller (1 para fuga, 0 para no fuga): "))
        if lecturasensor == 1:
            contadorfugas += 1
            print("Fuga de gas detectada en taller ", taller)
    if talleresmecanicos > 1 and contadorfugas > 0:
        print("Se ha detectado fuga de gas en al menos un taller. EMERGENCIA!!! ")
        print("Se ha enviado el resultado de la lectura de los sensores a ", correo)
        break
    else:
        print("No se ha detectado fuga de gas en ningún taller.")
        break 

#Ejercicio3
valor1= int(input("Ingrese el valor menor: "))
valor2= int(input("Ingrese el valor mayor: "))

if valor1 > valor2:
    print("Error: el valor menor debe ser menor o igual al valor mayor.")
else:
    suma2 = 0
    for i in range(valor1, valor2+1):
        suma2 += i
    print("La sumatoria de los números en el rango ", valor1," ", valor2, " es: ", suma2)

#Ejercicio4
calificacion_total = 0
for i in range(4):
    while True:
        calificacion = float(input(f"Ingrese la calificacion {i + 1}: "))
        if 0 <= calificacion <= 20:
            break
        else:
            print("Calificación incorrecta. Debe estar entre 0 y 20. Intente nuevamente.")
    calificacion_total += calificacion
promedio = calificacion_total / 4
if promedio >= 14:
    estado = "Aprobado"
elif 9 <= promedio <= 13:
    estado = "Supletorio"
else:
    estado = "Rechazado"
print("El promedio es:", promedio)
print("En conclusión usted a sido:", estado)

#Ejercicio5
numero5 = int(input("Ingrese un número entero positivo: "))
if 10 <= numero5 <= 100:
    print("El número pertenece al intervalo.")
else:
    print("El número no pertenece al intervalo.")

#Ejercicio6
nombrecliente = str(input("Ingrese su nombre: "))
tipotarjeta = int(input("Ingrese el tipo de tarjeta (1, 2, 3 o 4): "))
creditoanterior = float(input("Ingrese su crédito actual: "))
aumentoporcentaje = 0
if tipotarjeta == 1:
    aumentoporcentaje = 0.25
elif tipotarjeta == 2:
    aumentoporcentaje = 0.35
elif tipotarjeta == 3:
    aumentoporcentaje = 0.40
elif tipotarjeta == 4:
    aumentoporcentaje = 0.50
else:
    print("Tipo de tarjeta no válido. Por favor, ingrese el tipo de targeta del 1 al 4.")
creditonuevo = creditoanterior * (1 + aumentoporcentaje)
print("DATOS DEL CLIENTE")
print("Nombre del cliente: ", nombrecliente)
print("Tipo de tarjeta: ", tipotarjeta)
print("Crédito anterior: $", creditoanterior)
print("Crédito nuevo: $", creditonuevo)

#Ejercicio7
preciou = float(input("Ingrese el precio unitario de la prenda: "))
cantidad = int(input("Ingrese la cantidad de prendas adquiridas: "))
preciototal = preciou * cantidad
if cantidad > 20:
    descuento = 0.10
elif 10 < cantidad <= 20:
    descuento = 0.05
else:
    descuento = 0
preciocond = preciototal - (preciototal * descuento)
print("INFORMACION DE LA COMPRA")
print("Cantidad de prendas adquiridas:", cantidad)
print("Precio unitario: $", preciou)
print("Precio total antes del descuento: $", preciou)
print("Descuento aplicado: ", int(descuento*100), "%")
print("Nuevo precio total con descuento: $", preciocond)

#Ejercicio8
sumatotal = 0
sumamora = 0
nguaguas= int(input("Ingrese cuantas guaguas de pan necesita: "))
contador= 0
while contador < nguaguas:
    precio = float(input("Ingrese el precio de la guagua: "))
    sumatotal+=precio
    sabor = str(input("Ingrese si la guagua sea de mora o no): "))
    if sabor == "mora":
        sumamora += precio
    contador += 1
print("Resumen de la compra")
print("Número total de guaguas: ", nguaguas)
print("Suma total de guaguas: $", sumatotal)
print("Suma total de guaguas de mora: $", sumamora)

#Ejercicio9
sumatotal= 0
nprofesores= 0
nempleados = int(input("Ingrese la cantidad de empleados: "))
contador = 0
while contador < nempleados:
    horast = int(input("Ingrese las horas trabajadas del empleado: "))
    esprofesor = input("¿Usted es profesor? (Sí/No): ")
    sueldobase = 10
    if (esprofesor=="si" or esprofesor=="Sí"):
        sueldobase = 15
        nprofesores += 1
    sueldo = horast * sueldobase
    sumatotal += sueldo
    print("Empleado ", (contador+1), ": Horas trabajadas: ",horast,  " Sueldo: $",sueldo)
    contador += 1
print("Resumen de la nómina")
print("Número total de empleados:", nempleados)
print("Número total de profesores:", nprofesores)
print("Suma total de sueldos: $", sumatotal)

#Ejercio10
while True:
    print("Menú de Actividades:")
    print("1. Ver Película")
    print("2. Ver Serie")
    print("3. Jugar Videojuegos")
    print("4. Escuchar Música")
    print("5. Hacer Ejercicio")
    print("6. Estudiar")
    print("7. Navegar por Internet")
    print("8. Videoconferencia")
    print("9. Otra Actividad")
    print("0. Salir")
    opcion1 = int(input("Ingrese el número de la actividad deseada (0-9): "))
    if (0<=opcion1<=9):
        if (opcion1==0):
            print("¡Hasta luego!")
            break
        else:
            print("Sintonizando en el Smart TV la actividad: Actividad ", opcion1)
    else:
        print("Ingrese un número válido entre 0 y 9.")

#Ejercicio11
tahorrado =0
while True:
    print("Menú de Opciones:")
    print("1. Agregar dinero al ahorro del mes")
    print("2. Ver total ahorrado")
    print("0. Salir")
    opcion = input("Ingrese la opcion deseada (0-2): ")
    if opcion == "1":
        cantidad = float(input("Ingrese la cantidad de dinero a agregar al ahorro del mes: "))
        tahorrado += cantidad
        print("Se agregó $",cantidad, "al ahorro del mes.")
    elif opcion == "2":
        print("El total ahorrado hasta el momento es: $",tahorrado)
    elif opcion == "0":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Error: Ingrese un número válido entre 0 y 2.")
