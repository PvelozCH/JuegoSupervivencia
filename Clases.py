import random
import json

#Clase PERSONAJE
class Personaje:
    def __init__(self, nombre, vida, clase,atributos,arma,inventario):
        self.nombre = nombre
        self.vida = vida
        self.clase = clase
        self.atributos=atributos
        self.arma=arma
        self.inventario=inventario
        
         #Se define el arma aleatoriamente 
    def setArmaAleatoria(self):
    	#Primero abre el json que contiene los nombres:
    	   with open('Armas.json', 'r') as file:
    	      armas= json.load(file)
    	      # se asignan los nombres aleatorios:
    	      aleatorio = random.choice(armas)
    	      nomA= aleatorio['nombre']
    	      self.arma.nombre = nomA
        
        #Se definen sus atributos de manera aleatoria
    def setAtributos(self):
    	self.atributos.strenght = random.randint(1,5)+5
    	self.atributos.perception =random.randint(1,5)+5
    	self.atributos.endurance=random.randint(1,5)+5
    	self.atributos.carisma=random.randint(1,5)+5
    	self.atributos.inteligence=random.randint(1,5)+5
    	self.atributos.luck=random.randint(1,5)+5
    	
    	#Se define su nombre aleatoriamente
    def setNombreAleatorio(self):
    	#Primero abre el json que contiene los nombres:
    	   with open('NombresApellidos.json', 'r') as file:
    	      nombres= json.load(file)
    	      # se asignan los nombres aleatorios:
    	      aleatorio = random.choice(nombres)
    	      nomJ = aleatorio['nombre']
    	      apJ = aleatorio['apellido']
    	      
    	      self.nombre = nomJ+" "+apJ
    	      
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'vida': self.vida,
            'clase': self.clase,
            'atributos': {
                'strenght': self.atributos.strenght,
                'perception': self.atributos.perception,
                'endurance': self.atributos.endurance,
                'carisma': self.atributos.carisma,
                'inteligence': self.atributos.inteligence,
                'luck': self.atributos.luck
            },
            'arma': {
                'nombre': self.arma.nombre
            }
        }
    	      
    	
    def __str__(self):
        return f"******\nPersonaje:\nNombre={self.nombre}\nVida={self.vida}\nClase={self.clase}\nAtributos={self.atributos}\nArma={self.arma.nombre}"
 
        
#Clase Ambiente
class Ambiente:
	def __init__(self, nombre, visibilidad,temperatura):
		self.nombre=nombre
		self.visibilidad=visibilidad
		self.temperatura=temperatura
		
#Clase ATRIBUTOS
class Atributos:
	def __init__(self, strength,perception,endurance,carisma,inteligence,luck):
		self.strenght=strength
		self.perception=perception
		self.endurance=endurance
		self.carisma=carisma
		self.inteligence=inteligence
		self.luck=luck
	def __str__(self):
		return f"\n~Strenght={self.strenght}\n~Perception={self.perception}\n~Endurance={self.endurance}\n~Carisma={self.carisma}\n~Inteligence={self.inteligence}\n~Luck={self.luck}"
		
#Clase ARMA
class Arma:
    def __init__(self, id, tipo, nombre, daño, descripcion, tipo_municion, peso, durabilidad, modificaciones, nivel_requerido, precio, rango, velocidad_disparo, rareza, efecto_especial):
        self.id = id
        self.tipo = tipo
        self.nombre = nombre
        self.daño = daño
        self.descripcion = descripcion
        self.tipo_municion = tipo_municion
        self.peso = peso
        self.durabilidad = durabilidad
        self.modificaciones = modificaciones
        self.nivel_requerido = nivel_requerido
        self.precio = precio
        self.rango = rango
        self.velocidad_disparo = velocidad_disparo
        self.rareza = rareza
        self.efecto_especial = efecto_especial
        
    def __str__(self):
        return (f"Arma:\n"
                f"  id: {self.id}\n"
                f"  tipo: {self.tipo}\n"
                f"  nombre: {self.nombre}\n"
                f"  daño: {self.daño}\n"
                f"  descripcion: {self.descripcion}\n"
                f"  tipo_municion: {self.tipo_municion}\n"
                f"  peso: {self.peso}\n"
                f"  durabilidad: {self.durabilidad}\n"
                f"  modificaciones: {self.modificaciones}\n"
                f"  nivel_requerido: {self.nivel_requerido}\n"
                f"  precio: {self.precio}\n"
                f"  rango: {self.rango}\n"
                f"  velocidad_disparo: {self.velocidad_disparo}\n"
                f"  rareza: {self.rareza}\n"
                f"  efecto_especial: {self.efecto_especial}")
                
		
#Clase ITEM
class Item:
	def __init__(self,nombre,descripcion,precio):
		self.nombre=nombre
		self.descripcion=descripcion
		self.precio=precio