i: int = 0 # Inicio
print("Inicio lista impares")  # Imprime comentario antes de iniciar el ciclo.
while (i <=999): # Condición: Números menores o iguales a 999.
  i+=1 # Actualiza: "i" sumandole 1. 
  if i%2 == 0: # Nueva condición: Si el modulo "i" entre 2 es igual a 0. 
    continue # Si cumple la conción anteriormente dada, ignora el valor y continua con el siguiente número en la condición principal. 
  print(i) # Imprime valores dados dentro del ciclo. 
print("Fin lista impares") # Fin del ciclo: Imprime comentario indicando el fin de la lista de los número impares.

a: int = 0 #Inicio
print("Inicio lista pares")  # Imprime comentario antes de iniciar el ciclo. 
while (a <=1000): # Condición: Números menores o iguales a 1000.
  a +=1 #Actualiza "a" sumandole 1. 
  if not(a%2==0): # Nueva condición: Si el modulo "a" entre 2 NO es igual a 0. 
    continue # Si cumple la conción anteriormente dada, ignora el valor y continua con el siguiente número en la condición principal. 
  print(a) # Imprime valores dados dentro del ciclo. 
print("Fin lista pares") #Fin del ciclo: Imprime comentario indicando el fin de la lista de los número pares.