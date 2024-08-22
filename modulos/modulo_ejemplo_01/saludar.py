#existen dos maneras de importar
import modulo_saludar as mSalud
#from modulo_saludar import saludar
import math
#from modulo_saludar import * # no es buena practica 
import modulo_fuera.calular_edad as calEdad
 # creacion de la variable
varible_saludar = mSalud.saludar("diego")
varible_edad = calEdad.calcularEdad(2005,2024)

print(varible_saludar)
print(varible_edad)
print("El PI es: ",math.pi)

