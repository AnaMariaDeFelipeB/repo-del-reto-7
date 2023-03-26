# El programa adivina un número dado por el usuario.
 
n: int = int(input("Ingrese número entero a adivinar: ")) # Inicia: Pide ingresar un número. 
base = 0 # Nombra una segunda varible: En este caso será la base que el programa irá modificando hasta adivinar el número dado.  
while not(base==n) and 1<=n<=100: # Condición: Que base no sea igual a n y que este en el rango de 1 a 100. 
    if n>base: # Nueva condición: Si n es mayor que la base. 
        base +=1 # Si se cumple la condición suma 1 a la base y reevalúa el codigo. 
    if n<base: # Nueva condición: Si n es menor que la base. 
        base -=1  # Si se cumple la condición resta 1 a la base. 
print("El número puesto fue: " + str(base)) # Finaliza ciclo: Imprime comentario cuando hay un valor que no cumpla la condición. 