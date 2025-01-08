import pygame

class Jugador:
    def __init__(self, ancho_pantalla, alto_pantalla, ruta_imagen):
        # Inicializa las propiedades del jugador
        self.ancho_pantalla = ancho_pantalla  # Ancho de la pantalla
        self.alto_pantalla = alto_pantalla  # Alto de la pantalla

        # Carga la imagen del jugador y la ajusta al tamaño deseado
        self.imagen = pygame.image.load(ruta_imagen).convert_alpha()  # Carga la imagen con transparencia
        self.imagen = pygame.transform.scale(self.imagen, (60, 60))  # Redimensiona a 60x60 píxeles

        # Define el rectángulo que representa al jugador en la pantalla
        self.rect = self.imagen.get_rect()
        self.rect.center = (ancho_pantalla // 2, alto_pantalla // 2)  # Posición inicial en el centro

        # Velocidad de movimiento del jugador
        self.velocidad = 10

    def mover(self, teclas):
        # Controla el movimiento del jugador con las teclas de dirección
        if teclas[pygame.K_LEFT] and self.rect.left > 0:  # Movimiento a la izquierda
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.rect.right < self.ancho_pantalla:  # Movimiento a la derecha
            self.rect.x += self.velocidad
        if teclas[pygame.K_UP] and self.rect.top > 0:  # Movimiento hacia arriba
            self.rect.y -= self.velocidad
        if teclas[pygame.K_DOWN] and self.rect.bottom < self.alto_pantalla:  # Movimiento hacia abajo
            self.rect.y += self.velocidad

    def dibujar(self, pantalla):
        # Dibuja la imagen del jugador en la pantalla en su posición actual
        pantalla.blit(self.imagen, self.rect)
