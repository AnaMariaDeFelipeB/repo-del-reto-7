# El programa adivina un número dado por el usuario.
 
n: int = int(input("Ingrese número entero a adivinar: ")) # Inicia: Pide ingresar un número. 
base = 0 # Nombra una segunda varible: En este caso será la base que el programa irá modificando hasta adivinar el número dado.  
while not(base==n) and 1<=n<=100: # Condición: Que base no sea igual a n y que este en el rango de 1 a 100. 
    if n>base: # Nueva condición: Si n es mayor que la base. 
        base +=1 # Si se cumple la condición suma 1 a la base y reevalúa el codigo. 
    if n<base: # Nueva condición: Si n es menor que la base. 
        base -=1  # Si se cumple la condición resta 1 a la base. 
print("El número puesto fue: " + str(base)) # Finaliza ciclo: Imprime comentario cuando hay un valor que no cumpla la condición. 

















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