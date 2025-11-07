import pygame
import random
import sys
import csv
import os

# --- Inicialización de Audio ---
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()

# --- Configuración de la Ventana ---
ANCHO, ALTO = 1000, 500
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("SUMO DUMO WILD")

# --- Colores (UI y Texto) ---
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS = (100, 100, 100)
VERDE_CLARO = (0, 200, 0)
AMARILLO_TEXTO = (255, 255, 0)
AMARILLO_CLARO = (200, 200, 0)
ROJO_CLARO = (200, 0, 0)
AZUL_TEXTO = (0, 150, 255)
NARANJA_TEXTO = (255, 165, 0)
ROJO_TEXTO = (255, 0, 0)

# --- Variables Globales de Volumen ---
current_music_volume = 0.5
volume_before_mute = 0.5 

# --- Configuración de Tamaños (Hitbox) ---
JUGADOR_SIZE = (68, 68)
ENEMIGO_SIZE = (60, 60)
POWERUP_SIZE_VIDA = (60, 60)
POWERUP_SIZE_ESCUDO = (60, 60)
POWERUP_SIZE_SLOWMO = (60, 60)
POWERUP_VEL = 2

# --- Constantes de Efectos ---
INMORTAL_DURATION = 5000
SLOWMO_DURATION = 5000
POWERUP_SPAWN_RATE = 420

# --- Carga de Imágenes (Reemplaza con tus archivos) ---
try:
    FONDO_MENU_IMG = pygame.transform.scale(pygame.image.load("./assets/img/fondo_menu.jpg"), (ANCHO, ALTO)).convert()
    FONDO_JUEGO_IMG = pygame.transform.scale(pygame.image.load("./assets/img/fondo_juego.jpg"), (ANCHO, ALTO)).convert()
    FONDO_GAMEOVER_IMG = pygame.transform.scale(pygame.image.load("./assets/img/fondo_game_over.jpg"), (ANCHO, ALTO)).convert()

    # --- GRUPO DE IMÁGENES DEL JUGADOR ---
    JUGADOR_IMGS = {
        'down': pygame.transform.scale(pygame.image.load("./assets/img/sumo_azul_down.png"), JUGADOR_SIZE).convert_alpha(),
        'up': pygame.transform.scale(pygame.image.load("./assets/img/sumo_azul_up.png"), JUGADOR_SIZE).convert_alpha(),
        'left': pygame.transform.scale(pygame.image.load("./assets/img/sumo_azul_left.png"), JUGADOR_SIZE).convert_alpha(),
        'right': pygame.transform.scale(pygame.image.load("./assets/img/sumo_azul_right.png"), JUGADOR_SIZE).convert_alpha()
    }
    # --- GRUPO DE IMÁGENES DEL CLOWN (TRUCO) ---
    JUGADOR_CLOWN_IMGS = {
        'down': pygame.transform.scale(pygame.image.load("./assets/img/clown_sumo_down.png"), JUGADOR_SIZE).convert_alpha(), 
        'up': pygame.transform.scale(pygame.image.load("./assets/img/clown_sumo_up.png"), JUGADOR_SIZE).convert_alpha(), 
        'left': pygame.transform.scale(pygame.image.load("./assets/img/clown_sumo_left.png"), JUGADOR_SIZE).convert_alpha(),
        'right': pygame.transform.scale(pygame.image.load("./assets/img/clown_sumo_right.png"), JUGADOR_SIZE).convert_alpha()
    }
    
    ENEMIGO_IMG = pygame.transform.scale(pygame.image.load("./assets/img/sumo_rojo_down.png"), ENEMIGO_SIZE).convert_alpha()
    VIDA_IMG = pygame.transform.scale(pygame.image.load("./assets/img/shield_power_up.png"), POWERUP_SIZE_VIDA).convert_alpha()
    ESCUDO_IMG = pygame.transform.scale(pygame.image.load("./assets/img/empanada_shield.png"), POWERUP_SIZE_ESCUDO).convert_alpha()
    SLOWMO_IMG = pygame.transform.scale(pygame.image.load("./assets/img/choripan_slowmo_power_up.png"), POWERUP_SIZE_SLOWMO).convert_alpha()
    
except FileNotFoundError as e:
    print(f"¡Error! No se pudo cargar una imagen: {e}")
    print("Asegúrate de tener las imágenes 'up', 'left' y 'right' del jugador y del clown en la carpeta assets/img.")
    pygame.quit()
    sys.exit()

