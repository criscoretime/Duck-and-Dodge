import pygame
import random
import sys
from jugador import Jugador
from objetoCayendo import ObjetoCayendo
from enemigo import Enemigo
from menu import Menu

class Juego:
    def __init__(self):
        pygame.init()
        # Configuración básica de la pantalla y del juego
        self.ANCHO_PANTALLA = 800
        self.ALTO_PANTALLA = 600
        self.FPS = 60
        self.pantalla = pygame.display.set_mode((self.ANCHO_PANTALLA, self.ALTO_PANTALLA))
        pygame.display.set_caption("Duck and Dodge")
        self.reloj = pygame.time.Clock()
        self.fuente = pygame.font.Font(None, 36)

        # Cargar fondo del juego
        self.fondo = pygame.image.load("Duck and Dodge/media/fondo.png").convert()

        # Inicializar y reproducir música de fondo
        pygame.mixer.init()
        pygame.mixer.music.load("Duck and Dodge/media/musica_fondo.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        # Mostrar menú y seleccionar dificultad
        menu = Menu(self.pantalla, self.fuente, self.ANCHO_PANTALLA, self.ALTO_PANTALLA)
        self.dificultad = menu.mostrar_menu()

        # Inicializar jugador, enemigo y lista de objetos
        self.jugador = Jugador(self.ANCHO_PANTALLA, self.ALTO_PANTALLA, "Duck and Dodge/media/pato.png")
        self.enemigo = Enemigo(self.ANCHO_PANTALLA, self.ALTO_PANTALLA, "Duck and Dodge/media/perroredime.png")
        self.objetos = []
        self.puntuacion = 0

    def generar_objetos(self):
        # Generar gusanos 
        if random.randint(1, 40) == 1:
            self.objetos.append(ObjetoCayendo(
                "Duck and Dodge/media/gusano.png", bueno=True, especial=False,
                ancho_pantalla=self.ANCHO_PANTALLA,
                alto_pantalla=self.ALTO_PANTALLA,
                dificultad=self.dificultad
            ))

        # Generar huesos 
        if random.randint(1, 20) == 1:
            self.objetos.append(ObjetoCayendo(
                "Duck and Dodge/media/hueso.png", bueno=False, especial=False,
                ancho_pantalla=self.ANCHO_PANTALLA,
                alto_pantalla=self.ALTO_PANTALLA,
                dificultad=self.dificultad
            ))

        # Generar pelotas 
        if random.randint(1, 200) == 1:
            self.objetos.append(ObjetoCayendo(
                "Duck and Dodge/media/pelota.png", bueno=True, especial=True,
                ancho_pantalla=self.ANCHO_PANTALLA,
                alto_pantalla=self.ALTO_PANTALLA,
                dificultad=self.dificultad
            ))

    def mostrar_pantalla_game_over(self):
        # Pantalla de Game Over con puntuación y opción de volver al menú
        while True:
            self.pantalla.fill((255, 255, 255))
            mensaje_perdio = self.fuente.render("¡Has perdido!", True, (255, 0, 0))
            mensaje_puntuacion = self.fuente.render(f"Puntuación final: {self.puntuacion}", True, (0, 0, 0))
            mensaje_volver_menu = self.fuente.render("Presiona M para volver al menú", True, (0, 0, 0))

            self.pantalla.blit(mensaje_perdio, (self.ANCHO_PANTALLA // 2 - mensaje_perdio.get_width() // 2, 150))
            self.pantalla.blit(mensaje_puntuacion, (self.ANCHO_PANTALLA // 2 - mensaje_puntuacion.get_width() // 2, 200))
            self.pantalla.blit(mensaje_volver_menu, (self.ANCHO_PANTALLA // 2 - mensaje_volver_menu.get_width() // 2, 250))

            pygame.display.flip()

            # Manejar eventos para volver al menú
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_m:
                        return

    def manejar_colisiones(self):
        # Verificar colisiones entre objetos y jugador/enemigo
        for obj in self.objetos[:]:
            obj.actualizar()
            if obj.rect.top > self.ALTO_PANTALLA:
                self.objetos.remove(obj)  # Eliminar objetos que salen de la pantalla
            elif obj.rect.colliderect(self.jugador.rect):
                # Colisiones con el jugador
                if obj.especial:  # Objeto especial
                    self.enemigo.reducir_tamano(10)
                elif obj.bueno:  # Objeto bueno
                    self.puntuacion += 1
                else:  # Objeto malo
                    self.enemigo.aumentar_tamano()
                    self.enemigo.cambiar_velocidad()
                self.objetos.remove(obj)
            elif obj.rect.colliderect(self.enemigo.rect):
                # Colisiones con el enemigo
                if not obj.bueno and not obj.especial:
                    self.enemigo.aumentar_tamano()
                self.objetos.remove(obj)

        # Verificar colisión entre el jugador y el enemigo
        if self.jugador.rect.colliderect(self.enemigo.rect):
            self.mostrar_pantalla_game_over()
            return "menu"

    def ejecutar(self):
        # Bucle principal del juego
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            teclas = pygame.key.get_pressed()
            self.jugador.mover(teclas)
            self.enemigo.mover()
            self.generar_objetos()
            resultado = self.manejar_colisiones()

            if resultado == "menu":  # Si el jugador pierde, volver al menú
                return

            # Dibujar fondo, jugador, enemigo y objetos
            self.pantalla.blit(self.fondo, (0, 0))
            self.jugador.dibujar(self.pantalla)
            self.enemigo.dibujar(self.pantalla)

            for obj in self.objetos:
                obj.dibujar(self.pantalla)

            # Mostrar la puntuación
            texto_puntuacion = self.fuente.render(f"Puntuación: {self.puntuacion}", True, (0, 0, 0))
            self.pantalla.blit(texto_puntuacion, (10, 10))

            pygame.display.flip()
            self.reloj.tick(self.FPS)
