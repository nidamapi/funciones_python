print("---------------------------------")
print("- BUSCAR UN NUMERO EN CONJUNTO -")
print("---------------------------------")

#Entrada
b = int(input("Nùmero a buscar: ")) #se recibe el dato del usuario

#Procesamiento
a = [1,2,3,4,5] #Se almacena una lista de datos
r = False #se inicia la variable r con un valor Falso

for i in a:
    if i==b:
        print("Lo encontrè")
        r = True
if r==False:
    print ("No lo encontrè")

#Salida

print("\nEso era...")
