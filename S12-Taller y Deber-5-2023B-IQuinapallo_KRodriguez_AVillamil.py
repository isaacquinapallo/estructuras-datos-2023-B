#TALLER
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

#2
tupla = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

elemento = tupla[0][1]
print(elemento)  
#3
tupla = ('guayaquil', 'H', 'Ladrones')
a, b, c = tupla

print(a)  # Salida: 1
print(b)  # Salida: 2
print(c)  # Salida: 3

#4
#Metodo index con 1 parametr
tupla = ("manzana", "banana", "naranja", "pera")

fruta = "banana"
posicion = tupla.index(fruta)

print("La posición de" , fruta, "es", posicion)

#5
#Metodo index con 2 parametros
tupla=(7,7,7,7,4)
print(tupla.index(7,2))

#6
persona = ("Angel", "Villamil", "Sebastian", "Munoz")
nombre, apellido, _, _ = persona
print(apellido)
print(nombre)

#7
# Metodo enumerate
atletas=("juan","pablo","pedro")
posicion= enumerate(atletas)
print (posicion)


# Metodo enumerate
atletas=("juan","pablo","pedro")
for i, atleta in enumerate(atletas):
    print("posicion ",i+1, "atleta",atleta)


#8
nconocer=int(input("Ingrese el numero el cual quiere conocer cuantas veces se repite: "))
tupla=(1,2,3,4,5,1,6,7,8,1,9)
print(tupla.count(nconocer))

#9
#crear tupla con numeros e indicar numero mayor y menor
numeros=(1,5,6,2,4,8,3,0)
mayor=numeros[0]
menor=numeros[0]

for numero in numeros:
    if numero>mayor:
        mayor=numero
    if numero<menor:
        menor = numero
print("El numero mayor es: ",mayor," el numero menor es: ",menor)
#10
#crear tupla con numeros e indicar numero mayor y menor
#Metodos max y min
numeros=(1,5,6,2,4,8,3,0)
mayor=numeros[0]
menor=numeros[0]
print("El maximo es: ",max(numeros))
print("El minimo es: ",min(numeros))

#11
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

indice = int(input("Ingrese un indice: "))

valor = tupla[indice]

print("El valor de la tupla en el índice", indice, "es:", valor)
#12
#Lista tupla como 
#Convertir de lista a tupla
valores=[6,7,4,9,8,10]
tupla_lista=tuple(valores)
print(tupla_lista)

#13
lista = []
for i in range(10):
    valor = float(input("Ingrese el valor para la posición : "))
    lista.append(valor)

suma = sum(lista)
media = suma / len(lista)

print("La suma de los números es:", suma)
print("La media de los números es:", media)

#TAREA---------------------------------------------------------------------------------------------------------------------------------------
#Ejercicio1
#Crea una tupla con los meses del año, pide números al usuario,
# si el numero esta entre 1 y la longitud máxima de la tupla,
# muestra el contenido de esa posición sino muestra un mensaje de error.
#El programa termina cuando el usuario introduce un cero.

mesesdelaño = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

while True:
    numero = int(input("Introduce un numero (1-12) para obtener el mes correspondiente (o introduce 0 para salir): "))
    if numero == 0:
        print("Hasta luego")
        break
    if 1 <= numero <= len(mesesdelaño):
       
        print("El mes correspondiente al número {} es: {}".format(numero, mesesdelaño[numero - 1]))
    else:
       
        print("El número debe estar entre 1 y {} intentalo de nuevo.".format(len(mesesdelaño)))

#Implementa una función siguiente_mayor(lista),
# a la que se le pase como argumento una lista de números enteros 
# y reemplace cada número por el siguiente más grande de la lista.
def siguiente_mayor(lista):
    for i in range(len(lista)):
        mayor = None
        for j in range(i+1, len(lista)):
            if lista[j] > lista[i]:
                mayor = lista[j]
                break
        lista[i] = mayor
    return lista
0
numeros = [3, 1, 7, 4, 2, 5]
print("Lista original:", numeros)
print("Lista con el siguiente número más grande:", siguiente_mayor(numeros))

#Escribir una función poker que reciba cinco cartas de la baraja francesa 
# e informe (devuelva el valor lógico correspondiente) 
# si esas cartas forman o no un poker (es decir que hay 4 cartas con el mismo número).
def poker(cartas):
    contador = {}
    for carta in cartas:
        valor = carta[0] 
        if valor in contador:
            contador[valor] += 1
        else:
            contador[valor] = 1

    for count in contador.values():
        if count >= 4:
            return True
    return False
cartas = ['2D', '2C', '2H', '2S', '5D']
print("¿Forma un poker?", poker(cartas))


