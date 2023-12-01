#Ejercicio35 (Operadores de pertenencia)
lista = (10, 20, 30, 40, 50)
4 in lista
False
3 in lista
False
4 not in lista
True
#Ejercicio36 (Operadores de identidad)
x=0
y=4
lista=[1,9]
x is lista
False
x is y
False
x is 0 
True
#Ejercicio35 (Comentarios)
#Comentario xd
print("Esto es un comentario de Isaac Quinapallo")
"""Aveces
pienso 
que 
la 
vida 
es 
muy 
corta"""
#Ejercicio36 (Tipo de Datos)
numeroentero = 42
print(int(numeroentero), numeroentero)

numerodecimal = 3.14
print(float(numerodecimal), numerodecimal)
#Ejercicio37 (Real)
resultadod = 7.0 / 3.0
print(type(resultadod), resultadod)
#Ejercicio 38 (Complejo.real)
resultadodiv = 7.0 / 3.0
print(complex(resultadodiv), resultadodiv)
# Ejercicio 39 (Complejo. imag)
partereal = 2
parteimaginaria = 3j
numerocomp = partereal + parteimaginaria
print(complex(numerocomp), numerocomp)
# Ejercicio 40 (Booleanos)
c1 = True
print(c1);
c2 = False
print(c2);
c3 = 10 > 5
print(c3);
#Ejercicio 41 (Cadena de texto)
t1 = "Hola, mundo :D"
print(t1);
t2 = 'Hola Ing.'
print(t2);
#Ejercicio 42 (Lista, Tupla y Conjunto)
listanumeros = [1, 2, 3, 4, 5]
tuplacolores = ('rojo', 'verde', 'azul')
diccionarioedades = {'Alice': 25, 'Bob': 30, 'Charlie': 22}
print("Lista:", listanumeros)
print("Tupla:", tuplacolores)
print("Diccionario:", diccionarioedades)
#Ejercicio 43 (Ejemmplo tipo variable)
def verificartipo(objeto, t1):
    return isinstance(objeto, t1)
print(verificartipo(5, int))          
print(verificartipo("Hola", str))     
print(verificartipo([1, 2, 3], list)) 
#Ejercicio 44 (De str a int)
cadenan = "456"
numeroe = int(cadenan)
print("Cadena original:", cadenan)
print("Número entero:", numeroe)
print("Tipo de número entero:", str(numeroe))
