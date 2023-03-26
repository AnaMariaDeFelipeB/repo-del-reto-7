A: float = 25 # Inicia con la primer variable: Población del país A en millones 
B: float = 18.9  # Nombra segunda variable: Población del país B en millones.
añosQuePasan: int=2022 # Nombra tercer varible: Años que pasan. 

while (A>=B): # Condición: Que el "paisA" sea mayor al "pais B"
    A = A + (A*0.02)  # Actualiza: Opera el 2 porciento de la población de A y se lo suma a A. 
    B = B + (B*0.03) # Actualiza: Opera el 3 porciento de la población de B y se lo suma a B. 
    añosQuePasan +=1 # Actualiza: Suma un año más. 
print("Cuando el país B supere a la población del país A, sera en el año " + str(añosQuePasan)) # Fin del ciclo: Imprime comentario del valor que hace que termine el ciclo, es decir, cuando B, sea mayor a A. 