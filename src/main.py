import os
import subprocess
import sys
import time

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

dot = "audio/dot.wav"
dash = "audio/dash.wav"
morse = "lib/text-to-morse.exe"

def reproducir_sonido(ruta_sonido):
    pygame.mixer.init()
    pygame.mixer.music.load(ruta_sonido)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def ejecutar_programa_cpp(ruta_programa_cpp, argumento):
    proceso = subprocess.Popen([ruta_programa_cpp, argumento], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    salida_stdout, salida_stderr = proceso.communicate()
    output_texto = salida_stdout.decode('utf-8')
    return output_texto.strip()  # Elimina espacios en blanco alrededor del texto

# Establecer el valor de la variable de entorno para ocultar el mensaje de soporte de Pygame


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <string>")
        sys.exit(1)

    output_cpp = ejecutar_programa_cpp(morse, sys.argv[1])
    print(output_cpp)
    # Filtrar solo los caracteres permitidos (. - /) y eliminar otros caracteres
    output_cpp_filtrado = ''.join(filter(lambda x: x in ['.', '-', '/'], output_cpp))

    for char in output_cpp_filtrado:
        if char == '.':
            reproducir_sonido(dot)
        elif char == '-':
            reproducir_sonido(dash)
        elif char == '/':
            time.sleep(0.5)  # Espera medio segundo para la separación entre palabras