#Ejercicio 1
ps = 1.50
pd = 2.50
pt = 3.25

ts = 0
td = 0
tt = 0
total_acumulado = 0

while True:
    print("Seleccione el tipo de hamburguesa:")
    print("1. Sencilla")
    print("2. Doble")
    print("3. Triple")
    print("0. Finalizar compra")

    opcion = int(input("Ingrese el número de la hamburguesa deseada: "))

    def calcular_precio(opc, cant):
        switch = {
            1: cant * ps,
            2: cant * pd,
            3: cant * pt
        }
        return switch.get(opc, 0)

    if opcion == 0:
        break

    if 1 <= opcion <= 3:
        cantidad = int(input("Ingrese la cantidad de hamburguesas: "))
        ctotal = calcular_precio(opcion, cantidad)
        total_acumulado += ctotal

        comprarmas = input("¿Desea comprar más hamburguesas? (si/no): ")

        if comprarmas != "si":
            mpago = input("Ingrese el método de pago (efectivo o tarjeta): ")

            if mpago == "efectivo" or mpago == "tarjeta":
                dfactura = input("¿Desea factura? (si/no): ")

                if dfactura == "si":
                    ncliente = input("Ingrese su nombre: ")
                    ccliente = input("Ingrese su cédula: ")
                    ccliente = input("Ingrese su correo electrónico: ")

                    print("Factura a nombre de", ncliente)
                    print("Cédula:", ccliente)
                    print("Correo electrónico:", ccliente)
                    print("Total a pagar: $" + str(total_acumulado))
                else:
                    print("El cliente debe pagar: $" + str(total_acumulado))
                break
            else:
                print("El tipo de pago que ingresó no es válido.")
                break
    else:
        print("Lo sentimos, en el Carbonero no ofrecemos ese tipo de hamburguesas. Intente nuevamente.")

print("Compra finalizada. Gracias por su compra!")


#Ejercicio 2
while True:
    print("Operaciones disponibles:")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    print("5) Potencia")
    print("6) Módulo")
    print("0) Salir")

    opcion = int(input("Ingrese el número de la operación deseada: "))

    if opcion == 0:
        break

    if 1 <= opcion <= 6:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        if opcion == 1:
            resultado = numero1 + numero2
        elif opcion == 2:
            resultado = numero1 - numero2
        elif opcion == 3:
            resultado = numero1 * numero2
        elif opcion == 4:
            if numero2 != 0:
                resultado = numero1 / numero2
            else:
                print("Error: División por cero")
                continue #Sirve para regresar al inicio
        elif opcion == 5:
            resultado = numero1 ** numero2
        elif opcion == 6:
            if numero2 != 0:
                resultado = numero1 % numero2
            else:
                print("Error: Módulo por cero")
                continue #Sirve para regresar al inicio

        print("Resultado:", resultado)
    else:
        print("Error: Opción no válida. Intente nuevamente.")
        
