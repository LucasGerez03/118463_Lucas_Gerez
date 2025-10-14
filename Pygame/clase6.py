# 🐍 Código del Snake en Pygame
import pygame
import random

# Inicializar pygame
pygame.init()

# Tamaño de la ventana
ANCHO, ALTO = 800, 500
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake en Python")

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)


# Tamaño del bloque
BLOQUE = 20

# Fuente
fuente = pygame.font.SysFont("arial", 25)

# Dibujar texto
def mostrar_mensaje(texto: str, color: tuple, pos: tuple):
    render = fuente.render(texto, True, color)
    ventana.blit(render, pos)

# Juego principal (recursivo en caso de perder)
def juego():
    # posición inicial de la serpiente
    serpiente = [[100, 100]]
    direccion = "DERECHA"
    comida = [random.randrange(0, ANCHO, BLOQUE), random.randrange(0, ALTO, BLOQUE)]
    reloj = pygame.time.Clock()
    puntaje = 0

    while True:
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_UP and direccion != "ABAJO":
            #         direccion = "ARRIBA"
            #     elif event.key == pygame.K_DOWN and direccion != "ARRIBA":
            #         direccion = "ABAJO"
            #     elif event.key == pygame.K_LEFT and direccion != "DERECHA":
            #         direccion = "IZQUIERDA"
            #     elif event.key == pygame.K_RIGHT and direccion != "IZQUIERDA":
            #         direccion = "DERECHA"

            
            pygame.key.set_repeat(100, 100)  
            keys = pygame.key.get_pressed() # Obtengo el estado de las teclas
            if keys[pygame.K_UP] and direccion != "ABAJO":
                direccion = "ARRIBA"
            elif keys[pygame.K_DOWN] and direccion != "ARRIBA": 
                direccion = "ABAJO"
            elif keys[pygame.K_LEFT] and direccion != "DERECHA":
                direccion = "IZQUIERDA"
            elif keys[pygame.K_RIGHT] and direccion != "IZQUIERDA":
                direccion = "DERECHA"                        

        # Mover serpiente
        cabeza = list(serpiente[-1])
        if direccion == "ARRIBA":
            cabeza[1] -= BLOQUE
        elif direccion == "ABAJO":
            cabeza[1] += BLOQUE
        elif direccion == "IZQUIERDA":
            cabeza[0] -= BLOQUE
        elif direccion == "DERECHA":
            cabeza[0] += BLOQUE

        serpiente.append(cabeza)

        # Comer comida
        if cabeza == comida:
            puntaje += 1
            comida = [random.randrange(0, ANCHO, BLOQUE), random.randrange(0, ALTO, BLOQUE)]
        else:
            serpiente.pop(0)  # eliminar cola

        # Revisar colisiones (paredes o cuerpo)
        if (cabeza in serpiente[:-1] or
            cabeza[0] < 0 or cabeza[0] >= ANCHO or
            cabeza[1] < 0 or cabeza[1] >= ALTO):
            # Recursividad para reiniciar
            return juego()

        # Dibujar
        ventana.fill(NEGRO)
        for x, y in serpiente:
            pygame.draw.rect(ventana, VERDE, (x, y, BLOQUE, BLOQUE))
        pygame.draw.rect(ventana, ROJO, (comida[0], comida[1], BLOQUE, BLOQUE))
        mostrar_mensaje(f"Puntos: {puntaje}", ROJO, (10, 10))
        pygame.display.flip()
        reloj.tick(10)
        
# Ejecutar
juego()


"""- Hacer pantalla de inicio con 4 botoones: "JUGAR", "MODO FACIL", "MODO NORMAL", "MODO IMPOSIBLE"
- Hacer pantalla de fin cuando pierda con mi puntaje y un botón para reiniciar

"""

"""
-tratar de modularizar 
pantalla inicio archivo
#muestro los 4 botones
-archivo juego

"""