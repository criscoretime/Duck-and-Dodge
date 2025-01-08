import pygame
import random

class ObjetoCayendo:
    def __init__(self, ruta_imagen, bueno, especial, ancho_pantalla, alto_pantalla, dificultad):
        self.objeto = pygame.image.load(ruta_imagen).convert_alpha()
        self.objeto = pygame.transform.scale(self.objeto, (35, 35)) 

        self.rect = self.objeto.get_rect()
        self.rect.x = random.randint(0, ancho_pantalla - self.rect.width)
        self.rect.y = random.randint(-alto_pantalla, -20) 

        self.velocidad = random.randint(2, 5) if dificultad == "Normal" else random.randint(8, 12)

        self.bueno = bueno
        self.especial = especial

    def actualizar(self):
        self.rect.y += self.velocidad

    def dibujar(self, pantalla):
        pantalla.blit(self.objeto, self.rect)
