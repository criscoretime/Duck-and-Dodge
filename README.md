Duck and Dodge 🦆🐶

Un divertido juego donde controlas a un pato que debe recolectar gusanos mientras esquivas huesos y evitas a un perro enemigo. ¡Recoge pelotas para reducir el tamaño del perro y consigue la mayor puntuación posible!

---

🎮 Descripción del Proyecto

En este juego arcade, tu objetivo es recolectar gusanos verdes para aumentar tu puntuación y sobrevivir tanto como puedas. Sin embargo, debes esquivar los huesos, ya que estas hacen crecer al perro enemigo. También puedes recolectar pelotas para reducir su tamaño y darte más tiempo para escapar.

---

🚀 Instalación

Sigue estos pasos para instalar y ejecutar el proyecto:

Requisitos
1. Python 3.8+ instalado en tu sistema.
2. Instala la biblioteca `pygame` ejecutando en la consola del sistema(CMD):
   
   pip install pygame
   

Pasos

1. Descarga el proyecto o clona el repositorio(CMD):
   
   git clone https://github.com/criscoretime/duck-and-dodge.git
   cd duck-and-dodge
   
2. Ejecuta el archivo principal para iniciar el juego(CMD):
   
   python main.py
   

---

🕹️ Controles

- Flechas de dirección: Mueve al pato en todas las direcciones.
- Tecla `M`: Vuelve al menú principal desde la pantalla de derrota.
- Teclas `1`,`2`,`3`,`4`: Para el control del menu principal.

---

📂 Estructura del Proyecto

```
duck-and-dodge/
├── media/               # Carpeta con las imágenes del juego
│   ├── fondo.png        # Imagen del fondo
│   ├── gusano.png       # Imagen de los gusanos
│   ├── hueso.png        # Imagen de los huesos 
│   ├── pato.png         # Imagen del pato (personaje) 
│   ├── pelota.png       # Imagen de las pelotas 
│   ├── perroredime.png  # Imagen del perro redimenzionado (enemigo)
│   └── musica_fondo.ogg # Música de fondo
│
├── main.py              # Archivo principal para iniciar el juego
├── juego.py             # Lógica principal del juego
├── jugador.py           # Clase del pato (jugador)
├── enemigo.py           # Clase del perro (enemigo)
├── objetoCayendo.py     # Clase de los objetos que caen
├── menu.py              # Menú principal del juego
└── README.md            # Descripción del proyecto
```

---

🛠️ Funcionalidades

**Elementos del Juego**

1. Pato (Jugador):
   - Controla al pato para recolectar gusanos y esquivar los peligros.

2. Perro (Enemigo):
   - Persigue al pato y crece al recolectar huesos. Su tamaño puede reducirse con pelotas.

3. Gusanos (Verdes):
   - Recolecta estos objetos para sumar puntos.

4. Hueso (Rojas):
   - Incrementan el tamaño del perro. ¡Evítalas!

5. pelotas (Grises):
   - Reducen el tamaño del perro para darte más tiempo.

 **Pantallas del Juego**

1. Menú Principal:
   - Selecciona la dificultad (`Normal` o `Difícil`), consulta las instrucciones o sal del juego.

2. Juego:
   - Controla al pato y recolecta objetos mientras esquivas al enemigo.

3. Pantalla de Derrota:
   - Muestra la puntuación final y permite volver al menú principal.

4. Instrucciones:
   - Explica cómo jugar y las funciones de cada objeto.

---

📧 Contacto

**Nombre:** [Johann Orjuela]  
**Correo:** [jorjuelah@unbosque.edu.co]  
**GitHub:** [criscoretime]  

¡Gracias por jugar Duck and Dodge! 🦆🐶