#El tiempo como tuplas. Proponer una representación con tuplas
# para representar el tiempo. Escribir una función sumaTiempo
# que reciba dos tiempos dados y devuelva su suma.
def sumaTiempo(tiempo1, tiempo2):

    segundos = tiempo1[2] + tiempo2[2]
    
    segundos = segundos % 60
    acarreominutos = segundos // 60

    
    minuto= tiempo1[1] + tiempo2[1] + acarreominutos

    minutos = minuto % 60
    acarreo_horas = minuto// 60

    hora = tiempo1[0] + tiempo2[0] + acarreo_horas
    horas = hora % 24
    return (horas, minutos, segundos)
tiempo1 = (12, 30, 45)
tiempo2 = (5, 45, 20)
resultado = sumaTiempo(tiempo1, tiempo2)

print("tiempo 1",tiempo1)
print("tiempo2",tiempo2)
print("La suma de los tiempos es:", resultado)

#Escribir una función diaSiguienteE que dada una fecha expresada como la terna
# (Día, Mes, Año) (donde Día, Mes y Año son números enteros) 
# calcule el día siguiente al dado, en el mismo formato.

def bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

def diaSiguiente(fecha):
    dia, mes, año = fecha
    
    if mes == 2:
        if bisiesto(año):
            ultimodia = 29
        else:
            ultimodia = 28
    elif mes in (4, 6, 9, 11):
        ultimodia = 30
    else:
        ultimodia = 31

    if dia == ultimodia:
 
        dia = 1
        if mes == 12:

            mes = 1
            año += 1
        else:
            mes += 1
    else:
        dia += 1

    return (dia, mes, año)

fechaactual = (31, 1, 2024)
siguientedia = diaSiguiente(fechaactual)
print("la fecha actual es",fechaactual)
print("El día siguiente es:", siguientedia)

# Función para pedir números al usuario y mostrar el contenido de la posición correspondiente en la tupla
def mostrar_mes(meses, numero):
    if 1 <= numero <= len(meses):
        print("El mes correspondiente al número {} es: {}".format(numero, meses[numero - 1]))
    else:
        print("Error: El número debe estar entre 1 y {}. Inténtalo de nuevo.".format(len(meses)))

# Función para encontrar el siguiente número más grande en una lista
def siguiente_mayor(lista):
    for i in range(len(lista)):
        mayor = None
        for j in range(i+1, len(lista)):
            if lista[j] > lista[i]:
                mayor = lista[j]
                break
        lista[i] = mayor
    return lista

# Función para verificar si hay un poker en una mano de cartas
def poker(cartas):
    contador = {}
    for carta in cartas:
        valor = carta[0]  # El valor de la carta es el primer caracter
        if valor in contador:
            contador[valor] += 1
        else:
            contador[valor] = 1
    # Verificar si hay al menos cuatro cartas con el mismo valor
    for count in contador.values():
        if count >= 4:
            return True
    return False

# Función para sumar dos tiempos dados
def sumaTiempo(tiempo1, tiempo2):
    horas = tiempo1[0] + tiempo2[0]
    minutos = tiempo1[1] + tiempo2[1]
    segundos = tiempo1[2] + tiempo2[2]

    minutos += segundos // 60
    segundos %= 60
    horas += minutos // 60
    minutos %= 60

    return (horas, minutos, segundos)

# Función para calcular el día siguiente a una fecha dada
def diaSiguienteE(fecha):
    dia, mes, año = fecha

    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if es_bisiesto(año):
        dias_por_mes[2] = 29

    dia += 1
    if dia > dias_por_mes[mes]:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            año += 1

    return (dia, mes, año)

# Función para verificar si un año es bisiesto
def es_bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

# Programa principal
meses_del_año = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

while True:
    numero = int(input("Introduce un número (1-12) para obtener el mes correspondiente (o introduce 0 para salir): "))
    
    if numero == 0:
        print("¡Hasta luego!")
        break
    
    mostrar_mes(meses_del_año, numero)

# Ejemplos de uso de las funciones restantes:
lista_numeros = [3, 1, 7, 4, 2, 5]
print("Lista original:", lista_numeros)
print("Lista con el siguiente número más grande:", siguiente_mayor(lista_numeros))

mano_cartas = ['2D', '2C', '2H', '2S', '5D']  # Poker de doses
print("¿Forma un poker?", poker(mano_cartas))

tiempo1 = (12, 30, 45)
tiempo2 = (5, 45, 20)
print("La suma de los tiempos es:", sumaTiempo(tiempo1, tiempo2))

fecha_actual = (31, 12, 2023)
print("El día siguiente es:", diaSiguienteE(fecha_actual))

#Ejercicio6
#Escribir una función diaSiguienteT que dada una fecha expresada como la terna (Día, Mes, Año)
#(donde Día y Año son números enteros, y Mes es el texto Ene, Feb, ..., Dic, según corresponda) calcule el día siguiente al dado, en el mismo formato.

