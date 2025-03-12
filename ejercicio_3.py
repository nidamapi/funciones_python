# Construir una funciòn que reciba como paràmetro una lista de datos numèricos y que retorne el promedio de dichos datos.
import random

print("---------------------------------")
print("- SUMA LISTA DATOS -")
print("---------------------------------")

#Definiciòn de la funciòn
def sumar_lista_datos(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

#Entrada
# Creamos una lista vacìa
lista = []
# Tamaño de la lista
n = int(input("Digite el tamaño de la lista: )"))

for i in range(n):
    num = random.randint(1,9)
    lista.append(num)


#Procesamiento
print("Lista: ", lista)
print("Lista :", sumar_lista_datos(lista))


#Salida
print("\nEso era...")
