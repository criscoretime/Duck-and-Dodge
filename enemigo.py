import pygame
import random

class Enemigo:
    def __init__(self, ancho_pantalla, alto_pantalla, ruta_imagen):
        # Inicializa las propiedades del enemigo
        self.ancho_pantalla = ancho_pantalla
        self.alto_pantalla = alto_pantalla

        # Carga la imagen original y crea versiones escaladas
        self.imagen_original = pygame.image.load(ruta_imagen).convert_alpha()
        self.tamano = 40  # Tamaño inicial del enemigo
        self.imagenes_escaladas = [
            pygame.transform.smoothscale(self.imagen_original, (t, t)) for t in range(40, 500, 5)
        ]

        # Establece la imagen inicial y posición aleatoria
        self.imagen = self.imagenes_escaladas[(self.tamano - 40) // 5]
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randint(0, ancho_pantalla - self.tamano)
        self.rect.y = random.randint(0, alto_pantalla - self.tamano)

        # Velocidades iniciales y control de cambio de dirección
        self.velocidad_x = random.choice([-3, 3])
        self.velocidad_y = random.choice([-3, 3])
        self.cambio_velocidad_intervalo = 100  # Ciclos para cambiar la velocidad
        self.ciclos = 0  # Contador de ciclos

    def mover(self):
        # Actualiza la posición del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Rebota en los bordes de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocidad_x = -self.velocidad_x
        if self.rect.right > self.ancho_pantalla:
            self.rect.right = self.ancho_pantalla
            self.velocidad_x = -self.velocidad_x
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocidad_y = -self.velocidad_y
        if self.rect.bottom > self.alto_pantalla:
            self.rect.bottom = self.alto_pantalla
            self.velocidad_y = -self.velocidad_y

        # Cambia la velocidad cada cierto número de ciclos
        self.ciclos += 1
        if self.ciclos >= self.cambio_velocidad_intervalo:
            self.cambiar_velocidad()
            self.ciclos = 0

    def cambiar_velocidad(self):
        # Cambia las velocidades a valores aleatorios
        self.velocidad_x = random.choice([-5, -4, -3, 3, 4, 5])
        self.velocidad_y = random.choice([-5, -4, -3, 3, 4, 5])

    def aumentar_tamano(self):
        # Aumenta el tamaño del enemigo y actualiza la imagen
        self.tamano += 5
        indice = min(len(self.imagenes_escaladas) - 1, (self.tamano - 40) // 5)
        self.imagen = self.imagenes_escaladas[indice]
        centro_actual = self.rect.center  # Mantiene el centro al cambiar de tamaño
        self.rect = self.imagen.get_rect(center=centro_actual)

    def reducir_tamano(self, cantidad):
        # Reduce el tamaño del enemigo y actualiza la imagen
        self.tamano = max(40, self.tamano - cantidad)  # Tamaño mínimo de 40
        indice = min(len(self.imagenes_escaladas) - 1, (self.tamano - 40) // 5)
        self.imagen = self.imagenes_escaladas[indice]
        centro_actual = self.rect.center  # Mantiene el centro al cambiar de tamaño
        self.rect = self.imagen.get_rect(center=centro_actual)

    def dibujar(self, pantalla):
        # Dibuja el enemigo en la pantalla
        pantalla.blit(self.imagen, self.rect)
