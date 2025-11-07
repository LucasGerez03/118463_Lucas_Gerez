import pygame
import random
import sys
import csv
import os

# --- Inicialización de Audio ---
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()

# --- Configuración Global y Constantes ---
ANCHO, ALTO = 800, 600
screen = pygame.display.set_mode((ANCHO, ALTO))
PUNTAJES_FILE = 'puntajes.csv'

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

# --- Tamaños (Hitbox) ---
JUGADOR_SIZE = (68, 68)
ENEMIGO_SIZE = (60, 60)
POWERUP_SIZE_VIDA = (60, 60)
POWERUP_SIZE_ESCUDO = (60, 60)
POWERUP_SIZE_SLOWMO = (60, 60)
POWERUP_VEL = 2

# --- Constantes de Efectos ---
INMORTAL_DURATION = 5000
SLOWMO_DURATION = 5000
POWERUP_SPAWN_RATE = 420 # Frames

# --- Carga de Imágenes (Global) ---
try:
    FONDO_MENU_IMG = pygame.transform.scale(pygame.image.load("./assets/img/fondo_menu.png"), (ANCHO, ALTO)).convert()
    FONDO_JUEGO_IMG = pygame.transform.scale(pygame.image.load("./assets/img/fondo_juego.png"), (ANCHO, ALTO)).convert()
    FONDO_GAMEOVER_IMG = pygame.transform.scale(pygame.image.load("./assets/img/fondo_game_over.jpg"), (ANCHO, ALTO)).convert()

    JUGADOR_IMGS = {
        'down': pygame.transform.scale(pygame.image.load("./assets/img/sumo_azul_down.png"), JUGADOR_SIZE).convert_alpha(),
        'up': pygame.transform.scale(pygame.image.load("./assets/img/sumo_azul_up.png"), JUGADOR_SIZE).convert_alpha(),
        'left': pygame.transform.scale(pygame.image.load("./assets/img/sumo_azul_left.png"), JUGADOR_SIZE).convert_alpha(),
        'right': pygame.transform.scale(pygame.image.load("./assets/img/sumo_azul_right.png"), JUGADOR_SIZE).convert_alpha()
    }
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
    pygame.quit()
    sys.exit()

# --- Carga de Sonidos (Global) ---
try:
    BOTON_SOUND = pygame.mixer.Sound("./assets/sounds/power_up_sound.mp3")
    POWERUP_SOUND = pygame.mixer.Sound("./assets/sounds/power_up_sound.mp3")
    HIT_SOUND = pygame.mixer.Sound("./assets/sounds/hit_sound.mp3")
    MUSICA_MENU = "./assets/sounds/menu_music.mp3"
    MUSICA_JUEGO = "./assets/sounds/game_music.mp3"
    MUSICA_GAMEOVER = "./assets/sounds/game_over_sound.mp3"
    BOTON_SOUND.set_volume(0.5)
    POWERUP_SOUND.set_volume(0.5)
    HIT_SOUND.set_volume(0.5)
except FileNotFoundError as e:
    print(f"¡Error! No se pudo cargar un archivo de sonido: {e}")
    pygame.quit()
    sys.exit()

# --- Fuentes y Reloj (Global) ---
fuente = pygame.font.SysFont("arial", 35)
fuente_pequena = pygame.font.SysFont("arial", 25)
fuente_grande = pygame.font.SysFont("arial", 60)
reloj = pygame.time.Clock()

