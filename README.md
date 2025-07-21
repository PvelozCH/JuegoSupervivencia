#Documentación de archivos.

## main.py
	-- Archivo principal que lo corre todo.
	-- Paso a paso : 
		#Primero Muestra el menu de opciones.
		#Permite elegir una opcion al usuario.
		#OPCION 1 : 
			Permite a usuario crear nuevo refugio y gestionarlo.
			
			#CREACIÓN NUEVO REFUGIO 
			- Pide al usuario darle un numero al refugio
			- Crea una carpeta de saves donde se guardan los datos
			- Dentro de saves crea carpeta para refugio creado
			- Crea una lista de 5 personajes aleatorios.
				#Creación de personajes
				- Dentro de la clase Personaje se crean atributos
				aleatorios, le da una arma aleatoria(Armas.json) 
				y le da nombre y apellido aleatorios(NombresApellidos.json)
			- Los 5 personajes se guardan dentro de un json dentro de 
			una carpeta(ejem: Refugio21).
			
		#OPCION 2 : 
			Permite cargar la partida y gestionarlo
			
			#Carga de refugio
			- Pide al usuario que ingrese el refugio que quiere 
			cargar.
		#OPCION 3 :
			Se sale del juego
			
		##Una vez creado o cargado el refugio.
			- Muestra en pantalla las opciones dentro de un refugio
			# 1. Salir a explorar
				- Se inicia el MapaGrafico.py 
				- Se inicializa tamaño del mapa, tamaño de cuadros de
				este, cantidad de casillas y colores a utilizar.
				Se crea una clase CeldaMapa, para transformar 
				cada celda en un objeto.
				- Se crea la matriz del tamaño del mapa.
				- Se le agrega una cantidad aleatorio de celdas 
				diferentes a la base (agua, casas y lugares importantes)
				- Se cargan los personajes del json de personajes.
				- Se crea lista en donde se dejan esos personajes.
				- Deja a los personajes dentro del mapa en un lugar
				aleatorio.
				
				- Se comienza a ejecutar el mapa de color negro.
				- Obtiene las coordenadas del mouse.
				- 
				
				
				
