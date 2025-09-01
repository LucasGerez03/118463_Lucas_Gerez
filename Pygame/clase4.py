# Example file showing a basic pygame "game loop"
import pygame, sys

cord_x = 400
cord_y = 240

speed_x = 5
speed_y = 5

# pygame setup

pygame.init()  #!NO OLVIDAR (METODO)
size = (900, 720) #?tamaño de la pantalla 
screen = pygame.display.set_mode((size)) #?pantalla
#Control de FPS
clock = pygame.time.Clock() #? tiempo
running = True

#TODO FUENTES DEL JUEGO
fuenteInter = pygame.font.SysFont("Arial", 20)


while running:   
 
    for event in pygame.event.get(): #?eventos, son como acciones ,son muy importantes
        print(event) #? para ver los eventos en consola
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("HOLA")
        if event.type == pygame.KEYDOWN:
            print("CHAU")  
            if event.key == pygame.K_a:
                print("A")  
#TODO #################LOGICA DEL JUEGO#################
    if cord_x > 820 or cord_x < 0:
        speed_x = speed_x * -1
    if cord_y > 640 or cord_y < 0:
        speed_y = speed_y * -1
    cord_x += speed_x
    cord_y += speed_y
#TODO #################LOGICA DEL JUEGO#################


#?PARTE GRAFICA
    screen.fill("blue")

#TODO ################# ZONA DE DIBUJO #################                                        
    pygame.draw.rect(screen, "RED", (cord_x, cord_y, 80, 80)) #? rectangulo (pantalla,color,(x,y,ancho,alto))

    
#TODO ################# ZONA DE DIBUJO #################                 
#?RENDERIZADO
    texto = fuenteInter.render("Ahora si culiado", True, "black")
    screen.blit(texto, (150, 150))
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit() #!NO OLVIDAR (METODO)