# El usuario adivina un aleatorio número dado por el programa. 

import random  # Llama a la función aleatoria. 
n = random.randint(1, 100)   # Inicio: El programa soltará un número aleatorio. 
print("El número aleatorio fue: " + str(n)) # Imprime comentario antes de comenzar el ciclo. 
base: int = int(input("Ingrese número de 1 a 100 que considera es el número que tiene el programa: ")) #Segunda variable: pide al usuario ingresar un número. 

while (1<=base<=100): # Condición: Que la base este entre 1 y 100. 
    if n==base: # Nueva condicíon: Si la base es igual a n. 
        print("Adivinaste el número") # Imprime el comentario si se cumple la condición dada anteriormente. 
        break # Interrumple y termina el ciclo si se cumple la condición. 
    if base>n: # Nueva condicíon: Si la base es mayor a n.  
        base = int(input("El número es MENOR, inserte un nuevo número: ")) # Imprime el comentario si se cumple la condición dada anteriormente, pidiendo al usuario ingresar un nuevo valor y reevalúa. 
    if base<n: # Nueva condicíon: Si la base es menor a n.  
        base = int(input("El número es MAYOR, inserte un número nuevo: ")) # Imprime el comentario si se cumple la condición dada anteriormente, pidiendo al usuario ingresar un nuevo valor y reevalúa.  
print("El número que ingresaste fue: " + str(base)) # Final del ciclo. Imprime cuando el ciclo se termina. 