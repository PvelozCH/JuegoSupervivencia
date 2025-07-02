import os
#Limpia la pantalla
def cleanP():
	os.system('clear')
	
#Clase que contiene todos los menus
class MenuPrincipal:
	#Primer menu del juego
	def menuInicial(self):
		print("*Fallout*")
		print("1.Juego nuevo")
		print("2.Cargar juego")
		print("3.Salir")
		opcion = input("Elige una opcion: ")
		opcion = int(opcion)
		#Se crea refugio nuevo
		if(opcion == 1):
			cleanP()
			print("*Nuevo refugio*")
			numR= input("Asigna un número al refugio:")
			cleanP()
			print("Bienvenido al refugio",numR)
			print("Se crearan personajes")
			
		#Se carga un refugio
		if(opcion==2):
			cleanP()
			print("Has elegido cargar una partida")
			
		#Se sale de la partida
		if(opcion==3):
			print("Hasta pronto")
		
			
			
			
			
			
			
			
		