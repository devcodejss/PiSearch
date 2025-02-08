import mpmath
import logging
import os
import signal
import sys
from colorama import init, Fore, Back, Style

# Inicializar colorama
init(autoreset=True)

# Función para limpiar la terminal dependiendo del sistema operativo
def limpiar_terminal():
    sistema = os.name
    if sistema == 'nt':  # Windows
        os.system('cls')
    else:  # Unix-like (Linux, macOS)
        os.system('clear')

def manejar_signo_interrupcion(signum, frame):
    limpiar_terminal()  # Llama a la función para limpiar la terminal
    print(
        f'''
    {Fore.CYAN}
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⠊⣉⣉⠉⠉⠉⠙⢦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠐⢿⣿⣿⣦⡀⠀⠀⠀⠱⢄⠀⠀⠀⠀⡄⠶⠛⠙⠛⠉⠒⠤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⢀⣈⣅⣤⡤⠶⠒⠛⠛⠳⢯⡷⠶⢶⣾⣷⣆⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡶⠶⠚⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠘⢷⡄⠀⠉⠉⠙⠷⠀⠀⠀⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠛⠀⠀⠀⠀⠀⠀⠀⡀⠀⠄⠃⠀⠀⠄⠀⠀⠻⢧⡀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠂⠈⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠄⠀⠀⠉⠳⢦⣄⡀⠀⠀⢰⣼⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⡐⠀⠀⠁⠀⠄⠀⠀⢀⠈⠀⠀⠄⠀⠀⡀⠀⠀⠂⢀⠀⠀⠉⠉⠛⠳⠛⠻⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⡀⠠⠀⠁⠠⠀⠀⠀⠀⠀⢀⠀⠀⠀⠂⠀⠀⠠⠀⢀⠀⠂⡀⠐⠀⠤⢠⡁⠚⢷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢀⠀⠐⠀⠀⠀⠀⠄⠀⠀⠀⠀⠂⠀⡀⠂⠠⠐⠀⠄⠂⢀⠊⠀⣃⢦⢡⠉⠄⠛⣧⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠈⠀⠀⠀⠀⠀⢀⠀⠀⠄⠀⠁⡀⠐⡀⣀⠁⢠⢡⡌⣀⢆⡄⡌⡰⣈⠆⣻⠜⡂⠑⠬⢿⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⢃⣀⠀⠠⠀⠀⠄⠀⡀⠠⣀⢐⡈⣠⣄⢦⡵⢴⠮⠿⢶⠿⣾⣿⣶⣝⣷⣑⢪⡕⣏⡒⠈⢈⣹⣧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⢻⣿⣿⣷⣿⡶⠿⠾⠓⠚⠋⠉⠁⠈⣀⠤⣄⣆⢳⡬⡶⢤⢠⢉⠋⠻⣽⢦⣹⣿⢡⠂⠀⢼⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⣀⢶⣰⠾⣶⣷⡾⢿⣾⣸⢷⣹⢿⣿⢷⡏⣰⠀⡀⠰⠈⠱⠀⢀⠸⣾⢿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢶⣦⣜⣦⣻⣞⣷⣯⣶⣷⣿⣷⣿⣾⣟⣾⡝⣧⢟⡾⣿⣿⣿⢧⡝⣦⣒⢤⣀⣦⣠⢾⣿⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣾⣹⢯⣝⣮⢻⡜⣿⣿⣿⣿⣳⣯⣾⣿⣿⢿⣯⣿⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⢏⡿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⣻⠶⣭⡗⣞⢧⣿⢿⣿⣿⣿⣿⣿⣿⣟⣿⡏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣎⠜⣧⡻⣽⢿⣿⣿⣿⣿⣽⣿⣎⣿⣦⣽⡞⣮⢼⣛⢾⡹⢯⣿⣿⣳⣿⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣾⣰⢻⣭⣛⢿⣯⢿⣿⣟⣯⣟⣼⡷⣯⣝⢮⣳⠻⣬⣛⣿⣼⣿⣽⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠎⠠⠙⣯⠓⢮⠛⣾⡹⣷⡻⣯⣟⣾⡷⣟⡷⣯⢯⣷⣻⡷⣿⣾⡿⣟⣿⢸⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣴⡿⠁⠀⠁⠰⣯⠈⠤⡙⢤⠳⣵⣟⡿⣾⣻⣽⣟⣿⣿⣿⣿⣯⣿⣿⣯⣿⡻⢾⡉⢇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⢨⣴⠋⠀⠀⠀⠀⠀⣿⠀⡄⠑⢢⢱⡏⣾⣽⢳⡝⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⣯⡝⢻⡄⢩⢻⣦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣀⣴⡟⠉⠀⠠⠁⠀⠀⠀⠘⢷⣄⠑⢢⠙⣼⢣⡽⣻⢷⣿⣿⣿⣿⣿⣿⣿⣿⣟⣷⣭⢳⠽⢀⠡⢈⠙⢧⠀
⠀⠀⠀⠀⢀⣠⡶⠞⡉⠆⡍⡒⠠⢀⣠⣆⠀⠀⠀⠀⠀⠀⠙⠷⣦⣑⠮⣳⢟⣽⣻⣷⣯⣿⣿⣿⣿⣿⣿⣿⣿⣞⠯⠊⢄⠘⡠⠈⠊⡷
⠀⠀⠀⣤⠟⡉⠐⡀⢂⡱⢊⣥⣿⢿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠾⢷⣿⣼⣷⣟⣿⣿⣿⡿⠿⠛⠋⠌⠤⣉⠂⠄⠡⢀⠁⡗
⠀⣠⡊⢀⢂⠤⣱⣸⣿⣿⣝⠨⣁⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⠂⠀⠄


 {Fore.LIGHTCYAN_EX}..:: {Fore.WHITE}Desarrollado por github.com/devcodejss {Fore.LIGHTCYAN_EX}::..

        '''
        )  # Muestra el mensaje de despedida
    sys.exit(0)  # Termina el programa después de mostrar el mensaje

