#Ejercicios De Deber3
#Estructuras de condición
#Ejercicio 1
def calcularRectangulo(base, altura):
    perimetro = 2 * (base + altura)
    area = base * altura
    return perimetro, area
def calcularCirculo(radio):
    perimetro = 2 * 3.14 * radio
    area = 3.14 * radio ** 2
    return perimetro, area
baseRectangulo = float(input())
alturaRectangulo = float(input())
perimetroRectangulo, areaRectangulo = calcularRectangulo(baseRectangulo, alturaRectangulo)
print(perimetroRectangulo, areaRectangulo)
radioCirculo = float(input())
perimetroCirculo, areaCirculo = calcularCirculo(radioCirculo)
print(perimetroCirculo, areaCirculo)

#Ejercicio 2
fahrenheit = float(input("Hola, Indique temperatura en grados Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print("La temperatura en grados Celsius es:", celsius)

#Ejercicio 3
minutos = int(input("Indique minutos: "))
horas = minutos // 60
minutos_restantes = minutos % 60
print(str(minutos) + " minutos son " + str(horas) + " horas y " + str(minutos_restantes) + " minutos.")

#Ejercicio 4
sb = float(input("Indique el sueldo base del vendedor: "))
v1 = float(input("Indique la primera venta del mes: "))
v2 = float(input("Indique la segunda venta del mes: "))
v3 = float(input("Indique la tercera venta del mes: "))
comision = (v1 + v2 + v3) * 0.10
sueldoT = sb + comision
print("La comisión por las ventas es:", comision)
print("El sueldo total en el mes es:", sueldoT)

#Ejercicio 5
p1 = float(input("Introduce la calificación del primer parcial: "))
p2 = float(input("Introduce la calificación del segundo parcial: "))
p3 = float(input("Introduce la calificación del tercer parcial: "))
ef = float(input("Introduce la calificación del examen final: "))
tf = float(input("Introduce la calificación del trabajo final: "))
pp = (p1 + p2 + p3) / 3
cf = 0.55 * pp + 0.30 * ef + 0.15 * tf
print("La calificación final en Algoritmos es:", cf)

#Ejercicio 6
x1 = float(input("Introduce la coordenada x del punto1: "))
y1 = float(input("Introduce la coordenada y del punto1: "))
x2 = float(input("Introduce la coordenada x del punto2: "))
y2 = float(input("Introduce la coordenada y del punto2: "))
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("La distancia entre los dos puntos es:", distancia)

#Ejercicio 7
n = int(input("Introduce un número de dos cifras: "))
u = n % 10
d = n // 10
inv = u * 10 + d
print("El número invertido es:", inv)

#Ejercicio 8
d = float(input("Introduce la distancia entre los vehículos en kilómetros: "))
v1 = float(input("Introduce la velocidad del vehículo más lento en km/h: "))
v2 = float(input("Introduce la velocidad del vehículo más rápido en km/h: "))
th = d / (v2 - v1)
tm = round(th * 60, 2)   #Round sirve para redondear el tiempo :D
print("El vehículo más rápido alcanzará al más lento en", tm, "minutos.")

#Ejercicio 9
n = input("Introduce el nombre: ")
a1 = input("Introduce el primer apellido: ")
a2 = input("Introduce el segundo apellido: ")
inicialn = n[0]
iniciala1 = a1[0]       #Corchetes sirven para tomar el primer valor de algun caracter en este caso la inicial
iniciala2 = a2[0]
print("Las iniciales son:", inicialn, iniciala1, iniciala2)

#Ejercicio 10
me2 = int(input("Cantidad de monedas de 2 euros: "))
me1 = int(input("Cantidad de monedas de 1 euro: "))
m50 = int(input("Cantidad de monedas de 50 céntimos: "))
m20 = int(input("Cantidad de monedas de 20 céntimos: "))
m10 = int(input("Cantidad de monedas de 10 céntimos: "))
te = me2 * 2 + me1 * 1 + m50 * 0.5 + m20 * 0.2 + m10 * 0.1
tc = int((te % 1) * 100)
print("Tienes", int(te), "euros y", tc, "céntimos.")

#Estructuras de condición
#Ejercicio 1
cadena = input("Introduce una cadena: ")
if len(cadena) == 1 and cadena.isalpha() and cadena.isupper():
    print("La cadena es una letra mayúscula.")
else:
    print("La cadena no es una letra mayúscula.")

#Ejercicio 2
nota = float(input("Introduce la nota: "))
edad = int(input("Introduce la edad: "))
sexo = input("Introduce el sexo (F/M): ")
if nota >= 5 and edad >= 18:
    if sexo.upper() == 'F':
        print("ACEPTADA")
    elif sexo.upper() == 'M':
        print("POSIBLE")
    else:
        print("NO ACEPTADA")
else:
    print("NO ACEPTADA")

#Ejercicio 3
n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))
n3 = float(input("Introduce el tercer número: "))
mayor = max(n1, n2, n3)
menor = min(n1, n2, n3)
medio = (n1 + n2 + n3) - mayor - menor
print("Números ordenados de mayor a menor:", mayor, medio, menor)

