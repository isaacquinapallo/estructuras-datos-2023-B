#Ejercicio 1 Parte1
#Funcion
def sumadigito(valor1):
    suma=0
    while valor1!=0:
        digito = valor1%10        #Valor 13 entonces seria 3=digito     #1/10 seria a 1=digito ya que de residuo es 1
        suma=suma+digito         #suma=3                               #suma=3+1=4
        valor1=valor1//10        #Parte entera de Seria 1=numero       #parte entera de 1/10 es 0
        #Vuelve a repetir ya que numero es diferente de 0              #No se repite ya que numero= 0  por tanto se finaliza
    return suma
#Programa
sumadigitototal=0
print("Si quiere salir escriba 0")
valor=int(input("Ingrese un valor para sumar el valor de sus digitos: "))
while valor!=0:
    sumadigitototal+=sumadigito(valor)
    print("La suma de sus digitos es: ", sumadigitototal)
    valor=int(input("Si quiere salir escriba 0, caso contrario escriba otro valor: "))

#Ejercicio 2 Parte 1
#Suma de coordenadas dado que el usuario ingresa.
def sumacoordenadas(coordenada1, coordenada2):
    X= coordenada1+12
    Y= coordenada2+15
    sumaXY=X+Y
    return sumaXY
#Programa
coordenadax=int(input("Ingrese la coordenada x: "))
coordenaday=int(input("Ingrese la coordenada y: "))
print("La suma de coordenadas es: ", sumacoordenadas(coordenadax, coordenaday))

#Ejercicio 3 Parte 1
def sumadigito(valor1):
    suma=0
    while valor1!=0:
        digito = valor1%10        #Valor 13 entonces seria 3=digito     #1/10 seria a 1=digito ya que de residuo es 1
        suma=suma+digito         #suma=3                               #suma=3+1=4
        valor1=valor1//10        #Parte entera de Seria 1=numero       #parte entera de 1/10 es 0
        #Vuelve a repetir ya que numero es diferente de 0              #No se repite ya que numero= 0  por tanto se finaliza
    return suma
def sumatotal(valor2):
    suma2=0
    suma2 +=valor2
    return suma2
#Programa
sumadigitototal=0
sumatotal=0
print("Si quiere salir escriba 0")
valor=int(input("Ingrese un valor para sumar el valor de sus digitos y su suma: "))
while valor!=0:
    sumadigitototal+=sumadigito(valor)
    sumatotal+=valor
    print("La suma de sus digitos es: ", sumadigitototal," la suma de sus valores son: ",sumatotal)
    valor=int(input("Si quiere salir escriba 0, caso contrario escriba otro valor: "))

#Ejercicio 4 Parte 1
def paroimpar(numero1):
    if numero1%2==0:
        return " es un numero par"
    else:
        return " es un numero impar"
#Programa
numeroanalizar=int(input("Ingrese un numero para verificar si es par o impar: "))
print("Determinamos que ", numeroanalizar, paroimpar(numeroanalizar))

#Ejercicio 5 Parte 1
def cnumero(numero2, conjuntoanalizar):
    contador=0
    conjunto=str(conjuntoanalizar)
    for x in conjunto:
        if x ==str(numero2):
            contador+=1
    return contador
#Programa
conjunto=int(input("Ingrese el conjunto de numeros de los cuales se va a analizar: "))
nanalizar1=int(input("Ingrese un numero para contar la cantidad de ocurrencias de este: "))
print("La numero de veces que se repite el ", nanalizar1, "en: ", conjunto, " es: ", cnumero(nanalizar1, conjunto))

#Ejercicio 6 Parte 1
def factorial(numerofact):
    factorialguardada=1
    for i in range(1, numerofact+1):
        factorialguardada*=i
    return factorialguardada
nfactorial = int(input("Ingrese el número para determinar su factorial: "))
print("El factorial de", nfactorial, "es:", factorial(nfactorial))

#Ejercicio 7 Parte 1
def validacionDNI(Ndni):
    contador=0
    conjunto=str(Ndni)
    for i in conjunto:
        contador+=1
    if contador==10:
        return True
    else:
        return False
def mainfuncion():
    dni=int(input("Ingrese el numero de DNI: "))
    print("Si su DNI es falso se imprimira (False), caso contrario se mostrará (True)")
    print("Su Dni es: ", validacionDNI(dni))
mainfuncion() 

#EJERCICIO 8 
#PARTE 1

#8.	Contar de forma descendente hasta cero 
# el número que ingrese por teclado l usuario.
# (Función recursiva)
def contador(numero):
    if numero == 0:
        print("0")
    else:
        print(numero)
        contador(numero - 1)

numero = int(input("Ingresa un número: "))
contador(numero)
#9.	Contar de forma descendente hasta cero 
#los números pares a partir de un número ingresado por el usuario.
# (Función recursiva)
def contador(numero):
    if numero == 0:
        print("0")
    elif numero % 2 == 0:
        print(numero)
        contador(numero - 2)
    else:
        contador(numero - 1)

numero = int(input("Ingresa un número : "))
contador(numero)
#10.Calcular el factorial de un número ingresado por el usuario.
# (Función recursiva)
def factorial(numero):
    if numero ==0:
        return 1
    else:
        return numero*factorial(numero-1)
numero=int(input("ingresa un numero para calcular el factorial: "))
print("el factorial de",numero,"es",factorial(numero))

#PARTE 2
#1.	Solicitar al usuario que ingrese su dirección email. 
# Imprimir un mensaje indicando si la dirección es válida o no,
# valiéndose de una función para decidirlo. 
# Nota: El correo se considerará válido si tiene el símbolo "@".
def validarcorreo(correo):
    if "@" in correo:
        print("La dirección de correo es válida.",correo)
    else:
        print("La dirección de correo no es válida.")

