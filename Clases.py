import random
import json


#Clase AgenteVivo, padre de Personaje y de Criatura (y de otras futuras clases)
class AgenteVivo:
      def __init__(self,nombre,vida,atributos,inventario,hambre,sed,energia,estado,memoria,nivelEstres,fatiga,edad,reproduccion,sexo,alimentacion):
            self.nombre = nombre
            self.vida = vida
            self.atributos = atributos
            self.inventario = inventario
            self.hambre = hambre
            self.sed = sed
            self.energia = energia
            self.estado = estado
            self.memoria = memoria
            self.nivelEstres = nivelEstres
            self.fatiga = fatiga
            self.edad = edad
            self.reproduccion = reproduccion
            self.sexo = sexo
            self.alimentacion = alimentacion

    

#Clase PERSONAJE
class Personaje(AgenteVivo):
    def __init__(self,nombre,vida,atributos,inventario,hambre,sed,energia,estado,memoria,nivelEstres,fatiga,edad,reproduccion,sexo,alimentacion,arma):
        super().__init__(nombre,vida,atributos,inventario,hambre,sed,energia,estado,memoria,nivelEstres,fatiga,edad,reproduccion,sexo,alimentacion)
        self.arma=arma
        
         #Se define el arma aleatoriamente 
    def setArmaAleatoria(self):
        with open('Armas.json', 'r') as file:
             armas = json.load(file)
             aleatorio = random.choice(armas)
             nomA = aleatorio['nombre']
             self.arma = Arma(0, '', nomA, 0, '', '', 0, 0, '', 0, 0, 0, 0, '', '')
        
        #Se definen sus atributos de manera aleatoria
    def setAtributos(self):
        self.atributos.strenght = random.randint(1,5)+5
        self.atributos.perception =random.randint(1,5)+5
        self.atributos.endurance=random.randint(1,5)+5
        self.atributos.carisma=random.randint(1,5)+5
        self.atributos.inteligence=random.randint(1,5)+5
        self.atributos.luck=random.randint(1,5)+5
    	
    def setSexoAleatorio(self,cont,contMujeres):
          numSexo = random.randint(1,2)
          if numSexo == 1:
                self.sexo = "Masculino"
          else:
                self.sexo = "Femenino"

          #Si se crearon 5 personajes hombres, entonces que la ultima sea si o si mujer
          if cont == 5 and contMujeres == 0:
                self.sexo = "Femenino" 
          
          #Si se crearon 5 personajes mujeres, entonces que el ultimo sea si o si hombre
          if contMujeres == 5:
                self.sexo = "Masculino"
          return numSexo
        
    	#Se define su nombre aleatoriamente dependiendo de su sexo
    def setNombreAleatorio(self,sexo):
          nombre = ""
          apellido = ""

          if sexo == "Masculino":
                with open('nombresMasculinos.json', 'r') as file:
                    nombres= json.load(file)
                    aleatorio = random.choice(nombres)
                    nombre = aleatorio['nombre']
          else:
               with open('nombresFemeninos.json','r') as file:
                    nombres= json.load(file)
                    aleatorio = random.choice(nombres)
                    nombre = aleatorio['nombre']

          with open('apellidos.json','r') as file:
                    apellidos= json.load(file)
                    aleatorio = random.choice(apellidos)
                    apellido = aleatorio['apellido']
          
          self.nombre = nombre + " " + apellido
    	      
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'vida': self.vida,
            'atributos': {
                'strenght': self.atributos.strenght,
                'perception': self.atributos.perception,
                'endurance': self.atributos.endurance,
                'carisma': self.atributos.carisma,
                'inteligence': self.atributos.inteligence,
                'luck': self.atributos.luck
            },
            'hambre': self.hambre,
            'sed': self.sed,
            'energia': self.energia,
            'estado': self.estado,
            'memoria': self.memoria,
            'nivelEstres': self.nivelEstres,
            'fatiga': self.fatiga,
            'edad':self.edad,
            'reproduccion':self.reproduccion,
            'sexo': self.sexo,
            'alimentacion' : self.alimentacion,
            'arma': {
                'nombre': self.arma.nombre
            }
        }
    
    def __str__(self):
         return f"Nombre: {self.nombre}, Vida: {self.vida}, Sexo: {self.sexo}, Arma: {self.arma.nombre}"

    
#Clase criatura o enemigo
class Criatura(AgenteVivo):
     def __init__(self,nombre,vida,atributos,inventario,hambre,sed,energia,estado,memoria,nivelEstres,fatiga,edad,reproduccion,sexo,alimentacion,arma):
        super().__init__(nombre,vida,atributos,inventario,hambre,sed,energia,estado,memoria,nivelEstres,fatiga,edad,reproduccion,sexo,alimentacion)
        self.arma=arma

     def setAtributos(self):
             self.atributos.strenght = random.randint(1,5)+5
             self.atributos.perception =random.randint(1,5)+5
             self.atributos.endurance=random.randint(1,5)+5
             self.atributos.carisma=random.randint(1,5)+5
             self.atributos.inteligence=random.randint(1,5)+5
             self.atributos.luck=random.randint(1,5)+5

     def setNombreAleatorio(self):
    	#Primero abre el json que contiene los nombres:
    	   with open('CriaturasEnemigos.json', 'r') as file:
            nombres= json.load(file)
            aleatorio = random.choice(nombres)
            nomJ = aleatorio['nombre']
            self.nombre = nomJ


     def to_dict(self):
             return {
            'nombre': self.nombre,
            'vida': self.vida,
            'atributos': {
                'strenght': self.atributos.strenght,
                'perception': self.atributos.perception,
                'endurance': self.atributos.endurance,
                'carisma': self.atributos.carisma,
                'inteligence': self.atributos.inteligence,
                'luck': self.atributos.luck
            },
            'hambre': self.hambre,
            'sed': self.sed,
            'energia': self.energia,
            'estado': self.estado,
            'memoria': self.memoria,
            'nivelEstres': self.nivelEstres,
            'fatiga': self.fatiga,
            'edad':self.edad,
            'reproduccion':self.reproduccion,
            'sexo': self.sexo,
            'alimentacion' : self.alimentacion,
            'arma': {
                'nombre': self.arma.nombre
            }
        }
     
     def __str__(self):
          return f"Nombre: {self.nombre}, Vida: {self.vida}, Sexo: {self.sexo}, Arma: {self.arma.nombre}"
        

#Clase ATRIBUTOS
class Atributos:
	def __init__(self, strenght,perception,endurance,carisma,inteligence,luck):
		self.strenght=strenght
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
        
#Clase de comidas
class Comida:
    def __init__(self,nombre,descripcion,cantCalorias):
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantCalorias = cantCalorias
        
        
        
#Clase Ambiente -- CLASE A USAR A FUTURO EN VERSIONES MEJORADAS
class Ambiente:
	def __init__(self, nombre, visibilidad,temperatura):
		self.nombre=nombre
		self.visibilidad=visibilidad
		self.temperatura=temperatura
        
        
#Clase de edificio
class Edificio:
    def __init__(self,nombre,color,numPisos,personaje,criatura,comida,item):
        self.nombre = nombre
        self.color = color
        self.numPisos = numPisos
        self.personaje = personaje
        self.criatura = criatura
        self.comida = comida
        self.item = item