#Ejercicio 4
A = float(input("Introduce la longitud del lado A: "))
B = float(input("Introduce la longitud del lado B: "))
C = float(input("Introduce la longitud del lado C: "))
if A**2 + B**2 == C**2 or A**2 + C**2 == B**2 or B**2 + C**2 == A**2:
    tipo = "triángulo rectángulo"
elif A == B == C:
    tipo = "triángulo equilátero"
elif A == B or A == C or B == C:
    tipo = "triángulo isósceles"
else:
    tipo = "triángulo escaleno"
print("El triángulo es de tipo", tipo)

#Ejercicio 5
tu = input("Introduce el tipo de uva (A/B): ")
tu1 = int(input("Introduce el tamaño de uva (1/2): "))
pi = float(input("Introduce el precio inicial por kilo de uva: "))
ke = float(input("Introduce la cantidad de kilos de uva entregados: "))
if tu.upper() == 'A':
    if tu1 == 1:
        ga = pi + 0.20
    elif tu1 == 2:
        ga = pi + 0.30
elif tu.upper() == 'B':
    if tu1 == 1:
        ga = pi - 0.30
    elif tu1 == 2:
        ga = pi - 0.50
else:
    ga = 0
mt = ga * ke
print("La ganancia obtenida es:", mt)

#Ejercicio 6
ca = int(input("Introduce la cantidad de alumnos: "))
if ca >= 100:
    cpa = 65
    pac = ca * cpa
elif 50 <= ca <= 99:
    cpa = 70
    pac = ca * cpa
elif 30 <= ca <= 49:
    cpa = 95
    pac = ca * cpa
else:
    cpa = 0
    pac = 4000
print("El costo por cada alumno es de", cpa, "euros.")
print("El pago total a la compañía de autobuses es de", pac, "euros.")

#Ejercicio 7
zona = int(input("Introduce la zona de destino (1-5): "))
peso = float(input("Introduce el peso del paquete (en kg): "))
costoGramo = 0.00
if zona == 1:
    costoGramo = 24.00
elif zona == 2:
    costoGramo = 20.00
elif zona == 3:
    costoGramo = 21.00
elif zona == 4:
    costoGramo = 10.00
elif zona == 5:
    costoGramo = 18.00
costoTotal = 0.00
if peso <= 5:
    costoTotal = peso * costoGramo
    mensaje = "El costo por la entrega del paquete es de " + str(costoTotal) + " euros."
else:
    mensaje = "El paquete no puede ser transportado debido a su peso."
print(mensaje)

#Ejercicio 8
nd = int(input("Introduce el número del día de la semana (1-7): "))
if nd == 1:
    d = "Lunes"
elif nd == 2:
    d = "Martes"
elif nd == 3:
    d = "Miércoles"
elif nd == 4:
    d = "Jueves"
elif nd == 5:
    d = "Viernes"
elif nd == 6:
    d = "Sábado"
elif nd == 7:
    d = "Domingo"
else:
    d = "Error: Ingresa un número válido del 1 al 7."
print("Corresponde al día:", d)

#Ejercicio 9
tipo_motor = int(input("Introduce el tipo de motor (1, 2, 3, 4): "))
if tipo_motor == 0:
    print("No hay establecido un valor definido para el tipo de bomba")
elif tipo_motor == 1:
    print("La bomba es una bomba de agua")
elif tipo_motor == 2:
    print("La bomba es una bomba de gasolina")
elif tipo_motor == 3:
    print("La bomba es una bomba de hormigón")
elif tipo_motor == 4:
    print("La bomba es una bomba de pasta alimenticia")
else:
    print("No existe un valor válido para tipo de bomba")

#Ejercicio 10
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
nota_ingles = float(input("Ingrese la nota de Inglés: "))
mensaje = ""
if 9 <= nota_ingles <= 10:
    mensaje = "Felicitaciones " + nombre_estudiante + ", su nota es " + str(nota_ingles) + " equivalente a excelente"
elif 7 <= nota_ingles <= 8:
    mensaje = "Siga adelante " + nombre_estudiante + ", su nota es " + str(nota_ingles) + " equivalente a muy buena"
elif 5 <= nota_ingles <= 6:
    mensaje = "Debe esforzarse más " + nombre_estudiante + ", su nota es " + str(nota_ingles) + " equivalente a buena"
elif 0 <= nota_ingles <= 4:
    mensaje = "Usted puede reprobar ya que su nota es " + str(nota_ingles) + " equivalente a regular"
else:
    mensaje = "Ingrese una nota válida en el rango de 0 a 10"
print(mensaje)