import pygame
import random

# Configuración inicial
WIDTH, HEIGHT = 800, 600
FPS = 60
TILE_SIZE = 40
ROWS, COLS = HEIGHT // TILE_SIZE, WIDTH // TILE_SIZE

# Colores
GREEN = (34, 139, 34)
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Clases
class Entity:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

class Player(Entity):
    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  self.x = max(0, self.x - 1)
        if keys[pygame.K_RIGHT]: self.x = min(COLS - 1, self.x + 1)
        if keys[pygame.K_UP]:    self.y = max(0, self.y - 1)
        if keys[pygame.K_DOWN]:  self.y = min(ROWS - 1, self.y + 1)

class Enemy(Entity):
    def move_random(self):
        dx, dy = random.choice([(1,0), (-1,0), (0,1), (0,-1), (0,0)])
        self.x = max(0, min(COLS - 1, self.x + dx))
        self.y = max(0, min(ROWS - 1, self.y + dy))

class Object(Entity):
    pass

# Crear jugador, enemigos y objetos
player = Player(5, 5, BLUE)
enemies = [Enemy(random.randint(0, COLS-1), random.randint(0, ROWS-1), RED) for _ in range(5)]
objects = [Object(random.randint(0, COLS-1), random.randint(0, ROWS-1), YELLOW) for _ in range(8)]

# Bucle principal
running = True
while running:
    clock.tick(FPS)
    screen.fill(GREEN)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar
    player.handle_keys()
    for enemy in enemies:
        enemy.move_random()

    # Dibujar mapa de cuadrícula
    for x in range(0, WIDTH, TILE_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

    # Dibujar entidades
    player.draw()
    for obj in objects:
        obj.draw()
    for enemy in enemies:
        enemy.draw()

    # Actualizar pantalla
    pygame.display.flip()

pygame.quit()
