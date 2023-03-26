n: int = int(input("Ingrese un número entre 2 y 50: ")) # Inicia: Pide al usuario un valor. 
divisorDen: int = 1 # Segunda variable: divisores de "n". 
while (2<=n<=50) and divisorDen<=n: # Condición: que "n" este entre 2 y 50 y que la segunda variable sea menor a "n". 
    if n%divisorDen == 0: # Nueva condión: Que el modulo de "n" entre "divisorDen" sea igual a 0. 
        print ("El número", divisorDen, "es un divisor de", n) # Si se cumple, imprime el cometario. 
    divisorDen +=1 # Actualiza: Suma 1 y reevalúa. 