# --- Carga de Sonidos y Música (Reemplaza con tus archivos) ---
try:
    # SFX
    BOTON_SOUND = pygame.mixer.Sound("./assets/sounds/power_up_sound.mp3")
    POWERUP_SOUND = pygame.mixer.Sound("./assets/sounds/power_up_sound.mp3")
    HIT_SOUND = pygame.mixer.Sound("./assets/sounds/hit_sound.mp3")
    # BGM
    MUSICA_MENU = "./assets/sounds/menu_music.mp3"
    MUSICA_JUEGO = "./assets/sounds/game_music.mp3"
    MUSICA_GAMEOVER = "./assets/sounds/game_over_sound.mp3"
    # Volúmenes
    BOTON_SOUND.set_volume(0.5)
    POWERUP_SOUND.set_volume(0.5)
    HIT_SOUND.set_volume(0.5)
except FileNotFoundError as e:
    print(f"¡Error! No se pudo cargar un archivo de sonido: {e}")
    pygame.quit()
    sys.exit()

# --- Archivo de Puntajes ---
PUNTAJES_FILE = 'puntajes.csv'

# --- Fuentes y Reloj ---
fuente = pygame.font.SysFont("arial", 35)
fuente_pequena = pygame.font.SysFont("arial", 25)
fuente_grande = pygame.font.SysFont("arial", 60)
reloj = pygame.time.Clock()

