import pygame, random
pygame.init()


size = (800, 600)
scree = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True

coord_list = []
for i in range(100):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        coord_list.append([x, y])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
#TODO #################LOGICA DEL JUEGO#################

#TODO #################LOGICA DEL JUEGO#################

#?PANTALLA
    scree.fill("WHITE")
#TODO ################# ZONA DE DIBUJO #################
    for coor in coord_list:
        pygame.draw.line(scree, "BLUE", (coor), (coor[0], coor[1]+ 10), 2)
        coor[1] += 5
        if coor[1] > 600:
            coor[1] = 0
            coor[0] = random.randint(0, 800)

#TODO ################# ZONA DE DIBUJO #################
#?RENDERIZADO
    pygame.display.flip()
    clock.tick(60)

pygame.quit()