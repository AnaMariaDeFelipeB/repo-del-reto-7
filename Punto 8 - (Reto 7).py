def numerosprimos (n:int):  #Nombra la función. 
    # <Instrucciones de la función.>
    n= 1 # Iniciamos el while. 
    while 1<=n<=100: # Condición: Que n este entre 1 y 100. 
        totalDeCeros = 0 # Nombra variable dentro del while. (Para lograr volverlas a su estado original si lo deseamos.)
        divisor = 1 # Nombra variable dentro del while. (Para lograr volverlas a su estado original si lo deseamos.)
        while divisor<=n: # Genera un nuevo while, con instrucciones propias: Que la variable "divisor", sea menor o igual a "n"
            if n%divisor == 0:  # Nueva condición: Si el modulo de "n" entre "divisor" es igual a 0. 
                totalDeCeros +=1 # Si se cumple la condición anteriormente dada, suma 1. 
            divisor +=1 # Actualiza (solo dentro del nuevo while): Aumenta uno al divisor, si cumple el while. 
        # <Finaliza while secundario>
        if totalDeCeros==2: # Nueva condición: Si el "totalDeCeros" es igual a 2. 
            print(n) # Si cumple la condición anterior, imprime n. 
        n +=1 # Actualiza (en el while principal): Suma 1 a "n". 
    # <Finaliza función y while> 

if __name__ == "__main__": # Llama a la función principal. 
    númerosprimos = numerosprimos(n) # Nombra variable: Con las instrucciones y resultados de la función "numerosprimos"
    print (númerosprimos) # Imprime el resultado de la función. 