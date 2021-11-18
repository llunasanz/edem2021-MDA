# -*- coding: utf-8 -*-
# Se recomienda trabajar con distintos módulos.

# Para ampliar: buscar para descargar el vídeo y convertirlo en mp3 con otra librería.
import pygame

pygame.mixer.init()

class Animal():
    edad:int
    nPatas:int
    ruido:str
    nombre:str
    kgComida: int

    def __init__(self, nombre, edad, nPatas, ruido, kgComida):
        self.edad = edad
        self.nPatas = nPatas
        self.ruido = ruido
        self.nombre = nombre
        self.kgComida = kgComida
        
    def hacerRuido(self):
        if(self.ruido == "guau"):
            pygame.mixer.music.load(f"{self.ruido}.mp3")
            pygame.mixer.music.play()
        elif(self.ruido == "mercado" or self.nombre == "Rodrigo Rato"):
            pygame.mixer.music.load(f"{self.ruido}.mp3")
            pygame.mixer.music.play()
        elif(self.ruido == "kekw"):
            pygame.mixer.music.load(f"{self.ruido}.mp3")
            pygame.mixer.music.play()
        else:
            print(f'Hola me llamo {self.nombre}  tengo {self.edad} años, tengo {self.nPatas} patas y hago {self.ruido}.')


class Carnivoro(Animal):
    comida : str = "carne"
    def __init__(self, nombre, edad, nPatas, ruido, kgComida):
        super(Carnivoro, self).__init__(nombre, edad, nPatas, ruido, kgComida)
    
    def comer(self, kilos):
        if(kilos <= self.kgComida):
            print(f'{self.nombre} ha comido {kilos} kilos de {self.comida}.')
            self.kgComida -= kilos
        else:
            print(f"No hay comida suficiente para {self.nombre}. ¡Ponle comida!")


class Herbivoro(Animal):
    comida : str = "vegetales"
    def __init__(self, nombre, edad, nPatas, ruido, kgComida):
        super(Herbivoro, self).__init__(nombre, edad, nPatas, ruido, kgComida)
    
    def comer(self, kilos):
        if(kilos <= self.kgComida):
            print(f'{self.nombre} ha comido {kilos} kilos de {self.comida}.')
            self.kgComida -= kilos
        else:
            print(f'No hay comida suficiente para {self.nombre}. ¡Ponle comida!')


class Omnivoro(Carnivoro, Herbivoro):
    comida : str = "carne y vegetales"


miLeon = Carnivoro("Simba", 10, 4, "rugido", 40)
print(miLeon.nombre)
miLeon.hacerRuido()
miPerro = Omnivoro("Pancho", 15, 4, "guau", 5)
print(miPerro.nombre)
miPerro.hacerRuido()
