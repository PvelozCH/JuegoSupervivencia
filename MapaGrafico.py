#MAPA GRAFICO
import pygame
import random
#Para conectar personajes y elementos dentro del mapa.
from Clases import Personaje,Atributos,Arma
import json

def iniciarMapa(numRefugio):
    # Inicializar Pygame
    pygame.init()
    pixelesX = 800
    pixelesY = 600
    screen = pygame.display.set_mode((pixelesX, pixelesY))
    clock = pygame.time.Clock() 

    TILE_SIZE = 10  #Tamaño de cada cuadro.

    ## Cantidad de casillas por ancho y por largo
    cantCasillasX = int((pixelesX/TILE_SIZE))
    cantCasillasY = int((pixelesY/TILE_SIZE))

    # Colores de cada cuadro. (RGB)
    VERDE = (34, 139, 34)     # Terreno base
    AGUA = (0, 191, 255)
    ROCA = (120, 120, 120)
    ARENA = (200, 200, 50)
    MONTAÑA = (139, 69, 19)

    #Plantilla para cada una de las celdas del mapa.
    class CeldaMapa:
        def __init__(self, x,y,tipo_terreno,objeto=None):
            self.x = x
            self.y = y
            self.tipo_terreno = tipo_terreno
            self.objeto = objeto

    # Crea la matriz del mapa con terreno base
    mapa = []
    for x in range(cantCasillasX):
        fila = []
        for y in range(cantCasillasY):
            fila.append(CeldaMapa(x,y,VERDE))
        mapa.append(fila)

    # Crear relieves aleatorios
    cantRelieves = 300
    for _ in range(cantRelieves): # Crea x cantidad de relieves aleatorios
        x = random.randint(0, cantCasillasX - 1)
        y = random.randint(0, cantCasillasY - 1)
        color = random.choice([AGUA, ROCA, ARENA, MONTAÑA])
        mapa[x][y].tipo_terreno = color
        
    #traigo el numero del refugio creado en el main
    
    
    #Cargar personajes desde JSON
    #Como prueba solo conecta con Refugio1 en duro
    ruta_personajes = f"saves/Refugio{numRefugio}/personajes.json"

    personajes = [] #Lista dinámica de personajes dentro del mapa
    try:
        with open(ruta_personajes, "r") as file:
            datos = json.load(file)
        for p in datos:
            # ** agarra todos los atributos del personajes
            atributos = Atributos(**p['atributos'])
            arma = Arma(0, '', p['arma']['nombre'], 0, '', '', 0, 0, '', 0, 0, 0, 0, '', '')
            personaje = Personaje(p['nombre'], p['vida'], p['clase'], atributos, arma, 0)
            personajes.append(personaje)

        # Posicionar personajes en el mapa de manera aleatoria
        for personaje in personajes:
            while True:
                x = random.randint(0, cantCasillasX - 1)
                y = random.randint(0, cantCasillasY - 1)
                if mapa[x][y].objeto is None:
                    mapa[x][y].objeto = personaje
                    break
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta_personajes}")
        personajes = []

    # Bucle principal
    running = True 
    while running: # mientras se esté ejecutando
        screen.fill((0,0,0)) # se llena la pantalla de color negro

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Si le doy a la x se cierra
                running = False

        # Dibujar el mapa
        for fila in mapa:
            for celda in fila:
                # Dibuja el rectángulo de color del terreno
                pygame.draw.rect(screen, celda.tipo_terreno,
                                 (celda.x * TILE_SIZE, celda.y * TILE_SIZE,
                                  TILE_SIZE, TILE_SIZE))

                # Dibuja el borde negro alrededor de la celda
                pygame.draw.rect(screen, (0, 0, 0),
                                 (celda.x * TILE_SIZE, celda.y * TILE_SIZE,
                                  TILE_SIZE, TILE_SIZE), 1)  # El último "1" es el grosor del borde

                # Dibujar personajes si es que existe
                if celda.objeto and isinstance(celda.objeto, Personaje):
                    pygame.draw.circle(screen, (255, 0, 0),
                                       (celda.x * TILE_SIZE + TILE_SIZE // 2,
                                        celda.y * TILE_SIZE + TILE_SIZE // 2),
                                       TILE_SIZE // 3)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

# Ejecutar la función solo si el archivo es el principal
if __name__ == "__main__":
    iniciarMapa()
