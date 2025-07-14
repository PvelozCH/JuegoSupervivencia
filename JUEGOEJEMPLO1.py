import pygame
import random

# Inicializar Pygame
pygame.init()
pixelesX = 800
pixelesY = 600
screen = pygame.display.set_mode((pixelesX, pixelesY)) #800 x 600 pixeles.
clock = pygame.time.Clock()

TILE_SIZE = 6 #Tamaño de cada cuadro.

## Cantidad de casillas por ancho y por largo
cantCasillasX = int((pixelesX/TILE_SIZE)-1)
cantCasillasY = int((pixelesY/TILE_SIZE)-1)


# Colores de cada cuadro. (RGB)
VERDE = (34, 139, 34)     # Terreno base
AGUA = (0, 191, 255)
ROCA = (120, 120, 120)
ARENA = (200, 200, 50)
MONTAÑA = (139, 69, 19)

# Elementos del mapa (x, y, color)
relieves = []

# Crear relieves aleatorios
cantRelieves = 780
for _ in range(cantRelieves): # Crea x cantidad de relieves aleatorios
    x = random.randint(0, cantCasillasX)
    y = random.randint(0, cantCasillasY)
    color = random.choice([AGUA, ROCA, ARENA, MONTAÑA])
    relieves.append((x, y, color))

# Bucle principal
running = True 
while running: # mientras se esté ejecutando
    screen.fill(VERDE) # se llena la pantalla de color verde

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Si le doy a la x se cierra
            running = False

    # Dibujar cuadrícula
    for x in range(0, pixelesX, TILE_SIZE):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, 600))
    for y in range(0, pixelesY, TILE_SIZE):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (800, y))

    # Dibujar relieves
    for x, y, color in relieves:
        pygame.draw.rect(screen, color, (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