correo = input("Ingresa tu dirección de correo electrónico: ")
validarcorreo(correo)
#2.	Escribir un programa que pida números al usuario, 
# mostrar el factorial de cada uno y, al finalizar,
# la cantidad total de números leídos en total. 
# Nota: Utilice una o más funciones, si es necesario.
def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado
totalnumeros = 0
while True:
    numero = int(input("ingrese un número: "))
    print("El factorial es ",factorial(numero))
    totalnumeros += 1
    print("Entrada inválida ingrese un número entero")
    if input("¿Desea ingresar otro número? si o no: ").lower() != "si":
        break
print("la cantidad total de númerosleidos es ",totalnumeros)

#3.	Solicitar al usuario el ingreso de números primos.
# La lectura finalizará cuando ingrese un número que no sea primo. 
# Por cada número, mostrar la suma de sus dígitos.
# También solicitar al usuario un dígito
# e informar la cantidad de veces que aparece en el número (frecuencia). 
# Al finalizar el programa, mostrar el factorial del mayor número ingresado.

def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
def suma_digitos(numero):
    return sum(int(digito) for digito in str(numero))

def contar_digitos(numero, digito):
    frecuencia = 0
    for d in str(numero):
        if int(d) == digito:
            frecuencia += 1
    return frecuencia

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
mayor_numero = 0

while True:
        numero = int(input("Ingrese un número primo o un número no primo para salir: "))   
        if not primo(numero):
            break
        suma = suma_digitos(numero)
        print("La suma de los dígitos de",numero, "es: ",suma)
        digito = int(input("Ingrese un dígito para obtener su frecuencia: "))
        frecuencia = contar_digitos(numero, digito)
        print("El dígito ",digito," aparece", frecuencia ,"veces en",numero)

        if numero > mayor_numero:
            mayor_numero = numero
if mayor_numero > 0:
    resultado_factorial = factorial(mayor_numero)
    print("El factorial del mayor número ingresado ",mayor_numero, "es: ",resultado_factorial)
else:
    print("No se ingresaron números primos")

#4.	Dada una temperatura f en grados Fahrenheit, devuelva la temperatura en grados centígrados c
#ANGEL VILLAMIL, ISAAC QUINAPALLO, KARLA RODRIGUEZ
def fahrenheit_a_celsius():
    f = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    c = (f - 32) * 5/9
    c = round(c, 2)
    return c

temperatura_c = fahrenheit_a_celsius()
print("La temperatura en grados Celsius es:", temperatura_c)

#5.	Implementa una función llamada laboral que pregunte al usuario cuál es su ocupación 
# e imprima “Ok, tu trabajo es       ”.
#ANGEL VILLAMIL, ISAAC QUINAPALLO, KARLA RODRIGUEZ
def laboral():
    ocupacion = input("Cual es la ocupacion en tu trabajo?")
    print("Ok tu trabajo es ",ocupacion)

laboral()

#6.	Implementa una función llamada area_rectangulo(base, altura) que devuelva el 
# área del rectangulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base 10 de altura.     ”.
#ANGEL VILLAMIL, ISAAC QUINAPALLO, KARLA RODRIGUEZ
def area_rectangulo(base, altura):
    area = base * altura
    return area

base_rectangulo = 15
altura_rectangulo = 10

area = area_rectangulo(base_rectangulo, altura_rectangulo)
print("El area del rectángulo es:", area)

#7.	Construya una función que devuelva el área y la longitud de una circunferencia de 
#radio r que se introducirá como parámetro. Si no se especifica ningún parámetro se entenderá que el radio es la unidad.
#ANGEL VILLAMIL, ISAAC QUINAPALLO, KARLA RODRIGUEZ
import math

def circunferencia(radio=1):
    area = math.pi * radio**2
    longitud = 2 * math.pi * radio
    return area, longitud

radio = 15

area_rectangulo, longitud_circunferencia = circunferencia(radio)

print("El area de la circunferencia es:", area_rectangulo)
print("La longitud de la circunferencia es:", longitud_circunferencia)

#8
#ANGEL VILLAMIL, ISAAC QUINAPALLO, KARLA RODRIGUEZ

while True:
    nombre_completo = input("Ingrese el nombre completo del socio (o presione ENTER para finalizar): ")
    
    if nombre_completo == "":
        break

    dni = input("Ingrese el número de DNI del socio: ")

    while len(dni) != 10:
        print("El número de DNI debe tener 10 dígitos.")
        dni = input("Ingrese el número de DNI del socio: ")

    nombres = nombre_completo.split()
    primer_nombre = nombres[0]
    apellido = nombres[-1]
    primeros_tres_digitos_dni = dni[:3]

    identificador = primer_nombre + str(len(apellido)) + primeros_tres_digitos_dni
    print("Identificador único del socio:", identificador)

#9.	Calcular la serie de Fibonacci (Función recursiva)
#ANGEL VILLAMIL, ISAAC QUINAPALLO, KARLA RODRIGUEZ
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicitar al usuario el número de términos que desea calcular en la serie de Fibonacci
try:
    num_terminos = int(input("Ingrese el numero de términos de la serie de Fibonacci que desea calcular: "))
    if num_terminos <= 0:
        print("Por favor, ingrese un numero mayor que cero.")
    else:
        # Calcular y mostrar la serie de Fibonacci usando la función recursiva
        print("Serie de Fibonacci:")
        for i in range(num_terminos):
            print(f"Termino {i + 1}: {fibonacci(i)}")
except ValueError:
    print("Por favor, ingrese un numero entero.")
