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

