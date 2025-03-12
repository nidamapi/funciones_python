# Construir una funciòn que reciba como paràmentro una lista de datos numèricos y retorne el promedio de los datos pares.
import random 

print("---------------------------------")
print("- DIGITE EL TAMAÑO DE LA LISTA -")
print("---------------------------------")

#Definiciòn de la funciòn 
def calcular_pares_lista(lista):
    suma = 0
    n_p = 0
    for i in lista:
        if i % 2 == 0:
            suma = suma + i
            n_p = n_p+1
    return suma / n_p

     
    #Creamos una lista vacìa
lista = []
#Tamaño de la lista
n = int(input("Digite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(14,18)
    lista.append(num)

#Procesamiento
print("Lista: ", lista)
print("El promedio de la lista es: ", calcular_pares_lista(lista))

#Salida
print("\nEso era...")