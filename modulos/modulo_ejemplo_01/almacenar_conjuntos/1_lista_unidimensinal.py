#lista(array) unidimensional - numeros enteros 
listaNumeros = [1,2,3,4,5,6,7,8,9,10]
#creacion de variables
suma = 0
mayorNumero = listaNumeros[0]

#Bucle FOR - para encontar el mayor numero
for varNumero in listaNumeros: 
        suma += varNumero
        if varNumero > mayorNumero:
            mayorNumero = varNumero
            
print("El numero mayor es: ", mayorNumero) 
print("La suma de lista es: ", suma)
