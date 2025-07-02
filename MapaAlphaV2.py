import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mapa del Juego")

# Color de fondo
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Función para dibujar los ejes
def draw_axes():
    pygame.draw.line(screen, WHITE, (width // 2, 0), (width // 2, height))
    pygame.draw.line(screen, WHITE, (0, height // 2), (width, height // 2))

# Función para dibujar la cuadrícula
def draw_grid():
    for x in range(-400, 401, 20):
        pygame.draw.line(screen, GREEN, (width // 2 + x, 0), (width // 2 + x, height))
    for y in range(-400, 401, 20):
        pygame.draw.line(screen, GREEN, (0, height // 2 + y), (width, height // 2 + y))

# Crear el reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Posición inicial del personaje
player_pos = [width // 2, height // 2]

# Velocidad de movimiento del personaje
speed = 20

# Texto del menú
menu_font = pygame.font.SysFont(None, 30)
menu_text = [
    "1) Ejemplo 1",
    "2) Ejemplo 2",
    "3) Ejemplo 3"
]

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar el fondo negro
    screen.fill(BLACK)

    # Dibujar los ejes y la cuadrícula
    draw_axes()
    draw_grid()

    # Dibujar el personaje
    pygame.draw.circle(screen, (255, 0, 0), player_pos, 10)

    # Dibujar el menú de texto
    for i, text in enumerate(menu_text):
        text_render = menu_font.render(text, True, GREEN)
        screen.blit(text_render, (10, height - 30 * (i + 1)))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    clock.tick(10)