# Asocia la señal SIGINT (Ctrl + C) con la función manejar_signo_interrupcion
signal.signal(signal.SIGINT, manejar_signo_interrupcion)

from colorama import Fore, init

def imprimir_banner():
    banner = '''
    ⠀⠀⠀⠀⢀⣠⣤⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⠀
    ⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
    ⠀⣴⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⡟⠛⠛⠛⣿⣿⣿⣿⣿⠛⠛⠛⠛⠛⠛⠁⠀
    ⠘⣿⣿⣿⣿⠟⠁⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠉⠛⠛⠁⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡿⠀⠀⠀⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⠁⠀⠀⠀⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠀⠀⠀⢀⣤⣤⡀⠀
    ⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠀⠀⢠⣿⣿⣿⣿⡄
    ⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣤⣤⣾⣿⣿⣿⣿⠁
    ⠀⠀⠀⢰⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
    ⠀⠀⠀⠀⠻⠿⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠿⠿⠟⠋⠀⠀⠀

'''
    print(Fore.CYAN + banner)

    print(f"{Fore.LIGHTCYAN_EX}..:: {Fore.WHITE}Desarrollado por github.com/devcodejss {Fore.LIGHTCYAN_EX}::..\n")
# Llamada a la función para imprimir el banner
imprimir_banner()


imprimir_banner()
# Función para configurar colores en los logs
class ColoredFormatter(logging.Formatter):
    COLORS = {
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED + Style.BRIGHT,  # Usamos Style.BRIGHT para simular negrita
        'DEBUG': Fore.CYAN,
    }

    def format(self, record):
        log_message = super().format(record)
        color = self.COLORS.get(record.levelname, Fore.WHITE)
        return color + log_message

# Configurar logging con colores
def configurar_logging():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = ColoredFormatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

# Obtener la cantidad de caracteres a calcular
def obtener_decimales_pi():
    try:
        decimales = int(input(f"{Fore.LIGHTCYAN_EX}Número de decimales (por defecto 10000000): {Fore.WHITE}"))
        if decimales < 1:
            raise ValueError
    except ValueError:
        logging.warning("Entrada no válida. Se utilizarán 10 millones de decimales por defecto.")
        decimales = 10000000
    return decimales

# Limpiar la terminal y mostrar el banner
limpiar_terminal()
imprimir_banner()

# Configurar logging
configurar_logging()

# Obtener los decimales de Pi
decimales_a_obtener = obtener_decimales_pi()
logging.info(f"Obteniendo {decimales_a_obtener} decimales de Pi...")

mpmath.mp.dps = decimales_a_obtener + 2  # Ajustamos la precisión para cubrir los decimales
pi_decimales = str(mpmath.mp.pi)[2:]  # Tomamos solo los decimales
logging.info(f"Se obtuvieron {len(pi_decimales)} decimales de Pi.")

# Función para determinar si el carácter es válido
def es_caracter_valido(c):
    return (65 <= c <= 90) or (97 <= c <= 122) or c in [32, 241, 225, 233, 237, 243, 250]  # Espacios y tildes

# Convertir los decimales en caracteres
texto_generado = []
i = 0
while i < len(pi_decimales) - 2:
    num = int(pi_decimales[i:i+2])  # Tomamos 2 dígitos
    if es_caracter_valido(num):
        texto_generado.append(chr(num))
        i += 2  # Avanzamos 2 posiciones
    else:
        num = int(pi_decimales[i:i+3])  # Intentamos con 3 dígitos
        if es_caracter_valido(num):
            texto_generado.append(chr(num))
            i += 3  # Avanzamos 3 posiciones
        else:
            i += 1  # Si no es válido, avanzamos 1 posición
    if i % 100000 == 0:  # Cada vez que avanzamos mucho, se registra un log
        logging.info(f"Procesados {i} caracteres.")

# Convertimos la lista en una cadena
texto_final = ''.join(texto_generado)
logging.info(f"Se generaron {len(texto_final)} caracteres válidos.")

# Reemplazar completamente el contenido del archivo 'results.txt'
logging.info("Reemplazando el contenido del archivo 'results.txt'...")
with open("results.txt", "w", encoding="utf-8") as f:  # Usamos 'w' para sobrescribir el archivo
    f.write("Texto generado a partir de los decimales de Pi:\n\n" + texto_final + "\n")

logging.info("El archivo 'results.txt' ha sido reemplazado con los nuevos datos.")





# Mantén el programa en ejecución para escuchar la señal
while True:
    pass