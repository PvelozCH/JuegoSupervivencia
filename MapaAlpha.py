import turtle
import random

# Configuración de la pantalla
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Mapa del Juego")


# Configuración del tamaño de la pantalla
screen.setup(width=600, height=600)

# Creación del punto negro (personaje)
player = turtle.Turtle()
player.shape("circle")
player.color("red")
player.penup()

# Posición inicial del personaje
player.setposition(0, 0)  # Centro del plano cartesiano

# Función para dibujar los ejes
def dibujar_ejes():
    eje = turtle.Turtle()
    eje.speed(0)  # Dibujo instantáneo
    eje.color("green")
    eje.penup()
    eje.hideturtle()
    
    # Dibujar eje X
    eje.setposition(-400, 0)
    eje.pendown()
    eje.setposition(400, 0)
    eje.penup()
    
    # Dibujar eje Y
    eje.setposition(0, -400)
    eje.pendown()
    eje.setposition(0, 400)
    eje.penup()

# Función para dibujar la cuadrícula
def dibujar_cuadricula():
    cuadricula = turtle.Turtle()
    cuadricula.speed(0)  # Dibujo instantáneo
    cuadricula.color("green")
    cuadricula.penup()
    cuadricula.hideturtle()
    
    # Líneas verticales
    for x in range(-400, 401, 20):
        cuadricula.setposition(x, -400)
        cuadricula.pendown()
        cuadricula.setposition(x, 400)
        cuadricula.penup()
    
    # Líneas horizontales
    for y in range(-400, 401, 20):
        cuadricula.setposition(-400, y)
        cuadricula.pendown()
        cuadricula.setposition(400, y)
        cuadricula.penup()

# Función para mover el punto de manera aleatoria
def mover_aleatorio():
    x_move = random.choice([-20, 0, 20])
    y_move = random.choice([-20, 0, 20])
    
    new_x = player.xcor() + x_move
    new_y = player.ycor() + y_move

    # Asegurar que el punto no salga de los límites del mapa
    if -400 <= new_x <= 400 and -400 <= new_y <= 400:
        player.setposition(new_x, new_y)

    # Volver a llamar a esta función después de 250 milisegundos
    turtle.ontimer(mover_aleatorio, 200)
    
    #Agregar texto
def agregar_texto(texto):
    texto_turtle = turtle.Turtle()
    texto_turtle.speed(0)
    texto_turtle.color("green")
    texto_turtle.penup()
    texto_turtle.hideturtle()
    
    # Posición del texto
    texto_turtle.setposition(0, -525)
    texto_turtle.write(texto, align="center", font=("Arial", 10, "normal"))

#Escribir texto
agregar_texto("Este es un texto de ejemplo ")
# Dibujar los ejes y la cuadrícula
dibujar_ejes()
dibujar_cuadricula()

# Comenzar a mover el punto de manera aleatoria
mover_aleatorio()

# Mantener la ventana abierta
turtle.done()