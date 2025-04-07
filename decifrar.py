from scapy.all import rdpcap, ICMP
from termcolor import colored
import string

# Función para descifrar el mensaje usando el cifrado César
def descifrar_cesar(texto, desplazamiento):
    resultado = ""
    for c in texto:
        if c in string.ascii_lowercase:
            nueva = chr((ord(c) - ord('a') - desplazamiento) % 26 + ord('a'))
            resultado += nueva
        else:
            resultado += c
    return resultado

# Leer los paquetes desde un archivo .pcapng
def leer_paquete_pcapng(archivo_pcapng):
    paquetes = rdpcap(archivo_pcapng)  # Cargar los paquetes
    mensajes = []

    for paquete in paquetes:
        # Filtrar paquetes ICMP (Echo Request)
        if paquete.haslayer(ICMP):
            if paquete[ICMP].type == 8:  # Verificar si es un Echo Request (ping)
                if paquete[ICMP].payload:  # Asegurarse de que tenga carga útil
                    mensaje_cifrado = bytes(paquete[ICMP].payload)
                    mensajes.append(mensaje_cifrado.decode(errors='ignore'))
    return mensajes

# Algunas palabras comunes en español para evaluar el resultado más probable
palabras_comunes = ['el', 'la', 'que', 'en', 'de', 'y', 'los', 'por', 'un', 'una', 'es', 'con', 'para']

# Leer el archivo pcapng y obtener los mensajes
archivo_pcapng = "Trafico_Lab1.pcapng"  # Nombre del archivo pcapng que contiene los paquetes
mensajes_cifrados = leer_paquete_pcapng(archivo_pcapng)

mejor_puntaje = -1
mejor_texto = ""
mejor_k = 0

# Mostrar posibles resultados de descifrado
print("=== Posibles resultados de descifrado César ===\n")

for mensaje in mensajes_cifrados:
    for k in range(1, 26):  # Probar todos los desplazamientos
        texto_descifrado = descifrar_cesar(mensaje, k)
        puntaje = sum(palabra in texto_descifrado for palabra in palabras_comunes)
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_texto = texto_descifrado
            mejor_k = k

        print(f"🔁 Desplazamiento {k:2}: {texto_descifrado}")

# Mostrar el posible mensaje en claro
print("\n✅ Posible mensaje en claro:")
print(colored(f"[Desplazamiento {mejor_k}] {mejor_texto}", 'green'))