def diaSiguienteT(dia, mes, anio):
    diasMes={'Ene': 31, 'Feb': 28, 'Mar': 31, 'Abr': 30, 'May': 31, 'Jun': 30,  'Jul': 31, 'Ago': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dic': 31}
    dia+=1
    if (anio%4 ==0 and anio%100 !=0) or (anio%400 ==0):
        diasMes['Feb'] = 29
    if dia>diasMes[mes]:
        dia= 1
        meses= ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
        mes_index= meses.index(mes)
        mes=meses[(mes_index+1)%12]
        if mes== 'Ene':
            anio+= 1
    return dia,mes,anio
print("Recuerda que el mes se escribe así: Ene, Feb, Mar, Abr, Jun, Jul, Ago, Sep, Oct, Nov y Dic")
FechaAct=input("Ingrese el día, mes, año de la siguiente manera: (8,Feb,2024): ").split(',')
dia, mes, anio=int(FechaAct[0]),FechaAct[1],int(FechaAct[2])
siguiente=diaSiguienteT(dia, mes, anio)
print("El día siguiente de: ", FechaAct, " es: ", siguiente)

#Ejercicio7

def opcion1(total,catalogonombre,catalogoprecio,nvecescatalogo,precioProducto):
    print("1. Flores+Peluche=15,50")
    print("2. Flores+Carta=7,50")
    print("3. Flores+Chocolate=12,25")
    print("4. Flores+Perfume=22,75")
    opcionCatalogo=int(input("Ingrese una opcion: "))
    if opcionCatalogo==1 or opcionCatalogo==2 or opcionCatalogo==3 or opcionCatalogo==4:
        nvecescatalogo[opcionCatalogo-1]+=1
        precioProducto[opcionCatalogo-1]=nvecescatalogo[opcionCatalogo-1]*catalogoprecio[opcionCatalogo-1]
        total+=precioProducto[opcionCatalogo-1]
        print("Producto registrado exitosamente")
    else:
        print("Opcion Invalida")
    return(total,catalogonombre,catalogoprecio,nvecescatalogo,precioProducto)
        
def opcion2(total,catalogonombre,nvecescatalogo,precioProducto):
    if total==0:
        print("ERROR, COMPRAS NO RESGISTRADAS")
    elif total!=0:
        print("Se han insertado los siguientes productos: ")
        print(catalogonombre[0]," x ", nvecescatalogo[0], " = ", precioProducto[0])
        print(catalogonombre[1]," x ", nvecescatalogo[1], " = ", precioProducto[1])
        print(catalogonombre[2]," x ", nvecescatalogo[2], " = ", precioProducto[2])
        print(catalogonombre[3]," x ", nvecescatalogo[3], " = ", precioProducto[3])
        print("El total es: ", total)
    
def opcion3(factura, total):
    if total==0:
        print("ERROR, COMPRAS NO RESGISTRADAS")
    elif total!=0:
        ncliente=(input("Ingrese solo el nombre del cliente: "))
        acliente=(input("Ingrese solo el apellido del cliente: "))
        tcliente=input("Ingrese el telefono del cliente: ")
        ccliente=(input("Ingrese el correo del cliente: "))
        nentrega=(input("Ingrese el nombre de la persona que recibe el producto: "))
        aentrega=(input("Ingrese el apellido de la persona que recibe el producto: "))
        tentrega=(input("Ingrese el telefono de la persona que recibe el producto: "))
        factura+=1
        print("DETALLE DE COMPRA")
        print("-> Datos del Cliente")
        print("Nombre: ",ncliente)
        print("Apellido: ",acliente)
        print("Telefono: ",tcliente)
        print("Correo: ",ccliente)
        print("-> Datos del Entrega")
        print("Nombre: ",nentrega)
        print("Apellido: ",aentrega)
        print("Telefono: ",tentrega)
        print("-> Datos de Pago")
        print("Numero de factura: ",factura)
        print("Precio Final: ",total)
print("Bienvenido a RAPID")
factura=100000
opcion=0
total=0
catalogonombre=['Flores+Peluche','Flores+Carta','Flores+Chocolate','Flores+Perfume']
catalogoprecio=[15.50,7.5,12.25,22.75]
nvecescatalogo=[0,0,0,0]
precioProducto=[0,0,0,0]
while(opcion!=4):
    print("Indique con que podemos ayudarte: ")
    print("1. Registrar Compra")
    print("2. Mostrar Compra")
    print("3. Mostrar el detalle de la Compra")
    print("4. Salir del Sistema")
    opcion=int(input("Ingrese una opcion: "))
    if opcion==1:
        total,catalogonombre,catalogoprecio,nvecescatalogo,precioProducto=opcion1(total,catalogonombre,catalogoprecio,nvecescatalogo,precioProducto)
    elif opcion==2:
        opcion2(total,catalogonombre,nvecescatalogo,precioProducto)
    elif opcion==3:
        factura=opcion3(factura, total)
    elif opcion==4:
        print("Gracias por Comprar con nosotros :D")
        break
    else:
        print("Opcion Incorrecta...")
    