# --- Coordenadas de Volumen (Global) ---
VOL_Y_POS = 10 
VOL_BTN_WIDTH = 30
VOL_BTN_GAP = 5
TOTAL_VOL_WIDTH = (VOL_BTN_WIDTH * 3) + (VOL_BTN_GAP * 2) 
VOL_START_X = (ANCHO // 2) - (TOTAL_VOL_WIDTH // 2) 
VOL_MINUS_RECT = pygame.Rect(VOL_START_X, VOL_Y_POS, VOL_BTN_WIDTH, VOL_BTN_WIDTH)
VOL_MUTE_RECT = pygame.Rect(VOL_START_X + VOL_BTN_WIDTH + VOL_BTN_GAP, VOL_Y_POS, VOL_BTN_WIDTH, VOL_BTN_WIDTH)
VOL_PLUS_RECT = pygame.Rect(VOL_START_X + (VOL_BTN_WIDTH + VOL_BTN_GAP) * 2, VOL_Y_POS, VOL_BTN_WIDTH, VOL_BTN_WIDTH)

# --- Función Auxiliar ---
def mostrar_mensaje(surface, texto: str, fuente_render: pygame.font.Font, color: tuple, pos_centro: tuple):
    """Dibuja texto centrado en la superficie dada."""
    render = fuente_render.render(texto, True, color)
    surface.blit(render, render.get_rect(center=pos_centro))

# -----------------------------------------------------------------
# --- CLASE: ScoreManager (Estática) ---
# -----------------------------------------------------------------
class ScoreManager:
    @staticmethod
    def inicializar_csv():
        """Crea el archivo CSV con cabeceras si no existe."""
        if not os.path.exists(PUNTAJES_FILE):
            try:
                with open(PUNTAJES_FILE, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(['INICIALES', 'PUNTAJE'])
            except IOError as e: print(f"Error al inicializar el archivo CSV: {e}")

    @staticmethod
    def guardar_y_ordenar_puntaje(iniciales, puntaje):
        """Añade un puntaje y reescribe el CSV ordenado."""
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
            ScoreManager.inicializar_csv()
            ScoreManager.guardar_y_ordenar_puntaje(iniciales, puntaje)
            
    @staticmethod
    def leer_puntajes():
        """Lee y devuelve la lista de puntajes."""
        puntajes_leidos = []
        try:
            with open(PUNTAJES_FILE, 'r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader) # Saltar cabecera
                for fila in reader:
                    try: puntajes_leidos.append((fila[0], int(fila[1])))
                    except (ValueError, IndexError): continue
        except FileNotFoundError:
            ScoreManager.inicializar_csv()
        return puntajes_leidos

# -----------------------------------------------------------------
# --- CLASE: Button ---
# -----------------------------------------------------------------
class Button:
    def __init__(self, rect, texto, color_base, color_hover, color_texto=NEGRO):
        self.rect = rect
        self.texto = texto
        self.color_base = color_base
        self.color_hover = color_hover
        self.color_texto = color_texto

    def draw(self, surface):
        """Dibuja el botón, cambiando de color si el mouse está encima."""
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.color_hover, self.rect, border_radius=10)
        else:
            pygame.draw.rect(surface, self.color_base, self.rect, border_radius=10)
        mostrar_mensaje(surface, self.texto, fuente, self.color_texto, self.rect.center)
    
    def is_clicked(self, event):
        """Comprueba si el evento de clic ocurrió en este botón."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                BOTON_SOUND.play()
                return True
        return False

# -----------------------------------------------------------------
# --- CLASE: Player ---
# -----------------------------------------------------------------
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, JUGADOR_SIZE[0], JUGADOR_SIZE[1])
        self.vel = 0
        self.lives = 0
        self.direction = 'down'
        self.inmortal = False
        self.inmortal_start_time = 0
        self.truco_input = ""
        self.truco_activado = False

    def move(self, keys):
        """Actualiza la dirección y posición del jugador basado en las teclas."""
        # 1. Determinar la dirección (prioriza vertical sobre horizontal para la imagen)
        if keys[pygame.K_UP]:
            self.direction = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction = 'down'
        elif keys[pygame.K_LEFT]:
            self.direction = 'left'
        elif keys[pygame.K_RIGHT]:
            self.direction = 'right'
            
        # 2. Aplicar el movimiento (permite diagonales)
        if keys[pygame.K_UP] and self.rect.top > 0: 
            self.rect.y -= self.vel
        if keys[pygame.K_DOWN] and self.rect.bottom < ALTO: 
            self.rect.y += self.vel
        if keys[pygame.K_LEFT] and self.rect.left > 0: 
            self.rect.x -= self.vel
        if keys[pygame.K_RIGHT] and self.rect.right < ANCHO: 
            self.rect.x += self.vel
            
    def check_clown_truco(self, key_unicode):
        """Actualiza el input del truco y lo activa si coincide."""
        if key_unicode.isalpha():
            self.truco_input = (self.truco_input + key_unicode.lower())[-5:]
            if self.truco_input == "clown":
                self.truco_activado = True

    def get_hit(self):
        """Procesa un golpe. Devuelve True si el jugador se queda sin vidas."""
        if not self.inmortal:
            self.lives -= 1
            HIT_SOUND.play()
            return self.lives <= 0
        return False

    def activate_shield(self, current_time):
        """Activa el estado de inmortalidad."""
        self.inmortal = True
        self.inmortal_start_time = current_time
        POWERUP_SOUND.play()
        
    def add_life(self):
        """Añade una vida."""
        self.lives += 1
        POWERUP_SOUND.play()

    def update_timers(self, current_time):
        """Desactiva power-ups si el tiempo ha expirado."""
        if self.inmortal and current_time - self.inmortal_start_time > INMORTAL_DURATION:
            self.inmortal = False

    def draw(self, surface, current_time):
        """Dibuja al jugador en la pantalla, manejando el parpadeo."""
        if self.truco_activado:
            current_image_set = JUGADOR_CLOWN_IMGS
        else:
            current_image_set = JUGADOR_IMGS
            
        imagen_jugador_actual = current_image_set[self.direction]
        
        # Lógica de parpadeo (inmortalidad)
        if not (self.inmortal and (current_time // 150) % 2 == 0):
            surface.blit(imagen_jugador_actual, self.rect)
        
        # Dibuja el temporizador de inmortalidad
        if self.inmortal:
            tiempo_restante = (INMORTAL_DURATION - (current_time - self.inmortal_start_time)) // 1000 + 1
            mostrar_mensaje(surface, f"INMORTAL: {tiempo_restante}s", fuente_pequena, AZUL_TEXTO, (self.rect.centerx, self.rect.top - 20))

# -----------------------------------------------------------------
# --- CLASE: Enemy ---
# -----------------------------------------------------------------
class Enemy:
    def __init__(self, vel_min, vel_max):
        """Genera un enemigo en un borde aleatorio con una dirección fija."""
        lado = random.randint(1, 4) 
        velocidad = random.randint(vel_min, vel_max)
        self.dx, self.dy = 0, 0

        if lado == 1: # Arriba
            x, y = random.randint(0, ANCHO - ENEMIGO_SIZE[0]), -ENEMIGO_SIZE[1]
            self.dy = velocidad
        elif lado == 2: # Abajo
            x, y = random.randint(0, ANCHO - ENEMIGO_SIZE[0]), ALTO
            self.dy = -velocidad
        elif lado == 3: # Izquierda
            x, y = -ENEMIGO_SIZE[0], random.randint(0, ALTO - ENEMIGO_SIZE[1])
            self.dx = velocidad
        else: # Derecha
            x, y = ANCHO, random.randint(0, ALTO - ENEMIGO_SIZE[1])
            self.dx = -velocidad
            
        self.rect = pygame.Rect(x, y, ENEMIGO_SIZE[0], ENEMIGO_SIZE[1])

    def move(self, speed_multiplier):
        """Mueve al enemigo, aplicando el multiplicador de slow-mo."""
        self.rect.x += self.dx * speed_multiplier
        self.rect.y += self.dy * speed_multiplier

    def draw(self, surface):
        surface.blit(ENEMIGO_IMG, self.rect)
        
    def is_offscreen(self):
        """Comprueba si está fuera de la pantalla para ser eliminado."""
        return not (-100 < self.rect.x < ANCHO + 100 and -100 < self.rect.y < ALTO + 100)

# -----------------------------------------------------------------
# --- CLASE: PowerUp ---
# -----------------------------------------------------------------
class PowerUp:
    def __init__(self):
        """Genera un power-up aleatorio en una posición aleatoria."""
        spawn_x = random.randint(50, ANCHO - 50)
        spawn_y = random.randint(50, ALTO - 50)
        self.type = random.choice(['health', 'shield', 'slowmo'])
        self.dx, self.dy = 0, 0
        
        if self.type == 'health':
            self.rect = pygame.Rect(spawn_x, spawn_y, POWERUP_SIZE_VIDA[0], POWERUP_SIZE_VIDA[1])
            self.image = VIDA_IMG
        elif self.type == 'shield':
            self.rect = pygame.Rect(spawn_x, spawn_y, POWERUP_SIZE_ESCUDO[0], POWERUP_SIZE_ESCUDO[1])
            self.image = ESCUDO_IMG
        else: # 'slowmo'
            self.rect = pygame.Rect(spawn_x, spawn_y, POWERUP_SIZE_SLOWMO[0], POWERUP_SIZE_SLOWMO[1])
            self.image = SLOWMO_IMG
            self.dx = random.choice([-POWERUP_VEL, POWERUP_VEL])
            self.dy = random.choice([-POWERUP_VEL, POWERUP_VEL])

    def move(self):
        """Mueve el power-up (solo si es 'slowmo') y rebota."""
        if self.type == 'slowmo':
            self.rect.x += self.dx
            self.rect.y += self.dy
            if self.rect.left <= 0 or self.rect.right >= ANCHO: self.dx *= -1
            if self.rect.top <= 0 or self.rect.bottom >= ALTO: self.dy *= -1
            
    def draw(self, surface):
        surface.blit(self.image, self.rect)

# -----------------------------------------------------------------
# --- CLASE PRINCIPAL: Game ---
# -----------------------------------------------------------------
class Game:
    def __init__(self):
        """Inicializa el juego, la ventana, y los estados."""
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_state = 'MENU' # Estados: MENU, DIFFICULTY, SCORES, PLAYING, GAME_OVER
        
        # --- Variables de Volumen ---
        self.current_music_volume = 0.5
        self.volume_before_mute = 0.5
        
        # --- Inicializar Botones de Menús ---
        self.btn_jugar = Button(pygame.Rect(ANCHO // 2 - 100, ALTO // 2 - 40, 200, 60), "Jugar", VERDE_CLARO, AMARILLO_CLARO)
        self.btn_puntajes = Button(pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 40, 200, 60), "Puntajes", GRIS, AMARILLO_CLARO)
        
        self.btn_facil = Button(pygame.Rect(ANCHO // 2 - 100, ALTO // 2 - 100, 200, 50), "Bebe Lloron", VERDE_CLARO, AMARILLO_CLARO)
        self.btn_normal = Button(pygame.Rect(ANCHO // 2 - 100, ALTO // 2, 200, 50), "Normal", AMARILLO_TEXTO, AMARILLO_CLARO)
        self.btn_dificil = Button(pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 100, 200, 50), "HARDCORE", ROJO_TEXTO, ROJO_CLARO, BLANCO)
        self.btn_volver_menu = Button(pygame.Rect(20, ALTO - 70, 200, 50), "Volver", GRIS, AMARILLO_CLARO)
        
        self.btn_volver_scores = Button(pygame.Rect(ANCHO - 220, ALTO - 70, 200, 50), "Volver", GRIS, AMARILLO_CLARO)
        
        # --- Variables de estado del juego (se reinician en start_new_game) ---
        self.player = Player(ANCHO // 2 - JUGADOR_SIZE[0] // 2, ALTO // 2 - JUGADOR_SIZE[1] // 2)
        self.enemies = []
        self.powerups = []
        self.score = 0
        self.difficulty_settings = {}
        
        # Timers
        self.contador_spawn_enemigo = 0
        self.contador_spawn_powerup = 0
        self.slow_mo = False
        self.slow_mo_start_time = 0
        
        # Variables de Game Over
        self.iniciales_input = ""
        self.input_rect = pygame.Rect(ANCHO // 2 - 75, ALTO // 2 + 50, 150, 50)
        self.btn_volver_gameover = Button(pygame.Rect(ANCHO // 2 - 100, ALTO // 2 + 150, 200, 50), "Volver al Menu", GRIS, AMARILLO_CLARO)

    def start_new_game(self, dificultad: str):
        """Configura todas las variables para una nueva partida."""
        if dificultad == "facil":
            self.difficulty_settings = {'vidas': 4, 'max_spawn': 40, 'vel_min': 2, 'vel_max': 5, 'jugador_vel': 4, 'score_mult': 1}
        elif dificultad == "normal":
            self.difficulty_settings = {'vidas': 3, 'max_spawn': 35, 'vel_min': 4, 'vel_max': 8, 'jugador_vel': 6, 'score_mult': 3}
        else: # Dificil
            self.difficulty_settings = {'vidas': 2, 'max_spawn': 30, 'vel_min': 4, 'vel_max': 9, 'jugador_vel': 7, 'score_mult': 5}
            
        # Reiniciar jugador
        self.player = Player(ANCHO // 2 - JUGADOR_SIZE[0] // 2, ALTO // 2 - JUGADOR_SIZE[1] // 2)
        self.player.lives = self.difficulty_settings['vidas']
        self.player.vel = self.difficulty_settings['jugador_vel']
        
        # Reiniciar listas y puntaje
        self.enemies = []
        self.powerups = []
        self.score = 0
        
        # Reiniciar timers y estados
        self.contador_spawn_enemigo = 0
        self.contador_spawn_powerup = 0
        self.slow_mo = False
        self.slow_mo_start_time = 0
        
        # Empezar música del juego
        pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load(MUSICA_JUEGO)
            pygame.mixer.music.set_volume(self.current_music_volume) 
            pygame.mixer.music.play(-1)
        except pygame.error as e: print(f"No se pudo cargar la música del juego: {e}")

    # --- Funciones de Volumen ---
    def dibujar_ui_volumen(self):
        pygame.draw.rect(self.screen, GRIS, VOL_MINUS_RECT, 2, 3)
        pygame.draw.rect(self.screen, GRIS, VOL_MUTE_RECT, 2, 3)
        pygame.draw.rect(self.screen, GRIS, VOL_PLUS_RECT, 2, 3)
        mostrar_mensaje(self.screen, "-", fuente_pequena, BLANCO, VOL_MINUS_RECT.center)
        color_mute = ROJO_TEXTO if self.current_music_volume == 0 else BLANCO
        mostrar_mensaje(self.screen, "M", fuente_pequena, color_mute, VOL_MUTE_RECT.center)
        mostrar_mensaje(self.screen, "+", fuente_pequena, BLANCO, VOL_PLUS_RECT.center)

    def manejar_clic_volumen(self, event_pos):
        vol_changed = False
        if VOL_MINUS_RECT.collidepoint(event_pos):
            self.current_music_volume = max(0.0, self.current_music_volume - 0.1)
            vol_changed = True
        elif VOL_PLUS_RECT.collidepoint(event_pos):
            self.current_music_volume = min(1.0, self.current_music_volume + 0.1)
            vol_changed = True
        elif VOL_MUTE_RECT.collidepoint(event_pos):
            if self.current_music_volume > 0:
                self.volume_before_mute = self.current_music_volume 
                self.current_music_volume = 0.0
            else:
                self.current_music_volume = self.volume_before_mute 
            vol_changed = True
        
        if vol_changed:
            pygame.mixer.music.set_volume(round(self.current_music_volume, 2))

    # --- Bucles de Estado del Juego ---
    
    def run_menu(self):
        """Bucle para el estado del Menú Principal."""
        # Cargar música de menú solo si no está ya sonando
        if not pygame.mixer.music.get_busy():
            try:
                pygame.mixer.music.load(MUSICA_MENU)
                pygame.mixer.music.set_volume(self.current_music_volume) 
                pygame.mixer.music.play(-1)
            except pygame.error as e: print(f"No se pudo cargar la música del menú: {e}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.manejar_clic_volumen(event.pos)
                if self.btn_jugar.is_clicked(event):
                    self.game_state = 'DIFFICULTY'
                if self.btn_puntajes.is_clicked(event):
                    self.game_state = 'SCORES'
        
        self.screen.blit(FONDO_MENU_IMG, (0, 0))
        mostrar_mensaje(self.screen, "SUMO DUMO ARG", fuente_grande, BLANCO, (ANCHO // 2, ALTO // 2 - 120))
        self.btn_jugar.draw(self.screen)
        self.btn_puntajes.draw(self.screen)
        self.dibujar_ui_volumen()
        pygame.display.flip()
        self.clock.tick(15)

    def run_difficulty(self):
        """Bucle para la pantalla de selección de dificultad."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.manejar_clic_volumen(event.pos)
                
                if self.btn_volver_menu.is_clicked(event):
                    self.game_state = 'MENU'
                    return # Salir del bucle para cambiar de estado

                if self.btn_facil.is_clicked(event):
                    self.start_new_game("facil")
                    self.game_state = 'PLAYING'
                elif self.btn_normal.is_clicked(event):
                    self.start_new_game("normal")
                    self.game_state = 'PLAYING'
                elif self.btn_dificil.is_clicked(event):
                    self.start_new_game("dificil")
                    self.game_state = 'PLAYING'

        self.screen.blit(FONDO_MENU_IMG, (0, 0))
        mostrar_mensaje(self.screen, "Selecciona Dificultad", fuente_grande, BLANCO, (ANCHO // 2, 100))
        self.btn_facil.draw(self.screen)
        self.btn_normal.draw(self.screen)
        self.btn_dificil.draw(self.screen)
        self.btn_volver_menu.draw(self.screen)
        self.dibujar_ui_volumen()
        pygame.display.flip()
        self.clock.tick(15)

    def run_scores(self):
        """Bucle para la pantalla de puntajes."""
        puntajes_leidos = ScoreManager.leer_puntajes()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.manejar_clic_volumen(event.pos)
                if self.btn_volver_scores.is_clicked(event):
                    self.game_state = 'MENU'
                    return

        self.screen.blit(FONDO_MENU_IMG, (0, 0)) 
        mostrar_mensaje(self.screen, "Mejores Puntajes", fuente_grande, BLANCO, (ANCHO // 2, 80))
        
        if not puntajes_leidos:
            mostrar_mensaje(self.screen, "Aún no hay puntajes guardados", fuente, GRIS, (ANCHO // 2, ALTO // 2))
        else:
            y_pos = 150 
            for i, (iniciales, puntaje) in enumerate(puntajes_leidos[:10]): 
                mostrar_mensaje(self.screen, f"{i + 1}.", fuente, BLANCO, (ANCHO // 2 - 150, y_pos))
                mostrar_mensaje(self.screen, f"{iniciales}", fuente, AMARILLO_TEXTO, (ANCHO // 2, y_pos))
                mostrar_mensaje(self.screen, f"{puntaje}", fuente, BLANCO, (ANCHO // 2 + 150, y_pos))
                y_pos += 40 

        self.btn_volver_scores.draw(self.screen)
        self.dibujar_ui_volumen() 
        pygame.display.flip()
        self.clock.tick(15)

    def run_game_over(self):
        """Bucle para la pantalla de Game Over y guardado de puntaje."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.manejar_clic_volumen(event.pos)
                    # Botón de volver (si no se han escrito 3 iniciales)
                    if self.btn_volver_gameover.is_clicked(event) and len(self.iniciales_input) != 3:
                        pygame.mixer.music.stop()
                        self.game_state = 'MENU'
                        return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: 
                    if len(self.iniciales_input) == 3:
                        BOTON_SOUND.play()
                        ScoreManager.guardar_y_ordenar_puntaje(self.iniciales_input, self.score)
                        pygame.mixer.music.stop()
                        self.game_state = 'MENU'
                        return
                elif event.key == pygame.K_BACKSPACE:
                    self.iniciales_input = self.iniciales_input[:-1]
                elif len(self.iniciales_input) < 3 and event.unicode.isalpha():
                    self.iniciales_input += event.unicode.upper()
        
        self.screen.blit(FONDO_GAMEOVER_IMG, (0, 0))
        mostrar_mensaje(self.screen, "¡PERDISTE!", fuente_grande, ROJO_TEXTO, (ANCHO // 2, ALTO // 2 - 150))
        mostrar_mensaje(self.screen, f"Puntaje Final: {self.score}", fuente_grande, BLANCO, (ANCHO // 2, ALTO // 2 - 80))
        mostrar_mensaje(self.screen, "Ingresa tus 3 iniciales:", fuente, BLANCO, (ANCHO // 2, ALTO // 2 + 10))
        pygame.draw.rect(self.screen, BLANCO, self.input_rect, 2)
        mostrar_mensaje(self.screen, self.iniciales_input, fuente_grande, BLANCO, self.input_rect.center)
        
        if len(self.iniciales_input) == 3:
            mostrar_mensaje(self.screen, "Presiona ENTER para guardar", fuente_pequena, VERDE_CLARO, (ANCHO // 2, ALTO // 2 + 120))
        else:
            self.btn_volver_gameover.draw(self.screen)
        
        self.dibujar_ui_volumen() 
        pygame.display.flip()
        self.clock.tick(30)
        
    def run_playing(self):
        """Bucle principal del juego (donde se juega)."""
        current_time = pygame.time.get_ticks() 
        self.score += self.difficulty_settings['score_mult']
        
        # --- Manejo de Eventos ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.manejar_clic_volumen(event.pos) 
            if event.type == pygame.KEYDOWN:
                self.player.check_clown_truco(event.unicode)

        # --- Actualización de Timers ---
        self.player.update_timers(current_time)
        if self.slow_mo and current_time - self.slow_mo_start_time > SLOWMO_DURATION:
            self.slow_mo = False

        # --- Movimiento ---
        keys = pygame.key.get_pressed()
        self.player.move(keys)
        
        speed_multiplier = 0.4 if self.slow_mo else 1.0
        for enemy in self.enemies:
            enemy.move(speed_multiplier)
            
        for pu in self.powerups:
            pu.move() # Solo se mueve si es 'slowmo'

        # --- Spawning ---
        self.contador_spawn_enemigo += 1
        if self.contador_spawn_enemigo >= self.difficulty_settings['max_spawn']:
            self.contador_spawn_enemigo = 0
            for _ in range(random.randint(1, 2)):
                self.enemies.append(Enemy(self.difficulty_settings['vel_min'], self.difficulty_settings['vel_max']))

        self.contador_spawn_powerup += 1
        if self.contador_spawn_powerup >= POWERUP_SPAWN_RATE:
            self.contador_spawn_powerup = 0
            self.powerups.append(PowerUp())

        # --- Colisiones ---
        for enemy in self.enemies[:]:
            if self.player.rect.colliderect(enemy.rect):
                self.enemies.remove(enemy) # El enemigo desaparece al chocar
                if self.player.get_hit(): # Si el jugador muere
                    pygame.mixer.music.stop()
                    try:
                        pygame.mixer.music.load(MUSICA_GAMEOVER)
                        pygame.mixer.music.set_volume(self.current_music_volume) 
                        pygame.mixer.music.play(-1)
                    except pygame.error as e: print(f"No se pudo cargar la música de game over: {e}")
                    
                    self.game_state = 'GAME_OVER'
                    self.iniciales_input = "" # Reiniciar input
                    return
            elif enemy.is_offscreen():
                self.enemies.remove(enemy)

        for pu in self.powerups[:]:
            if self.player.rect.colliderect(pu.rect):
                if pu.type == 'health':
                    self.player.add_life()
                elif pu.type == 'shield':
                    self.player.activate_shield(current_time)
                elif pu.type == 'slowmo':
                    self.slow_mo = True
                    self.slow_mo_start_time = current_time
                    POWERUP_SOUND.play()
                self.powerups.remove(pu)

        # --- Renderizado ---
        self.screen.blit(FONDO_JUEGO_IMG, (0, 0))
        
        for pu in self.powerups:
            pu.draw(self.screen)
        
        self.player.draw(self.screen, current_time)
        
        for enemy in self.enemies:
            enemy.draw(self.screen)
            
        # UI del Juego
        mostrar_mensaje(self.screen, f"Vidas: {self.player.lives}", fuente, BLANCO, (ANCHO - 100, 30))
        mostrar_mensaje(self.screen, f"Puntaje: {self.score}", fuente, BLANCO, (120, 30))
        self.dibujar_ui_volumen() 
        
        if self.slow_mo:
            tiempo_restante = (SLOWMO_DURATION - (current_time - self.slow_mo_start_time)) // 1000 + 1
            mostrar_mensaje(self.screen, f"SLOW-MO: {tiempo_restante}s", fuente_pequena, NARANJA_TEXTO, (120, 60))

        pygame.display.flip()
        self.clock.tick(60)

    # --- Bucle Principal del Juego ---
    def run(self):
        """El bucle principal que maneja los estados del juego."""
        while self.running:
            if self.game_state == 'MENU':
                self.run_menu()
            elif self.game_state == 'DIFFICULTY':
                self.run_difficulty()
            elif self.game_state == 'SCORES':
                self.run_scores()
            elif self.game_state == 'PLAYING':
                self.run_playing()
            elif self.game_state == 'GAME_OVER':
                self.run_game_over()
        
        pygame.quit()
        sys.exit()

# -----------------------------------------------------------------
# --- Punto de Entrada Principal ---
# -----------------------------------------------------------------
if __name__ == "__main__":
    ScoreManager.inicializar_csv() 
    game = Game()
    game.run()