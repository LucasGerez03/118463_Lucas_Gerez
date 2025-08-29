# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()  #!NO OLVIDAR (METODO)
screen = pygame.display.set_mode((1280, 720)) #?pantalla
clock = pygame.time.Clock() #? tiempo
running = True

#TODO FUENTES DEL JUEGO
fuenteInter = pygame.font.SysFont("Arial", 20)  

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get(): #?eventos, son como acciones ,son muy importantes
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("HOLA")
        if event.type == pygame.KEYDOWN:
            print("CHAU")  
            if event.key == pygame.K_a:
                print("A")  
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
                                        #TODO (x, y , ancho, alto)
    pygame.draw.rect(screen, "yellow", (screen.get_width()/2 -50 , screen.get_height()/2 - 50, 100, 100)) #? Creamos nuestro rectangulo
    
                                      #TODO (x,y), *tamaño del circulo*
    pygame.draw.circle(screen, "red", (250,250), 100) #? Los valores del centro del circulo
    
    # RENDER YOUR GAME HERE
    texto = fuenteInter.render("Ahora si culiado", True, "black")
    screen.blit(texto, (150, 150))
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit() #!NO OLVIDAR (METODO)