import base64
import tempfile
import os
import time
import pygame
from colorama import init, Fore, Style

init(autoreset=True)

# ------------------ CONFIGURACIÓN DE COLORES ------------------
colores = {
    "Hakari": Style.BRIGHT + Fore.MAGENTA,
    "Karane": Fore.YELLOW,
    "Shizuka": Fore.BLUE,
    "Nano": Fore.MAGENTA,
    "Kusuri": Fore.RED,
    "Todas": Fore.WHITE + Style.BRIGHT,
    "Instrumental": Fore.LIGHTBLACK_EX,
}


def imprimir_linea(cantantes, texto):
    if cantantes[0] == "Instrumental":
        print(f"{Fore.LIGHTBLACK_EX}♪ (instrumental) ♪{Style.RESET_ALL}")
        return

    if len(cantantes) >= 5:
        print(f"{Fore.WHITE}{Style.BRIGHT}[TODAS] {texto}{Style.RESET_ALL}")
        return

    if len(cantantes) == 1:
        color = colores.get(cantantes[0], Fore.WHITE)
        print(f"{color}[{cantantes[0]}] {texto}{Style.RESET_ALL}")
        return

    # Nombres, cada uno con su color
    nombres_coloreados = []
    for cantante in cantantes:
        color = colores.get(cantante, Fore.WHITE)
        nombres_coloreados.append(f"{color}{cantante}{Style.RESET_ALL}")
    etiqueta = " & ".join(nombres_coloreados)

    # Texto repartido por caracteres (no por palabras)
    n = len(cantantes)
    largo = len(texto)
    tam = max(1, largo // n)

    partes_texto = []
    for i in range(n):
        inicio = i * tam
        fin = (i + 1) * tam if i < n - 1 else largo
        partes_texto.append(texto[inicio:fin])

    salida = f"[{etiqueta}] "
    for cantante, parte in zip(cantantes, partes_texto):
        color = colores.get(cantante, Fore.WHITE)
        salida += f"{color}{parte}{Style.RESET_ALL}"

    print(salida)


# ------------------ CARGAR LETRA ------------------
def cargar_letra(ruta):
    letra = []
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            if linea.strip():
                partes = linea.strip().split("|", 2)
                tiempo = partes[0]
                cantantes = partes[1]
                texto = partes[2] if len(partes) > 2 else ""
                lista_cantantes = [c.strip() for c in cantantes.split(",")]
                letra.append((float(tiempo), lista_cantantes, texto))
    return letra


# ------------------ CARGAR Y DECODIFICAR AUDIO ------------------
print("Iniciando sistema...")
time.sleep(0.8)
print("Decodificando datos...")
time.sleep(1)

with open("data.txt", "r") as f:
    audio_b64 = f.read()

datos = base64.b64decode(audio_b64)
print("Datos reconstruidos ✓")
time.sleep(0.5)

with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp:
    temp.write(datos)
    ruta_temporal = temp.name

print("Inicializando reproductor...")
time.sleep(0.6)

# ------------------ CARGAR LETRA SINCRONIZADA ------------------
letra = cargar_letra("config.txt")

# ------------------ REPRODUCIR ------------------
pygame.mixer.init()
pygame.mixer.music.load(ruta_temporal)
pygame.mixer.music.play()

print("Reproduciendo 🎵\n")

inicio = time.time()
indice = 0

while pygame.mixer.music.get_busy():
    tiempo_actual = time.time() - inicio

    if indice < len(letra) and tiempo_actual >= letra[indice][0]:
        _, cantantes, texto = letra[indice]
        imprimir_linea(cantantes, texto)
        indice += 1

    pygame.time.Clock().tick(30)

# ------------------ LIMPIEZA ------------------
pygame.mixer.music.unload()
pygame.mixer.quit()
os.remove(ruta_temporal)
