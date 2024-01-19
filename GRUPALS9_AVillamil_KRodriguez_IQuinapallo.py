#Ejercicio Normal
#S9 #ANGEL VILLAMIL, ISAAC QUINAPALLO, KARLA RODRIGUEZ

# Calculamos la suma de los cuadrados de los primeros diez números naturales
suma_cuadrados = 0

for numero in range(1, 11):
    cuadrado = numero ** 2
    suma_cuadrados += cuadrado

print("La suma de los cuadrados es: ",suma_cuadrados)


#Numpy
#1
#ANGEL VILLAMIL, ISAAC QUINAPALLO, KARLA RODRIGUEZ
import numpy as np

# Creamos un arreglo de los primeros diez números naturales
numeros = np.arange(1, 11)

# Calculamos la suma de los cuadrados utilizando Numpy
suma_cuadrados = np.sum(numeros**2)

print("La suma de los cuadrados usando numpy es: ",suma_cuadrados)



#2 NORMAL
# Definimos una lista de numeros
numeros = [12, 18, 25, 30, 42]

#Se va calcular la media aritmetica
suma_numeros = sum(numeros)
cantidad_numeros = len(numeros)
media_aritmetica = suma_numeros / cantidad_numeros

print("La media aritmetica es: ",media_aritmetica)


#USANDO NUMPY

import numpy as np

# Definimos un arreglo
arr_numeros = np.array([12, 18, 25, 30, 42])

media_aritmetica = np.mean(arr_numeros)
print("La media aritmética usando Numpy es: ",media_aritmetica)
