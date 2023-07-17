import subprocess
import time
import requests
from termcolor import colored

# Verificar se a biblioteca termcolor está instalada
try:
    import termcolor
except ImportError:
    print("A biblioteca 'termcolor' não está instalada. Instalando...")
    subprocess.run(["pip", "install", "termcolor"])

# Verificar se o player mpv está instalado
try:
    import mpv
except ImportError:
    print("O player 'mpv' não está instalado. Instalando...")
    subprocess.run(["pkg", "install", "mpv"])

# Verificar se a biblioteca pulsectl está instalada
try:
    import pulsectl
except ImportError:
    print("A biblioteca 'pulsectl' não está instalada. Instalando...")
    subprocess.run(["pip", "install", "pulsectl"])

# Script de susto
def animar_texto(texto, cor):
    for char in texto:
        print(colored(char, cor), end='', flush=True)
        time.sleep(0.1)  # Pausa entre cada caractere
    print()  # Nova linha após a animação

def aumentar_volume_gradualmente():
    with pulsectl.Pulse('app-volume-control') as pulse:
        volume_atual = pulse.sink_input_volume_get_all()[0]  # Obtém o volume atual
        for volume in range(volume_atual, 100, 5):  # Aumenta gradualmente o volume até 100
            pulse.sink_input_volume_set_all(volume)  # Define o novo volume
            time.sleep(0.5)  # Pausa entre cada incremento

def assustar():
    animar_texto("PREPARE-SE PARA ADVINHAR!", "red")
    time.sleep(2)
    
    print(colored("[ ALERTA!!! ] O VOLUME DO CELULAR ESTÁ BAIXO DEMAIS", "magenta"))
    time.sleep(6)
    
    animar_texto("3...", "yellow")
    time.sleep(1)
        
    animar_texto("2...", "yellow")
    time.sleep(1)
    
    animar_texto("1...", "yellow")
    time.sleep(1)
    
    animar_texto("HAHAHAHA!", "red")
    
    # Download automático do arquivo de áudio
    url = "https://raw.githubusercontent.com/Pauloh2206/Script-top/pypy.WAV"
    response = requests.get(url)
    with open("pypy.WAV", "wb") as arquivo:
        arquivo.write(response.content)
    
    subprocess.run(["mpv", "pypy.WAV"])  # Reproduzir o áudio
    
    time.sleep(2)
    animar_texto("HAHA! FOI SÓ UMA BRINCADEIRA!", "green")

while True:
    assustar()
    input("Pressione Enter para repetir o susto.")
