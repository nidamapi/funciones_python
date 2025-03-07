print("---------------------------------")
print("- BUSCAR UN NUMERO EN CONJUNTO -")
print("---------------------------------")

#Definiciòn de la funciòn 
def buscarDatoEnLista(datoABuscar, lista):
    r = False
    for i in lista:
        if i == datoABuscar:
            r = True
    return r

#Entrada
dato = int(input("Nùmero a buscar: ")) #se recibe el dato del usuario

#Procesamiento
lista = [1,2,3,4,5] #Se almacena una lista de datos
if buscarDatoEnLista(dato, lista):
    print("Lo encontrè")
else:
    print("No lo encontrè")

#Salida
print("\nEso era...")