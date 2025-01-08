import pygame
import sys

class Menu:
    def __init__(self, pantalla, fuente, ancho_pantalla, alto_pantalla):
        # Inicializa las propiedades del menú
        self.pantalla = pantalla  
        self.fuente = fuente 
        self.ancho_pantalla = ancho_pantalla  
        self.alto_pantalla = alto_pantalla  

    def mostrar_menu(self):
        # Bucle principal del menú
        while True:
            self.pantalla.fill((255, 255, 255))  # Fondo blanco

            # Títulos y opciones del menú
            titulo = self.fuente.render("Duck and Dodge", True, (0, 0, 0))
            texto = self.fuente.render("Presione el número indicado para cada opción", True, (0, 0, 0))
            jugar_normal = self.fuente.render("1. Jugar (Normal)", True, (0, 0, 0))
            jugar_dificil = self.fuente.render("2. Jugar (Difícil)", True, (0, 0, 0))
            instrucciones = self.fuente.render("3. Instrucciones", True, (0, 0, 0))
            salir = self.fuente.render("4. Salir", True, (0, 0, 0))

            # Mostrar texto en pantalla, centrado
            self.pantalla.blit(titulo, (self.ancho_pantalla // 2 - titulo.get_width() // 2, 100))
            self.pantalla.blit(texto, (self.ancho_pantalla // 3 - titulo.get_width(), 150))
            self.pantalla.blit(jugar_normal, (self.ancho_pantalla // 2 - jugar_normal.get_width() // 2, 200))
            self.pantalla.blit(jugar_dificil, (self.ancho_pantalla // 2 - jugar_dificil.get_width() // 2, 250))
            self.pantalla.blit(instrucciones, (self.ancho_pantalla // 2 - instrucciones.get_width() // 2, 300))
            self.pantalla.blit(salir, (self.ancho_pantalla // 2 - salir.get_width() // 2, 350))

            pygame.display.flip()  # Actualiza la pantalla

            # Manejar eventos del menú
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Salir del juego
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    # Selección de opciones
                    if evento.key == pygame.K_1:
                        return "Normal"  # Jugar en dificultad Normal
                    elif evento.key == pygame.K_2:
                        return "Difícil"  # Jugar en dificultad Difícil
                    elif evento.key == pygame.K_3:
                        self.mostrar_instrucciones()  # Muestra las instrucciones
                    elif evento.key == pygame.K_4:
                        pygame.quit()  # Salir del juego
                        sys.exit()

    def mostrar_instrucciones(self):
        # Bucle para mostrar la pantalla de instrucciones
        while True:
            self.pantalla.fill((255, 255, 255))  # Fondo blanco

            # Instrucciones del juego
            titulo = self.fuente.render("Instrucciones", True, (0, 0, 0))
            linea1 = self.fuente.render("1. Usa las flechas de dirección para mover al pato.", True, (0, 0, 0))
            linea2 = self.fuente.render("2. Recolecta gusanos verdes para ganar puntos.", True, (0, 0, 0))
            linea3 = self.fuente.render("3. Evita los huesos, harán crecer al perro.", True, (0, 0, 0))
            linea4 = self.fuente.render("4. Recolecta pelotas para reducir el tamaño del perro.", True, (0, 0, 0))
            regresar = self.fuente.render("Presiona M para volver al menú.", True, (0, 0, 0))

            # Mostrar instrucciones en pantalla
            self.pantalla.blit(titulo, (self.ancho_pantalla // 2 - titulo.get_width() // 2, 50))
            self.pantalla.blit(linea1, (50, 150))
            self.pantalla.blit(linea2, (50, 200))
            self.pantalla.blit(linea3, (50, 250))
            self.pantalla.blit(linea4, (50, 300))
            self.pantalla.blit(regresar, (self.ancho_pantalla // 2 - regresar.get_width() // 2, 400))

            pygame.display.flip()  # Actualiza la pantalla

            # Manejar eventos para volver al menú
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Salir del juego
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_m:  # Regresar al menú
                    return
