# Construir una funciòn que reciba su nombre como paràmetro y que lo muestre 5 veces en la pantalla.
print("---------------------------------")
print("- MOSTRAR NOMBRE EN PANTALLA -")
print("---------------------------------")

#Definiciòn de la funciòn
def mostrarNombre(nombre):
    for i in range(1,6):
        print(f"{i}{nombre}")

#Entrada
nombre = input("Digite: ")

#Procesamiento
mostrarNombre(nombre)

#Salida
print("*\nEso era...")

