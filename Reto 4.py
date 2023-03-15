# Pseudocodigo numeros primos
print ("Reto 4")
# Variables
num = int
x = int
contador = int
# Ingrese un numero
a : int = int(input("Ingresa un numero"))
#Inicializamos n en cero
num = 0
while a>0:
    num = num + 1
    x = 1 #Inicializamos x en uno
    contador = 0 #Inicializamos contador en cero
    while x<=num:
        if num % x == 0:
            contador = contador + 1
        break
    x = x + 1 #Incrememtamos la variable x
    break
    if contador == 2:
        print("El numero ",num,"es primo")
        a = a - 1
break