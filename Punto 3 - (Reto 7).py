n : int = int(input("Ingrese un número mayor o igual a 2: ")) # Inicia. Pide ingresar un número. 
print("El número ingresado fue: " + str(n)) # Imprime el comentario antes de iniciar el ciclo
while (n>=2): # Condición: Que n sea mayor a 2. 
    n -=1 # Actualiza: Resta 1 a n
    if n%2==0: # Nueva condición: Si n el modulo de n entre 2 es igual a 0. 
        print(n) # Si se cumple la condición anteriormente dada, imprime a n y reevalúa el código. 