# --- Coordenadas de Volumen (Top Center) ---
VOL_Y_POS = 10 
VOL_BTN_WIDTH = 30
VOL_BTN_GAP = 5
TOTAL_VOL_WIDTH = (VOL_BTN_WIDTH * 3) + (VOL_BTN_GAP * 2) 
VOL_START_X = (ANCHO // 2) - (TOTAL_VOL_WIDTH // 2) 

VOL_MINUS_RECT = pygame.Rect(VOL_START_X, VOL_Y_POS, VOL_BTN_WIDTH, VOL_BTN_WIDTH)
VOL_MUTE_RECT = pygame.Rect(VOL_START_X + VOL_BTN_WIDTH + VOL_BTN_GAP, VOL_Y_POS, VOL_BTN_WIDTH, VOL_BTN_WIDTH)
VOL_PLUS_RECT = pygame.Rect(VOL_START_X + (VOL_BTN_WIDTH + VOL_BTN_GAP) * 2, VOL_Y_POS, VOL_BTN_WIDTH, VOL_BTN_WIDTH)


# --- Funciones de guardado (Sin cambios) ---
def inicializar_csv():
    if not os.path.exists(PUNTAJES_FILE):
        try:
            with open(PUNTAJES_FILE, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['INICIALES', 'PUNTAJE'])
        except IOError as e: print(f"Error al inicializar el archivo CSV: {e}")

def guardar_y_ordenar_puntaje(iniciales, puntaje):
    puntajes = []
    try:
        with open(PUNTAJES_FILE, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            cabecera = next(reader) 
            for fila in reader:
                try: puntajes.append((fila[0], int(fila[1])))
                except (ValueError, IndexError): continue
        
        puntajes.append((iniciales, puntaje))
        puntajes.sort(key=lambda x: x[1], reverse=True)
        
        with open(PUNTAJES_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(cabecera)
            writer.writerows(puntajes)
    except IOError as e: print(f"Error al guardar y ordenar puntajes: {e}")
    except FileNotFoundError:
        inicializar_csv()
        guardar_y_ordenar_puntaje(iniciales, puntaje)

# --- Funciones de UI (Sin cambios) ---
def mostrar_mensaje(texto: str, fuente_render: pygame.font.Font, color: tuple, pos_centro: tuple):
    render = fuente_render.render(texto, True, color)
    ventana.blit(render, render.get_rect(center=pos_centro))

def dibujar_boton(rect: pygame.Rect, texto: str, color_base: tuple, color_hover: tuple, color_texto: tuple):
    mouse_pos = pygame.mouse.get_pos()
    if rect.collidepoint(mouse_pos):
        pygame.draw.rect(ventana, color_hover, rect, border_radius=10)
    else:
        pygame.draw.rect(ventana, color_base, rect, border_radius=10)
    mostrar_mensaje(texto, fuente, color_texto, rect.center)

# --- Funciones de Control de Volumen (Sin cambios) ---
def dibujar_ui_volumen():
    pygame.draw.rect(ventana, GRIS, VOL_MINUS_RECT, 2, 3)
    pygame.draw.rect(ventana, GRIS, VOL_MUTE_RECT, 2, 3)
    pygame.draw.rect(ventana, GRIS, VOL_PLUS_RECT, 2, 3)
    
    mostrar_mensaje("-", fuente_pequena, BLANCO, VOL_MINUS_RECT.center)
    if current_music_volume == 0:
        mostrar_mensaje("M", fuente_pequena, ROJO_TEXTO, VOL_MUTE_RECT.center)
    else:
        mostrar_mensaje("M", fuente_pequena, BLANCO, VOL_MUTE_RECT.center)
    mostrar_mensaje("+", fuente_pequena, BLANCO, VOL_PLUS_RECT.center)

def manejar_clic_volumen(event_pos):
    global current_music_volume, volume_before_mute
    vol_changed = False
    
    if VOL_MINUS_RECT.collidepoint(event_pos):
        current_music_volume = max(0.0, current_music_volume - 0.1)
        vol_changed = True
    elif VOL_PLUS_RECT.collidepoint(event_pos):
        current_music_volume = min(1.0, current_music_volume + 0.1)
        vol_changed = True
    elif VOL_MUTE_RECT.collidepoint(event_pos):
        if current_music_volume > 0:
            volume_before_mute = current_music_volume 
            current_music_volume = 0.0
        else:
            current_music_volume = volume_before_mute 
        vol_changed = True
        
    if vol_changed:
        pygame.mixer.music.set_volume(round(current_music_volume, 2))


# --- Pantalla de Puntajes (ACTUALIZADA) ---
def pantalla_puntajes():
    puntajes_leidos = []
    try:
        with open(PUNTAJES_FILE, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader) 
            for fila in reader:
                try: puntajes_leidos.append((fila[0], int(fila[1])))
                except (ValueError, IndexError): continue
    except FileNotFoundError:
        inicializar_csv() 

    boton_volver = pygame.Rect(ANCHO - 220, ALTO - 70, 200, 50) 
    
    mostrando = True
    while mostrando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    manejar_clic_volumen(event.pos) 
                    if boton_volver.collidepoint(event.pos):
                        BOTON_SOUND.play()
                        mostrando = False 
            
            # --- BLOQUE KEYDOWN ELIMINADO ---
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_r or event.key == pygame.K_ESCAPE:
            #         BOTON_SOUND.play()
            #         mostrando = False

        ventana.blit(FONDO_MENU_IMG, (0, 0)) 
        mostrar_mensaje("Mejores Puntajes", fuente_grande, BLANCO, (ANCHO // 2, 80))
        
        if not puntajes_leidos:
            mostrar_mensaje("Aún no hay puntajes guardados", fuente, GRIS, (ANCHO // 2, ALTO // 2))
        else:
            y_pos = 150 
            for i, (iniciales, puntaje) in enumerate(puntajes_leidos[:10]): 
                texto_rank = f"{i + 1}."
                texto_nombre = f"{iniciales}"
                texto_puntaje = f"{puntaje}"
                mostrar_mensaje(texto_rank, fuente, BLANCO, (ANCHO // 2 - 150, y_pos))
                mostrar_mensaje(texto_nombre, fuente, AMARILLO_TEXTO, (ANCHO // 2, y_pos))
                mostrar_mensaje(texto_puntaje, fuente, BLANCO, (ANCHO // 2 + 150, y_pos))
                y_pos += 40 

        # --- Texto del botón actualizado (quitado "(R)") ---
        dibujar_boton(boton_volver, "Volver", GRIS, AMARILLO_CLARO, NEGRO)
        dibujar_ui_volumen() 
        pygame.display.flip()
        reloj.tick(15)

# --- Menús (Sin cambios) ---
def main_menu():
    try:
        pygame.mixer.music.load(MUSICA_MENU)
        pygame.mixer.music.set_volume(current_music_volume) 
        pygame.mixer.music.play(-1)
    except pygame.error as e: print(f"No se pudo cargar la música del menú: {e}")

    boton_jugar = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 - 40, 200, 60)
    boton_puntajes = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 40, 200, 60)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    manejar_clic_volumen(event.pos) 
                    if boton_jugar.collidepoint(event.pos):
                        BOTON_SOUND.play()
                        select_difficulty()
                        return 
                    if boton_puntajes.collidepoint(event.pos):
                        BOTON_SOUND.play()
                        pantalla_puntajes()
        
        ventana.blit(FONDO_MENU_IMG, (0, 0))
        mostrar_mensaje("SUMO DUMO WILD", fuente_grande, BLANCO, (ANCHO // 2, ALTO // 2 - 120))
        dibujar_boton(boton_jugar, "Jugar", VERDE_CLARO, AMARILLO_CLARO, NEGRO)
        dibujar_boton(boton_puntajes, "Puntajes", GRIS, AMARILLO_CLARO, NEGRO)
        dibujar_ui_volumen() 
        pygame.display.flip()
        reloj.tick(15)

# --- Pantalla de Dificultad (Sin cambios, ya funciona como se pide) ---
def select_difficulty():
    boton_facil = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 - 100, 200, 50)
    boton_normal = pygame.Rect(ANCHO // 2 - 100, ALTO // 2, 200, 50)
    boton_dificil = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 100, 200, 50)
    boton_volver = pygame.Rect(20, ALTO - 70, 200, 50) 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    manejar_clic_volumen(event.pos) 
                    
                    if boton_volver.collidepoint(event.pos):
                        BOTON_SOUND.play()
                        return 

                    if boton_facil.collidepoint(event.pos):
                        BOTON_SOUND.play()
                        juego("facil")
                        return
                    if boton_normal.collidepoint(event.pos):
                        BOTON_SOUND.play()
                        juego("normal")
                        return
                    if boton_dificil.collidepoint(event.pos):
                        BOTON_SOUND.play()
                        juego("dificil")
                        return

        ventana.blit(FONDO_MENU_IMG, (0, 0))
        mostrar_mensaje("Selecciona Dificultad", fuente_grande, BLANCO, (ANCHO // 2, 100))
        dibujar_boton(boton_facil, "Fácil", VERDE_CLARO, AMARILLO_CLARO, NEGRO)
        dibujar_boton(boton_normal, "Normal", AMARILLO_TEXTO, AMARILLO_CLARO, NEGRO)
        dibujar_boton(boton_dificil, "Difícil", ROJO_TEXTO, ROJO_CLARO, BLANCO)
        dibujar_boton(boton_volver, "Volver", GRIS, AMARILLO_CLARO, NEGRO) 
        dibujar_ui_volumen() 
        pygame.display.flip()
        reloj.tick(15)

# --- Pantalla de Game Over (ACTUALIZADA) ---
def pantalla_guardar_puntaje(score: int):
    pygame.mixer.music.stop()
    try:
        pygame.mixer.music.load(MUSICA_GAMEOVER)
        pygame.mixer.music.set_volume(current_music_volume) 
        pygame.mixer.music.play(-1)
    except pygame.error as e: print(f"No se pudo cargar la música de game over: {e}")

    iniciales = ""
    input_rect = pygame.Rect(ANCHO // 2 - 75, ALTO // 2 + 50, 150, 50)
    
    # --- NUEVO BOTÓN "VOLVER" ---
    boton_volver_menu = pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 150, 200, 50)
    
    guardando = True
    while guardando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                 if event.button == 1:
                    manejar_clic_volumen(event.pos) 
                    
                    # --- Lógica de clic para el nuevo botón ---
                    if boton_volver_menu.collidepoint(event.pos) and len(iniciales) != 3:
                        BOTON_SOUND.play()
                        guardando = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: 
                    if len(iniciales) == 3:
                        BOTON_SOUND.play()
                        guardar_y_ordenar_puntaje(iniciales, score)
                        guardando = False
                elif event.key == pygame.K_BACKSPACE:
                    iniciales = iniciales[:-1]
                
                # --- "elif" para la tecla 'R' ELIMINADO ---
                # elif event.key == pygame.K_r and len(iniciales) != 3:
                #     BOTON_SOUND.play()
                #     guardando = False
                
                elif len(iniciales) < 3 and event.unicode.isalpha():
                    iniciales += event.unicode.upper()

        ventana.blit(FONDO_GAMEOVER_IMG, (0, 0))
        mostrar_mensaje("¡PERDISTE!", fuente_grande, ROJO_TEXTO, (ANCHO // 2, ALTO // 2 - 150))
        mostrar_mensaje(f"Puntaje Final: {score}", fuente_grande, BLANCO, (ANCHO // 2, ALTO // 2 - 80))
        mostrar_mensaje("Ingresa tus 3 iniciales:", fuente, BLANCO, (ANCHO // 2, ALTO // 2 + 10))
        
        # --- Corregido el color del borde del input a BLANCO ---
        pygame.draw.rect(ventana, BLANCO, input_rect, 2)
        mostrar_mensaje(iniciales, fuente_grande, BLANCO, input_rect.center)
        
        if len(iniciales) == 3:
            mostrar_mensaje("Presiona ENTER para guardar", fuente_pequena, VERDE_CLARO, (ANCHO // 2, ALTO // 2 + 120))
        else:
            # --- Texto de "R" reemplazado por el dibujo del botón ---
            dibujar_boton(boton_volver_menu, "Volver al Menu", GRIS, AMARILLO_CLARO, NEGRO)
        
        dibujar_ui_volumen() 
        pygame.display.flip()
        reloj.tick(30)
    
    pygame.mixer.music.stop() 
    return

# --- Función Principal del Juego (Sin cambios) ---
def juego(dificultad: str):
    pygame.mixer.music.stop()
    try:
        pygame.mixer.music.load(MUSICA_JUEGO)
        pygame.mixer.music.set_volume(current_music_volume) 
        pygame.mixer.music.play(-1)
    except pygame.error as e: print(f"No se pudo cargar la música del juego: {e}")
    
    if dificultad == "facil":
        vidas, max_spawn_tiempo, vel_min, vel_max, jugador_vel, score_mult = 5, 40, 2, 5, 5, 1
    elif dificultad == "normal":
        vidas, max_spawn_tiempo, vel_min, vel_max, jugador_vel, score_mult = 3, 25, 4, 8, 6, 3
    else: 
        vidas, max_spawn_tiempo, vel_min, vel_max, jugador_vel, score_mult = 3, 10, 7, 12, 7, 5

    jugador = pygame.Rect(ANCHO // 2 - JUGADOR_SIZE[0] // 2, ALTO // 2 - JUGADOR_SIZE[1] // 2, JUGADOR_SIZE[0], JUGADOR_SIZE[1])
    score = 0
    enemigos, health_packs, shields, slow_mos = [], [], [], []
    contador_spawn_enemigo, contador_spawn_powerup = 0, 0
    inmortal, slow_mo = False, False
    inmortal_start_time, slow_mo_start_time = 0, 0
    truco_input, truco_activado = "", False
    player_direction = 'down' 

    corriendo = True
    while corriendo:
        reloj.tick(60)
        current_time = pygame.time.get_ticks() 
        score += score_mult
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                 if event.button == 1:
                    manejar_clic_volumen(event.pos) 
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    truco_input = (truco_input + event.unicode.lower())[-5:]
                    if truco_input == "clown":
                        truco_activado = True

        if inmortal and current_time - inmortal_start_time > INMORTAL_DURATION: inmortal = False
        if slow_mo and current_time - slow_mo_start_time > SLOWMO_DURATION: slow_mo = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_direction = 'up'
        elif keys[pygame.K_DOWN]:
            player_direction = 'down'
        elif keys[pygame.K_LEFT]:
            player_direction = 'left'
        elif keys[pygame.K_RIGHT]:
            player_direction = 'right'
            
        if keys[pygame.K_UP] and jugador.top > 0: 
            jugador.y -= jugador_vel
        if keys[pygame.K_DOWN] and jugador.bottom < ALTO: 
            jugador.y += jugador_vel
        if keys[pygame.K_LEFT] and jugador.left > 0: 
            jugador.x -= jugador_vel
        if keys[pygame.K_RIGHT] and jugador.right < ANCHO: 
            jugador.x += jugador_vel

        # Spawning Enemigos
        contador_spawn_enemigo += 1
        if contador_spawn_enemigo >= max_spawn_tiempo:
            contador_spawn_enemigo = 0
            for _ in range(random.randint(1, 2)):
                lado, velocidad = random.randint(1, 4), random.randint(vel_min, vel_max)
                dx, dy = 0, 0
                if lado == 1: x, y, dy = random.randint(0, ANCHO - ENEMIGO_SIZE[0]), -ENEMIGO_SIZE[1], velocidad
                elif lado == 2: x, y, dy = random.randint(0, ANCHO - ENEMIGO_SIZE[0]), ALTO, -velocidad
                elif lado == 3: x, y, dx = -ENEMIGO_SIZE[0], random.randint(0, ALTO - ENEMIGO_SIZE[1]), velocidad
                else: x, y, dx = ANCHO, random.randint(0, ALTO - ENEMIGO_SIZE[1]), -velocidad
                enemigos.append({'rect': pygame.Rect(x, y, ENEMIGO_SIZE[0], ENEMIGO_SIZE[1]), 'dx': dx, 'dy': dy})

        # Spawning Power-ups
        contador_spawn_powerup += 1
        if contador_spawn_powerup >= POWERUP_SPAWN_RATE:
            contador_spawn_powerup = 0
            spawn_x, spawn_y = random.randint(50, ANCHO - 50), random.randint(50, ALTO - 50)
            tipo = random.choice(['health', 'shield', 'slowmo'])
            if tipo == 'health': health_packs.append(pygame.Rect(spawn_x, spawn_y, POWERUP_SIZE_VIDA[0], POWERUP_SIZE_VIDA[1]))
            elif tipo == 'shield': shields.append(pygame.Rect(spawn_x, spawn_y, POWERUP_SIZE_ESCUDO[0], POWERUP_SIZE_ESCUDO[1]))
            elif tipo == 'slowmo': slow_mos.append({'rect': pygame.Rect(spawn_x, spawn_y, POWERUP_SIZE_SLOWMO[0], POWERUP_SIZE_SLOWMO[1]), 'dx': random.choice([-POWERUP_VEL, POWERUP_VEL]), 'dy': random.choice([-POWERUP_VEL, POWERUP_VEL])})

        # Colisiones Enemigos
        velocidad_mult = 0.4 if slow_mo else 1.0
        enemigos_activos = []
        for enemigo in enemigos:
            enemigo['rect'].x += enemigo['dx'] * velocidad_mult
            enemigo['rect'].y += enemigo['dy'] * velocidad_mult
            
            if jugador.colliderect(enemigo['rect']):
                if not inmortal:
                    vidas -= 1
                    HIT_SOUND.play() 
                    if vidas <= 0: corriendo = False
            elif -100 < enemigo['rect'].x < ANCHO + 100 and -100 < enemigo['rect'].y < ALTO + 100:
                enemigos_activos.append(enemigo)
        enemigos = enemigos_activos
        
        if not corriendo: break

        # Colisiones Power-ups
        for slow in slow_mos:
            slow['rect'].x += slow['dx']; slow['rect'].y += slow['dy']
            if slow['rect'].left <= 0 or slow['rect'].right >= ANCHO: slow['dx'] *= -1
            if slow['rect'].top <= 0 or slow['rect'].bottom >= ALTO: slow['dy'] *= -1

        for pack in health_packs[:]:
            if jugador.colliderect(pack):
                vidas += 1; health_packs.remove(pack); POWERUP_SOUND.play()
        for shield in shields[:]:
            if jugador.colliderect(shield):
                inmortal, inmortal_start_time = True, current_time; shields.remove(shield); POWERUP_SOUND.play()
        for slow in slow_mos[:]:
            if jugador.colliderect(slow['rect']):
                slow_mo, slow_mo_start_time = True, current_time; slow_mos.remove(slow); POWERUP_SOUND.play()

        # Renderizado
        ventana.blit(FONDO_JUEGO_IMG, (0, 0))
        for pack in health_packs: ventana.blit(VIDA_IMG, pack)
        for shield in shields: ventana.blit(ESCUDO_IMG, shield)
        for slow in slow_mos: ventana.blit(SLOWMO_IMG, slow['rect'])
        
        if truco_activado:
            current_image_set = JUGADOR_CLOWN_IMGS
        else:
            current_image_set = JUGADOR_IMGS
            
        imagen_jugador_actual = current_image_set[player_direction]
        
        if not (inmortal and (current_time // 150) % 2 == 0):
            ventana.blit(imagen_jugador_actual, jugador)
        
        for enemigo in enemigos: ventana.blit(ENEMIGO_IMG, enemigo['rect'])
            
        # UI
        mostrar_mensaje(f"Vidas: {vidas}", fuente, BLANCO, (ANCHO - 100, 30))
        mostrar_mensaje(f"Puntaje: {score}", fuente, BLANCO, (120, 30))
        dibujar_ui_volumen() 
        
        if inmortal:
            tiempo_restante = (INMORTAL_DURATION - (current_time - inmortal_start_time)) // 1000 + 1
            mostrar_mensaje(f"INMORTAL: {tiempo_restante}s", fuente_pequena, AZUL_TEXTO, (jugador.centerx, jugador.top - 20))
        if slow_mo:
            tiempo_restante = (SLOWMO_DURATION - (current_time - slow_mo_start_time)) // 1000 + 1
            mostrar_mensaje(f"SLOW-MO: {tiempo_restante}s", fuente_pequena, NARANJA_TEXTO, (120, 60))

        pygame.display.flip()

    pantalla_guardar_puntaje(score)
    return 

# --- Bucle Principal del Programa ---
inicializar_csv() 
while True:
    main_menu()