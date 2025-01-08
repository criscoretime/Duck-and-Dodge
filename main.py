
# Autor: Johann Orjuela

from juego import Juego

# Punto de entrada del programa
if __name__ == "__main__":
    while True:  # Bucle principal para reiniciar el juego tras perder
        # Crea una instancia de la clase Juego
        juego = Juego()

        # Ejecuta el juego
        juego.ejecutar()
