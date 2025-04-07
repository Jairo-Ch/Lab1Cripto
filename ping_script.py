from scapy.all import IP, ICMP, Raw, sr1
import time

def send_stealth_ping(message, target_ip):
    print(f"\n📡 Enviando mensaje oculto completo a {target_ip}")
    
    # Enviar todo el mensaje completo en un solo ping
    pkt = IP(dst=target_ip)/ICMP(type=8)/Raw(load=message)
    reply = sr1(pkt, timeout=1, verbose=0)
    
    # Confirmar que el mensaje fue enviado
    print(f"Mensaje enviado: {message}")

def show_normal_ping(target_ip):
    print(f"\n🌐 Ping normal hacia {target_ip} para comparación:")
    pkt = IP(dst=target_ip)/ICMP()
    reply = sr1(pkt, timeout=1, verbose=0)
    if reply:
        reply.show()
    else:
        print("No se recibió respuesta.")

if __name__ == "__main__":
    print("=== 🕵️ Modo Stealth - Laboratorio Cripto UDP ===")
    target_ip = input("🔹 Ingresa la IP de destino (por ejemplo 127.0.0.1): ")

    # Mensaje encriptado con desplazamiento de 9
    mensaje = "larycxpajorj h bnpdarmjm nw anmnb"

    show_normal_ping(target_ip)
    send_stealth_ping(mensaje, target_ip)
