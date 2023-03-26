n: int = int(input("Ingrese un número natural: ")) # Inicia: Pide ingresar un número. 
valorIncialn: int = n  # Nombra la segunda variable: Esta va tomar el valor de original de n
while (n>0): # Condición: Que n sea mayor a 0. 
    n -=1 # Actualiza: Resta 1 a n. 
    valorIncialn= valorIncialn*n # Actualiza: Multiplica el nuevo valor de n.
    if n==0: # Da una condición: Si "n" es igual a 0. 
        break # Ocasiona que si se cumple la condición anterior termina el ciclo. 
    if n == 1: # Da una condición: Si "n" es igual a 1. 
        print("El factorial es", valorIncialn)  # Si cumple la condición anterior imprime el cometario. 