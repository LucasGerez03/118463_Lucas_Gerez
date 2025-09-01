import pygame

size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
pygame.mouse.set_visible(True)

cord_x = 10
cord_y = 10

speed_x = 0
speed_y = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #eventos teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -3
            if event.key == pygame.K_RIGHT:
                speed_x = 3
            if event.key == pygame.K_UP:
                speed_y = -3
            if event.key == pygame.K_DOWN:
                speed_y = 3
        
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed_x = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0
            if event.key == pygame.K_UP:
                speed_y = 0
            if event.key == pygame.K_DOWN:
                speed_y = 0
    cord_x += speed_x
    cord_y += speed_y
#TODO #################LOGICA DEL JUEGO#################
    # mouse_pos = pygame.mouse.get_pos()
    # x = mouse_pos[0]
    # y = mouse_pos[1]
#TODO #################LOGICA DEL JUEGO#################

#?PANTALLA
    screen.fill("WHITE")
#TODO ################# ZONA DE DIBUJO #################
    pygame.draw.circle(screen, "purple", (cord_x, cord_y), 30)
#TODO ################# ZONA DE DIBUJO #################
#?RENDERIZADO
    pygame.display.flip()
    clock.tick(90)
pygame.quit()