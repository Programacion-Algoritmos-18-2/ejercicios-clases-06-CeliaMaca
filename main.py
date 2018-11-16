from paquete.model import *			# Se importa todo el archivo modelado
# p=PersonaEquipo("Luis")
f=Futbolista("Antonio")				# Se crea el Objeto Futbolista 
m=MedicoEquipo("Ramon")				# Se crea el Objeto Medico
p=PresidenteEquipo("Francisco") 	# Se crea el Objeto Presidente 
e=Entrenador("Jose")				# Se crea el Objeto Entrenador 
lista=[f,m,p,e]						# Se crea una lista que almacena los objetos creados
for l in lista:						# Se recorre los objetos de la lista
	l.entrenar()					
